import os
import time
import json
import requests
import logging
from datetime import datetime
from ratelimit import limits, sleep_and_retry

# Создаём базовый логгер
logger = logging.getLogger(__name__)
if not logger.handlers:
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

RATE_LIMIT = 7  # Максимум 7 запросов в секунду

class Deal(dict):
    """
    Объект сделки расширяет стандартный словарь данными из custom_fields_values.

    Обеспечивает два способа доступа к кастомным полям:
      1. get(key): при обращении по названию (строкой) или по ID поля (integer)
         возвращает текстовое значение поля (например, «Дурина Юлия»).
      2. get_id(key): возвращает идентификатор выбранного варианта (enum_id) для полей типа select.
         Если в данных enum_id отсутствует, производится поиск в переданной конфигурации полей,
         сравнение выполняется без учёта регистра и лишних пробелов.

    Параметр custom_fields_config – словарь, где ключи – ID полей, а значения – модели полей.
    """
    def __init__(self, data, custom_fields_config=None, logger=None):
        super().__init__(data)
        self._custom = {}
        self._custom_config = custom_fields_config  # сохраняем конфигурацию кастомных полей
        self._logger = logger or logging.getLogger(__name__)
        custom = data.get("custom_fields_values") or []
        self._logger.debug(f"Processing custom_fields_values: {custom}")
        for field in custom:
            if isinstance(field, dict):
                field_name = field.get("field_name")
                values = field.get("values")
                if field_name and values and isinstance(values, list) and len(values) > 0:
                    key_name = field_name.lower().strip()
                    stored_value = values[0].get("value")
                    stored_enum_id = values[0].get("enum_id")  # может быть None для некоторых полей
                    # Сохраняем полную информацию (и для get() и для get_id())
                    self._custom[key_name] = {"value": stored_value, "enum_id": stored_enum_id}
                    self._logger.debug(f"Set custom field '{key_name}' = {{'value': {stored_value}, 'enum_id': {stored_enum_id}}}")
                field_id = field.get("field_id")
                if field_id is not None and values and isinstance(values, list) and len(values) > 0:
                    stored_value = values[0].get("value")
                    stored_enum_id = values[0].get("enum_id")  # может быть None для некоторых полей
                    self._custom[int(field_id)] = {"value": stored_value, "enum_id": stored_enum_id}
                    self._logger.debug(f"Set custom field id {field_id} = {{'value': {stored_value}, 'enum_id': {stored_enum_id}}}")
        if custom_fields_config:
            for cid, field_obj in custom_fields_config.items():
                key = field_obj.get("name", "").lower().strip() if isinstance(field_obj, dict) else str(field_obj).lower().strip()
                if key not in self._custom:
                    self._custom[key] = None
                    self._logger.debug(f"Field '{key}' not found in deal data; set to None")

    def __getitem__(self, key):
        if key in super().keys():
            return super().__getitem__(key)
        if isinstance(key, str):
            lower_key = key.lower().strip()
            if lower_key in self._custom:
                stored = self._custom[lower_key]
                return stored.get("value") if isinstance(stored, dict) else stored
        if isinstance(key, int):
            if key in self._custom:
                stored = self._custom[key]
                return stored.get("value") if isinstance(stored, dict) else stored
        raise KeyError(key)

    def get(self, key, default=None):
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    def get_field_type(self, key):
        """
        Определяет тип кастомного поля.
        
        :param key: Название поля (строка) или ID поля (integer).
        :return: Строка с типом поля ('text', 'select', 'numeric', 'checkbox', и т.д.) 
                 или None, если поле не найдено или тип не определён.
        """
        field_def = None
        
        # Получаем определение поля из конфигурации
        if self._custom_config:
            if isinstance(key, int):
                field_def = self._custom_config.get(key)
            else:
                for fid, fdef in self._custom_config.items():
                    if isinstance(fdef, dict) and fdef.get("name", "").lower().strip() == key.lower().strip():
                        field_def = fdef
                        break
        
        # Если нашли определение, возвращаем его тип
        if field_def and isinstance(field_def, dict):
            return field_def.get("type")
        
        # Если конфигурации нет или поле не найдено, пробуем определить тип по данным
        stored = None
        if isinstance(key, str):
            lower_key = key.lower().strip()
            if lower_key in self._custom:
                stored = self._custom[lower_key]
        elif isinstance(key, int):
            if key in self._custom:
                stored = self._custom[key]
                
        if isinstance(stored, dict) and "enum_id" in stored:
            return "select"
        
        return None

    def get_id(self, key, default=None):
        """
        Возвращает идентификатор выбранного варианта (enum_id) для кастомного поля типа select.
        Для полей других типов возвращает их значение, как метод get().
        
        Если значение enum_id отсутствует в данных, производится поиск в конфигурации кастомных полей,
        сравнение значения выполняется без учёта регистра и пробелов.

        :param key: Название поля (строка) или ID поля (integer).
        :param default: Значение по умолчанию, если enum_id не найден.
        :return: Для полей типа select - идентификатор варианта (целое число).
                 Для других типов полей - значение поля. 
                 Если поле не найдено - default.
        """
        field_type = self.get_field_type(key)
        
        # Если это не поле списка, возвращаем значение как get()
        if field_type is not None and field_type != "select":
            return self.get(key, default)
            
        stored = None
        if isinstance(key, str):
            lower_key = key.lower().strip()
            if lower_key in self._custom:
                stored = self._custom[lower_key]
        elif isinstance(key, int):
            if key in self._custom:
                stored = self._custom[key]
        if isinstance(stored, dict):
            enum_id = stored.get("enum_id")
            if enum_id is not None:
                return enum_id
            if self._custom_config:
                field_def = None
                if isinstance(key, int):
                    field_def = self._custom_config.get(key)
                else:
                    for fid, fdef in self._custom_config.items():
                        if fdef.get("name", "").lower().strip() == key.lower().strip():
                            field_def = fdef
                            break
                if field_def:
                    enums = field_def.get("enums") or []
                    for enum in enums:
                        if enum.get("value", "").lower().strip() == stored.get("value", "").lower().strip():
                            return enum.get("id", default)
        
        # Если это не поле типа select или не удалось найти enum_id, 
        # возвращаем значение поля
        return self.get(key, default)

class CacheConfig:
    """
    Конфигурация кэширования для AmoCRMClient.
    
    Параметры:
        enabled (bool): Включено ли кэширование
        storage (str): Тип хранилища ('file' или 'memory')
        file (str): Путь к файлу кэша (используется только при storage='file')
        lifetime_hours (int|None): Время жизни кэша в часах (None для бесконечного)
    """
    def __init__(self, enabled=True, storage='file', file=None, lifetime_hours=24):
        self.enabled = enabled
        self.storage = storage.lower()
        self.file = file
        self.lifetime_hours = lifetime_hours
    
    @classmethod
    def disabled(cls):
        """Создает конфигурацию с отключенным кэшированием"""
        return cls(enabled=False)
    
    @classmethod
    def memory_only(cls, lifetime_hours=24):
        """Создает конфигурацию с кэшированием только в памяти"""
        return cls(enabled=True, storage='memory', lifetime_hours=lifetime_hours)
    
    @classmethod
    def file_cache(cls, file=None, lifetime_hours=24):
        """Создает конфигурацию с файловым кэшированием"""
        return cls(enabled=True, storage='file', file=file, lifetime_hours=lifetime_hours)

class AmoCRMClient:
    """
    Клиент для работы с API amoCRM.

    Основные функции:
      - load_token: Загружает и проверяет токен авторизации.
      - _make_request: Выполняет HTTP-запрос с учетом ограничения по скорости.
      - get_deal_by_id: Получает данные сделки по ID и возвращает объект Deal.
      - get_custom_fields_mapping: Загружает и кэширует список кастомных полей.
      - find_custom_field_id: Ищет кастомное поле по его названию.
      - update_lead: Обновляет сделку, включая стандартные и кастомные поля.

    Дополнительно можно задать уровень логирования через параметр log_level,
    либо полностью отключить логирование, установив disable_logging=True.
    """
    def __init__(
        self, 
        base_url, 
        token_file=None, 
        cache_config=None, 
        log_level=logging.INFO, 
        disable_logging=False
    ):
        """
        Инициализирует клиента, задавая базовый URL, токен авторизации и настройки кэша для кастомных полей.
        
        :param base_url: Базовый URL API amoCRM.
        :param token_file: Файл, содержащий токен авторизации.
        :param cache_config: Конфигурация кэширования (объект CacheConfig или None для значений по умолчанию)
        :param log_level: Уровень логирования (например, logging.DEBUG, logging.INFO).
        :param disable_logging: Если True, логирование будет отключено.
        """
        self.base_url = base_url.rstrip('/')
        domain = self.base_url.split("//")[-1].split(".")[0]
        self.domain = domain
        self.token_file = token_file or os.path.join(os.path.expanduser('~'), '.amocrm_token.json')
        
        # Создаем логгер для конкретного экземпляра клиента
        self.logger = logging.getLogger(f"{__name__}.{self.domain}")
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
            self.logger.propagate = False  # Отключаем передачу логов в родительский логгер
        
        if disable_logging:
            self.logger.setLevel(logging.CRITICAL + 1)  # Выше, чем любой стандартный уровень
        else:
            self.logger.setLevel(log_level)
        
        # Настройка кэширования
        if cache_config is None:
            self.cache_config = CacheConfig()
        else:
            self.cache_config = cache_config
            
        # Установка файла кэша, если используется файловое хранилище
        if self.cache_config.enabled and self.cache_config.storage == 'file':
            if not self.cache_config.file:
                self.cache_config.file = f"custom_fields_cache_{self.domain}.json"
        
        self.logger.debug(f"AmoCRMClient initialized for domain {self.domain}")
        
        self.token = self.load_token()
        self._custom_fields_mapping = None

    def load_token(self):
        """
        Загружает токен авторизации из файла или строки, проверяет его срок действия.

        :return: Действительный access_token.
        :raises Exception: Если токен не найден или истёк.
        """
        data = None
        if os.path.exists(self.token_file):
            with open(self.token_file, 'r') as f:
                data = json.load(f)
            self.logger.debug(f"Token loaded from file: {self.token_file}")
        else:
            try:
                data = json.loads(self.token_file)
                self.logger.debug("Token parsed from provided string.")
            except Exception as e:
                raise Exception("Токен не найден и не удалось распарсить переданное содержимое.") from e

        expires_at_str = data.get('expires_at')
        try:
            expires_at = datetime.fromisoformat(expires_at_str).timestamp()
        except Exception:
            expires_at = float(expires_at_str)
        
        if expires_at and time.time() < expires_at:
            self.logger.debug("Token is valid.")
            return data.get('access_token')
        else:
            raise Exception("Токен найден, но он истёк. Обновите токен.")

    @sleep_and_retry
    @limits(calls=RATE_LIMIT, period=1)
    def _make_request(self, method, endpoint, params=None, data=None):
        """
        Выполняет HTTP-запрос к API amoCRM с учетом ограничения по скорости (rate limit).

        :param method: HTTP-метод (GET, PATCH, POST, DELETE и т.д.).
        :param endpoint: Конечная точка API (начинается с /api/v4/).
        :param params: GET-параметры запроса.
        :param data: Данные, отправляемые в JSON-формате.
        :return: Ответ в формате JSON или None (если статус 204).
        :raises Exception: При получении кода ошибки, отличного от 200/204.
        """
        url = f"{self.base_url}{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        self.logger.debug(f"Making {method} request to {url} with params {params} and data {data}")
        response = requests.request(method, url, headers=headers, params=params, json=data)
        if response.status_code not in (200, 204):
            self.logger.error(f"Request error {response.status_code}: {response.text}")
            raise Exception(f"Ошибка запроса: {response.status_code}, {response.text}")
        if response.status_code == 204:
            return None
        return response.json()

    def get_deal_by_id(self, deal_id, skip_fields_mapping=False):
        """
        Получает данные сделки по её ID и возвращает объект Deal.
        Если данные отсутствуют или имеют неверную структуру, выбрасывается исключение.
        
        :param deal_id: ID сделки для получения
        :param skip_fields_mapping: Если True, не загружает справочник кастомных полей
                                   (используйте для работы только с ID полей)
        :return: Объект Deal с данными сделки
        """
        endpoint = f"/api/v4/leads/{deal_id}"
        params = {'with': 'contacts,companies,catalog_elements,loss_reason,tags'}
        data = self._make_request("GET", endpoint, params=params)
        
        # Проверяем, что получили данные и что они содержат ключ "id"
        if not data or not isinstance(data, dict) or "id" not in data:
            self.logger.error(f"Deal {deal_id} not found or invalid response: {data}")
            raise Exception(f"Deal {deal_id} not found or invalid response.")

        custom_config = None if skip_fields_mapping else self.get_custom_fields_mapping()
        self.logger.debug(f"Deal {deal_id} data received (содержимое полей не выводится полностью).")
        return Deal(data, custom_fields_config=custom_config, logger=self.logger)

    def _save_custom_fields_cache(self, mapping):
        """
        Сохраняет кэш кастомных полей в файл, если используется файловый кэш.
        Если кэширование отключено или выбран кэш в памяти, операция пропускается.
        """
        if not self.cache_config.enabled:
            self.logger.debug("Caching disabled; cache not saved.")
            return
        if self.cache_config.storage != 'file':
            self.logger.debug("Using memory caching; no file cache saved.")
            return
        cache_data = {"last_updated": time.time(), "mapping": mapping}
        with open(self.cache_config.file, "w") as f:
            json.dump(cache_data, f)
        self.logger.debug(f"Custom fields cache saved to {self.cache_config.file}")

    def _load_custom_fields_cache(self):
        """
        Загружает кэш кастомных полей из файла, если используется файловый кэш.
        Если кэширование отключено или выбран кэш в памяти, возвращает None.
        """
        if not self.cache_config.enabled:
            self.logger.debug("Caching disabled; no cache loaded.")
            return None
        if self.cache_config.storage != 'file':
            self.logger.debug("Using memory caching; cache will be kept in memory only.")
            return None
        if os.path.exists(self.cache_config.file):
            with open(self.cache_config.file, "r") as f:
                try:
                    cache_data = json.load(f)
                    self.logger.debug("Custom fields cache loaded successfully.")
                    return cache_data
                except Exception as e:
                    self.logger.error(f"Error loading cache: {e}")
                    return None
        return None

    def get_custom_fields_mapping(self, force_update=False):
        """
        Возвращает словарь отображения кастомных полей для сделок.
        Если данные кэшированы и не устарели, возвращает кэш; иначе выполняет запросы для получения данных.
        """
        if not force_update and self._custom_fields_mapping is not None:
            return self._custom_fields_mapping

        cache_data = self._load_custom_fields_cache() if self.cache_config.enabled else None
        if cache_data:
            last_updated = cache_data.get("last_updated", 0)
            if self.cache_config.lifetime_hours is not None:
                if time.time() - last_updated < self.cache_config.lifetime_hours * 3600:
                    self._custom_fields_mapping = cache_data.get("mapping")
                    self.logger.debug("Using cached custom fields mapping.")
                    return self._custom_fields_mapping
            else:
                # Бесконечный кэш – не проверяем срок
                self._custom_fields_mapping = cache_data.get("mapping")
                self.logger.debug("Using cached custom fields mapping (infinite cache).")
                return self._custom_fields_mapping

        mapping = {}
        page = 1
        total_pages = 1  # Значение по умолчанию
        while page <= total_pages:
            endpoint = f"/api/v4/leads/custom_fields?limit=250&page={page}"
            response = self._make_request("GET", endpoint)
            if response and "_embedded" in response and "custom_fields" in response["_embedded"]:
                for field in response["_embedded"]["custom_fields"]:
                    mapping[field["id"]] = field
                total_pages = response.get("_page_count", page)
                self.logger.debug(f"Fetched page {page} of {total_pages}")
                page += 1
            else:
                break

        self.logger.debug("Custom fields mapping fetched (содержимое маппинга не выводится полностью).")
        self._custom_fields_mapping = mapping
        if self.cache_config.enabled:
            self._save_custom_fields_cache(mapping)
        return mapping

    def find_custom_field_id(self, search_term):
        """
        Ищет кастомное поле по заданному названию (или части названия).

        :param search_term: Строка для поиска по имени поля.
        :return: Кортеж (field_id, field_obj) если найдено, иначе (None, None).
        """
        mapping = self.get_custom_fields_mapping()
        search_term_lower = search_term.lower().strip()
        for key, field_obj in mapping.items():
            if isinstance(field_obj, dict):
                name = field_obj.get("name", "").lower().strip()
            else:
                name = str(field_obj).lower().strip()
            if search_term_lower == name or search_term_lower in name:
                self.logger.debug(f"Found custom field '{name}' with id {key}")
                return int(key), field_obj
        self.logger.debug(f"Custom field containing '{search_term}' not found.")
        return None, None

    def update_lead(self, lead_id, update_fields: dict, tags_to_add: list = None, tags_to_delete: list = None):
        """
        Обновляет сделку, задавая новые значения для стандартных и кастомных полей.

        Для кастомных полей:
          - Если значение передается как целое число, оно интерпретируется как идентификатор варианта (enum_id)
            для полей типа select.
          - Если значение передается как строка, используется ключ "value".

        :param lead_id: ID сделки, которую нужно обновить.
        :param update_fields: Словарь с полями для обновления. Ключи могут быть стандартными или названием кастомного поля.
        :param tags_to_add: Список тегов для добавления к сделке.
        :param tags_to_delete: Список тегов для удаления из сделки.
        :return: Ответ API в формате JSON.
        :raises Exception: Если одно из кастомных полей не найдено.
        """
        payload = {}
        standard_fields = {
            "name", "price", "status_id", "pipeline_id", "created_by", "updated_by",
            "closed_at", "created_at", "updated_at", "loss_reason_id", "responsible_user_id"
        }
        custom_fields = []
        for key, value in update_fields.items():
            if key in standard_fields:
                payload[key] = value
                self.logger.debug(f"Standard field {key} set to {value}")
            else:
                if isinstance(value, int):
                    field_value_dict = {"enum_id": value}
                else:
                    field_value_dict = {"value": value}
                try:
                    field_id = int(key)
                    custom_fields.append({"field_id": field_id, "values": [field_value_dict]})
                    self.logger.debug(f"Custom field by id {field_id} set to {value}")
                except ValueError:
                    field_id, field_obj = self.find_custom_field_id(key)
                    if field_id is not None:
                        custom_fields.append({"field_id": field_id, "values": [field_value_dict]})
                        self.logger.debug(f"Custom field '{key}' found with id {field_id} set to {value}")
                    else:
                        raise Exception(f"Custom field '{key}' не найден.")
        if custom_fields:
            payload["custom_fields_values"] = custom_fields
        if tags_to_add:
            payload["tags_to_add"] = tags_to_add
        if tags_to_delete:
            payload["tags_to_delete"] = tags_to_delete
        self.logger.debug("Update payload for lead {} prepared (содержимое payload не выводится полностью).".format(lead_id))
        endpoint = f"/api/v4/leads/{lead_id}"
        response = self._make_request("PATCH", endpoint, data=payload)
        self.logger.debug("Update response received.")
        return response
    
    def get_entity_notes(self, entity, entity_id, get_all=False, note_type=None, extra_params=None):
        """
        Получает список примечаний для указанной сущности и её ID.

        Используется эндпоинт:
        GET /api/v4/{entity_plural}/{entity_id}/notes

        :param entity: Тип сущности (например, 'lead', 'contact', 'company', 'customer' и т.д.).
                    Передаётся в единственном числе, для формирования конечной точки будет использована
                    таблица преобразования (например, 'lead' -> 'leads').
        :param entity_id: ID сущности.
        :param get_all: Если True, метод автоматически проходит по всем страницам пагинации.
        :param note_type: Фильтр по типу примечания. Может быть строкой (например, 'common') или списком строк.
        :param extra_params: Словарь дополнительных GET-параметров, если требуется.
        :return: Список примечаний (каждый элемент – словарь с данными примечания).
        """
        # Преобразуем тип сущности в форму во множественном числе (для известных типов)
        mapping = {
            'lead': 'leads',
            'contact': 'contacts',
            'company': 'companies',
            'customer': 'customers'
        }
        plural = mapping.get(entity.lower(), entity.lower() + "s")
        
        endpoint = f"/api/v4/{plural}/{entity_id}/notes"
        params = {
            "page": 1,
            "limit": 250
        }
        if note_type is not None:
            params["filter[note_type]"] = note_type
        if extra_params:
            params.update(extra_params)
        
        notes = []
        while True:
            response = self._make_request("GET", endpoint, params=params)
            if response and "_embedded" in response and "notes" in response["_embedded"]:
                notes.extend(response["_embedded"]["notes"])
            if not get_all:
                break
            total_pages = response.get("_page_count", params["page"])
            if params["page"] >= total_pages:
                break
            params["page"] += 1
        self.logger.debug(f"Retrieved {len(notes)} notes for {entity} {entity_id}")
        return notes

    def get_entity_note(self, entity, entity_id, note_id):
        """
        Получает расширенную информацию по конкретному примечанию для указанной сущности.

        Используется эндпоинт:
        GET /api/v4/{entity_plural}/{entity_id}/notes/{note_id}

        :param entity: Тип сущности (например, 'lead', 'contact', 'company', 'customer' и т.д.).
        :param entity_id: ID сущности.
        :param note_id: ID примечания.
        :return: Словарь с полной информацией о примечании.
        :raises Exception: При ошибке запроса.
        """
        mapping = {
            'lead': 'leads',
            'contact': 'contacts',
            'company': 'companies',
            'customer': 'customers'
        }
        plural = mapping.get(entity.lower(), entity.lower() + "s")
        endpoint = f"/api/v4/{plural}/{entity_id}/notes/{note_id}"
        self.logger.debug(f"Fetching note {note_id} for {entity} {entity_id}")
        note_data = self._make_request("GET", endpoint)
        self.logger.debug(f"Note {note_id} for {entity} {entity_id} fetched successfully.")
        return note_data

    # Удобные обёртки для сделок и контактов:
    def get_deal_notes(self, deal_id, **kwargs):
        return self.get_entity_notes("lead", deal_id, **kwargs)

    def get_deal_note(self, deal_id, note_id):
        return self.get_entity_note("lead", deal_id, note_id)

    def get_contact_notes(self, contact_id, **kwargs):
        return self.get_entity_notes("contact", contact_id, **kwargs)

    def get_contact_note(self, contact_id, note_id):
        return self.get_entity_note("contact", contact_id, note_id)
    
    def get_entity_events(self, entity, entity_id=None, get_all=False, event_type=None, extra_params=None):
        """
        Получает список событий для указанной сущности.
        Если entity_id не указан (None), возвращает события для всех сущностей данного типа.

        :param entity: Тип сущности (например, 'lead', 'contact', 'company' и т.д.).
        :param entity_id: ID сущности или None для получения событий по всем сущностям данного типа.
        :param get_all: Если True, автоматически проходит по всем страницам пагинации.
        :param event_type: Фильтр по типу события. Может быть строкой или списком строк.
        :param extra_params: Словарь дополнительных GET-параметров.
        :return: Список событий (каждый элемент – словарь с данными события).
        """
        params = {
            'page': 1,
            'limit': 100,
            'filter[entity]': entity,
        }
        # Добавляем фильтр по ID, если он указан
        if entity_id is not None:
            params['filter[entity_id]'] = entity_id
        # Фильтр по типу события
        if event_type is not None:
            params['filter[type]'] = event_type
        if extra_params:
            params.update(extra_params)

        events = []
        while True:
            response = self._make_request("GET", "/api/v4/events", params=params)
            if response and "_embedded" in response and "events" in response["_embedded"]:
                events.extend(response["_embedded"]["events"])
            # Если не нужно получать все страницы, выходим
            if not get_all:
                break
            total_pages = response.get("_page_count", params['page'])
            if params['page'] >= total_pages:
                break
            params['page'] += 1
        return events

    # Удобные обёртки:
    def get_deal_events(self, deal_id, **kwargs):
        return self.get_entity_events("lead", deal_id, **kwargs)

    def get_contact_events(self, contact_id, **kwargs):
        return self.get_entity_events("contact", contact_id, **kwargs)

    def get_event(self, event_id):
        """
        Получает подробную информацию по конкретному событию по его ID.
        
        Используется эндпоинт:
          GET /api/v4/events/{event_id}
        
        :param event_id: ID события.
        :return: Словарь с подробной информацией о событии.
        :raises Exception: При ошибке запроса.
        """
        endpoint = f"/api/v4/events/{event_id}"
        self.logger.debug(f"Fetching event with ID {event_id}")
        event_data = self._make_request("GET", endpoint)
        self.logger.debug(f"Event {event_id} details fetched successfully.")
        return event_data
    
    def get_pipelines(self):
        """
        Получает список всех воронок и их статусов из amoCRM.

        :return: Список словарей, где каждый словарь содержит данные воронки, а также, если присутствует, вложенные статусы.
        :raises Exception: Если данные не получены или структура ответа неверна.
        """
        endpoint = "/api/v4/leads/pipelines"
        response = self._make_request("GET", endpoint)
        if response and '_embedded' in response and 'pipelines' in response['_embedded']:
            pipelines = response['_embedded']['pipelines']
            self.logger.debug(f"Получено {len(pipelines)} воронок")
            return pipelines
        else:
            self.logger.error("Не удалось получить воронки из amoCRM")
            raise Exception("Ошибка получения воронок из amoCRM")