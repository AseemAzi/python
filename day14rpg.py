import random
def hero():
    hhp = 100
    ehp = 100
    t = 1
    while hhp > 0 and ehp > 0:
        print("turn:",t)
        player_damage = random.randint(7,20)
        hhp = hhp - player_damage
        print(f"{name} got  damage:{player_damage} hp remains:{hhp}")
        enemy_damage = random.randint(7,20)
        ehp = ehp - enemy_damage
        print(f"{enemy} got damage:{enemy_damage} hp remains:{ehp}")
        t+=1
    if hhp > 0:
        return f"{name} dead"
    elif ehp > 0:
        return f"{enemy} wins"
    else:
        return " both dead"
        



time = random.choice(["once up on a time","long ago","one decade ago"," before 1000 years "])
loc = random.choice(["city","dessert","jungle","wild","sea","hill","cave"])
enemy = random.choice(["negromancer","aizen","sukuna","gojo","toji"])
name = input("enter a name:")
print(f"{time} in {loc} there lived a hero named {name} and a enemy lived in {loc} named {enemy} one day they fought each other")
print(hero())
