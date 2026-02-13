# Задание 1: Базовое наследование
# 1. Создай родительский класс `Transport`.
#    Добавь для него метод `move`, который будет выводить на экран фразу "Транспорт движется".
# 2. Создай дочерний класс `Car`, который наследуется от `Transport`.
#    Не добавляй пока в него никаких новых методов или атрибутов.
# 3. Создай объект (экземпляр) класса `Car` и вызови у него метод `move()`.
#    Убедись, что он выведет фразу от родительского класса.

class Transport:
    def move(self):
        print("Транспорт движется")

class Car(Transport):
    pass
car = Car()
car.move()

# Задание 2: Переопределение методов (Method Overriding)
# 1. Используй классы из предыдущей задачи (или создай заново):
#    - Родительский класс `Transport` с методом `move`, который выводит "Транспорт движется".
# 2. Создай дочерний класс `Bicycle` (Велосипед), который наследуется от `Transport`.
# 3. В классе `Bicycle` переопредели (напиши заново) метод `move` так,
#    чтобы он выводил на экран фразу "Велосипед крутит педали".
# 4. Создай объект класса `Bicycle` и вызови у него метод `move()`.
#    Убедись, что выводится фраза про велосипед, а не про транспорт.

class Transport:
    def move(self):
        print("Транспорт движется")

class Bicycle(Transport):
    def move(self):
        print("Велосипед крутит педали")

bicycle = Bicycle()
bicycle.move()

# Задание 3: Вызов методов родителя (super())
# 1. Создай родительский класс `Device` (Устройство).
#    - Добавь метод `turn_on`, который выводит: "Устройство включается в сеть".
# 2. Создай дочерний класс `Laptop` (Ноутбук), который наследуется от `Device`.
# 3. В классе `Laptop` переопредели метод `turn_on`.
#    Внутри этого метода нужно:
#    - Сначала вызвать метод `turn_on` родительского класса (используй `super()`).
#    - Затем добавить свою фразу: "Ноутбук загружает операционную систему".
# 4. Создай объект класса `Laptop` и вызови его метод `turn_on()`.
# Подсказка: вызов родительского метода через super() выглядит так:
# super().имя_метода()

class Device:
    def turn_on(self):
        print("Устройство включается в сеть")

class Laptop(Device):
    def turn_on(self):
        super().turn_on()
        print("Ноутбук загружает операционную систему")
device = Laptop()
device.turn_on()


# Задание 4: Множественное наследование
# 1. Создай два родительских класса:
#    - `Flyer` (Летающий): с методом `fly`, который выводит "Могу летать".
#    - `Swimmer` (Плавающий): с методом `swim`, который выводит "Могу плавать".
# 2. Создай класс `Duck` (Утка), который наследуется ОТ ОБОИХ классов: `Flyer` и `Swimmer`.
#    Внутри класса `Duck` пока ничего не пиши (используй `pass`).
# 3. Создай объект класса `Duck` и вызови у него оба метода: `fly()` и `swim()`.
#    Убедись, что утка умеет и летать, и плавать.
# Подсказка: при множественном наследовании родители перечисляются в скобках через запятую:
# class Child(Parent1, Parent2):
class Flyer:
    def fly(self):
        print("Могу летать")

class Swimmer:
    def swim(self):
        print("Могу плавать")

class Duck(Flyer, Swimmer):
    pass

duck = Duck()
duck.fly()
duck.swim()

# Задание 5: Проверка принадлежности к классу (isinstance)
# 1. Создай класс `Animal` (Животное) с методом `speak`, который выводит "Издает звук".
# 2. Создай два дочерних класса:
#    - `Dog` (Собака): переопредели метод `speak` на вывод "Гав!".
#    - `Cat` (Кошка): переопредели метод `speak` на вывод "Мяу!".
# 3. Создай по одному объекту каждого класса: `dog` и `cat`.
# 4. Используя функцию `isinstance()`, напиши проверки:
#    - Является ли `dog` объектом класса `Dog`? (выведи результат)
#    - Является ли `dog` объектом класса `Animal`? (выведи результат)
#    - Является ли `cat` объектом класса `Dog`? (выведи результат)
#    - Является ли `cat` объектом класса `Animal`? (выведи результат)
# Подсказка: isinstance(объект, Класс) возвращает True или False.
# Просто выведи результаты этих проверок на экран через print().
class Animal:
    def speak(self):
        print("Издает звук")

class Dog(Animal):
    def speak(self):
        print("Гав!")
class Cat(Animal):
    def speak(self):
        print("Мяу!")

dog = Dog()
cat = Cat()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(isinstance(cat, Dog))
print(isinstance(cat, Animal))

# Задание 6: Атрибуты класса и наследование
# 1. Создай родительский класс `Employee` (Сотрудник).
#    - Добавь атрибут класса `company = "Рога и Копыта"`.
#    - Добавь метод `__init__`, который принимает `name` и сохраняет его как атрибут экземпляра.
#    - Добавь метод `show_info`, который выводит: "Имя: {name}, Компания: {company}".
# 2. Создай дочерний класс `Developer` (Разработчик), наследующий от `Employee`.
#    - В `__init__` добавь ещё один параметр `programming_language` и сохрани его.
#    - Переопредели метод `show_info` так, чтобы он выводил:
#      "Имя: {name}, Компания: {company}, Язык: {programming_language}".
#    - Используй `super().__init__(name)` для вызова родительского конструктора.
# 3. Создай объект `dev = Developer("Анна", "Python")` и вызови его метод `show_info()`.
# Подсказка: чтобы обратиться к атрибуту класса внутри метода, пиши `self.company`.
class Employee:
    company = "Рога и Копыта"
    def __init__(self, name):
        self.name = name
    def show_info(self):
        print(f"Имя: {self.name}, Компания: {self.company}")

class Developer(Employee):
    def __init__(self, name, programming_language):
        super().__init__(name)
        self.programming_language = programming_language
    def show_info(self):
         print(f"Имя: {self.name}, Компания: {self.company}, Язык: {self.programming_language}")

dev = Developer("Анна", "Python")
dev.show_info()

# Задание 7: Множественное наследование и порядок разрешения методов (MRO)
#
# 1. Создай класс `A` с методом `who_am_i`, который выводит "Я класс A".
# 2. Создай класс `B` с методом `who_am_i`, который выводит "Я класс B".
# 3. Создай класс `C` с методом `who_am_i`, который выводит "Я класс C".
# 4. Создай класс `D(A, B)` (наследуется от A и B, в этом порядке). Внутри `pass`.
# 5. Создай класс `E(B, C)` (наследуется от B и C, в этом порядке). Внутри `pass`.
# 6. Создай класс `F(D, E)` (наследуется от D и E, в этом порядке). Внутри `pass`.
# 7. Создай объект класса `F` и вызови его метод `who_am_i`.
# 8. Выведи на экран `F.__mro__` чтобы увидеть порядок поиска методов.
#
# Подсказка: метод ищется слева направо по дереву наследования.
class A:
    def who_am_i(self):
        print("Я класс А")
class B:
    def who_am_i(self):
        print("Я класс В")
class C:
    def who_am_i(self):
        print("Я класс С")

class D(A, B):
    pass
class E(B, C):
    pass
class F(D, E):
    pass
obj = F()
obj.who_am_i()
print(F.__mro__)

# Задание 8: Проверка подклассов (issubclass)
# 1. Создай класс `Vehicle` (Транспортное средство).
# 2. Создай класс `GroundVehicle` (Наземный транспорт), наследующий от `Vehicle`.
# 3. Создай класс `WaterVehicle` (Водный транспорт), наследующий от `Vehicle`.
# 4. Создай класс `AmphibiousVehicle` (Транспорт-амфибия), наследующий от `GroundVehicle` и `WaterVehicle`.
# 5. Используя функцию `issubclass()`, проверь и выведи на экран:
#    - Является ли `AmphibiousVehicle` подклассом `Vehicle`?
#    - Является ли `AmphibiousVehicle` подклассом `GroundVehicle`?
#    - Является ли `AmphibiousVehicle` подклассом `WaterVehicle`?
#    - Является ли `GroundVehicle` подклассом `AmphibiousVehicle`?
#    - Является ли `Vehicle` подклассом `object`?
# Подсказка: issubclass(ДочернийКласс, РодительскийКласс) возвращает True/False.
class Vehicle:
    pass
class GroundVehicle(Vehicle):
    pass
class WaterVehicle(Vehicle):
    pass
class AmphibusVehicle(GroundVehicle, WaterVehicle):
    pass
print(issubclass(AmphibusVehicle, Vehicle))
print(issubclass(AmphibusVehicle, GroundVehicle))
print(issubclass(AmphibusVehicle, WaterVehicle))
print(issubclass(GroundVehicle, AmphibusVehicle))
print(issubclass(Vehicle, object))

# Задание 9: super() с множественным наследованием
# 1. Создай класс `Base` с методом `__init__`, который выводит "Base init".
# 2. Создай класс `A(Base)` с методом `__init__`, который:
#    - Выводит "A init"
#    - Вызывает `super().__init__()`
# 3. Создай класс `B(Base)` с методом `__init__`, который:
#    - Выводит "B init"
#    - Вызывает `super().__init__()`
# 4. Создай класс `C(A, B)` с методом `__init__`, который:
#    - Выводит "C init"
#    - Вызывает `super().__init__()`
# 5. Создай объект класса `C` и посмотри на порядок вызовов.
# 6. Выведи `C.__mro__` чтобы понять, почему порядок именно такой.
# Подсказка: super() вызывает следующий класс по цепочке MRO.
class Base:
    def __init__(self):
        print("Base init")
class A(Base):
    def __init__(self):
        print("A init")
        super().__init__()
class B(Base):
    def __init__(self):
        print("B init")
        super().__init__()
class C(A, B):
    def __init__(self):
        print("C init")
        super().__init__()
c = C()
print(C.__mro__)

# Задание 10: Наследование и переопределение __str__
# 1. Создай класс `Person` с методом `__init__`, который принимает `name` и `age`.
# 2. Добавь метод `__str__`, который возвращает строку: "Имя: {name}, Возраст: {age}".
# 3. Создай класс `Student`, который наследует от `Person`.
# 4. В классе `Student` переопредели метод `__str__` так, чтобы он возвращал:
#    "Студент: {name}, Возраст: {age}".
# 5. Создай объект `student = Student("Анна", 20)` и выведи его через `print()`.
# Подсказка: print(объект) автоматически вызывает __str__.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Имя: {self.name}, Возраст: {self.age}"
class Student(Person):
    def __str__(self):
        return f"Студент: {self.name}, Возраст: {self.age}"
student = Student("Анна", 20)
print(student)

# Задание 11: Наследование и super() в __init__
# 1. Создай класс `Product` с методом `__init__`, который принимает `name` и `price`.
#    Сохрани их как атрибуты.
# 2. Создай класс `Food`, который наследует от `Product`.
# 3. В классе `Food` добавь в `__init__` третий параметр `expiration_date` (срок годности).
#    - Вызови `super().__init__(name, price)` для инициализации родительских атрибутов.
#    - Сохрани `expiration_date` как атрибут.
# 4. Создай объект `food = Food("Молоко", 80, "10.03.2026")`.
# 5. Выведи на экран все три атрибута через `print(food.name, food.price, food.expiration_date)`.
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class Food(Product):
    def __init__(self, name, price, expiration_date):
        super().__init__(name, price)
        self.expiration_date = expiration_date
food = Food("Молоко", 80, "10.03.2026")
print(food.name, food.price, food.expiration_date)

# Задание 12: Защищённые атрибуты и наследование
# 1. Создай класс `BankAccount` с методом `__init__`, который принимает `owner` и `balance`.
#    - Сохрани `owner` как публичный атрибут.
#    - Сохрани `balance` как защищённый атрибут (с одним подчёркиванием: `_balance`).
# 2. Добавь метод `get_balance`, который возвращает значение `_balance`.
# 3. Добавь метод `deposit`, который принимает сумму и увеличивает `_balance` на эту сумму.
# 4. Создай класс `SavingsAccount`, который наследует от `BankAccount`.
# 5. В классе `SavingsAccount` добавь метод `add_interest`, который увеличивает `_balance` на 10%.
# 6. Создай объект `savings = SavingsAccount("Иван", 1000)`.
# 7. Вызови `savings.add_interest()` и затем выведи баланс через `savings.get_balance()`.
# Подсказка: защищённые атрибуты доступны в дочерних классах.
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount


class SavingsAccount(BankAccount):
    def add_interest(self):
        self._balance = self._balance / 100 * 110


savings = SavingsAccount("Иван", 1000)
savings.add_interest()
savings.get_balance()
print(savings.get_balance())