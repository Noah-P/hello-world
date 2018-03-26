import random
import pprint
coordinateplane = int(input("How big should to coordinate plane be?"))
moves = 0
x, y = 0, 0
dx, dy = 0, 0
goalx = random.choice(list(range(-coordinateplane, coordinateplane)))
goaly = random.choice(list(range(-coordinateplane, coordinateplane)))
distance = abs(goalx+coordinateplane) + abs(goaly+coordinateplane) 
tryList = {}
finalList = {}
simulation = 0
jk = 0


def randomwalks(n):
    for d in range(n):
        choose()
        if abs(dy)+abs(dx) == 0:
            global distance
            distance = 0
            tryList.clear()
            finalList["Simulation", jk] = moves               
            break


def choose():
        global x
        global y
        choice = random.choice(["N", "S", "E", "W"])
        if choice == "N":
            if y + 1 < coordinateplane + 1:
                y += 1
                update()
            else:
                choose()
        elif choice == "S":
            if y - 1 > -coordinateplane - 1:
                y -= 1
                update()
            else:
                choose()
        elif choice == "E":
            if x + 1 < coordinateplane + 1:
                x += 1
                update()
            else:
                choose()
        else:
            if x - 1 > - coordinateplane - 1:
                x -= 1
                update()
            else:
                choose()
            
            
def update():
    global moves
    global distance
    global tryList
    global dx
    global dy
    moves += 1
    print(str(simulation)+"."+str(moves) + "| Cordinates:", str(x) + ",", y)
    if x >= 0:
        dx = goalx - x
    elif x < 0:
        dx = goalx + abs(x)
    if y >= 0:
        dy = goaly - y
    elif y < 0:
        dy = goaly + abs(y)
    if abs(dy)+abs(dx) < distance:
        distance = abs(dy) + abs(dx)
        tryList.clear()
        tryList['Simulation', jk] = moves
    elif abs(dy) + abs(dx) > distance:
        pass
    elif abs(dy) + abs(dx) == distance:
        tryList['Simulation', jk] = moves


num_of_choice = int(input('How many simulations to run?'))
choiceTwo = int(input('How many movements in each simulation?'))

for i in range(num_of_choice):
    jk = i + 1
    simulation += 1
    moves = 0
    x, y = 0, 0
    randomwalks(choiceTwo)


if finalList:
    print(distance)
    print(str(goalx)+","+str(goaly))
    pprint.pprint(finalList)
else:
    print(distance)
    print(str(goalx)+","+str(goaly))
    pprint.pprint(tryList)
