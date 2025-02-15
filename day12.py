# args 
# (*)used to pass multiple positional arguments
# def add_z(*args):
#     s= 0
#     for i in args:
#         s+=i
#     return s
# print(add_z(1,2,3,4,5,6,7,8,9,10))

# kwargs
# (**)used for passing multiple keyword arguments
# def name_(**kwargs):
#     a = []
#     for i in kwargs.values():
#         a.append(i)
#     return a
# print(name_(first_name='itachi',second_name='madara',third_name='hashirama senju',forth_name='tobirama',fifth_name= "rock lee"))

# def name_(**kwargs):
#     a = ""
#     for i in kwargs:
#         a+=kwargs[i]+" "
#     return a
# print(name_(first_name='itachi',second_name='madara',third_name='hashirama senju',forth_name='tobirama',fifth_name= "rock lee"))


# lambda functions
def product_(a,b):
    return a*b
# instead 
# p = lambda a,b:a*b 
# print(p(2,3))

# sqr = lambda a:a**2
# print(sqr(5))

# syntax 
# lambda parametre1,parametre2,:expression

# average of 5 numbers
# av = lambda a,b,c,d,e:a+b+c+d+e/5
# print(av(1,13,12,45,25))

# square root of a number
# sqrt = lambda a:a**0.5
# print(sqrt(10))

# full name fname lname mname
# f = lambda fname,mname,lname:fname + " " + mname + " "+ lname
# fname = input("enter the fname:")
# mname = input("enter the sname:")
# lname = input("enter the lname:")
# print(f(fname,mname,lname))

# sum of 3 numbers 
# s = lambda a,b,c:a+b+c
# a = int(input("enter a number:"))
# b = int(input(" enter a number:"))
# c = int(input("enter a number:"))
# print(s(a,b,c))

# perimetre of circle
# p = lambda r:2 * 3.14159 * r
# print(p(10))

# recursion 

# 10 number count_down

# def count_down(n):
#     print(n)
#     if n > 0:
#         return count_down(n-1)
# count_down(10)
    
# sum using recursion 
# def sum_(num):
#     if num ==0:
#         return 0
#     else:
#         return num + sum_(num-1)
# print(sum_(10))   
     
# factorial 
# def fac_(num):
#     if num == 1:
#         return 1
#     else:
#         return num * fac_(num-1)
# print(fac_(2))

# fibanocci_series using recursion 

def fib_(num,a = 0,b=1):
  if  num<= 0:
    return []
  elif num == 1:
    return [a]
  else: 
    return [a]+fib_(num-1,b,a+b)
    
    
   
num = int(input("enter a number:"))  
print(fib_(num))
