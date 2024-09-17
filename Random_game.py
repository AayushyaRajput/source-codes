import random
rando = random.randint(1,50)
player = None
guess = 0

while player!= rando:
    player = int(input("Try your luck "))
    if player==rando:
        print("You won ")
    elif player>rando:
        print("Try again this time lesser number")
    else:
        print("Try again but this time greater number")
    guess += 1

print(f"Congrates you took {guess} guesses")   

with open("files.txt","r") as f:
    bestscore = int(f.read())

if bestscore is None or guess>bestscore:
    print("Congrats you just break the record")
    with open("file.txt","w") as f:
        f.write(str(guess))

else:
    print(f"The current high score is {bestscore}")