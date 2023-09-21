import module_of_815 

user_profile = module_of_815.build_profile('Dhruv', 'Saini', Weight = '68', Height = '170cm', Hobbies = 'Reading')
print(user_profile)


from module_of_815 import build_profile

user_profile = build_profile('Dhruv', 'Saini', Weight = '68', Height = '170cm', Hobbies = 'Reading')
print(user_profile)


from module_of_815 import build_profile as bp

user_profile = bp('Dhruv', 'Saini', Weight = '68', Height = '170cm', Hobbies = 'Reading')
print(user_profile)


import module_of_815 as mn 

user_profile = mn.build_profile('Dhruv', 'Saini', Weight = '68', Height = '170cm', Hobbies = 'Reading')
print(user_profile)


from module_of_815 import *

user_profile = build_profile('Dhruv', 'Saini', Weight = '68', Height = '170cm', Hobbies = 'Reading')
print(user_profile)