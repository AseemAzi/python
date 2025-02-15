# dictionaries
# unindexed
# mutable
# print only using key

# student={11:"shahin",12:"abit",13:"reka",14:"azzim",15:"fida",16:"vineeth",17:"divya"}
# print(student[14])

# c = {"name":"rameesh","age":30,"location":"tvm","work":"no"}
# d = {}
# d["name"] = "aseem"
# d["age"] = 21
# d["location"]= "edappal"
# d["work"] = "yes"
# print(d)

# restrictions of dictionaries
# key in a dict should be unique
# key should be immutable



student={11:"shahin",12:"abit",13:"reka",14:"azzim",15:"fida",16:"vineeth",17:"divya"}

# clear
# student.clear()
# print(student)

# get
# print(student[14])
# print(student.get(15))

# key
# print(student.keys())
# value
# print(student.values())
# items
# print(student.items())
# update 
# student.update({11:"rahul"})
# print(student)
# if there key and it will update and there no key in that key_name it will create a new key

# pop
# student.pop(11)
# print(student)

# pop items
# delete last key
# print(student)
# student.popitem()
# student.popitem()
# print(student)

# * 5 , s,p


a = [
    [3,4],
    [1,2]
]
b = [
    [3,4],
    [1,2]
]
# op [
#     [6,8],
#     [2,4]
# ]
c = [[0,0],
     [0,0]]
z = len(a)
y = len(a[0])
for i in range(z):
  for j in range(y):
    c[i][j] = a[i][j]+b[i][j]
print(c)



#print prime numbers between an interval
# starting 100
# ending  200
st = int(input("enter the starting number:"))
ed = int(input("enter the ending number:"))
for i in range(st,ed+1):
  if i < 2:
    continue
  is_prime = True

  for j in range(2,i):
    if i % j == 0:
      is_prime = False
      break
  if is_prime:
    print(i)   
  
  
  # * 5

num = int(input("enter a number:"))
for i in range(num+1):
  if i == 0 or i == 3 or i == 5:
    print("*"*num)
  elif i == 4:
    print(" "*(num-1)+"*")
  else:
    print("*")
    
    
# * s

num = int(input("enter a number:"))
for i in range(num+1):
  if i == 0 or i == 3 or i == 5:
    print("*"*num)
  elif i == 4:
    print(" "*(num-1)+"*")
  else:
    print("*")
    
#p
# *****
# *    *
# *    *
# *****
# *     
# * 
num = int(input("enter a number:"))
for i in range(num+1):
  if i == 0 or i == 3 :
    print("*"*num)
  elif i == 1 or i == 2:
    print("*"*(num -4)+" "*(num-1)+"*")
  else:
    print("*")
