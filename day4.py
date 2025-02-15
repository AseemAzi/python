# number prime or not 1357
num = 1
is_prime = True

if num == 1:
    pass
else:
    i = 2
    while i < num:
        if num % i == 0:
            is_prime = False
        i+=1
        
if num == 1:
    print(num,"is not a prime number")

elif is_prime == True:
    print(num,'prime number ')   

else:
    print(num," is not a prime number")

   
# for loop
# for i in range(start,stop,increment) 

# sum of numbers
num =123
sum = 0
for i in range(1,num):
    sum+= i
print(sum)

     
# odd or even
num = 10

for i in range(1):
    if num % 2 == 1:
        print(num,"is a odd number")
    else:
        print(num,"is a even number")
        
    

# continue
a = 10
for i in range(1,a):
    if i % 2 == 0:
        continue
    else:
        print(i)

# pass
a = 10
if a == 10:
    pass
else:
    print("hello")
    
# break
num = 10
i = 0
while i < num:
    if i % 2 == 0:
        break
    i +=1
    
    print(i)
# all while loop convert into for loop
# prime 
num = 6
is_prime = True
if num == 1:
        pass
else:
        
        for i in range(2 ,num):

            if num % i == 0:
               
               is_prime = False
            
      
        
if num == 1:
    print("1 is not a prime number")        
elif is_prime == True:
    print(num,"is a prime number")
else:
    print(num,"is not prime number")
    
    


# reverse 
num = 1234
rev = 0
m = 0
for i in range(num):
    if num!= 0:
        m = num % 10
        num = num // 10
        rev = rev * 10 + m
print(rev)

# 15 multiple numbers
num = 100
for i in range(15,num+1,15):
    print(i)

# factorial numbers
num = 10
fac = 1
for i in range(1,num+1):
    fac = i * fac   
print(fac)

# sum of digits
num = 12345
sum = 0
for i in range(num):
    m =  num % 10
    num = num // 10
    sum = sum + m     
print(sum)
        
# first 200 numbers divisble by 5
num = 200
for i in range(5,num+1):
    if i % 5 == 0:
        print(i)