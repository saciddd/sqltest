from controllers import auth_controller
from views.dashboard_view import DashboardView
from views.login_view import LoginView
from views.mesai_view import MesaiView
from views.personel_view import PersonelView
import tkinter as tk
from tkinter import Frame, Menu

class AppController:
    def __init__(self, root, auth_controller, dashboard_controller, mesai_controller, personel_controller):
        self.root = root  # Ana pencereyi burada kullanıyoruz
        self.auth_controller = auth_controller
        self.dashboard_controller = dashboard_controller
        self.mesai_controller = mesai_controller
        self.personel_controller = personel_controller
        self.active_user = None
        self.main_frame = None
        self.left_menu = None

    def clear_main_frame(self):
        """Ana ekranı temizle"""
        if self.main_frame is not None:
            self.main_frame.destroy()  # Mevcut ana çerçeveyi yok et
        self.main_frame = Frame(self.root)  # Yeni bir ana çerçeve oluştur
        self.main_frame.pack(fill="both", expand=True)


    def show_login(self, login_view):
        """Login ekranını göster"""
        self.clear_main_frame()  # Eski içerikleri temizle
        login_view.pack(fill="both", expand=True)


    def setup_menu(self):
        """Sol tarafta hamburger menüsü oluştur"""
        menu_bar = Menu(self.root)
        self.root.config(menu=menu_bar)

        # Hamburger menüsü
        hamburger_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Menü", menu=hamburger_menu)

        # Yetkili olduğu menüler ekleniyor
        hamburger_menu.add_command(label="Dashboard", command=self.show_dashboard)
        hamburger_menu.add_command(label="Mesai Yönetimi", command=self.show_mesai)
        hamburger_menu.add_command(label="Personel Yönetimi", command=self.show_personel)
        hamburger_menu.add_command(label="İstatistik", command=self.show_dashboard)

        if self.auth_controller.has_permission(self.active_user, 'mesai'):
            hamburger_menu.add_command(label="Mesai Yönetimi", command=self.show_mesai)
        if self.auth_controller.has_permission(self.active_user, 'personel'):
            hamburger_menu.add_command(label="Personel Yönetimi a1", command=self.show_personel)
        if self.auth_controller.has_permission(self.active_user, 'İstatistik'):
            hamburger_menu.add_command(label="İstatistik Sayfası", command=self.show_personel)

        hamburger_menu.add_separator()
        hamburger_menu.add_command(label="Çıkış", command=self.logout)

    def show_dashboard(self):
        """Dashboard görünümüne geçiş yap"""
        self.clear_main_frame()  # Öncelikle mevcut ana çerçeveyi temizle
        print("Dashboard oluşturuluyor")
        # Dashboard ekranını oluştur
        self.dashboard_view = DashboardView(self.main_frame, self.dashboard_controller, self.active_user)
        self.dashboard_view.pack(fill="both", expand=True)

        # Menü görünümünü başlat
        self.setup_menu()

    def handle_login(self, user):
        """Login sonrası dashboard ekranına geçiş"""
        print(">>>Login işlemi başladı.")
        self.active_user = user
        self.show_dashboard()

    def show_mesai(self):
        """Mesai yönetim ekranını göster"""
        self.clear_main_frame()
        mesai_view = MesaiView(self.main_frame, self.mesai_controller)
        mesai_view.pack(fill="both", expand=True)

    def show_personel(self):
        """Personel yönetim ekranını göster"""
        self.clear_main_frame()
        personel_view = PersonelView(self.main_frame, self.personel_controller)
        personel_view.pack(fill="both", expand=True)

    def logout(self):
        """Çıkış yap ve giriş ekranına dön"""
        self.active_user = None
        for widget in self.root.winfo_children():
            widget.destroy()
        if self.main_frame is not None:
            self.main_frame.destroy()  # Mevcut ana çerçeveyi yok et
        # Giriş ekranını göster
        login_view = LoginView(self, auth_controller, self)
        self.show_login(login_view)
