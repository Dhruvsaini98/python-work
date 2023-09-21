def fibonacci(n):
    fibo = []
    n1,n2 = 0,1
    fibo.append(n1)
    fibo.append(n2)
    if n <= 0:
        return None
    elif n == 1:
        return fibo[0]
    else:
        for i in range(1,n-1):
           n3 = n1 + n2
           fibo.append(n3)
           n1 = n2
           n2 = n3
        return fibo

n = int(input("Enter a number: "))
result = fibonacci(n)
if result == None:
    print("Please enter number greater than 0")
elif result == 0:
    print(result)
else: 
    for r in result:
        print(r)