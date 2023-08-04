import random
no=random.randint(1,6)

question=input("Do you wish to roll a dice? Answer Yes if you do and answer No if you don't: ")
if(question=="Yes"):
    print(no)
elif(question=="No"):
    print("Ok, I guess you don't care about dice :(")