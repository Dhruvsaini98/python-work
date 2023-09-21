from user import User
class Privilegdes():
    def __init__(self):
        super().__init__()
        
        self.privilegdes = []
    def admin_privilegde_list(self):
        """Showing admin privilegdes"""
        print("Admin has the following priviledges :")
        for privilegdes in self.admin_privilegdes:
            print(f'- {privilegdes}')        

class Admin(User):
    def __init__(self, first_name, last_name, username, phone_no, location, gendre):
        """Initializing the attributes of the parent class"""
        super().__init__(first_name, last_name, username, phone_no, location, gendre)
        self.privileges = Privilegdes()