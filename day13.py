# scope
# l e g b

# function age calculator
# def age_calc(st,ct):
#     return ct - st
    
# st = int(input("enter your born year:"))
# ct =int(input("enter the current year:"))
# print(age_calc(st,ct))    

# modular programming

# from md import * # for importing all
# print(a,b)
# print(say_name())

# from md import say_name # here only importing a function

# from md import a as byte # assign variable to another variable
# a = 10
# print(a)
# print(byte)

# import time
# print(time.time()) #time in seconds for the begining of time
# print(time.ctime(1737612181.3022878)) ctime used to convert seconds to time
# a = time.time()
# for i in range(1,4):
#     print(i)
#     time.sleep(2)
# b = time.time()
# print(b-a)

# quiz with timer
# import random
# print(random.randint(1,10))
# a = ['apple',"ornage","banana","pineapple","mango"]
# print(random.choice(a)) # value
# print(random.choices(a)) # list as output

# coin toss
# coin = ["head","tail"]
# print(random.choice(coin))
# result =random.randint(1,2)
# if result == 1:
#     print("heads")
# else:
#     print("tails")
import random
com = ["rock","paper","scissor"]
def comp_mov(com):
    mov = random.choice(com)
    return mov
    
def wincomb_(ch):
    mov = comp_mov(com)
    if ch == "rock"and mov == "scissor"or ch == "paper"and mov == "rock"or ch == "scissor"and mov == "paper":
        return f"com mov is {mov} congrats you win!!!"
    elif ch == mov:
        return "it is tie"
    elif mov == "rock"and ch == "scissor"or mov == "paper"and ch == "rock"or mov == "scissor"and ch == "paper":
        return f"{mov} computer wins!!!"
    else:
        return "invalid move!! try again:"

while(True):
        ch=input("rock,paper,scissor\nenter your move:").lower()
        if ch not in com:
            print("invalid move try again")
        else:     
            print(wincomb_(ch))
            break
 