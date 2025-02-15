# tuples
# b = [(1,1),(2,4),(3,)]
# a = [1,2,3,4,5,6]
# b = []
# for i in a:
#     z = (i,i*i)
#     b.append(z)
# print(b)
    
# find the missing number
# a = [1,2,3,4,5,7,8,9,10]
# c= len(a)
# for i in range(1,c):
#     if i in a:
#         continue
#     else:
#         print(i)
        
# chessborad pattern
# W B W B W B W B
# B W B W B W B W
# repeat
# a ="W B W B W B W B "
# b ="B W B W B W B W"
# for i in range(8):
#   if i % 2 == 0:
#       print(a)
#   else:
#        print(b)

# a = ['hello', 'my', 'name','is','hari']
# b = ''
# op = 'hello my name is hari'
# for i in a:
#     b = b +' '+ i
# print(b)

# split
# x = 'hello my name is hari' 
# y = []
# z = x.split()
# print(z)
# do without split
# word = ''
# for i in x:
#   if i != " ":
#     word = word+i
#   else:
#     y.append(word)
#     word = ''
# if word != 0:
#   y.append(word)
# print(y)

#join
# a = ['hello', 'my', 'name','is','hari']
# b =' '.join(a)
# print(b)
# only strings can be joined

#set
# name = {1,2,3,4,56,7}
# for i in name:
#     print(i) 
# unordered
# no duplicates
# no index

# a = {1,2,3,45,6,7}
# b = {1,2,3,4,5,67,8}

#union
# print(a.union(b))
# print(a|b)

#intersection
# print(a.intersection(b))
# print(b&a)

# differnce
# print(a.difference(b))
# print(b-a)


# add elements in a list
a = [11,12,13,14,15,20]
s = []
for i in a:
    m = i % 10
    d = i // 10
    sum = m + d
    s.append(sum)
print(s)
