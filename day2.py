    # boolean datatype used to check true or false
    
    # comparison operators
    
    # equal to ==
    
a = 10 
b = 10
print(a==b)
    
# not equal to !=
a= 10
b= 5   
print(a!=b)

# greater than >
a= 100
b= 50
print(a>b)

# less than <
a= 10
b=100
print(a<b)

# greater than  or equal to >=
a= 200
b= 50
print(a>=b)

# less than equal to <=
a= 40
b=30
print(a<= b)


# condition operators 

# if statement 
a = 10
 
if a > 5:
     print("a is greater") 
     
# if else statement

num = 23

# odd or even 

if num % 2== 0:
    print("even number")
else:
    print("odd number")
  
# largest of 2 numbers
    
num1 = 10
num2 = 20

if num1 > num2:
    print("num1 is greater")
else:
    print("num2 is greater")
    

# nested if 

a = 10
if a <= 1:
    print("a is 1 ")
elif a <= 2:
    print("a is 2")
elif a <= 3:
    print("a is 3")
elif a<=4:
    print("a is 5")
elif a<= 5:
    print("a is 5 ")
else:
    print(" a is greater than 5")
    
# check if a number is positive , negative or zero 
num = 100
if num > 0:
    print("number is positive")
elif num < 0:
    print("number is negative")
else:
    print("number is zero")
    
# largest among  3 numbers

num1 = 10
num2 = 500
num3 = 150

if num1 > num2 and num1 > num3:
    print("num1 is greater")
elif num2 > num1 and num2 > num3:
    print("num2 is greater")
else:
    print("num3 is greater")
    
# swap numbers 

a = 5 
b = 7
temp = 0
temp = a
a = b
b = temp

print(a)
print(b)

# swap without temp

a = 5
b = 7
a = a + b
b = a - b
a = a - b
print(a)
print(b)


# eligible for vote

age = 10
if age >= 18:
    print("you are eligible for vote")
else:
    print("you are minor")