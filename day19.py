# method overloading

# not possible in python

# method overriding


# abstract method

import random
from abc import ABC,abstractmethod

class Vehicle(ABC): #inheriting abstract class
    def __init__(self):
        pass
    def generate_(self):
        z =f"VH{ random.randint(2000,30000)}"
        print(z)
        
    @abstractmethod #setting abstract decorater
    def run(self):
        print("petrol")

class Car:
    def __init__(self):
        pass
    
    def run(self): #if we don't define a run method here it will raise an error
        print("disel")
        
# c1=Car()
# c1.run()
        
# exception handling

# used to not stop executing code 

# try:
#     a=int(input("enter an number:"))
#     b=int(input("enter a number:"))
#     c = a/b
#     print(c)
# except ZeroDivisionError: #used for zero division error
#     print("you can't divide a number with zero")

# except ValueError: #used for value error
#     print("invalid input")
    
# else: #if try is correct then only the else statement print
#     print("heyy",c)

# finally: # aways print
#     print("always printing")
    
    
        
# creating exception error(our own error)

# class myerror(Exception):#inheriting exception class
#     pass
# a = 10
# if a>5:
#     raise myerror('wrong') #raise used to raise error

# list comprehension
# a = [i for i in range(1,10)] # no conditions
# print(a)
# a = [i for i in range(1,10) if i%2==0] # if one condtions
# print(a)
# a = [-11,12,35,-65,-45,-32,78,-78,-30,10]
# res = [  'postive'if i > 0 else 'negative' for i in a] #u can't give two more conditions like elif
# print(res)
# multiple of 3 and 5
# a=[i  for i in range(1,100) if i%3==0 and i%5==0]
# print(a)

# first 1000 numbers with 6
 