from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import declarative_base

postgres_db="postgresql+psycopg2://vic:Vatika%4024.sql@127.0.0.1:5432/my_db"

engine=create_engine(postgres_db)
Base= declarative_base()

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    age=Column(Integer)

Base.metadata.create_all(engine)

