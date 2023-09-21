def tempt_convert(c):
    f = (c * 1.8) + 32
    return f

c = float(input("Enter tempterature in celcius: "))
result = tempt_convert(c)
print(result)
    