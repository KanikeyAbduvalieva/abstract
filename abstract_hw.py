from abc import ABC, abstractmethod, abstractproperty
# Task 1
class Transport(ABC):
    @property
    @abstractmethod
    def move(self):
        ...

class Car(Transport):
    def move(self):
        return 'Car is moving on the road'

class Plane(Transport):
    def move(self):
        return 'Plane is flying in the sky'

car = Car()
plane = Plane()

#print(car.move())   
#print(plane.move()) 

# Task 2
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        ...

class CreditCard(PaymentMethod):
    def pay(self, amount):
        return f'Оплата {amount} через Credit Card'


class PayPal(PaymentMethod):
    def pay(self, amount):
        return f'Оплата {amount} через PayPal'
    
obj1 = CreditCard()
obj2 = PayPal()

#print(obj1.pay(1000))   
#print(obj2.pay(500))   

# Task 3
class Shape(ABC):
    @abstractmethod
    def area(self):
        ...

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
         return 3.14 * self.radius ** 2
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

obj1 = Circle(11)
obj2 = Rectangle(11, 14)

#print(f'Площадь круга: {obj1.area()}')          
#print(f'Площадь прямоугольника: {obj2.area()}')  

# Task 4
class OutputDevice(ABC):
    @abstractmethod
    def display(self, text):
        ...

class Monitor(OutputDevice):
    def display(self, text):
        print(f'[Monitor] {text}')

class Printer(OutputDevice):
    def display(self, text):
        print(f'[Printer] {text}')

obj1 = Monitor()
obj2 = Printer()

#obj1.display('Hello, world!')   
#obj2.display('Hello, world!') 

# Task 5
'''Создай абстрактный класс Animal с методом make_sound(). Создай два класса Dog и
Cat, которые реализуют этот метод (выводят «Гав!» и «Мяу!» соответственно).
Пример вывода: Гав!             Мяу!     '''

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        ...

class Dog(Animal):
    def make_sound(self):
        return 'Гав!'

class Cat(Animal):
    def make_sound(self):
        return 'Мяу!'
    
obj1 = Cat()
obj2 = Dog()

#print(obj2.make_sound())  
#print(obj1.make_sound())

# Task 6
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        ...

class Developer(Employee):
    def __init__(self, fix_salary, bonus):
        self.fix_salary = fix_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.fix_salary + self.bonus

class Manager(Employee):
    def __init__(self, worked_hours, hour_rate):
        self.worked_hours = worked_hours
        self.hour_rate = hour_rate

    def calculate_salary(self):
        return self.worked_hours * self.hour_rate

obj1 = Developer(fix_salary=27000, bonus=3000)
obj2 = Manager(worked_hours=189, hour_rate=160)

#print(f'Зарплата разработчика: {obj1.calculate_salary()}')  
#print(f'Зарплата менеджера: {obj2.calculate_salary()}') 

# Task 7
class Database(ABC):
    @abstractmethod
    def connect(self):
        ...
    
    @abstractmethod
    def disconnect(self):
        ...

class MySQLDatabase(Database):
    def connect(self):
        return "Подключение к MySQL"

    def disconnect(self):
        return "Отключение от MySQL"

class PostgreSQLDatabase(Database):
    def connect(self):
        return "Подключение к PostgreSQL"

    def disconnect(self):
        return "Отключение от PostgreSQL"

obj1 = MySQLDatabase()
obj2 = PostgreSQLDatabase()

print(obj1.connect())
print(obj1.disconnect())
print(obj2.connect())
print(obj2.disconnect())

