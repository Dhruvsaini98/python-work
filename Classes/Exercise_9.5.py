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
        print(f"Welcome {self.first_name.title()} {self.last_name.title()} to the website!!")
        print("\n")

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1

    def reset_login_attempt(self):
        self.login_attempts = 0

first_user = User("dhruv", "saini", "dhruvsaini98", "7714171400", "india", "male")

first_user.increment_login_attempts()
first_user.increment_login_attempts()
first_user.increment_login_attempts()
first_user.describe_user()
first_user.message()
first_user.reset_login_attempt()
first_user.describe_user()


