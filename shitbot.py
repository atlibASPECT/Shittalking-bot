import sys
import random

ans = True

while ans:
    question = input("Ask the trashtalking bot what to say: (press enter to quit) ")
    
    answers = random.randint(1,8)
    
    if question == "":
        sys.exit()
    
    elif answers == 1:
        print ("I am better then you tho!")
    
    elif answers == 2:
        print ("Are you dumb or what?")
    
    elif answers == 3:
        print ("You are just shit so stfu!")
    
    elif answers == 4:
        print ("Cant ever hear you dumbass!")
    
    elif answers == 5:
        print ("Sure, but you are more gay!")
    
    elif answers == 6:
        print ("Sure thing buddy, wanna hit first?")
    
    elif answers == 7:
        print ("Whatever floats your boat dumbass!")
    
    elif answers == 8:
        print ("Imagine being gay...")