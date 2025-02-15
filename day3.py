# # condition statement


# # while loop 
# # condition based

# # even numbers in ten 


# # print 10 numbers 
i = 1 
while i <= 10:
    print(i)
    i+=1
      
# # first 200 numbers divisble by 5

i = 1
while i <= 200:
 if i % 5 == 0:
    print(i)
 i+=1 
    
#  print 100 numberas and its final sum   
i = 1 
sum = 0
while i <= 100:
    print(i)
    sum = sum + i
    i+=1
    
print("total sum",sum)
    

# factorial of a  number
num = 5
i = 1
fac = 1
while i <= num:
    fac *= i
    i+=1
    print(fac)

    
    
    
 # 15 multiple   numbers
num = 100
i = 1

while i <= num:
    if i % 15 == 0:
        print(i)
    i+=1
 
 
 
#  sum of the digits 
#   num = 12345
#  output = 15
# print(123//10)
# print(123%10)
num = 12345
m = 0
sum = 0
while num != 0:
    
    m = num % 10 #5
    num = num//10
    sum = sum + m
   
print(sum)
    
    

 
#home work reverse of a number 
num = 12345
m = 0
rev = 0
while num != 0:
    
    m = num % 10 
    num = num//10
    rev = rev*10+m
print(rev)


