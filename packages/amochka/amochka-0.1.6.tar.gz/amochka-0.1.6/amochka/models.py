from sqlalchemy import Column, Integer, String, Boolean, BigInteger, ForeignKey, UniqueConstraint
from sqlalchemy.orm import declarative_base, relationship

# Базовый класс для всех моделей
Base = declarative_base()

class Pipeline(Base):
    """
    Модель для хранения воронок из amoCRM.
    """
    __tablename__ = 'a_pipelines'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    account_id = Column(Integer, nullable=False)
    pipeline_id = Column(BigInteger, nullable=False, unique=True)
    name = Column(String)
    sort = Column(Integer)
    is_main = Column(Boolean)
    is_archive = Column(Boolean)
    
    # Определяем связь с моделью статусов
    statuses = relationship("Status", back_populates="pipeline")
    
    __table_args__ = (
        UniqueConstraint('pipeline_id', name='uq_pipeline_id'),
    )

class Status(Base):
    """
    Модель для хранения статусов воронок.
    """
    __tablename__ = 'a_statuses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    account_id = Column(Integer, nullable=False)
    # Ссылка на внутренний id воронки (Pipeline.id)
    pipeline_id = Column(Integer, ForeignKey('a_pipelines.id'), nullable=False)
    status_id = Column(BigInteger, nullable=False)
    name = Column(String)
    color = Column(String)
    sort = Column(Integer)
    is_editable = Column(Boolean)
    type = Column(Integer)
    
    # Определяем обратную связь с моделью Pipeline
    pipeline = relationship("Pipeline", back_populates="statuses")
    
    __table_args__ = (
        UniqueConstraint('pipeline_id', 'status_id', name='uq_pipeline_status_id'),
    )