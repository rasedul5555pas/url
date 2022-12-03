# number = int(input('Enter your number: '))
# start = 1
# while number <= 10:
#     print(number, 'x', start, '=', number* start)
#     start = start + 1

# name = ['rahim', 'karim', 'sumon', 'rasel', 'roton', 'jamal', 'hanif']
# i = 0
# while i < len(name):
#     print(name[i])
#     i = i + 1

# number = int(input('Enter your number: '))
# start = 1
# while start <= 10:
#     print(number, 'x', start, '=', number * start)
#     start = start + 1


# number = int(input("enter your number: "))
# r = 1
#
# while r <= 10:
#     print(number, 'x', r, '=', number * r)
#     r = r + 1

#
# years = [2020, 2000, 2004, 2008, 1994, 1988, 1230, 1520]
# i = 0
# while i < len(years):
#     if years[i] % 4 == 0:
#         print(years[i], 'is Leap Year.')
#     i = i +1

# person_one = ['Asif', 'India', '10th July 1988', 'asif@gmail.com', '01814703329']
#
# line = f'{person_one[0].title()} is a good boy. He was born {person_one[2]} in {person_one[1].title()}. He is available in {person_one[3]}. {person_one[-1]} him mobile number.'
#
# print(line)

# import random
# ludu = [1,2,3,4,5,6]
#
# random_number = random.choice(ludu)
# if random_number == 6:
#     print('yes, you won the game.')
# else:
#     print(random_number, 'is not 6.')

#
# students = [ ]
# while True:
#     name = input('Enter students name: ')
#     if name == 'shesh':
#         print(students)
#         print('Total Students: ', len(students))
#         break
#     else:
#         students.append(name)


# import random
# number = [1,2,3,4,5,6,7,8,9,0,]
#
# print('Lets play a game guess a number from 0-9')
# print('**'*20)
#
# pc_number= random.choice(number)
# while True:
#     number = int(input('Enter your guess number: '))
#     if pc_number == number:
#         print('Congratulation')
#         break
#     else:
#         print('Hoy nai.')


# person = ['Asif', 'India', 'rohim', 'korim', 'belal']
#
# for man in person:
#     print(man)

# user = {
#     'id': 1,
#     'first_name': 'Rahman',
#     'last_name': 'Islam',
#     'mail': 'test@gmail.com',
#     'username': 'rislam',
#     'password': '123456',
#      'role': 'admin' ,
#
# }


# first_name = user['first_name']
# last_name = user['last_name']
# print(first_name, last_name)

# first_name = user.get('first_name')
# print(first_name)

# keys = user.keys()
# values = user.values()
# print(list(keys))
# print(list(values))

post = {'id': 1,
'first_name': 'Rahman',
'last_name': 'Islam',
'mail': 'test@gmail.com',
'username': 'rislam',
'password': '123456',
'role': 'admin',
        }

# post['role'] = 'model'
# post.update({'sticky': True})
# post.update({'father_name' : 'sofi'})
#
#
# print(post)
# print(post.get('mail'))

# car = {
#         'name': "Toyota",
#         'model': "Axio",
#         'year': 2014,
#         'color': 'red'
# }
#
# # print(car.get('name'))
# car.update({"model": 'Primio'})
# car.pop('color')
# car.pop('year')
# print(car)

# car = [
#         {
#         'name': "Toyota",
#         'model': "Axio",
#         'year': 2014,
#         'color': 'red'
# },
#
#   {
#         'name': "Honda",
#         'model': "dazzel",
#         'year': 2016,
#         'color': 'yello'
# }
#
# ]
# for gari in car:
#         print(gari.get('model'))































