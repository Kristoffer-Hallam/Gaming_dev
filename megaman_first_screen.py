# import modules
import pygame
from pygame.locals import *
import sys
import random

# Creating a tuple to hold the RGC values so that we can print our screen blue later
colorBLUE = (0, 0, 255)
colorRED = (255, 0, 0)
colorBLACK = (0, 0, 0)
colorPINK = (255, 200, 200)
colorGREEN = (0, 255, 0)
colorWHITE = (255, 255, 255)
colorYELLOW = (255, 255, 0)

# Initialize all of the Pygame modules so we can use them later on
pygame.init()

# Create the game screen and set it to 800 x 600 pixels
screen = pygame.display.set_mode((800, 600), 0, 32)

# Set a caption to our window
pygame.display.set_caption("Megaman")

# Draw a blue background ont our screen/window
screen.fill(colorBLACK)

# Prepare our font for text
myFont = pygame.font.SysFont('None', 40)

# Create a text object
# firstText = myFont.render("Megaman", True, colorRED, colorBLACK)

# Create the surface to write our text onto and its position
# firstTextRect = firstText.get_rect()
# firstTextRect.left = 500
# firstTextRect.top = 400

# blit our text to the window
# screen.blit(firstText, firstTextRect)

# Logo  image
logo_screen = pygame.Rect(0, 0, 800, 600)
logo = pygame.image.load('MM1_logo.jpeg')
thumbnail_logo = pygame.transform.scale(logo, (800, 400))
screen.blit(thumbnail_logo, logo_screen)

# Megaman image
megaman_screen = pygame.Rect(50, 250, 200, 350)#300, 250, 200, 350)
megaman = pygame.image.load('buster_above.png')
thumbnail_megaman = pygame.transform.scale(megaman, (200, 350))
screen.blit(thumbnail_megaman, megaman_screen)

# Drawing a circle
# pygame.draw.circle(screen, colorRED, (330, 475), 15, 1)
# pygame.draw.circle(screen, colorYELLOW, (375, 475), 15, 15)
# pygame.draw.circle(screen, colorPINK, (420, 475), 20, 10)

# Drawing rectangle
# pygame.draw.rect(screen, colorYELLOW, (455, 470, 20, 20))
# Drawing lines
# pygame.draw.line(screen, colorRED, (300, 500), (500, 500), 1)
# pygame.draw.line(screen, colorYELLOW, (300, 515), (500, 515), 1)
# pygame.draw.line(screen, colorWHITE, (300, 530), (500, 530), 1)

# Draw the now blue window to the screen
pygame.display.update()

# Create a variable to hold the value of whether the game should or not end
running = True

# Create a loop that will keep the game running
# until the user decides to quit
# When they do, it will change the value of running
# to False, ending the game

while True:
    # Get feedback from the player in the form of events
    for event in pygame.event.get():
        # If the player clicks the x button, it is considered a quit event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                shootText = myFont.render("Buster Fire!", True, colorRED, colorBLACK)
                shootTextRect = shootText.get_rect()
                shootTextRect.left = 500
                shootTextRect.top = 400
                screen.blit(shootText, shootTextRect)
                pygame.display.update()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_b:
                shootText = myFont.render("Buster Fire!", True, colorBLACK, colorBLACK)
                shootTextRect = shootText.get_rect()
                shootTextRect.left = 500
                shootTextRect.top = 400
                screen.blit(shootText, shootTextRect)
                pygame.display.update()
