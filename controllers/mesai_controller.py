from sqlalchemy.orm import Session
from models.mesai_model import Mesai
from models.personel_model import Personel
from datetime import datetime

class MesaiController:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def query_mesai(self, start_date: datetime, end_date: datetime):
        mesailer = (
            self.db_session.query(Mesai, Personel)
            .join(Personel, Mesai.PersonelID == Personel.PersonelID)
            .filter(Mesai.MesaiDate >= start_date, Mesai.MesaiDate <= end_date)
            .all()
        )
        return mesailer

    def update_mesai(self, mesai_id: int, new_shift_type: str):
        mesai = self.db_session.query(Mesai).filter(Mesai.MesaiID == mesai_id).first()
        if mesai:
            mesai.ShiftType = new_shift_type
            self.db_session.commit()
            return True
        return False
