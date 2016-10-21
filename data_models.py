from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Resource(Base):
     __tablename__ = 'Resource'

     id = Column(Integer, primary_key=True)
     name = Column(String(100))
     value = Column(String(100))

class Role(Base):
    __tablename__ = 'Role'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))

class Action(Base):
    __tablename__ = 'Action'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    value = Column(String(100))

class Permission(Base):
    __tablename__ = 'Permission'
    id = Column(Integer, primary_key=True)
    value = Column(String(100))


class __ResourceRoleAssociation(Base):
    __tablename__ = '__ResourceRoleAssociation'
    resource_id = Column(Integer, ForeignKey('Resource.id'))
    resource = relationship("Resource")
    role_id = Column(Integer, ForeignKey('Role.id'))
    role = relationship("Role")

class __UserRoleAssociation(Base):
    pass

class UserRole(Base):
    __tablename__ = 'UserRole'
    id = Column(Integer, primary_key=True)


