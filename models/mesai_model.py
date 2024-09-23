from sqlalchemy import Column, Integer, String, Date, ForeignKey
from db import Base

class Mesai(Base):
    __tablename__ = 'Mesailer'

    MesaiID = Column(Integer, primary_key=True, autoincrement=True)
    PersonelID = Column(Integer, ForeignKey('Personeller.PersonelID'))
    MesaiDate = Column(Date, nullable=False)
    MesaiData = Column(String(11), nullable=True)
