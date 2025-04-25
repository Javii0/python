print("Welcome to my Quiz")
playing = input("Do you want to play? ") #input is a function for next user input
if playing != "yes":
    quit() 
print("Okay!")
score = 0
ans = input("Best Healer in Rivals?: ")
if ans.lower() == "luna":
    print("Corect!")
    score += 1
else:
    print("Wrong!")

ans = input("Best DPS in Rivals?: ")
if ans.lower() == "bucky":
    print("Corect!")
    score += 1
else:
    print("Wrong!")

ans = input("Best Tank in Rivals?: ")
if ans.lower() == "groot":
    print("Corect!")
    score += 1
else:
    print("Wrong!")

print("Score is :"  + str(score) + "/3")
print(str((score/3) * 100) + "%")