#Задача 1. Переменные и типы данных.
import csv
from itertools import count

number = 42
number_str = str(number)
text = "The answer is:"
result = number_str + " " + text
print(f"Значение: 'number' =  {number}, тип данных: {type(number)}")
print(f"Значение: 'number_str' = {number_str}, тип данных: {type(number_str)}")
print(f"Значение: 'text' = {text}, тип данных: {type(text)}")
print(f"Значение: 'result' = {result}, тип данных: {type(result)}")

#Задача 2. Строки.
name = "Иван"
age = 23
print(f"Меня зовут {name}, мне {age} года.")

#Задача 3. Списки.
my_list = [1, 2, 3]
copy_list = my_list.copy()
copy_list[0] = 10
print(my_list)
print(copy_list)

#Задача 4. Условные операторы.
inp1 = int(input("Введите число: "))
if inp1 > 0:
    print("Положительное")
elif inp1 == 0:
    print("Ноль")
elif inp1 < 0:
    print("Отрицательное")

#Задача 5. Словари.
person = {
    "name":{
        "first_name":"Иван",
        "last_name":"Иванов"
},
    "adress":{
        "city":"Москва",
        "country":"Россия",
    }
}
person["adress"]["city"] = "Санкт - Петербург"
person["adress"]["postal_code"] = "333777"
print(person)
del person["adress"]["city"]
print(person)

#Задача 6. Циклы.
count = 1
while count <= 20:
    if count % 4 == 0:
        count += 1
        continue
    print(count)
    count += 1

#Задача 7. Файлы.
with open("fruits.txt", "w", encoding="utf-8") as file:
    file.write("яблоко \nбанан \nапельсин")

with open("fruits.txt", "r", encoding="utf-8") as file:
    readd= file.read()
    print(readd)
# Забыл как пропускать :)

#Задача 8. Функции.
def greet_user(user_role, user_name = ):
    if user_name == "":
        print(f"Привет, {user_name}")
    elif user_name == "" and user_role == "<UNK>":
#Забыл)!


#Задача 9. ООП ч.1
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
student = Student("Иван", 23)
print(student.name, student.age)

#Задача 10. ООП ч.2
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def eat(self):
        pass
    def sleep(self):
        pass
class Dog(Animal):
    def bark(self):
        pass
my_dog = Dog("Барсик", "Собака")
my_dog.eat()
my_dog.sleep()
my_dog.bark()