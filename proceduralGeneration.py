import random
import rooms

# test

# 1 = room
# 0 = empty cell

stairCase = False


def generateDungeon():
    dungeonArray = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    roomNumb = 1
    while roomNumb < 9:
        for y in range(len(dungeonArray)):
            for x in range(len(dungeonArray[y])):
                if dungeonArray[y][x] == 1:
                    pass
                elif (y == 0 and dungeonArray[y + 1][x] == 1) or (x == 0 and dungeonArray[y][x + 1] == 1) or (
                        x != 0 and x != (len(dungeonArray[y]) - 1) and (
                        dungeonArray[y][x + 1] == 1 or dungeonArray[y][x - 1] == 1)) or (
                        y != 0 and y != (len(dungeonArray[y]) - 1) and (
                        dungeonArray[y + 1][x] == 1 or dungeonArray[y - 1][x] == 1)) or (
                        x == (len(dungeonArray[y]) - 1) and dungeonArray[y][x - 1] == 1) or (
                        y == (len(dungeonArray) - 1) and dungeonArray[y - 1][x] == 1):
                    chance = random.randint(0, 2)
                    if chance == 0:
                        dungeonArray[y][x] = 1
                        roomNumb += 1
                    else:
                        dungeonArray[y][x] = 0

    def naming():
        global stairCase
        for y in range(len(dungeonArray)):
            for x in range(len(dungeonArray[y])):
                if x == 2 and y == 2:
                    dungeonArray[y][x] = rooms.StartRoom()
                elif dungeonArray[y][x] == 0:
                    dungeonArray[y][x] = "     "
                elif dungeonArray[y][x] == 1:
                    if stairCase == False:
                        stairChance = random.randint(0, 20)
                        if stairChance == 0:
                            dungeonArray[y][x] = rooms.StairsRoom()
                            stairCase = True
                            return ()
                    elif stairCase == True:
                        chance = random.randint(1, 100)
                        if chance >= 1 and chance <= 10:
                            dungeonArray[y][x] = rooms.MoneyRoom()
                        elif chance >= 11 and chance <= 40:
                            dungeonArray[y][x] = rooms.MobRoom()
                        elif chance >= 41 and chance <= 100:
                            dungeonArray[y][x] = rooms.EmptyRoom()

                        # if chance >= 1 and chance <= 6:
                        #     dungeonArray[y][x] = rooms.VendorRoom()
                        # elif chance >= 7 and chance <= 30:
                        #     dungeonArray[y][x] = rooms.MobRoom()
                        # elif chance >= 31 and chance <= 50:
                        #     dungeonArray[y][x] = rooms.EmptyRoom()
                        # elif chance >= 51 and chance <= 80:
                        #     dungeonArray[y][x] = rooms.TrapsRoom()
                        # elif chance >= 81 and chance <= 84:
                        #     dungeonArray[y][x] = rooms.ItemsRoom()
                        # elif chance == 85:
                        #     dungeonArray[y][x] = rooms.MoneyRoom()
                        # elif chance >= 86 and chance <= 100:
                        #     dungeonArray[y][x] = rooms.BossRoom()

    while stairCase == False:
        naming()
    naming()

    for y in range(len(dungeonArray)):
        print(dungeonArray[y])
    return dungeonArray
