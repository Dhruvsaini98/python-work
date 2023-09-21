from random import choice

lottery = [2, 4, 7, 10, 12, 56, 67, 45, 23, 69,'a', 'd', 'z', 't', 'r']
lottery_numbers = choice(lottery)
lottery_numbers1 = choice(lottery)
lottery_numbers2 = choice(lottery)
lottery_numbers3 = choice(lottery)
print(f'Any ticket containing numbers or letters - {lottery_numbers}, {lottery_numbers1}, {lottery_numbers2}, {lottery_numbers3} wins the lottery')