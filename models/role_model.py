from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db import Base

class Role(Base):
    __tablename__ = 'Roles'

    RoleID = Column(Integer, primary_key=True, autoincrement=True)
    RoleName = Column(String(100), nullable=False)

    # Bir rolün birden fazla kullanıcısı olabilir
    users = relationship("User", back_populates="role")