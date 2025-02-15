# quiz with timer wednesday submission
import random,time
score = 0
questions_ =["1.What is the largest planet in our solar system?\na.jupiter\nb.uranus\nc.mecury\nd.earth\n",
           "2.What is the chemical symbol for water?\na.h2o\nb.hno3\nc.h2h\nd.w2o\n",
           "3.Which organ pumps blood in the human body?\na.kidney\nb.brain\nc.heart\nd.liver\n",
           "4.What is the capital city of France?\na.russia\nb.china\nc.india\nd.paris\n",
           "5.Which metal is liquid at room temperature?\na.steel\nb.mercury\nc.aluminium\nd.iron\n"]
answer_ = ["jupiter","h2o","heart","paris","mercury"]
score = 0
time_limit = 10

for i  in range (len(questions_)):
    print(f"score:{score}\n")
    print(questions_[i])
    st_tm = time.time()
    an =(input("answer:")).lower().strip(" ")
    time_che = time.time() - st_tm
    if  time_che > time_limit:
            print("time is up!!")
            continue
    if an  == answer_[i]  :
        print("\n")
        print(f"{an} is correct\n")
        score+=1
       
    elif an!= answer_[i]:
        print(f"incorrect !!  correct is:{answer_[i]}\n ")
    else:
      print("invalid input")
print(f"total score is: {score}/5 questions")
  