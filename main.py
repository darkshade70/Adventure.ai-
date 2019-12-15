import pygame
import proceduralGeneration

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

#Setting display parentheses
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
roomImg = pygame.image.load('room.png')
vendorImg = pygame.image.load('vendor.png')
moneyImg = pygame.image.load('money.png')
horizontalImg = pygame.image.load('horizontal.png')
verticalImg = pygame.image.load('vertical.png')
itemImg = pygame.image.load('item.png')
mobImg = pygame.image.load('mob.png')
stairsImg = pygame.image.load('stairs.png')
trapImg = pygame.image.load('trap.png')
bossImg = pygame.image.load('boss.png')
startImg = pygame.image.load('start.png')
playerImg = pygame.image.load('player.png')

def displayRoom(x, y):
    gameDisplay.blit(roomImg, (x, y))

def displayVendor(x, y):
    gameDisplay.blit(vendorImg, (x, y))

def displayMoney(x, y):
    gameDisplay.blit(moneyImg, (x, y))

def displayHorizontal(x, y):
    gameDisplay.blit(horizontalImg, (x, y))

def displayVertical(x, y):
    gameDisplay.blit(verticalImg, (x, y))

def displayItem(x, y):
    gameDisplay.blit(itemImg, (x, y))

def displayMob(x, y):
    gameDisplay.blit(mobImg, (x, y))

def displayStairs(x, y):
    gameDisplay.blit(stairsImg, (x, y))

def displayTrap(x, y):
    gameDisplay.blit(trapImg, (x, y))

def displayBoss(x, y):
    gameDisplay.blit(bossImg, (x, y))

def displayStart(x, y):
    gameDisplay.blit(startImg, (x, y))

def displayPlayer(x, y):
    gameDisplay.blitz(playerImg, (x, y))


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
            generatedValue = dungeonArray[y][x]
            if generatedValue == "     ":
                continue
            displayRoom(MARGIN + x*WIDTH + MARGIN*x, MARGIN + y*HEIGHT + MARGIN*y)
            if generatedValue == "Player":
                displayPlayer(MARGIN + x*WIDTH + MARGIN*x + 52.5, MARGIN + y*HEIGHT + MARGIN*y + 17.5)
            elif generatedValue == "VendR":
                displayVendor(MARGIN + x*WIDTH + MARGIN*x + 52.5, MARGIN + y*HEIGHT + MARGIN*y + 17.5)
            elif generatedValue == "Guard":
                displayMob(MARGIN + x*WIDTH + MARGIN*x + 52.5, MARGIN + y*HEIGHT + MARGIN*y + 17.5)
            elif generatedValue == "Traps":
                displayTrap(MARGIN + x*WIDTH + MARGIN*x + 52.5, MARGIN + y*HEIGHT + MARGIN*y + 17.5)
            elif generatedValue == "Items":
                displayItem(MARGIN + x*WIDTH + MARGIN*x + 52.5, MARGIN + y*HEIGHT + MARGIN*y + 17.5)
            elif generatedValue == "Money":
                displayMoney(MARGIN + x*WIDTH + MARGIN*x + 52.5, MARGIN + y*HEIGHT + MARGIN*y + 17.5)
            elif generatedValue == "BossR":
                displayBoss(MARGIN + x*WIDTH + MARGIN*x + 52.5, MARGIN + y*HEIGHT + MARGIN*y + 17.5)
            elif generatedValue == "Stair":
                displayStairs(MARGIN + x*WIDTH + MARGIN*x + 52.5, MARGIN + y*HEIGHT + MARGIN*y + 17.5)
            elif generatedValue == "Start":
                displayStart(MARGIN + x*WIDTH + MARGIN*x + 60, MARGIN + y*HEIGHT + MARGIN*y + 17.5)
            elif generatedValue == "PlayRer":
                displayStairs(MARGIN + x*WIDTH + MARGIN*x + 52.5, MARGIN + y*HEIGHT + MARGIN*y + 17.5)

            # Connections
            if x > 0 and y > 0 and generatedValue != "     ":
                valueAbove = dungeonArray[y-1][x]
                if valueAbove != "     ":
                    # Generate Vertical Connection Above
                    displayVertical(MARGIN + x*WIDTH + MARGIN*x + 65, MARGIN + y*HEIGHT + MARGIN*y - 21)
                valueLeft = dungeonArray[y][x-1]
                if valueLeft != "     ":
                    # Generate Horizontal Connection to the left
                    displayHorizontal(MARGIN + x*WIDTH + MARGIN*x - 21, MARGIN + y*HEIGHT + MARGIN*y + 30)



    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    pygame.display.update()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
