import admin_privileges

admin_user = admin_privileges.Admin('Dhruv', 'Saini', 'dhruvsaini98', '7714171400', 'India', 'Male')
admin_user.describe_user()
admin_user.message()
admin_user.privileges.admin_privilegdes = ['Can add a user', 'Can remove a user', 'Can delete the group', 'Can post anything']
admin_user.privileges.admin_privilegde_list()