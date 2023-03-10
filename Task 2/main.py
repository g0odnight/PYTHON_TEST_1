from operator import *
import operator


# Turimas "users" masyvas. 

# Parašykite funkcijas, kurios atlikas nurodytas užduotis:
# 1. funkcija "getUserAverageAge" - kaip argumentą priims masyvą ir duoto masyvo 
# atveju grąžins visų "users" amžiaus visurkį kaip skaičių.
# 2. funkcija "getUsersNames" -  kaip argumentą priims masyvą ir duoto masyvo 
# atveju grąžins visų "users" vardus naujame list'e pvz., ['Alex John', 'Ann Smith'...].

# Pastaba: rezultatai turi būti išrikiuoti abėcėlės tvarka

users = [
  { "id": '1', "name": 'John Smith', "age": 20 },
  { "id": '2', "name": 'Ann Smith', "age": 24 },
  { "id": '3', "name": 'Tom Jones', "age": 31 },
  { "id": '4', "name": 'Rose Peterson', "age": 17 },
  { "id": '5', "name": 'Alex John', "age": 25 },
  { "id": '6', "name": 'Ronald Jones', "age": 63 },
  { "id": '7', "name": 'Elton Smith', "age": 16 },
  { "id": '8', "name": 'Simon Peterson', "age": 30 },
  { "id": '9', "name": 'Daniel Cane', "age": 51 },
]

#1 
print('------------------------------------------------------------')

def getUserAverageAge(users): 
    usersAgeAverage = sum(item['age'] for item in users) / len(users)
    print('The average age of all users is:',round(usersAgeAverage, 2))
    print(type(usersAgeAverage))

getUserAverageAge(users)

#2 
print('------------------------------------------------------------')


def filterAdults(users): 
    usersName =[]
    for i in users:
          usersName.append(i["name"])
          sortedUsersNames = sorted(usersName)
    print(sortedUsersNames)

filterAdults(users)

print('------------------------------------------------------------')