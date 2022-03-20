import datetime

from db import Base

from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.dialects.mysql import INTEGER, BOOLEAN

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
    
    protein = Column('protein', INTEGER(unsigned=True))
    carbon = Column('carbon', INTEGER(unsigned=True))
    fat = Column('fat', INTEGER(unsigned=True))
    mineral = Column('mineral', INTEGER(unsigned=True))
    vitamin = Column('vitamin', INTEGER(unsigned=True))
    fiber = Column('fiber', INTEGER(unsigned=True))
    description = Column('description', String(256))
    
    def __init__(self, date: datetime.date, protein: int, carbon: int, fat: int, mineral: int, vitamin: int, fiber: int, description: str):
        self.date = date
        self.protein = protein
        self.carbon = carbon
        self.fat = fat
        self.mineral = mineral
        self.vitamin = vitamin
        self.fiber = fiber
        self.description = description