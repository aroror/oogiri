from flask_sqlalchemy import SQLAlchemy
from app.app import app
from datetime import datetime

class OogiriContent(Base):
    __tablename__ = 'oogiricontents'
    id = Column(Integer, primary_key=True)
    title = Column(String(128), unique=True)
    image_path = Column(String(128))
    date = Column(DateTime, default=datetime.now())
    tags = Column(postgresql.ARRAY(Integer))

    def __init__(self, title=None,image_path=None,tags = None, date=None):
        self.title = title
        self.image_path = image_path
        self.date = date
        self.tags = tags

    def __repr__(self):
        return '<Title %r>' % (self.title)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(128), unique=True)
    hashed_password = Column(String(128))

    def __init__(self, user_name=None, hashed_password=None):
        self.user_name = user_name
        self.hashed_password = hashed_password

    def __repr__(self):
        return '<Name %r>' % (self.user_name)    


