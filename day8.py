# from first 100 numbers create 2 lists with even and odd numbers
# odd = []
# even = []
# for i in range(1,100+1):
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("odd ",odd)
# print("even",even)

# remove duplicates  from a list
# li = []
# dp = []
# num = int(input("enter a number:"))
# for i in range(num):
#     li.append(int(input("enter a element:"))) 
# print(li)
# for i in li:
#     if i not  in dp:
#         dp.append(i)
# print(dp)
      
# a = [1,2,3,4,5,6,7,8,9,10]
# [1,2,3,4,5]
# [6,7,8,9,10]


# a = [1,2,3,4,5,6,7,8,9,10]
# z = len(a)//2
# b = []
# c = []
# for i in range(len(a)):
#     if i < z:
#         b.append(a[i])
#     else:
#         c.append(a[i])
# print(b)
# print(c)
        
    
# a = [1,100,200,67,-5,0,-10,49]
# smallest element -10
# largest element 200

# a = [1,100,200,67,-5,0,-10,49]
# s = a[0]
# l = a[0]
# for i in a:
#     if i < s:
#       s = i
#     if i > l:
#         l = i
# print(s,"smallest")
# print(l,"largest")


# manually sort above list 
a = [1,100,200,67,-5,0,-10,49]
x = len(a)

for i in range(x-1):
    for j in range(x-1-i):
      if a[j] > a[j+1]:
          temp = a[j]
          a[j] = a[j+1]
          a[j+1]= temp 
print(a)

    
    