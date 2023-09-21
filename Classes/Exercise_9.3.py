class User:
    def __init__(self, first_name, last_name, username, phone_no, location, gendre) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.phone_no = phone_no
        self.location = location
        self.gendre = gendre

    def describe_user(self):
        print(f"First name: {self.first_name.title()}\nLast name: {self.last_name.title()}\nUsername: {self.username}\nPhone No.:{self.phone_no}\nLocation: {self.location.title()}\nGendre: {self.gendre.title()}")
        
    def message(self):
        print(f"Welcome {self.first_name.title()} {self.last_name.title()} to the website!!")
        print("\n")
first_user = User("dhruv", "saini", "dhruvsaini98", "7714171400", "india", "male")
first_user.describe_user()
first_user.message()

second_user = User("sarthak", "kaushik", "sarthakkaushik98", "7714171400", "india", "male")
second_user.describe_user()
second_user.message()

third_user = User("mehul", "goyal", "mehulgoyal98", "7714171400", "india", "male")
third_user.describe_user()
third_user.message()