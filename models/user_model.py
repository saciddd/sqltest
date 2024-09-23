from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class User(Base):
    __tablename__ = 'Users'

    UserID = Column(Integer, primary_key=True, autoincrement=True)
    Username = Column(String(100), nullable=False, unique=True)
    Password = Column(String(50), nullable=False)  # Geçici olarak password hash kullanmıyoruz
    FullName = Column(String(150), nullable=False)
    RoleID = Column(Integer, ForeignKey('Roles.RoleID'))

    # İlişki tanımlama (bir kullanıcının bir rolü vardır)
    role = relationship("Role", back_populates="users")
