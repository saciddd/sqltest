import ttkbootstrap as ttk
from tkinter import StringVar, messagebox

class PersonelView(ttk.Frame):
    def __init__(self, parent, personel_controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.personel_controller = personel_controller

        self.name_var = StringVar()
        self.title_var = StringVar()
        self.birthdate_var = StringVar()

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Personel Adı").grid(row=0, column=0, padx=10, pady=10)
        ttk.Entry(self, textvariable=self.name_var).grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(self, text="Görevi").grid(row=1, column=0, padx=10, pady=10)
        ttk.Entry(self, textvariable=self.title_var).grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(self, text="Doğum Tarihi").grid(row=2, column=0, padx=10, pady=10)
        ttk.Entry(self, textvariable=self.birthdate_var).grid(row=2, column=1, padx=10, pady=10)

        ttk.Button(self, text="Kaydet", command=self.add_personel).grid(row=3, column=1, padx=10, pady=10)

    def add_personel(self):
        name = self.name_var.get()
        title = self.title_var.get()
        birthdate = self.birthdate_var.get()

        # Personel ekleme işlemi
        new_personel = self.personel_controller.add_personel(name, title, birthdate)
        if new_personel:
            messagebox.showinfo("Başarılı", "Personel başarıyla eklendi!")
        else:
            messagebox.showerror("Hata", "Personel eklenirken bir hata oluştu.")
