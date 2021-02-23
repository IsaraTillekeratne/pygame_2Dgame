import pygame
import random #to get random values
import math
from pygame import mixer
import time

#initialize
pygame.init() ##needed

#create game screen
screen = pygame.display.set_mode((800,600))

#title & icon
pygame.display.set_caption("Catch It")
icon = pygame.image.load("apple_logo.png") #32px
pygame.display.set_icon(icon)

#background
backgroundImg = pygame.image.load("backnew.jpg")

#background sound
mixer.music.load("backmusic.mp3")
mixer.music.play(-1) #play on loop

#player
playerImg = pygame.image.load("net.png") #128px
playerX = 335 #initiale position
playerY = 480
playerX_change = 0


#apple
appleImg = []
appleX = []
appleY  = []
appleY_change  = []
num_of_apples = 3

for i in range(num_of_apples):
    appleImg.append(pygame.image.load("apple.png")) #64px
    appleX.append(random.randint(0,735))
    appleY.append(random.randint(50,150))
    appleY_change.append(0.5)
    #time.sleep(2)


#print score
dropped = 0
score = 0
font = pygame.font.Font("freesansbold.ttf",32)
textX = 10
textY = 10

#game over
over_font = pygame.font.Font("freesansbold.ttf",32)

def game_over():
    over_text = over_font.render("YOU DROPPED 10 APPLES",True,(0,0,0))
    over_text2 = over_font.render("GAME OVER!",True,(0,0,0))
    screen.blit(over_text,(200,250))
    screen.blit(over_text2,(280,300))

def show_score(x,y):
    scoreVal = font.render("Score: "+ str(score),True,(255,255,255))
    screen.blit(scoreVal,(x,y))

def player(x,y):
    screen.blit(playerImg,(x,y)) #draw an image on screen

def apple(x,y,i):
    screen.blit(appleImg[i],(x,y))
    
def isCaught(appleX,appleY,playerX,playerY):
    distance = math.sqrt((math.pow(appleX-playerX,2))+(math.pow(appleY-playerY,2)))
    if distance<27:
        return True
    else:
        return False
    
def isDropped(appleY):
    if(appleY>500):
        return True
    return False
    
#infinite game loop
running = True
while running:
    screen.fill((0,0,0))   
    screen.blit(backgroundImg,(0,0))
    
    #go through events - button pressed
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False #close button ##needed
        if(event.type==pygame.KEYDOWN): #pressing any key
            if(event.key==pygame.K_LEFT): #checks if key is left
                playerX_change = -1
            if(event.key==pygame.K_RIGHT): #checks if key is right
                playerX_change = 1
            
                    
            
        if(event.type==pygame.KEYUP): #releasing key
            if(event.key==pygame.K_LEFT)or(event.key==pygame.K_RIGHT):
                playerX_change = 0
                
    
    #player movement            
    playerX += playerX_change

    if playerX <=0:
        playerX = 0
    if playerX >=736:
        playerX = 736
    
    for i in range(num_of_apples): 
        #score - when caught
        catch = isCaught(appleX[i],appleY[i],playerX,playerY)
        drop = isDropped(appleY[i])
        
        if(catch):
            catch_sound = mixer.Sound("catch.mp3")
            catch_sound.play()
            appleY[i] = 2000
            score += 1
            appleX[i] = random.randint(0,735)
            appleY[i] = random.randint(50,150)
        
        elif(drop):
            drop_sound = mixer.Sound("drop.mp3")
            drop_sound.play()
            appleY[i] = 2000
            dropped += 1
            appleX[i] = random.randint(0,735)
            appleY[i] = random.randint(50,150)
            
        #enemy movement
        
        appleY[i] += appleY_change[i]   
        apple(appleX[i],appleY[i],i)
       
        
    #loose
    if(dropped>=10):
        end_sound = mixer.Sound("gameEnd.mp3")
        end_sound.play()
        game_over()
        
    
    player(playerX,playerY)  
    show_score(textX,textY)  
    #update display
    pygame.display.update() ##needed
   