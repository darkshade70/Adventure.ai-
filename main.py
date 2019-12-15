import pygame
import proceduralGeneration

import rooms
from random import randrange
import json

dungeonArray = proceduralGeneration.generateDungeon(False)

# Define some colors
GREY = (90, 90, 90)
BLACK = (60, 60, 60)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 155
HEIGHT = 85

# This sets the margin between each cell
MARGIN = 17

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(5):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(5):
        grid[row].append(0)  # Append a cell

# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)

# Initialize pygame
pygame.init()

# Font
font = pygame.font.SysFont('ariel', 20)

# Setting display parentheses
display_width = 1200
display_height = 790


# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [800, 877]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Adventure Text Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width, display_height))

# VARIABLES TO MODIFY FOR USER GUI
mainText = "You find yourself in the middle of a dungeon, dark, and alone. Which way will you go?"
text1 = ""
text2 = ""
text3 = ""
text4 = ""

# Top variables
levelCounter = 0
moneyCounter = 50

# starting points for graph
updatedX = 2
updatedY = 2

# ROOMS
startImg = pygame.image.load(rooms.StartRoom().image)
stairsImg = pygame.image.load(rooms.StairsRoom().image)
vendorImg = pygame.image.load(rooms.VendorRoom().image)
mobImg = pygame.image.load(rooms.MobRoom().image)
emptyImg = pygame.image.load(rooms.EmptyRoom().image)
trapsImg = pygame.image.load(rooms.TrapsRoom().image)
itemsImg = pygame.image.load(rooms.ItemsRoom().image)
moneyImg = pygame.image.load(rooms.MoneyRoom().image)
bossImg = pygame.image.load(rooms.BossRoom().image)

# PATHS
horizontalImg = pygame.image.load('Pixel Art/horizontal.png')
verticalImg = pygame.image.load('Pixel Art/vertical.png')


def displayRoom(x, y):
    gameDisplay.blit(emptyImg, (x, y))


def displayVendor(x, y):
    gameDisplay.blit(vendorImg, (x, y))


def displayMoney(x, y):
    gameDisplay.blit(moneyImg, (x, y))


def displayHorizontal(x, y):
    gameDisplay.blit(horizontalImg, (x, y))


def displayVertical(x, y):
    gameDisplay.blit(verticalImg, (x, y))


def displayItem(x, y):
    gameDisplay.blit(itemsImg, (x, y))


def displayMob(x, y):
    gameDisplay.blit(mobImg, (x, y))


def displayStairs(x, y):
    gameDisplay.blit(stairsImg, (x, y))


def displayTrap(x, y):
    gameDisplay.blit(trapsImg, (x, y))


def displayBoss(x, y):
    gameDisplay.blit(bossImg, (x, y))


def displayStart(x, y):
    gameDisplay.blit(startImg, (x, y))


def computeCood(x, y, direction):
    newY = y
    newX = x
    print(direction)
    if direction == "up":
        newY -= 1
    elif direction == "down":
        newY += 1
    elif direction == "left":
        newX -= 1
    elif direction == "right":
        newX += 1
    print(newX, newY)
    return newX, newY


released = True
# for each room
alreadyRand = False
rand = 1
result1 = ""
result2 = ""
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Set the screen background
    screen.fill(GREY)

    # Player Location Rectangle
    pygame.draw.rect(gameDisplay, RED, (14 + updatedX*159 + 13.5*updatedX, 14 + updatedY*89 + 13.5*updatedY, 159, 89))

    for x in range(5):
        for y in range(5):
            generatedObject = dungeonArray[y][x]
            if generatedObject == "     ":
                continue
            displayRoom(MARGIN + x*WIDTH + MARGIN*x,
                        MARGIN + y*HEIGHT + MARGIN*y)
            if generatedObject.name == "Vendor":
                displayVendor(MARGIN + x*WIDTH + MARGIN*x + 52.5,
                              MARGIN + y*HEIGHT + MARGIN*y + 17.5)
            elif generatedObject.name == "Mob":
                displayMob(MARGIN + x*WIDTH + MARGIN*x + 52.5,
                           MARGIN + y*HEIGHT + MARGIN*y + 17.5)
            elif generatedObject.name == "Traps":
                displayTrap(MARGIN + x*WIDTH + MARGIN*x + 52.5,
                            MARGIN + y*HEIGHT + MARGIN*y + 17.5)
            elif generatedObject.name == "Items":
                displayItem(MARGIN + x*WIDTH + MARGIN*x + 52.5,
                            MARGIN + y*HEIGHT + MARGIN*y + 17.5)
            elif generatedObject.name == "Money":
                displayMoney(MARGIN + x*WIDTH + MARGIN*x + 52.5,
                             MARGIN + y*HEIGHT + MARGIN*y + 17.5)
            elif generatedObject.name == "Boss":
                displayBoss(MARGIN + x*WIDTH + MARGIN*x + 52.5,
                            MARGIN + y*HEIGHT + MARGIN*y + 17.5)
            elif generatedObject.name == "Stairs":
                displayStairs(MARGIN + x*WIDTH + MARGIN*x + 52.5,
                              MARGIN + y*HEIGHT + MARGIN*y + 17.5)
            elif generatedObject.name == "Start":
                displayStart(MARGIN + x*WIDTH + MARGIN*x + 60,
                             MARGIN + y*HEIGHT + MARGIN*y + 17.5)

            if x > 0 and generatedObject.name != "     ":
                valueLeft = dungeonArray[y][x - 1]
                if valueLeft != "     ":
                    # Generate Horizontal Connection to the left
                    displayHorizontal(
                        MARGIN + x * WIDTH + MARGIN * x - 21, MARGIN + y * HEIGHT + MARGIN * y + 30)
                    # Create horizontal connections in objects
                    if len(generatedObject.connected) < 4 and len(valueLeft.connected) < 4:
                        generatedObject.connected.add("left")
                        valueLeft.connected.add("right")
            if y > 0 and generatedObject.name != "     ":
                valueAbove = dungeonArray[y-1][x]
                if valueAbove != "     ":
                    # Generate Vertical Connection Above
                    displayVertical(MARGIN + x*WIDTH + MARGIN *
                                    x + 65, MARGIN + y*HEIGHT + MARGIN*y - 21)
                    # Create vertical connections in objects
                    if len(generatedObject.connected) < 4 and len(valueAbove.connected) < 4:
                        generatedObject.connected.add("up")
                        valueAbove.connected.add("down")

    room = dungeonArray[updatedY][updatedX]

    # Room checks! Code for rooms can be written here!
    if room == "     ":
        print("Something went terribly wrong, as you've ended up on an empty space! Please contact the developers for further assistance. ")
        continue
    if room.name == "Stairs":
        mainText = "You find a spiralling staircase, and slowly make your way to the next level of the dungeon."
        # Put ML code here if you want andy
        dungeonArray = proceduralGeneration.generateDungeon(False)
        room = dungeonArray[2][2]
        updatedX = 2
        updatedY = 2
        levelCounter += 1
    elif room.name == "Empty":
        pass  # Code here ML for empty room
    if room.state or len(room.outcomes) == 0:
        for i, connectedRoom in enumerate(room.connected):
            if i == 0:
                text1 = connectedRoom
            elif i == 1:
                text2 = connectedRoom
            elif i == 2:
                text3 = connectedRoom
            elif i == 3:
                text4 = connectedRoom
    else:
        outcomes_pth = room.outcomes
        # random generation for prompts
        if not alreadyRand:
            rand = randrange(10) + 1
            alreadyRand = True

        with open(outcomes_pth) as f:
            json_outcomes = json.load(f)
            prompt = json_outcomes[str(rand)]
        mainText = prompt["text"]
        # print(prompt["action"])
        for i, action in enumerate(prompt["action"]):
            if i == 0:
                text1 = action
                result1 = prompt["result"][i]
            elif i == 1:
                text2 = action
                result2 = prompt["result"][i]

    # ANDY LOOK THROUGH THIS IF YOU WANT TO USE ANY OF IT?
    # Room checks! Code for rooms can be written here!
    # if room == "     ":
    #     print(
    #         "Something went terribly wrong, as you've ended up on an empty space! Please contact the developers for further assistance. ")
    #     continue
    # if room.name == "Stairs":
    #     mainText = "You find a spiralling staircase, and slowly make your way to the next level of the dungeon."
    #     # Put ML code here if you want andy
    #     dungeonArray = proceduralGeneration.generateDungeon(False)
    #     room = dungeonArray[2][2]
    #     updatedX = 2
    #     updatedY = 2
    #     levelCounter += 1
    # elif room.name == "Empty":
    #     pass  # Code here ML for empty room
    # elif room.name == "Money":
    #     randomMoney = random.randint(levelCounter - levelCounter / 2, levelCounter + levelCounter / 2) * 100
    #     mainText = "You find a chest with " + str(randomMoney) + " in it! All the gear you could buy with that..."
    #     moneyCounter += randomMoney
    # elif room.name == "Mob":
    #     pass  # Combat Mechanics? :D

    # Text box
    pygame.draw.rect(gameDisplay, RED, (8, 550, 1185, 100))
    mainTextRender = font.render(mainText, True, (255, 255, 255))
    gameDisplay.blit(mainTextRender, (20, 595))

    # Choice Background
    pygame.draw.rect(gameDisplay, BLACK, (8, 650, 1185, 135))

    # Choices
    button1 = pygame.draw.rect(gameDisplay, WHITE, (12, 655, 585, 60))
    text1render = font.render(text1, True, (0, 0, 0))
    gameDisplay.blit(text1render, (20, 680))
    button2 = pygame.draw.rect(gameDisplay, WHITE, (604, 655, 585, 60))
    text2render = font.render(text2, True, (0, 0, 0))
    gameDisplay.blit(text2render, (612, 680))
    button3 = pygame.draw.rect(gameDisplay, WHITE, (12, 720, 585, 60))
    text3render = font.render(text3, True, (0, 0, 0))
    gameDisplay.blit(text3render, (20, 745))
    button4 = pygame.draw.rect(gameDisplay, WHITE, (604, 720, 585, 60))
    text4render = font.render(text4, True, (0, 0, 0))
    gameDisplay.blit(text4render, (612, 745))

    # Display counter at the top
    levelFont = pygame.font.SysFont('arial', 40)
    levelText = "Level: " + str(levelCounter)
    levelTextRender = levelFont.render(levelText, True, (255, 255, 255))
    gameDisplay.blit(levelTextRender, (900, 70))

    moneyText = "AdventureCoins: " + str(moneyCounter)
    moneyTextRender = levelFont.render(moneyText, True, (255, 255, 255))
    gameDisplay.blit(moneyTextRender, (900, 20))

    pos = pygame.mouse.get_pos()
    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
    # Check if the rect collided with the mouse pos
    # and if the left mouse button was pressed.

    # Released is defined before the game loop to ensure it doesn't keep resetting, and stops buttons
    # firing 30 times on click.
    # Replace print function with anything you want the scenarios to do as we discussed
    if pressed1 and released is True:
        if button1.collidepoint(pos):
            if(len(text1) > 0):
                if room.state or len(room.outcomes) == 0:
                    updatedX, updatedY = computeCood(updatedX, updatedY, text1)
                    mainText = ""
                    text1 = ""
                    text2 = ""
                    text3 = ""
                    text4 = ""
                    alreadyRand = False
                    result1 = ""
                    result2 = ""
                else:
                    mainText = result1
                    room.state = True

            released = False
        elif button2.collidepoint(pos):
            if(len(text2) > 0):
                if room.state or len(room.outcomes) == 0:
                    updatedX, updatedY = computeCood(updatedX, updatedY, text2)
                    mainText = ""
                    text1 = ""
                    text2 = ""
                    text3 = ""
                    text4 = ""
                    alreadyRand = False
                    result1 = ""
                    result2 = ""
                else:
                    mainText = result2
                    room.state = True

            released = False
        elif button3.collidepoint(pos):
            if(len(text3) > 0):
                if room.state or len(room.outcomes) == 0:
                    updatedX, updatedY = computeCood(updatedX, updatedY, text3)
                    mainText = ""
                    text1 = ""
                    text2 = ""
                    text3 = ""
                    text4 = ""
                    alreadyRand = False
                    actualResult = ""
                    result1 = ""
                    result2 = ""
                else:
                    pass

            released = False
        elif button4.collidepoint(pos):
            if(len(text4) > 0):
                if room.state or len(room.outcomes) == 0:
                    updatedX, updatedY = computeCood(updatedX, updatedY, text4)
                    mainText = ""
                    text1 = ""
                    text2 = ""
                    text3 = ""
                    text4 = ""
                    alreadyRand = False
                    actualResult = ""
                    result1 = ""
                    result2 = ""
                else:
                    pass

            released = False
    if not pressed1 and released is False:
        released = True

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    pygame.display.update()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
