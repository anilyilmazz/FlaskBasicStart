from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Users(Base):

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

engine = create_engine('sqlite:///test.db', echo=True)
#Base.metadata.drop_all(bind=engine)
#Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)