from random import randint

def superheroListItem():
    superheroList = ["Batman", "Superman", "Flash", "Iron Man", "Ant Man", "Spider Man", "Wonder Woman"]
    x = randint(0, len(superheroList) - 1)
    return superheroList[x]
