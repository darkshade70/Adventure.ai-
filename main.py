import pygame
import proceduralGeneration

import rooms

dungeonArray = proceduralGeneration.generateDungeon()

# Define some colors
BLACK = (90, 90, 90)
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

# Setting display parentheses
display_width = 1200
display_height = 750


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


# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Set the screen background
    screen.fill(BLACK)

    # # Draw the grid
    # for row in range(5):
    #     for column in range(5):
    #         color = WHITE
    #         pygame.draw.rect(screen,
    #                          color,
    #                          [(MARGIN + WIDTH) * column + MARGIN,
    #                           (MARGIN + HEIGHT) * row + MARGIN,
    #                           WIDTH,
    #                           HEIGHT])

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
            if y > 0 and generatedObject.name != "     ":
                valueAbove = dungeonArray[y-1][x]
                if valueAbove != "     ":
                    # Generate Vertical Connection Above
                    displayVertical(MARGIN + x*WIDTH + MARGIN *
                                    x + 65, MARGIN + y*HEIGHT + MARGIN*y - 21)

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    pygame.display.update()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
