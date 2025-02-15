# file handling

# open a file and reading it content and close it
# f = open('rock.txt','r')
# print(f.read())
# f.close()

# write a file if the file has content it will overwrite
# f = open('rocky.txt','w')
# f.write('hey rock key')
# f.close()

# append it will add to the next line
# f = open("rocky.txt","a")
# f.write('\nhey i know you ')
# f.close()

# without close file
# with open('rock.txt','a') as f:
#     for i in range(1,10):
#         f.write(f"\nhi turn:{i}")

# print single line
# with open('rock.txt',"r") as f:
#     print(f.readline())
    
# print multiple lines
# with open ('rock.txt', "r") as f:
#     print(f.readlines())

# commandline arguments
#  only run wth command prompt
# import sys
# a = int(sys.argv[1]) #0 th index in the list will be file name 
# b = int(sys.argv[2])
# c = int(sys.argv[3])
# print(a+b+c)


# name = input("enter your name:")
# age = int(input("enter your age:"))
# loc = input("enter your address:")
# with open(f'{name}.txt','a') as f:
#     f.write(f"name:{name}\n")
#     f.write(f"age:{age}\n")
#     f.write(f"location:{loc}\n")

# os 
# used to do os functions
# import os

# loc = 'aseem.txt'
# path = "C:\\Users\\Administrator\\python\\aseem.txt"
# if os.path.exists(loc):
#     print("path exists")
# if os.path.isfile:
#     print("It is a file")
# elif os.path.isdir:
#     print("it is directory")