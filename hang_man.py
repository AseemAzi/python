import random

def hangman_(ch,dup):
        print(f"chance: {ch}")
        guess = input("enter your guess:").lower().strip(" ")
        if guess in li:
            print("already guessed")
            return ch-1 
        
        for i in range(z):  
            if guess == word :
                dup[:] = list(word)
                print(f" guessed the {word} correct") 
                return ch 
             
            elif word[i] == guess: 
                dup[i] = word[i]
                li.append(dup[i])
                print("letter is correct ")
                print(" ".join(dup))
                        
        if guess not in word :
            print(" letter not in word")
            print(" ".join(dup))
            return  ch-1
                
        return ch  
         
word = random.choice(["thegodfather","pulpfiction","thedarkknight","inception","fightclub",
"forrestgump","thematrix","goodfellas","parasite",
"interstellar","gladiator","theshawshankredemption","lordoftherings",
"starwars","thesilenceofthelambs","savingprivateryan","thedeparted","se7en","thegreenmile",
"joker","avengersendgame","thewolfofwallstreet","whiplash","djangounchained",
"nocountryforoldmen","therevenant","madmaxfuryroad","onceuponatimeinhollywood","casablanca",
"theprestige","lalaland","americanhistoryx","thegrandbudapesthotel","insideout",
"shutterisland","thetrumanshow","blackswan","thesocialnetwork","memento",
"eternalsunshineofthespotlessmind","oldboy","aclockworkorange","12angrymen","citizenkane",
"toystory","thelionking","walle","coco","ratatouille",
"findingnemo","up","spidermanintothespider-verse","theincredibles","zootopia",
"harrypotterandtheprisonerofazkaban","fantasticmr.fox","howlsmovingcastle","spiritedaway","yourname",
"princessmononoke","myneighbortotoro","asilentvoice","weatheringwithyou","graveofthefireflies",
"batmanbegins","logan","deadpool","x-mendaysoffuturepast","guardiansofthegalaxy",
"captainamericathewintersoldier","ironman","doctorstrange","thorragnarok","blackpanther",
"theavengers","thedarkknightrises","manofsteel","wonderwoman","joker",
"it","hereditary","aquietplace","theconjuring","theexorcist",
"getout","us","theshining","psycho","alien",
"predator","bladerunner2049","thething","jurassicpark","terminator2judgmentday",
"indianajonesandthelastcrusade","backtothefuture","ghostbusters","theprincessbride","thegreatgatsby"
])
z= len(word)
dup = ["_"]*z
print(" ".join(dup))
ch = 8
li=[]

while "_" in dup and ch != 0:
   ch = hangman_(ch,dup) 
   if ch == 0:
       print(f"you lost you couldn't guess {word} ")
   elif  "_" not in dup:
       print("you guessed it correct")        

