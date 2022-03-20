import datetime

from db import Base

from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.dialects.mysql import INTEGER, BOOLEAN
from sqlalchemy.types import Float, Integer, String, Date

import hashlib

SQLITE3_NAME = "./db.sqlite3"

class Receipt(Base):
    """
    Receipt モデル
    id              :主キー
    date            :投稿日
    protein         :タンパク質のスコア
    carbon          :炭水化物のスコア
    fat             :脂質のスコア
    mineral         :無機質のスコア
    vitamin         :ビタミンのスコア
    fiber           ;食物繊維のスコア
    description     :概要
    """
    __tablename__ = 'receipt'
    id = Column(
        'id',
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )
    
    date = Column(
        'date',
        DateTime,
        default=None,
        nullable=False,
    )
    
    protein = Column('protein', Float)
    carbon = Column('carbon', Float)
    fat = Column('fat', Float)
    mineral = Column('mineral', Float)
    vitamin = Column('vitamin', Float)
    fiber = Column('fiber', Float)
    description = Column('description', String(256))
    
    def __init__(self, date: datetime.date, protein: float, carbon: float, fat: float, mineral: float, vitamin: float, fiber: float, description: str):
        self.date = date
        self.protein = protein
        self.carbon = carbon
        self.fat = fat
        self.mineral = mineral
        self.vitamin = vitamin
        self.fiber = fiber
        self.description = description