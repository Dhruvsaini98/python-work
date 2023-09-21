def average_num(num_list):
    average = 0
    for n in num_list:
        average = average + n
    return average / len(num_list)

num_list = [11,22,33,44,55,66,77,88,99]
print(average_num(num_list))
