#random
#choice()
#randint(start,end)

#prrogram Constraints:
#take user input for no. of rounds
#for computers choice user random Module
#takes users input in every round
#after every round show the user and computers choice
#at last show the score and declare the winner

#NOTE : use your creativity to make the user Interface more meaningful

import random

def choice():
    return random.choice(["rock","paper","scissor"])

def randint(start,end):
    return random.randint(start,end)

def score():
    return randint(1,3)

def rock_paper_scissor(user,comp):
    if user == comp:
        print("user : ",user,"computer : ",comp,"draw")

    elif user == "rock" and comp == "scissor" :
        print("user : ",user,"computer : ",comp,"win")
    
    elif user == "rock" and comp == "paper" :
        print("user : ",user,"computer : ",comp,"lose")

    elif user == "paper" and comp == "sicssors":
        print("user : ",user,"computer : ",comp,"win")

    elif user == "paper" and comp == "rock":
        print("user : ",user,"computer : ",comp,"lose")

    elif user == "scissor" and comp == "paper":
        print("user : ",user,"computer : ",comp,"win")

    elif user == "scissor" and comp == "rock":
        print("user : ",user,"computer : ",comp,"lose")
    else:
        print("user : ",user,"computer : ",comp,"lose")
    
round = input()
for i in range(int(round)):
    user = input()
    comp = choice()
    # score = score()
    rock_paper_scissor(user,comp)
    # print("score : ",score)


    # if user == comp:
    #     print("user : ",user,"computer : ",comp,"draw")

    # elif user == "rock" and comp == "scissor" :
    #     print("user : ",user,"computer : ",comp,"win")
    
    # elif user == "rock" and comp == "paper" :
    #     print("user : ",user,"computer : ",comp,"lose")

    # elif user == "paper" and comp == "sicssors":
    #     print("user : ",user,"computer : ",comp,"win")

    # elif user == "paper" and comp == "rock":
    #     print("user : ",user,"computer : ",comp,"lose")

    # elif user == "scissor" and comp == "paper":
    #     print("user : ",user,"computer : ",comp,"win")

    # elif user == "scissor" and comp == "rock":
    #     print("user : ",user,"computer : ",comp,"lose")
    # else:
    #     print("user : ",user,"computer : ",comp,"lose")


#scores of rock,paper,sicssor
# if user == comp:
#     print("user : ",user,"computer : ",comp,"draw")
# elif user == "rock" and comp == "scissor" :
#     print("user : ",user,"computer : ",comp,"win")
# elif user == "rock" and comp == "paper" :
#     print("user : ",user,"computer : ",comp,"lose")
# elif user == "paper" and comp == "sicssors":
#     print("user : ",user,"computer : ",comp,"win")
# elif user == "paper" and comp == "rock":
#     print("user : ",user,"computer : ",comp,"lose")
# elif user == "scissor" and comp == "paper":
#     print("user : ",user,"computer : ",comp,"win")
# elif user == "scissor" and comp == "rock":
#     print("user : ",user,"computer : ",comp,"lose")
# else:
#     print("user : ",user,"computer : ",comp,"lose")
