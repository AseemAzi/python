# variables in class

# class Car:
#     wheel = 4 #class varibale / static varibale  can used in class and object cann call it using object and class
    
#     def __init__(self,brand,model,year):
#         self.brand = brand
#         self.model=model #instance variable only used in objects only call using object
#         self.year=year

# print(Car.wheel) # class variable
# car1=Car("honda","city",2015)
# print(car1.wheel) #class varibale
# print(car1.brand) #static varibale


# methods in class 

# class Car:
#     wheel = 4
#     def __init__(self,brand,model,year):
#         self.brand = brand
#         self.model=model 
#         self.year=year
    
#     def brand_(self): #instance method required self parametre
#         return self.brand
    
#     @classmethod # class method can call by class name
#     def wheels_(cls): #instead of self use cls
#         return cls.wheel
    
#     @staticmethod # method which not have access in self or class attributes 
#     def sum_(a,b):
#         return a+b

# print(Car.wheels_()) #calling class method
# car1=Car("honda","city",2015)
# print(Car.sum_(1,2)) #calling static method


# class Con:
#     I = 1
#     V = 5
#     X = 10
#     L = 50
#     C = 100
#     D = 500
#     M = 1000
    
#     def __init__(self,value):
#         self.value = value
        
#         result=" "
#     for i  in value:
#         if i == I:
            
        
            
