import random
def player_():
    dice = (random.randint(1,6))
    sum_0 = 0
    for i in range(dice):
        score_1 = random.randint(1,6)
        sum_0 = sum_0+ score_1
        
    return sum_0
player_1 = player_()        
player_2 = player_()
if player_1 > player_2:
    print(f"player 1 wins with score of {player_1} and player 2 loses with score of {player_2}")
elif player_2 > player_1:
    print(f"player 2 wins with score of {player_2} and player 1 lose with score of {player_1}")
else:
    print("it is a tie")
        
    
