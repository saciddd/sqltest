from sqlalchemy.orm import Session
from models.user_model import User
from models.role_model import Role
#from werkzeug.security import check_password_hash  # Password hashing için kullanabilirsin

class AuthController:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def login(self, username: str, password: str):
        user = self.db_session.query(User).filter(User.Username == username).first()
        if user and user.Password == password:  # Şimdilik password hash yok
            # Oturum oluşturma işlemleri (örneğin kullanıcı id'sini saklama)
            return True, user  # Başarılı giriş
        return False, None  # Başarısız giriş

    def logout(self):
        # Oturum sonlandırma işlemleri (örneğin session veya token temizleme)
        pass
