#PyGame
import pygame
import random

#initialize the pygame
pygame.init()

#Two values
screen = pygame.display.set_mode((800, 600))

#Title and icon
pygame.display.set_caption("Space Pirates")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

#Enemy
enemyImg = pygame.image.load("enemy.png")
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 0
enemyY_change = 0

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

#Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        #if keystroke is pressed check whether right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left arrow is pressed")
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                print("Right arrow is pressed")
                playerX_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Keystroke has been released")
            
            
    #RGB - red, green, blue - 0-255
    screen.fill((0, 0, 255))
    playerX += playerX_change
    if playerX <=0:
        playerX = 0
    elif playerX >= 700:
        playerX = 736
    
    playerY -= playerY_change
    
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
