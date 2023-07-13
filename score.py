import random
user_score=0
computer_score=0
for type in range(1,6,1):
    user_guess=int(input("Enter a number from 1 to 6: "))
    computer_guess= random.randint(1,6)
    print("computer guess is: "+str(computer_guess))
    if user_guess>computer_guess:
        user_score+=10
        print("You win")
        print("you:",user_score)
        print("computer:",computer_score)
    elif computer_guess>user_guess:
        computer_score+=10
        print("You lose")
        print("you:",user_score)
        print("computer:",computer_score)
    elif user_guess==computer_guess:
        print("draw")
        print("No score")
    



