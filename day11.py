# functions,
# block of code to be executed when it is called
# def function_name():
#     code to be execueted

# def my_name():
#     print(f"my name is {name}")

# name = input("enter your name:" )
# my_name()

# arguments or parameters
# values passed into a function
# def add(a,b):
#     print(a+b)
# add(2,4)

# factorial using function
  
# def fac(num):
#     fac = 1
#     for i in range(1,num):
#         fac*=i
#     print(fac)
               
# fac(3)

# positional arguments
# def add(a,b,c):
#     print(a+b+c)

# add(1,2,4)

# keyword arguments
# def add(a = 0, b= 0,c = 0):
#     print(a+b+c)
# add(a=5,b= 8,c = 9)#assinging values 

#return odd or even
# def odd_(num):
#     if num % 2 == 0:
#          return True
#     else:
#          return False
    
# num = int(input("enter a number:"))
# if odd_(num):
#     print("even")
# else:
#     print("odd")
 

#  first 100 numbers 
# def numbers_(num):
#     li = []
#     for i in range(num):
#         li.append(i)
#     return li
    
# print(numbers_(100))

# def add_(num1,num2):
#     return num1 + num2
# def sub_(num1,num2):
#     return num1 - num2
# def div_(num1,num2):
#     return num1 / num2
# def mul_(num1,num2):
#     return num1 * num2
# def mod_(num1,num2):
#     return num1 % num2\

# calculator
 
# num1 = int( input("enter your number:"))
# num2 = int(input("enter your second number:"))
# print("1.add\n2,sub\n3.div\n4.mul\n5.mod\n")
# op = int(input( "enter the operation you want to do:"))
# if op == 1:
#     print(add_(num1,num2))
# elif op == 2:
#     print(sub_(num1,num2))
# elif op == 3:
#     print(div_(num1,num2))
# elif op == 4:
#     print(mul_(num1,num2))
# elif op == 5:
#     print(mod_(num1,num2))
# else:
#     print("invalid choice")

# def check_num(num):
#   if num > 0 :
#     return "positive"
#   elif num < 0:
#     return " negative"
#   else:
#     return "number is zero"

# largest
# def lar_(num1,num2,num3):
#   if num1 > num2 and num1 > num3:
#     return num1
#   elif num2 > num1 and num2 > num3:
#     return num2
#   elif num3 > num1 and num3 > num2:
#     return num3
  
# num1 = int( input(" enter your  1st number:"))
# num2 = int(input(" enter your 2nd number:"))
# num3 = int(input("enyer your  3rd number:"))
# print("largest number is",lar_(num1,num2,num3))

# swap
# def swap_(a,b):
#   temp = 0
#   temp = a
#   a = b
#   b = temp
#   return a,b

# a = int(input("enter a number:"))
# b = int(input("enter b  nummber"))
# print("a,b =",swap_(a,b))

# sum of digits
# def sum_(num):
#     m = 0
#     sum = 0
#     while num != 0:
    
#         m = num % 10 #5
#         num = num//10
#         sum = sum + m
#     return sum
# num = int(input("enter a number(more than 1 digit):"))
# print(sum_(num))

# reverse
# def rev_(num):
#     m = 0
#     rev = 0
#     while num != 0:
    
#         m = num % 10 
#         num = num//10
#         rev = rev*10+m
#     return rev
# num = int(input("enter a number(more than 1 digits):"))
# print(rev_(num))

# prime
# def prime_(num):
#   is_prime = True
#   if num == 1:
#         pass
#   else:
        
#         for i in range(2 ,num):

#             if num % i == 0:
               
#                is_prime = False
                    
#   if num == 1:
#     return " 1 is not prime number "     
#   elif is_prime == True:
#     return num,"is a prime number"
#   else:
#     return num,"is not prime number"
  
# num = int(input("enter a number:"))
# print(prime_(num))

# sum of digits
# def sum_(num):
#   sum = 0
#   for i in range(num):
#     m =  num % 10
#     num = num // 10
#     sum = sum + m     
#   return sum

# num = int(input("enter a number:"))
# print(sum_(num))

# first 200 numbers divisble by 5
# def div_(num):
#   a = []
#   for i in range(5,num+1):
#       if i % 5 == 0:
#           a.append(i)
#   return a
# num= int(input("enter a number:"))
# print(div_(num))        


# fibanocci series
# 0 1 1 2 3 5 8 13 21

# def fib_(num):
#   a = 0
#   b = 1
#   temp = 0
#   li=[]
#   for i in range(num):
#       li.append(a)
#       temp = b
#       b = a + b
#       a = temp
#   return li
# num = int(input("enter a number:"))
# print(fib_(num))

# palaindrome
# 131 121
# def pal_(num):
#   pal = num
#   m = 0
#   rev = 0
#   for i in range(num):
#       if num!= 0 :
#           m = num % 10
#           num = num // 10
#           rev = rev* 10 + m
          
              
#   if rev == pal:
#       return pal,"is a palindrome"
#   else:
#       return pal,"is not palindrome"
    
# num = int(input("enter a number:"))
# print(pal_(num))

# reverse of string without using [::-1]
# def stri_(word):
#   b = ''
#   for i in range(len(word)):
      
#       b = word[i] + b
#   return b

# word = input("enter a word:")
# print(stri_(word))
      

# from first 100 numbers create 2 lists with even and odd numbers
# def odd_even(num):
#   odd = []
#   even = []
#   for i in range(1,100+1):
#       if i % 2 == 0:
#           even.append(i)
#       else:
#           odd.append(i)
#   return "odd",odd,"even",even
# num = int(input("enter a number"))
# print(odd_even(num))

# remove duplicates  from a list
# def dupli_():
#   li = []
#   dp = []
#   num = int(input("enter a number:"))
#   for i in range(num):
#       li.append(int(input("enter a element:"))) 
#   # return li
#   for i in li:
#       if i not  in dp:
#           dp.append(i)
#   return "list",li,"without dupli",dp
# print(dupli_())


# split a list
# def split_():
#   a = [1,2,3,4,5,6,7,8,9,10]
#   z = len(a)//2
#   b = []
#   c = []
#   for i in range(len(a)):
#       if i < z:
#           b.append(a[i])
#       else:
#           c.append(a[i])
#   return "b",b,"c",c
# print(split_())

# a = [1,100,200,67,-5,0,-10,49]
# smallest element -10
# largest element 200

# def lar_sma():
#   a = [1,100,200,67,-5,0,-10,49]
#   s = a[0]
#   l = a[0]
#   for i in a:
#       if i < s:
#         s = i
#       if i > l:
#           l = i
#   return "smallest",s,"largest",l
# print(lar_sma())

# manually sort above list 
# def sort_():
#   a = [1,100,200,67,-5,0,-10,49]
#   x = len(a)

#   for i in range(x-1):
#       for j in range(x-1-i):
#         if a[j] > a[j+1]:
#             temp = a[j]
#             a[j] = a[j+1]
#             a[j+1]= temp 
#   return a
# print(sort_())

# find the missing number
# def miss_():
#   a = [1,2,3,4,5,7,8,9,10]
#   c= len(a)
#   for i in range(1,c):
#       if i in a:
#           continue
#       else:
#           return i
# print(miss_())

# def stp_():
#   a = ['hello', 'my', 'name','is','hari']
#   b = ''
#   # op = 'hello my name is hari'
#   for i in a:
#       b = b +' '+ i
#   return b
# print(stp_())


# add elements in a list
# def add_ele():
#   a = [11,12,13,14,15,20]
#   s = []
#   for i in a:
#       m = i % 10
#       d = i // 10
#       sum = m + d
#       s.append(sum)
#   return s
# print(add_ele())

# def matr_():
#   a = [
#       [3,4],
#       [1,2]
#   ]
#   b = [
#       [3,4],
#       [1,2]
#   ]
#   # op [
#   #     [6,8],
#   #     [2,4]
#   # ]
#   c = [[0,0],
#       [0,0]]
#   z = len(a)
#   y = len(a[0])
#   for i in range(z):
#     for j in range(y):
#       c[i][j] = a[i][j]+b[i][j]
#   return c
# print(matr_())

#print prime numbers between an interval
# starting 100
# ending  200

# def prime_(st,ed):
#   a = []
#   for i in range(st,ed+1):
#     if i < 2:
#       continue
#     is_prime = True

#     for j in range(2,i):
#       if i % j == 0:
#         is_prime = False
#         break
#     if is_prime:
#       a.append(i)
#   return a

# st = int(input("enter the starting number:"))
# ed = int(input("enter the ending number:"))
# print(prime_(st,ed))

