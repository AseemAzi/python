# object oriented programming

# class Car: #created a class named Car
    
#     def start(): #created a method its behavior of object
#         print("car started")
        
#     def run():
#         print("car is running")
        
# car1 = Car #created a object name car1
# car1.run()
# car1.start()

# car2 = Car
# car2.start()
# car2.run()

# class Mobile:
#     def __init__(self,brand,model,color,price): #init is constractor
#         self.brand = brand #this the attributes used to describe object
#         self.model = model
#         self.color = color
#         self.price = price
    
#     def product_(self):
#         print (f"{self.brand} {self.model} with {self.color} color price is {self.price} is launched")
        

# mob1 = Mobile("sumsung","13 pro","black",70000)
# mob2 = Mobile("realme","13","grey",25000)
# print(mob1.brand)
# print(mob2.brand)
# mob1.product_()
# mob2.product_()

# class Student:
#     def __init__(self,name,rollno,m1,m2,m3,m4,m5):
#         self.name = name
#         self.rollno = rollno
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
#         self.m4 = m4
#         self.m5 = m5
    
#     def sum_(self):   
#         return self.m1 +self.m2+self.m3+self.m4+self.m5
    
#     def average_(self):
#         return self.sum_()/5
    
#     def percetage_(self):
#         return (self.sum_()/250)*100
    
#     def result_(self):
#         return (f" Name:{self.name} rollno:{self.rollno} totalmark:{self.sum_()} in 250 and average mark is:{self.average_()} and have {self.percetage_()} percentage mark")
    
# stud1 =Student("aseem",1231,10,20,30,40,50)
# stud2  =Student("max",1123,20,46,23,12,36)
# print(stud1.result_())
# print(stud2.result_())
        
# comparison
# class Bike:
#     def __init__(self,model,price):
#         self.model = model
#         self.price = price
    
#     def compare(self,obj):  #comparing 
#         if self.price > obj.price:
#             print(f"{self.model} have higher price")
#         else:
#             print(f"{obj.model} have higher price")
# bike1=Bike("ns200",50000)
# bike2=Bike("v3",80000)
# bike1.compare(bike2)

# day16
# employee id 
# salary 5 month
# balance salary
# percentage

# class Employee:
#     def __init__(self,employeename,employeeid,salary1,salary2,salary3,salary4,salary5):
#         self.employeename=employeename
#         self.employeeid = employeeid
#         self.salary1 = salary1
#         self.salary2 = salary2
#         self.salary3 = salary3
#         self.salary4 = salary4
#         self.salary5 = salary5
    
#     def sum_(self):
#         return self.salary1+self.salary2+self.salary3+self.salary4+self.salary5
    
#     def balance_(self):
#         return (5*40000)-(self.sum_())
    
#     def percentage_(self):
#         return (self.sum_()/200000)*100
        
#     def emp_show(self):
#         return (f" Name: {self.employeename} ID: {self.employeeid} got  salary {self.sum_()} from salary 200000 . Balance salary is {self.balance_()} he got {self.percentage_()}%  of salary.  ")
# emp1 = Employee("aseem",1120,10000,20000,25000,15000,35000)
# emp2 = Employee("jack",2544,30000,20000,10000,32000,28000)

# print(emp1.emp_show())
# print(emp2.emp_show())


# class Lemon:
#     def __init__(self,bill):
#         self.bill = bill
        
#     def change_(self):
#         five = 0
#         ten = 0
#         for i in self.bill:
#             if i == 5:
#                 five+= 1
#             elif i == 10:
#                 if five > 0:
#                     five-= 1
#                     ten+=1
#             elif i == 20:
#                 if five > 0 and ten > 0:
#                     five-=1
#                     ten-=1
#             else:
#                 return False
#         return True

# lm1= Lemon([5,5,10,10,20,30])
# print(lm1.change_())