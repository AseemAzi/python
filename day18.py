# inheritance
# types of inheritance 

# single inheritance 

# class Peson1:
#     def walk():
#         print("person1 is walking")
        
# class Person2(Peson1): #single inheritance use parent class and have only 1 child class
#     def run():
#         print("person2 is running")
# p2=Person2
# p2.walk() #calling single inheritance

# multi level inheritance

# class Peson1:
#     def walk():
#         print("person1 is walking")
        
# class Person2(Peson1): 
#     def run():
#         print("person2 is running")
        
# class Person3(Person2): #inheriting like a chain multi level inherietance have more than 1 child classes and pass parametre only 1
#     def eat():
#         print("person3 is eating")
        
# class Person4(Person3):
#     def sleep():
#         print("person4 can sleep")   

# p1=Person4
# p1.walk() #calling mutl level inheritance

# multiple inheritance

# class Person1:
#     def walk():
#         print("person1 is walking")
#     def speak(): 
#         print("speak1")
        
# class Person2: 
#     def run():
#         print("person2 is running")
#     def speak(): 
#         print("speak2")
        
# class Person3: 
#     def eat():
#         print("person3 is eating")
#     def speak(): 
#         print("speak3")
        
# class Person4(Person1,Person2,Person3): #inherienting multiple parent class 
#     def sleep():
#         print("person4 can sleep") 
#     def speak():  
#         print("speak4") # it it have no method here it will take from parent class in MRO(method resolution order) order(parametre passed order)

# p2=Person4
# p2.speak()

# super method used call super class in child class
# super().__init__ for printing super class init
# super().speak() for pinting method in super class(if the super class and child class have same name method)

# polymorphism
# types of polymorphism

# duck typing
# if it look like a duck and it quack like a duck it is a duck

# class Chicken:
#     def coko():
#         print("cokocoko")
#     def walk():
#         print("walking")

# class Duck:
#     def quack():
#         print("quack quack")
#     def walk():
#         print("walking")
        
# class Farmer:
#     def catches(bird):
#         bird.walk() #
        
# c = Chicken
# d = Duck
# f = Farmer
# f.catches(d) #if the class have have method that we are checking it will run

# operater overloading

#__add__() 

# class Student:
#     def __init__(self,m1,m2):
#         self.m1=m1
#         self.m2=m2
    
#     def __add__(self,otr):
#         return (self.m1+otr.m1,self.m2+otr.m2) #overloading fucntion with our code 

# s1=Student(10,11)
# s2=Student(15,3)
# print(s1+s2)

# __sub__()

# class Student:
#     def __init__(self,m1,m2):
#         self.m1=m1
#         self.m2=m2

#     def __sub__(self,otr):
#         return (self.m1- otr.m1 ,self.m2-otr.m2)

# s1=Student(21,32)
# S2=Student(11,23)
# print(s1-S2)

# __mul__()

# class Student:
#     def __init__(self,m1,m2):
#         self.m1=m1
#         self.m2=m2
    
#     def __mul__(self,otr):
#         return (self.m1*otr.m1,self.m2*otr.m2)
# s1=Student(5,6)
# s2=Student(2,3)
# print(s1*s2)

# __truediv__

# class Student:
#     def __init__(self,m1,m2):
#         self.m1=m1
#         self.m2=m2
    
#     def __truediv__(self,otr):
#         return (self.m1/otr.m1,self.m2/otr.m2)
# s1=Student(5,6)
# s2=Student(2,3)
# print(s1/s2)

# __cmp__

# class Student:
#     def __init__(self,name,m1):
#         self.m1=m1
#         self.name=name
    
#     def __gt__(self,otr):
#         if self.m1 > otr.m1:
#             return self.name
#         else:
#             return otr.name
# s1=Student("aseem",1)
# s2=Student("rahul",3)
# print(s1>s2)

class Point:
    
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        
    def reset(self):
        self.mov(0,0)
        
    def mov(self,nx,ny):    
        self.x=nx
        self.y=ny
        
    def xmov(self,nx):
        self.x=nx
    
    def ymov(self,ny):
        self.y=ny

p=Point(7,8)
print(p.reset())
print(p.mov(5,4))
