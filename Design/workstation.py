from Implementare.user_functions import *

# table_user = get_table_user()
create_new_user('Emanuel', 'emanuel@gamil.com', '1234', 'Timis', 'Timisoara', '0724037007', 300, 2)

table_user = get_table_user()
print(table_user)
# table_user = get_table_user()
# print(table_user)

change_attr('1', {
    'name' : 'Emanuel_1',
    'email' : 'emanuel_1@gmail.com',
    'password' : '1234_parola_1',
    'county' : 'Arad',
    'city' : 'Arad',
    'phone' : '1234567890',
    'avg_consumption' : 400,
    'surface' : 20,

})
