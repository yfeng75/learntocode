
locations={0: "You are sitting in front of a computer learning python",
            1: "You are stadning at the endo f a road before a small brick building",
            2: "You are at the top of a hill",
            3: "You are inside a building, a well house for a small stream",
            4: "You are in a valley beside a stream",
            5: "You are in the forest"}

exits = {0:{"Q": 0},
        1:{"W": 2, "E": 3,"N": 5, "S": 4 , "Q": 0},
        2:{"N": 5,  "Q": 0},
        3:{"W": 1, "Q": 0},
        4:{"N": 1, "W": 2,"Q": 0},
        5:{"W": 2,  "S": 1 , "Q": 0}}

letter = {"WEST":"W","EAST": "E","NORTH": "N","SOUTH": "S","QUIT": "Q"}
# print(letter.values())
loc =1
while True:
    availableExits = ", ".join(exits[loc].keys())

    print(locations[loc])

    if loc ==0:
        break
    direction = input("Available exits are " +availableExits +":").upper()
    print()

    if letter[direction] in exits[loc]:
        loc=exits[loc][letter[direction]]
    else:
        print("You cannot go in that direction")
        