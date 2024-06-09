
from sqlalchemy import MetaData, Boolean, Column, Integer, String, Text, DateTime, ForeignKey,Table,Float,JSON
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

import datetime
Base = declarative_base()

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

Base.metadata = MetaData(naming_convention=naming_convention)

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    create_date = Column(DateTime, nullable=True, default=datetime.datetime.now())
    update_date = Column(DateTime, nullable=True, default=datetime.datetime.now())
    delete_yn = Column(Boolean, nullable=True, default=False)

class UserDetail(Base):
    __tablename__ = "user_detail"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    interests = Column(String, nullable=True)
    json_data = Column(JSON, nullable=True)
    create_date = Column(DateTime, nullable=True, default=datetime.datetime.now())
    update_date = Column(DateTime, nullable=True, default=datetime.datetime.now())
    delete_yn = Column(Boolean, nullable=True, default=False)

class Archive(Base):
    __tablename__ = "archive"

    id = Column(Integer, primary_key=True)
    category = Column(String, nullable=False)
    collect_ymd = Column(String, nullable=False)
    language = Column(String, nullable=False)
    title = Column(String, nullable=True)
    author = Column(String, nullable=True)
    content = Column(Text, nullable=False)
    url = Column(String, nullable=False)
    create_date = Column(DateTime, nullable=True, default=datetime.datetime.now())
    update_date = Column(DateTime, nullable=True, default=datetime.datetime.now())
    delete_yn = Column(Boolean, nullable=True, default=False)

class Refine(Base):
    __tablename__ = "refine"

    id = Column(Integer, primary_key=True)
    archive_id = Column(Integer, ForeignKey("archive.id"))
    refine_ymd = Column(String, nullable=False)
    title = Column(String, nullable=True)
    author = Column(String, nullable=True)
    content = Column(Text, nullable=False)
    url = Column(String, nullable=False)
    create_date = Column(DateTime, nullable=True, default=datetime.datetime.now())
    update_date = Column(DateTime, nullable=True, default=datetime.datetime.now())
    delete_yn = Column(Boolean, nullable=True, default=False)