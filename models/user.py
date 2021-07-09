'''
Author: Yang
Date: 2021-07-08 09:54:00
LastEditors: Yang
LastEditTime: 2021-07-09 11:25:07
FilePath: /flaskDemo/ZeeRay/models/user.py
Description: 头部注释
'''
from click.utils import echo
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import false

URI = 'mysql+pymysql://root:12345678@localhost:3306/testDemo?charset=utf8'
engine = create_engine(URI, echo=True)
Base = declarative_base(engine)


class User(Base):
    __tablename__ = 'user'
    # __mapper_args__ = {'column_prerfix': '_'}	# 自动给所有的列添加一个前缀
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    tel = Column(String(20), nullable=False)
    # __repr__ 方法定义了一个对象的比较易读的显式方式

    def __repr__(self):
        tpl = "User(id={},username={},password={},tel={})"
        return tpl.format(self.id, self.username, self.password, self.tel)


Base.metadata.create_all(engine)  # 创建表
