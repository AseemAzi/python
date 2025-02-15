# list 
# collection of data

# a = [1,2,3,4,56]
# print(a)

# list are ordered
# a = [1,2,3,4,5,6]
# b =[6,5,4,3,2,1]
# print(a==b)

# store different type of data
# a = [12,"my name ",7.8,True,[1,23,45]]
# print(a)

# nested list
# a = [1,3,4,5,[983,123,['my','name',['wolverine'],8],0],23]
# print(a[4][2][2])


# li = [1.1,2,2,2,2,3,3,4,['ha',[11,12,['python','django'],13,14],'ri'],4,5,65]
# print(li[8][1][2][1])

# dynamic
# we can easily add element and remove element
# mutable
# we can cjange value after assigning it

# append
# a = [1,2,34,56,77]
# a.append(20)
# print(a)

# extend 
# used to add multiple values
# a = [1,2,34,56,77]
# a.extend([1,2,3,4,45,6])
# print(a)

# insert
# a = [1,2,34,56,77]
# a.insert(0,200)
# print(a)

# pop
# a = [1,2,34,56,77]
# a.pop() #without index removes last index value
# print(a)

# pop with index
# a = [1,2,34,56,77]
# a.pop(1)
# print(a)

# remove
# a = [1,2,34,56,77]
# a.remove(2) #won't remove  all duplicate value from list
# print(a)
#  0 zero
#  1 positive
#  2 positive
data = [0,1,2,3,-4,-7,0,10,-100,7]
for i in range(len(data)):
    if data[i] == 0:
        print(data[i],"is zero")
    elif data[i] < 0:
        print(data[i],"is negative")
    else:
        print(data[i],"is positive")
    
 

# print pattern
# *******
# *
# *
# *******

# print pattern
# *******
# *
# *
# *******

num = int(input("enter a number:"))
for i in range(num):
  if i == 0 or i == num -1:
    print("*"* num)
    
  else:
    print("*")