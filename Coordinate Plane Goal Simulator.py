import random, sys
coordinateplane = int(input("How big should to coordinate plane be?"))
moves = 0
x, y = 0, 0
goalx = random.choice(list(range(-coordinateplane,coordinateplane)))
goaly = random.choice(list(range(-coordinateplane,coordinateplane)))
distance = abs(goalx+coordinateplane) + abs(goaly+coordinateplane) 
tryVar = ""
tryList = []
def randomwalks(n):
    for i in range(n):
        global x
        global y
        global tryVar
        choice = random.choice(["N", "S", "E", "W"])
        tryVar = str(i+1)
        if choice == "N":
            y += 1
            update()
        elif choice == "S":
            y -= 1
            update()
        elif choice == "E":
            x += 1
            update()
        else:
            x -= 1
            update()
            
def update():
    global moves
    global distance
    global tryList
    moves += 1
    print(str(moves) + "| Cordinates:", str(x)+ ",", y)
    if x >= 0:
        dx = goalx - x
    elif x < 0:
        dx = goalx + abs(x)
    if y >= 0:
        dy = goaly - y
    elif y < 0:
        dy = goaly + abs(y)
    
    if abs(dy)+abs(dx) == 0:
        distance = 0
        tryList.clear()
        tryList.append(tryVar)
        printStuff()
        sys.exit()
    if abs(dy)+abs(dx) < distance:
        distance = abs(dy) + abs(dx)
        tryList.clear()
        tryList.append(tryVar)
    elif abs(dy) + abs(dx) > distance:
        pass
    elif abs(dy) + abs(dx) == distance:
        tryList.append(tryVar)

def printStuff():
    print(distance)
    print(str(goalx)+","+str(goaly))
    print (tryList)

choice = int(input('How many simulations to run?'))

randomwalks(choice)

print(distance)
print(str(goalx)+","+str(goaly))
print(tryList)

        
    
