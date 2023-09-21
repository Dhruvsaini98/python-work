def armstrong(num):
    result = 0
    for i in num:
        result = result + int(i) ** len(num)

    return int(num) == result

num = input("Enter a number: ")
print(armstrong(num))