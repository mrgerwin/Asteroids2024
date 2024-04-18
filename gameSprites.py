import math
import pygame 
import random
import time

Speeds = [[0,1],[0,2],[0,3],[1,1], [1,2], [1,3], [-1, 1], [-1, 2], [-1, 3], [2, 1], [2, 2], [2, 3], [-2, 1], [-2, 2], [-2, 3], [0,-1],[0,-2],[0,-3],[1,-1], [1,-2], [1,-3], [-1, -1], [-1, -2], [-1, -3], [2, -1], [2, -2], [2, -3], [-2, -1], [-2, -2], [-2, -3]]

class Ammo(pygame.sprite.Sprite):
    def __init__(self, screen, position):
        super().__init__()
        self.image = pygame.image.load("Rockets_Bonus.png")
        self.image = pygame.transform.rotozoom(self.image, 0, .25)
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.screen = screen
        
class Asteroid(pygame.sprite.Sprite):
    def __init__(self, screen, position, size, speed=[1,1]):
        super().__init__()
        self.size = size
        self.speed = speed
        self.TurnSpeed = 10
        self.angle = 0
        self.screen = screen
        self.OriginalImage = pygame.image.load("Asteroid.png")
        self.OriginalImage = pygame.transform.rotozoom(self.OriginalImage, 0, self.size*.04)
        self.image = self.OriginalImage
        #self.rect = self.screen.blit(self.AsteroidImage, self.position)
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.HitImage = pygame.image.load("AsteroidHit.png")
        
    def rotate(self):
        self.angle += self.TurnSpeed
        originalPosition = self.rect.topleft
        originalCenter = self.rect.center
        self.image = pygame.transform.rotate(self.OriginalImage, self.angle)
        newRect = self.image.get_rect()
        self.rect.topleft = [originalCenter[0]-int(newRect.width/2), originalCenter[1]-int(newRect.height/2)]
        self.rect = self.screen.blit(self.image, self.rect.topleft)
        print("Rotating")
        
    def move(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]
        
    def collide(self):
        pass            
            
    def AsteroidTeleport(self):
        pass
    
    def hit(self):
        pass


class Ship(pygame.sprite.Sprite):
    def __init__(self, screen, position):
        super().__init__()
        self.OriginalImage = pygame.image.load("NewFrigate3.png")
        self.image = self.OriginalImage
        self.screen = screen
        #self.rect = self.screen.blit(self.image, self.position)
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.angle = 0
        self.speed = 0
        self.acceleration = 4
        self.TurnSpeed = 0
        self.TurnAcceleration = 4
        self.lives = 3
        self.fuel = 100
        self.alive = True
        self.shipImageGo = pygame.image.load("FrigateGo.png")
        self.explosion1 = pygame.image.load("explosion1.png")
        self.explosion2 = pygame.image.load("explosion2.png")
        self.explosion3 = pygame.image.load("explosion3.png")
    
    def rotate(self):
        self.angle += self.TurnSpeed
        originalPosition = self.rect.topleft
        originalCenter = self.rect.center
        self.image = pygame.transform.rotate(self.OriginalImage, self.angle)
        newRect = self.image.get_rect()
        self.rect.topleft = [originalCenter[0]-int(newRect.width/2), originalCenter[1]-int(newRect.height/2)]
        self.rect = self.screen.blit(self.image, self.rect.topleft)
     
    def move(self):

        self.rect.x += self.speed*math.cos((self.angle*math.pi)/180)  
        self.rect.y -= self.speed*math.sin((self.angle*math.pi)/180)
    
    def shipDeath(self, frame):
        #print ("you died FrameNum: " +str(frame))
        
        
        if self.alive == True:
            self.startFrame = frame
            self.alive = False
        frameDiff = frame - self.startFrame
        if frameDiff <= 5:
            self.image = self.explosion1
            print("Exp1")
        elif frameDiff <= 10:
            self.image = self.explosion2
            print("Exp2")
        elif frameDiff <= 15:
            self.image = self.explosion3
            print("Exp3")
        elif frameDiff == 20:
            self.position = [200,400]
            self.image = self.OriginalImage
            self.alive = True
            self.lives = 3
        self.rect = self.screen.blit(self.image, self.rect.topleft)
        #print(self.position)

  
class Laser(pygame.sprite.Sprite):
    def __init__(self, screen, position, angle, speed):
        super().__init__()
        self.Originalimg = pygame.image.load("LaserBeam.png")
        self.angle = angle
        self.screen = screen
        self.image = self.Originalimg
        self.speed = speed
        #self.Laserimage = pygame.transform.rotate(self.Laserimage, self.angle)
        
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.newRect = ""
        self.originalCenter = ""
        self.originalPosition = ""
        self.rotate()
        
    def rotate(self):
        self.originalPosition = self.rect.topleft
        self.originalCenter = self.rect.center
        self.image = pygame.transform.rotate(self.Originalimg, self.angle)
        self.newRect = self.image.get_rect()
        #self.rect.center = [self.originalCenter[0] -int(self.newRect.width/2), self.originalCenter[1] -int(self.newRect.height/2)]
    
    def shoot(self):
        self.rect.x+= self.speed*math.cos((self.angle*math.pi)/180)
        self.rect.y-= self.speed*math.sin((self.angle*math.pi)/180)
        #print(self.position)         
        
class Background:
    def __init__(self, screen):
        self.screen = screen
        self.BgImage = pygame.image.load("Background.jpg")
        self.BgRect = self.screen.blit(self.BgImage,[0,0])
    
    def drawBg(self):
        self.BgRect = self.screen.blit(self.BgImage,[0,0])
        