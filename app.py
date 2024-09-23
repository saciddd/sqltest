from tkinter import Tk
from controllers.app_controller import AppController
from controllers.auth_controller import AuthController
from controllers.dashboard_controller import DashboardController
from controllers.mesai_controller import MesaiController
from controllers.personel_controller import PersonelController
from views.login_view import LoginView
from db import SessionLocal

class Application(Tk):
    def __init__(self):
        super().__init__()
        self.title("Mesai Yönetim Sistemi")
        self.geometry("1024x768")
        
        # Veritabanı bağlantısını al
        self.db_session = SessionLocal()

        # Controller'lar
        auth_controller = AuthController(self.db_session)
        dashboard_controller = DashboardController(self.db_session)
        mesai_controller = MesaiController(self.db_session)
        personel_controller = PersonelController(self.db_session)

        # AppController
        self.app_controller = AppController(self, auth_controller, dashboard_controller, mesai_controller, personel_controller)
        
        # Giriş ekranını göster
        login_view = LoginView(self, auth_controller, self.app_controller)
        self.app_controller.show_login(login_view)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
