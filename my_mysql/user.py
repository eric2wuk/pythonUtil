from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
# 定义User对象:
# 创建对象的基类:
Base = declarative_base()

class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
