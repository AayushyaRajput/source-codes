# stone paper scissors game
import random
def game(comp,admin):
    if comp ==admin:
        return None
    if comp =="s":
        if admin == "p":
            return True
        elif admin =="sc":
            return False
    if comp == "p":
        if admin =="s":
            return False
        elif admin =="sc":
            return True
    if comp =="sc":
        if admin=="s":
            return False
        elif admin =="p":
            return True

print("comp turn = stone (s) paper (p) or scissors (sc)")
rando = random.randint(1,3)
if rando == 1:
    comp = "s"
elif rando ==2:
    comp= "p"
elif rando ==3:
    comp = "sc"

admin = input(" Your turn ")
a = game(comp,admin)