string = input('Enter a sentence: ')
string1 = string.split()
string5 = []
for string2 in string1:
    string3 = list(string2)
    string3.reverse()
    string4 = ''.join(string3)
    string5.append(string4)
string6 = string5[::-1]
reversed_sentence = ' '.join(string6)
print(reversed_sentence)
#string5.reverse()
#string6 = ' '.join(string5)
#print(string6)