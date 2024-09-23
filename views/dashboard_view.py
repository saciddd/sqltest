import ttkbootstrap as ttk

class DashboardView(ttk.Frame):
    def __init__(self, parent, dashboard_controller, user, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.dashboard_controller = dashboard_controller
        self.user = user

        self.create_widgets()

    def create_widgets(self):
        welcome_message = self.dashboard_controller.get_welcome_message(self.user)
        ttk.Label(self, text=welcome_message, font=("Helvetica", 16)).pack(padx=20, pady=20)

        # Menü ağacını buraya ekleyebilirsin
        self.create_menu()

    def create_menu(self):
        menu_tree = ttk.Treeview(self)
        menu_tree.insert("", "end", "mesai", text="Mesai Yönetimi")
        menu_tree.insert("", "end", "personel", text="Personel Yönetimi")

        # Menüyü ekranda göster
        menu_tree.pack(padx=20, pady=20)

        menu_tree.bind("<Double-1>", self.on_menu_select)

    def on_menu_select(self, event):
        item = event.widget.selection()[0]
        if item == "mesai":
            # Mesai ekranına geçiş
            print("Mesai yönetimi")
        elif item == "personel":
            # Personel yönetimi ekranına geçiş
            print("Personel yönetimi")
