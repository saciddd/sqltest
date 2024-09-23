from datetime import date
from sqlalchemy import Column, Integer, String, Date
from db import Base

class Personel(Base):
    __tablename__ = 'Personeller'

    PersonelID = Column(Integer, primary_key=True, autoincrement=True)
    PersonelName = Column(String(100), nullable=False)
    PersonelTitle = Column(String(100), nullable=True)
    BirthDate = Column(Date, nullable=True)

    @property
    def Age(self):
        if self.BirthDate:
            today = date.today()
            return today.year - self.BirthDate.year - ((today.month, today.day) < (self.BirthDate.month, self.BirthDate.day))
        return None
