# function to output something without class
# class can have attributes
# class produce real instant of an objects
# function within class is called method
# class Test:

#     name = 'I am the class'
#     variable = 10

#     def printName(self, age):                        # self  - mandatory parameters
#         print('I am a method of the class')
#         print(age)
# x = Test()
# # print(x.name)

# class Test2:
#     def __init__(self, name):
#         self.name = name
#         print('I am the init function')

# y = Test2('y')
# # print(y.name)
# x = Test2('x')
# print(x.name)

# x.printName(27)

# y = Test()
# print(x.name)
# print(x.variable)
# print(y.name)
# print(y.variable)

# class Dog:

#     scientific_name = 'Canis'

#     def __init__(self, name):
#         self.name = name

# duke = Dog('duke')
# bob = Dog('bob')

# print(duke.scientific_name)
# print(duke.name)

# print(bob.scientific_name)
# print(bob.name)

# class Hero:

#     def __init__(self, name):
#         self.name = name
#         self.energy = 100
    
#     def eating(self, food):
#         if food == 'pasta':
#             self.energy = self.energy + 10
#         elif food == 'pizza':
#             self.energy = self.energy - 20

# mario = Hero('mario')
# print(mario.name)
# print(mario.energy)
# mario.eating('pasta')
# print(mario.energy)
# mario.eating('pizza')
# print(mario.energy)

# adissu = Hero('adissu')
# print(adissu.name)
# print(adissu.energy)
# adissu.eating('pasta')
# print(adissu.energy)
# adissu.eating('pizza')
# print(adissu.energy)

# for i in range(0, 4):
#     mario.eating('pizza')

# print(mario.energy)

# class BaseClass:

#     def printName(self):
#         print('I come from Base class')

# class SubClass(BaseClass):
    
#     def printName(self):
#         print('I am from the Sub Class')

# a = SubClass()           # trick to call subclass
# a.printName()

class Employee:

    def __init__(self, name, paycheck):
        self.name = name
        self.paycheck = paycheck

    def raise_paycheck(self, number):

        self.paycheck = self.paycheck + (self.paycheck * number)
        

luk = Employee('Lukman', 1000)
print(luk.name)
print(luk.paycheck)

luk.raise_paycheck(0.1)
print(luk.paycheck)
