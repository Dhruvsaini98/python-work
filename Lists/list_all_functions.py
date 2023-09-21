countries = ['india', 'srilanka', 'brazil', 'thailand', 'ireland', 'usa', 'australia']

#edit a list element
countries[0] = 'pakistan'
print(countries)

#append() method
countries.append('india')
print(countries)

#insert() method
countries.insert(2, 'argentina')
print(countries)

#del statement
del countries[4]
print(countries)

#pop() method
countries.pop()
print(countries)
countries.pop(-2)
print(countries)

#remove() method
new_list = 'ireland'
countries.remove(new_list)
print(countries)

#sorted() function
print(sorted(countries))
print(countries)
print(sorted(countries, reverse=True))

#reverse() method
countries.reverse()
print(countries)
countries.reverse()
print(countries)

#sort() method
countries.sort()
print(countries)
countries.sort(reverse=True)
print(countries)