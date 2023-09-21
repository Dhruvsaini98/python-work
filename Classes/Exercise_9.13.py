from random import randint

class Die:
    def __init__(self, num):
        """Initializing the attributes of the class Die"""
        self.sides6 = 6
        self.sides10 = 10
        self.sides20 = 20
        self.num = num
    def roll_die(self):
        random_number = randint(self.num, self.sides20)
        print(f'{random_number}')


random = Die(1)
random.roll_die()
