class DashboardController:
    def __init__(self, db_session):
        self.db_session = db_session  # db_session burada tanımlanıyor

    def get_welcome_message(self, user):
        """Kullanıcıya özel bir hoş geldiniz mesajı döndür"""
        return f"Hoş geldiniz, {user.FullName}!"

    def get_user_permissions(self, user):
        """Kullanıcının yetkilerine göre ana menü öğelerini oluştur"""
        # Kullanıcının yetkilerini sorgulamak için db_session'i kullanıyoruz
        permissions = [perm.PermissionName for perm in user.role.permissions]
        return permissions
