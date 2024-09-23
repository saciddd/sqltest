from sqlalchemy import Column, Integer, ForeignKey
from db import Base

class RolePermission(Base):
    __tablename__ = 'RolePermissions'

    RoleID = Column(Integer, ForeignKey('Roles.RoleID'), primary_key=True)
    PermissionID = Column(Integer, ForeignKey('Permissions.PermissionID'), primary_key=True)