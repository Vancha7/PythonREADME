# Задача №1 | Создание класса и общие атрибуты
# 1. Создай класс с именем Robot.
# 2. Добавь в класс общий (классовый) атрибут species.
#    Установи для него значение "Humanoid Robot".
# 3. Код должен содержать только объявление класса и атрибута.
#    Ничего выводить на экран не нужно.
from ast import increment_lineno
from itertools import product
from turtledemo.penrose import start


class Robot:
    species="Humanoid Robot"

# Задача №2 | Конструктор __init__
# 1. Создай класс Dog.
# 2. Добавь конструктор (метод __init__), который принимает параметры:
#    - name (кличка)
#    - age (возраст)
# 3. Внутри конструктора сохрани эти параметры как атрибуты экземпляра
#    (self.name и self.age).
# 4. Ничего выводить на экран не нужно.
class  Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Задача №3 | Объект класса
# 1. Используй класс Dog из предыдущей задачи (или создай его заново).
# 2. Создай экземпляр (объект) класса Dog с именем "Rex" и возрастом 5.
# 3. Сохрани этот объект в переменную my_dog.
# 4. Ничего выводить на экран не нужно.
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
my_dog = Dog("Rex", 5)

# Задача №4 | Методы класса
# 1. Создай класс Car.
# 2. Добавь конструктор (__init__), который принимает параметр brand (марка)
#    и сохраняет его как атрибут экземпляра self.brand.
# 3. Добавь метод info, который возвращает строку вида:
#    "Марка автомобиля: {brand}"
#    (метод ничего не выводит на экран, а именно возвращает строку).
# 4. Код должен содержать только объявление класса.
class Car:
    def __init__(self, brand):
        self.brand = brand
    def display_info(self):
        return "Марка автомобиля: " + self.brand + " ."

# Задача №5 | Понимание параметра self
# 1. Создай класс Counter.
# 2. Добавь конструктор, который принимает начальное значение start
#    и сохраняет его в атрибут экземпляра self.value.
# 3. Добавь метод increment, который увеличивает self.value на 1.
#    Метод ничего не принимает (кроме self) и ничего не возвращает.
# 4. Добавь метод get_value, который возвращает текущее self.value.
# 5. Код должен содержать только объявление класса.
class Counter:
    def __init__(self, start):
        self.value = start
    def increment(self):
        self.value += 1
    def get_value(self):
       return self.value

# Задача №6 | Общие атрибуты и объекты
# 1. Создай класс Employee.
# 2. Добавь общий (классовый) атрибут company со значением "TechCorp".
# 3. Добавь конструктор, который принимает name и сохраняет как атрибут экземпляра.
# 4. Создай два объекта Employee: с именами "Anna" и "Oleg".
# 5. Сохрани их в переменные emp1 и emp2 соответственно.
# 6. Код должен содержать объявление класса и создание объектов.
class Employee:
    company = "TechCorp"
    def __init__(self, name):
        self.name = name
emp1 = Employee("Anna")
emp2 = Employee("Oleg")

# Задача №7 | Методы с возвратом значений
# 1. Создай класс Rectangle.
# 2. Добавь конструктор, который принимает width и height (ширина и высота)
#    и сохраняет их как атрибуты экземпляра.
# 3. Добавь метод area, который возвращает площадь прямоугольника.
# 4. Добавь метод perimeter, который возвращает периметр.
# 5. Код должен содержать только объявление класса.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return (self.width + self.height) * 2

# Задача №8 | Атрибуты по умолчанию в конструкторе
# 1. Создай класс Book.
# 2. Добавь конструктор с параметрами:
#    - title (обязательный)
#    - author (обязательный)
#    - year (необязательный, значение по умолчанию — 2023)
# 3. Сохрани все три параметра как атрибуты экземпляра.
# 4. Код должен содержать только объявление класса.\
class Book:
    def __init__(self, title , author, year=2023):
        self.title = title
        self.author = author
        self.year = year

# Задача №9 | Строковое представление объекта
# 1. Создай класс Person.
# 2. Добавь конструктор, который принимает name и age.
# 3. Добавь метод __str__, который возвращает строку:
#    "Имя: {name}, Возраст: {age}"
# 4. Код должен содержать только объявление класса.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Имя: {self.name}, Возраст: {self.age}"

# Задача №10 | Взаимодействие методов
# 1. Создай класс BankAccount.
# 2. Добавь конструктор, который принимает owner (владелец)
#    и устанавливает начальный баланс balance = 0.
# 3. Добавь метод deposit(amount), который увеличивает баланс на amount.
# 4. Добавь метод withdraw(amount), который уменьшает баланс на amount,
#    но только если на счету достаточно средств.
#    Если средств недостаточно, баланс не меняется.
#    Метод ничего не возвращает и ничего не выводит.
# 5. Добавь метод get_balance, который возвращает текущий баланс.
# 6. Код должен содержать только объявление класса.
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
            self.balance += amount
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
    def get_balance(self):
        return self.balance

# Задача №11 | Общие атрибуты и методы класса
# 1. Создай класс Library.
# 2. Добавь общий (классовый) атрибут total_books = 0.
# 3. Добавь конструктор, который принимает name (название библиотеки)
#    и сохраняет как атрибут экземпляра.
# 4. Добавь метод add_book, который увеличивает общий счётчик total_books на 1.
#    Метод ничего не принимает (кроме self) и ничего не возвращает.
# 5. Добавь классовый метод get_total_books, который возвращает значение total_books.
#    (Не забудь про декоратор @classmethod)
# 6. Код должен содержать только объявление класса.
class Library:
    total_books = 0
    def __init__(self, name):
        self.name = name
    def add_book(self):
        type(self).total_books += 1
    @classmethod
    def get_total_books(cls):
        return cls.total_books

# Задача №12 | Статические методы
# 1. Создай класс MathUtils.
# 2. Добавь статический метод add, который принимает два числа и возвращает их сумму.
#    (Не забудь про декоратор @staticmethod)
# 3. Добавь статический метод multiply, который принимает два числа и возвращает их произведение.
# 4. Код должен содержать только объявление класса.
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    @staticmethod
    def multiply(a, b):
        return a * b

# Задача №13 | Свойства (property)
# 1. Создай класс Circle.
# 2. Добавь конструктор, который принимает radius и сохраняет его в атрибут _radius.
# 3. Добавь метод radius (геттер) с декоратором @property,
#    который возвращает значение _radius.
# 4. Добавь метод radius (сеттер) с декоратором @radius.setter,
#    который принимает новое значение и проверяет:
#    - если значение > 0, сохраняет его в _radius
#    - если значение <= 0, ничего не меняет (просто пропускает)
# 5. Код должен содержать только объявление класса.
class  Circle:
    def __init__(self, radius):
        self._radius = radius
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value

# Задача №14 | Инкапсуляция (приватные атрибуты)
# 1. Создай класс Student.
# 2. Добавь конструктор, который принимает name и grade (оценка).
# 3. Сделай так, чтобы атрибут grade был "приватным" (с двумя подчёркиваниями в начале: __grade).
# 4. Добавь метод get_grade, который возвращает текущее значение __grade.
# 5. Добавь метод set_grade, который принимает новое значение и проверяет:
#    - если значение от 2 до 5 включительно, сохраняет его в __grade
#    - если значение вне этого диапазона, ничего не меняет
# 6. Код должен содержать только объявление класса.
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade
    def get_grade(self):
        return self.__grade
    def set_grade(self,new_grade):
        if 2 <= new_grade <= 5:
            self.__grade = new_grade

# Задача №15 | Магический метод __len__
# 1. Создай класс Playlist.
# 2. Добавь конструктор, который принимает название плейлиста (name)
#    и создаёт пустой список songs (атрибут экземпляра).
# 3. Добавь метод add_song, который принимает название песни и добавляет её в список songs.
# 4. Добавь магический метод __len__, который возвращает количество песен в плейлисте (длину списка songs).
# 5. Код должен содержать только объявление класса.
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
    def add_song(self, name_song):
        self.songs.append(name_song)
    def __len__(self):
        return len(self.songs)

# Задача №16 | Сравнение объектов (__eq__)
# 1. Создай класс Product.
# 2. Добавь конструктор, который принимает name и price.
# 3. Добавь магический метод __eq__, который сравнивает два товара.
#    Два товара считаются равными, если у них одинаковые name И price.
# 4. Код должен содержать только объявление класса.
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __eq__(self, other):
        return self.name == other.name and self.price == other.price

# Задача №17 | Наследование (базовый класс)
# 1. Создай класс Animal.
# 2. Добавь конструктор, который принимает name и сохраняет как атрибут.
# 3. Добавь метод speak, который возвращает строку "Some sound".
# 4. Создай класс Dog, который наследует от Animal.
# 5. В классе Dog переопредели метод speak так, чтобы он возвращал "Woof!".
# 6. Код должен содержать только объявление классов.
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "Some sound"
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Задача №18 | Наследование и super()
# 1. Создай класс Employee (сотрудник).
# 2. Добавь конструктор, который принимает name и salary.
# 3. Создай класс Manager, который наследует от Employee.
# 4. В конструкторе Manager добавь третий параметр department.
# 5. Используй super(), чтобы вызвать конструктор родителя и передать ему name и salary,
#    а department сохрани как атрибут экземпляра в самом Manager.
# 6. Код должен содержать только объявление классов.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
class Manager(Employee):
    def __init__(self,name, salary, department):
        super().__init__(name, salary)
        self.department = department

# Задача №19 | Множественное наследование
# 1. Создай класс Flyer с методом fly, который возвращает "Flying".
# 2. Создай класс Swimmer с методом swim, который возвращает "Swimming".
# 3. Создай класс Duck, который наследует от Flyer и Swimmer.
#    (Порядок наследования: сначала Flyer, потом Swimmer)
# 4. В классе Duck не нужно добавлять новые методы или конструктор.
# 5. Код должен содержать только объявление трёх классов.
class Flyer:
    def fly(self):
        return "Flying"
class Swimmer:
    def swim(self):
        return "Swimming"
class Duck(Flyer, Swimmer):

# Задача №20 | Методы и атрибуты экземпляра
# 1. Создай класс Smartphone.
# 2. Добавь конструктор, который принимает brand и model.
# 3. Добавь метод make_call, который принимает phone_number и возвращает строку:
#    "Calling {phone_number} from {brand} {model}"
# 4. Код должен содержать только объявление класса.
class Smartphone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def make_call(self, phone_number):
        return f"Calling {phone_number} from {self.brand} {self.model}"

