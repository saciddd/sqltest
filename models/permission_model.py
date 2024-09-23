from sqlalchemy import Column, Integer, String
from db import Base

class Permission(Base):
    __tablename__ = 'Permissions'

    PermissionID = Column(Integer, primary_key=True, autoincrement=True)
    PermissionName = Column(String(100), nullable=False)