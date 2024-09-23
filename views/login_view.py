import ttkbootstrap as ttk
from tkinter import StringVar, messagebox

class LoginView(ttk.Frame):
    def __init__(self, parent, auth_controller, app_controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.auth_controller = auth_controller
        self.app_controller = app_controller  # App controller referansı ekledim

        self.username_var = StringVar()
        self.password_var = StringVar()

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Kullanıcı Adı").grid(row=0, column=0, padx=10, pady=10)
        ttk.Entry(self, textvariable=self.username_var).grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(self, text="Şifre").grid(row=1, column=0, padx=10, pady=10)
        ttk.Entry(self, textvariable=self.password_var, show='*').grid(row=1, column=1, padx=10, pady=10)

        ttk.Button(self, text="Giriş", command=self.login).grid(row=2, column=1, padx=10, pady=10)

    def login(self):
        username = self.username_var.get()
        password = self.password_var.get()

        success, user = self.auth_controller.login(username, password)
        if success:
            messagebox.showinfo("Başarılı", f"Hoş geldiniz, {user.FullName}!")
            self.app_controller.handle_login(user)  # Giriş başarılı olursa dashboard'a yönlendir
        else:
            messagebox.showerror("Hata", "Giriş başarısız! Kullanıcı adı veya şifre hatalı.")