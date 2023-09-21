class User:
    def __init__(self, first_name, last_name, username, phone_no, location, gendre) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.phone_no = phone_no
        self.location = location
        self.gendre = gendre
        self.login_attempts = 0

    def describe_user(self):
        print(f"First name: {self.first_name.title()}\nLast name: {self.last_name.title()}\nUsername: {self.username}\nPhone No.:{self.phone_no}\nLocation: {self.location.title()}\nGendre: {self.gendre.title()}\nLogin attempt: {self.login_attempts}")
        
    def message(self):
        print(f"Welcome {self.first_name.title()} {self.last_name.title()} to the website!!\n")
        

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1

    def reset_login_attempt(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, username, phone_no, location, gendre):
        """Initializing the attributes of the parent class"""
        super().__init__(first_name, last_name, username, phone_no, location, gendre)
        self.admin_privilegdes = []

    def admin_privilegde_list(self):
        """Showing admin privilegdes"""
        print(f"{self.first_name} {self.last_name} is the Admin. {self.first_name} {self.last_name} has the following priviledges :")
        for privilegdes in self.admin_privilegdes:
            print(f'- {privilegdes}')

admin_user = Admin('Dhruv', 'Saini', 'dhruvsaini98', '7714171400', 'India', 'Male')
admin_user.describe_user()
admin_user.message()
admin_user.admin_privilegdes = ['Can add a user', 'Can remove a user', 'Can delete the group', 'Can post anything']
admin_user.admin_privilegde_list()