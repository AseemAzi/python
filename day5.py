# string 
a = 'aseem'
b = "aseem 's wsa"
c= '''aseem "is waskk"'''
print(a)
print(b)
print(c)

# \'
# \" 
# \n new line
# \t tabspace
# \b backspace
a = 'he was a god\'s man'
print(a)
b= "he was a god\b  \n he said \" nothing \t ever\""
print(b)

# type casting or type converision
a = 10
b = '10'
b = int(b)
print(a+b)

a = 'virtual studio code'
print(a[1:10])
print(a[:15:3])
print(a[::-1])
print(a[1:])
print(a[:6:-1])

# concatination addition
a = "python"
b = "core" 
c = a +" "+b 
print(a+b)
print(c)

#multiplication
# can't multiply 2 strings
a = "python "
b =  2
print(a*b)

# in operator membership in operator
name = "askelad"
if "as" in name:
    print("as is in ", name)
if "ak" in name:
    print("ad in ",name)
    
# 2 type of loops

name = "thorfin"
for i in name:
    print(i)
    
name = "jomvikings"
a = len(name)

for i in range(a):
    print(i,name[i])
    
    
a = 'harikrishnan'
v = 'aeiou'

for i in range(len(a)):
    
    if a[i] in v :
        print(a[i], " at position",i)   
        
        
# fibanocci series
# 0 1 2 3 5 8 13 21

num = 10
a = 0
b = 1
temp = 0
for i in range(num):
    print(a)
    temp = b
    b = a + b
    a = temp
 
    

# palaindrome
# 131 121
num = 123
pal = num
m = 0
rev = 0
for i in range(num):
    if num!= 0 :
        m = num % 10
        num = num // 10
        rev = rev* 10 + m
        
            
if rev == pal:
    print(pal,"is a palindrome")
else:
    print(pal,"is not palindrome")
    

# reverse of string without using [::-1]
# reverse of string without using [::-1]
a = 'hobbit'
b = ''
for i in range(len(a)):
    
    b = a[i] + b
print(b)
    
