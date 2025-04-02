import logging
from sqlalchemy import select, or_
from sqlalchemy.dialects.postgresql import insert  # Правильный импорт для PostgreSQL
from sqlalchemy.ext.asyncio import AsyncSession
from amochka.models import Pipeline, Status

logger = logging.getLogger(__name__)

async def update_pipelines(session: AsyncSession, pipelines_data):
    """
    Обновляет таблицы воронок (Pipeline) и статусов (Status) в базе данных.
    
    :param session: Асинхронная сессия SQLAlchemy.
    :param pipelines_data: Список воронок, полученных из API amoCRM.
    """
    if not pipelines_data:
        logger.warning("Получен пустой список воронок, обновление не выполнено")
        return
        
    account_id = 1111  # Пример: замените на актуальный идентификатор аккаунта
    pipeline_values = []
    all_statuses = []

    # Подготавливаем данные для вставки в таблицу Pipeline и собираем статусы
    for pipeline in pipelines_data:
        pipeline_values.append({
            'account_id': account_id,
            'pipeline_id': pipeline['id'],
            'name': pipeline['name'],
            'sort': pipeline.get('sort'),
            'is_main': pipeline.get('is_main'),
            'is_archive': pipeline.get('is_archive'),
        })
        # Если воронка содержит статусы, обрабатываем их
        if '_embedded' in pipeline and 'statuses' in pipeline['_embedded']:
            for status in pipeline['_embedded']['statuses']:
                all_statuses.append((pipeline['id'], status['id'], status))

    # Массовая вставка/обновление данных в таблице Pipeline
    stmt = insert(Pipeline).values(pipeline_values)
    stmt = stmt.on_conflict_do_update(
        index_elements=['pipeline_id'],
        set_={
            'name': stmt.excluded.name,
            'sort': stmt.excluded.sort,
            'is_main': stmt.excluded.is_main,
            'is_archive': stmt.excluded.is_archive,
        }
    )
    await session.execute(stmt)
    logger.debug(f"Обновлено {len(pipeline_values)} воронок")

    # Получаем сопоставление внутренних ID воронок по pipeline_id
    result = await session.execute(select(Pipeline.id, Pipeline.pipeline_id))
    pipeline_id_map = {row.pipeline_id: row.id for row in result}

    # Подготавливаем данные для вставки в таблицу Status
    status_values = []
    for pipeline_id, status_id, status in all_statuses:
        internal_pipeline_id = pipeline_id_map.get(pipeline_id)
        if internal_pipeline_id is None:
            logger.warning(f"Не найден внутренний ID для воронки {pipeline_id}, пропускаю статус {status_id}")
            continue
            
        status_values.append({
            'account_id': account_id,
            'pipeline_id': internal_pipeline_id,
            'status_id': status_id,
            'name': status.get('name', ''),
            'color': status.get('color', ''),
            'sort': status.get('sort'),
            'is_editable': status.get('is_editable'),
            'type': status.get('type'),
        })

    if status_values:
        stmt = insert(Status).values(status_values)
        stmt = stmt.on_conflict_do_update(
            index_elements=['pipeline_id', 'status_id'],
            set_={
                'name': stmt.excluded.name,
                'color': stmt.excluded.color,
                'sort': stmt.excluded.sort,
                'is_editable': stmt.excluded.is_editable,
                'type': stmt.excluded.type,
            }
        )
        await session.execute(stmt)
        logger.debug(f"Обновлено {len(status_values)} статусов")

    logger.info(f"Обновлено {len(pipeline_values)} воронок и {len(status_values)} статусов.")