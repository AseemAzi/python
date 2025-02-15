import random
def comp_mov():
    com = ["rock","paper","scissor"]
    mov = random.choice(com)
    return mov
    
def wincomb_(ch):
    mov = comp_mov()
    if ch == "rock "and mov == "scissor"or ch == "paper "and mov == "rock"or ch == "scissor"and mov == "paper":
        return "congrats you win!!!"
    elif ch == mov:
        return "it is tie"
    else:
        return mov,"computer wins!!!"

ch = input("rock,paper,scissor\nenter your move:")
print(wincomb_(ch))