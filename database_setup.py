
import sys
from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

from passlib.apps import custom_app_context as pwd_context

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(32), nullable=False)


class Project(Base):
    __tablename__ = 'project'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    # @property
    # def serialize(self):
    #     # Returns object data in easily serializable format
    #     return {
    #         'name' : self.name,
    #         'id' : self.id,
    #         'price' : self.price,
    #         'course' : self.course
    #     }

# Insert at end of file

engine = create_engine('sqlite:///capexprojectswithusers.db')
Base.metadata.create_all(engine)
