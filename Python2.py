import random
max = input("Type a max number: ")

if max.isdigit():
    max = int(max)

    if max <= 0:
        print("enter number > 0 please!")
        quit()
else:
    print("Type number ")
    quit()

num = random.randrange(0,max)
guesses = 0

while True:
    guesses += 1
    User_guess = input("Make a guess: ")
    if User_guess.isdigit():
        User_guess = int(User_guess)
    else:
        print("Please type a number")
        continue
    if User_guess == num:
        print("You got it in " + str(guesses) + " tries!")
        break
    else:
        if User_guess > num:
            print("go lower")
        else:
            print("go higher")
    print("Incorrect!")