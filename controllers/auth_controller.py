from sqlalchemy.orm import Session
from models.user_model import User
from models.role_model import Role

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

    def has_permission(self, user, permission_name: str) -> bool:
        """
        Kullanıcının belirli bir yetkiye sahip olup olmadığını kontrol eder.
        :param user: Giriş yapmış kullanıcı
        :param permission_name: Kontrol edilecek yetkinin adı (örneğin 'mesai', 'personel')
        :return: Boolean (True or False)
        """
        # Kullanıcının rollerini ve yetkilerini alalım
        roles = self.db_session.query(Role).filter(Role.RoleID == user.RoleID).all()
        
        for role in roles:
            if role.RoleName == permission_name:
                return True
        return False

