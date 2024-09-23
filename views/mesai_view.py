import ttkbootstrap as ttk
from tkinter import StringVar

class MesaiView(ttk.Frame):
    def __init__(self, parent, mesai_controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.mesai_controller = mesai_controller
        self.start_date_var = StringVar()
        self.end_date_var = StringVar()

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Başlangıç Tarihi").grid(row=0, column=0, padx=10, pady=10)
        ttk.Entry(self, textvariable=self.start_date_var).grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(self, text="Bitiş Tarihi").grid(row=1, column=0, padx=10, pady=10)
        ttk.Entry(self, textvariable=self.end_date_var).grid(row=1, column=1, padx=10, pady=10)

        ttk.Button(self, text="Sorgula", command=self.query_mesai).grid(row=2, column=1, padx=10, pady=10)

    def query_mesai(self):
        start_date = self.start_date_var.get()
        end_date = self.end_date_var.get()

        # Mesai sorgulama işlemi
        mesailer = self.mesai_controller.query_mesai(start_date, end_date)
        print(f"Bulunan mesailer: {mesailer}")

        # Tabloyu oluşturmak için ekleme yapabilirsiniz.
