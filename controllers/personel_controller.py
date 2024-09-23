from sqlalchemy.orm import Session
from models.personel_model import Personel
from datetime import datetime

class PersonelController:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def add_personel(self, name: str, title: str, birthdate: datetime):
        new_personel = Personel(
            PersonelName=name,
            PersonelTitle=title,
            BirthDate=birthdate
        )
        self.db_session.add(new_personel)
        self.db_session.commit()
        return new_personel

    def get_all_personel(self):
        personeller = self.db_session.query(Personel).all()
        return personeller

    def update_personel(self, personel_id: int, name: str, title: str, birthdate: datetime):
        personel = self.db_session.query(Personel).filter(Personel.PersonelID == personel_id).first()
        if personel:
            personel.PersonelName = name
            personel.PersonelTitle = title
            personel.BirthDate = birthdate
            self.db_session.commit()
            return True
        return False
