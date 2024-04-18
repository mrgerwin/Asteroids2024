import math
import pygame 
import random
import time
from gameSprites import *

def drawText(font):
    label = font.render("OBJECTIVE: DESTROY THE ASTEROIDS", True, white)
    
    window.blit(label, (130, 20))

def drawText2(font):
    controlText = font.render("SPACE = Shoot            Arrow Keys to Move", True, white)
    
    window.blit(controlText, (35, 700))
    
def drawPoints(font):
    PointsText = font.render("Rocks Destroyed:", True, white)
    
    window.blit(PointsText, (235, 50))
def drawLives(font):
    livesText = font.render("Lives: ", True, white)
    
    window.blit(livesText, (280, 700))
    
def DrawPointIncrease(position):
    PointIncreaseText = font.render("+1",True, white)

    window.blit(PointIncreaseText, position)
    
def increasePoints():
    pass

def Split(asteroid):
    global tempPosition
    tempPosition = asteroid.rect.topright
    NumOfAst = random.randint(2,4)
    for i in range(NumOfAst):
        NewAst = Asteroid(window,[asteroid.rect.x, asteroid.rect.y] , asteroid.size-1, [1,1])
        asteroidSprites.add(NewAst)
    asteroidSprites.kill(asteroid)
def SpawnAsteroid():
    X = random.randint(-150, 800)
    Y = -150
    NewAst = Asteroid(window,[X, Y], random.randint(1, 3), random.choice(AsteroidSpeeds))
    asteroidSprites.add(NewAst)

#Intial Game Variables
black = [0 ,0,0]
white = [255, 255, 255]
screen_size = [800,800]
window = pygame.display.set_mode(screen_size)
timer = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont("consolas", 30)
FrameNum = 0
tempPosition = [-10,0]
Background = Background(window)

#Initial Game Objects
player = Ship(window,[200,400])
Asteroid1 = Asteroid(window,[100,100], 3, [1,1])
ammo = Ammo(window, [600, 500])
laser = Laser(window, [400, 400], 0, 3) 

#Sprite Groups Lists
laserSprites = pygame.sprite.Group()
missleSprites= pygame.sprite.Group()
shipSprites = pygame.sprite.Group()
asteroidSprites = pygame.sprite.Group()
powerupSprites = pygame.sprite.Group()
allSprites = pygame.sprite.Group()

#Adding Sprites to their correct groups
shipSprites.add(player)
asteroidSprites.add(Asteroid1)
powerupSprites.add(ammo)
laserSprites.add(laser)
allSprites.add(player)
allSprites.add(Asteroid1)
allSprites.add(ammo)
allSprites.add(laser)

while True:
    FrameNum += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit = True
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:

                print("Pressed space")
            
            elif event.key == pygame.K_a:
                player.TurnSpeed=player.TurnAcceleration
                #print(player.TurnSpeed)
            if event.key == pygame.K_d:
                player.TurnSpeed=-player.TurnAcceleration
                #print(player.TurnSpeed)
            if event.key == pygame.K_w:
                player.speed = player.acceleration
            if event.key == pygame.K_LEFT:
                player.TurnSpeed=player.TurnAcceleration
                #print(player.TurnSpeed)
            if event.key == pygame.K_RIGHT:
                player.TurnSpeed=-player.TurnAcceleration
                #print(player.TurnSpeed)
            if event.key == pygame.K_UP:
                player.speed = player.acceleration
            
            #These keys only used for testing
            if event.key == pygame.K_k:
                player.lives = 0
                print("Player Died")
            if event.key == pygame.K_r:
                for sprite in asteroidSprites:
                    sprite.rotate()
                for sprite in laserSprites:
                    sprite.angle += 45
                    sprite.rotate()
            if event.key == pygame.K_s:
                for sprite in laserSprites:
                    sprite.shoot()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.speed =0
            if event.key == pygame.K_LEFT:
                player.TurnSpeed=0
            if event.key == pygame.K_RIGHT:
                player.TurnSpeed=0  
            if event.key == pygame.K_w:
                player.speed =0
            if event.key == pygame.K_a:
                player.TurnSpeed=0
            if event.key == pygame.K_d:
                player.TurnSpeed=0
    window.fill(black)
    Background.drawBg()
    
    if player.lives>0:
        player.rotate()
        player.move()
    else:
        player.shipDeath(FrameNum)
    #player.draw(FrameNum)
    if pygame.sprite.spritecollideany(player, powerupSprites):
        powerup = pygame.sprite.spritecollideany(player, powerupSprites)
        powerup.kill()
    drawText(font)
    drawText2(font)
    drawLives(font)
    drawPoints(font)
    allSprites.draw(window)
    #DrawPointIncrease(tempPosition)
    
    pygame.display.flip()
    timer.tick(30)


