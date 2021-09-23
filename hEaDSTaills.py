import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800,600))
green = (0,255,0)
red = (199,0,0)
blue = (0,0,255)
hX = 100   
hY = 460
tX = 530
tY = 445
rX = 320
rY = 453
h = pygame.image.load('H.jpg')
t = pygame.image.load('T.jpg')
bg = pygame.image.load('htbg.png')
uWINH = pygame.image.load('uWINH.jpg')#DONE
uWIN = pygame.image.load('uWIN.jpg')#DONE
uLOST = pygame.image.load('uLOST.jpg')
uLOSTT = pygame.image.load('uLOSTT.jpg')#DONE
icon = pygame.image.load('coint.png ')
RESET = pygame.image.load('RESET_BUTTON.jpg')
headsCOIN = pygame.image.load('headsCOIN..png') 
tailsCOIN = pygame.image.load('tailsCOIN.png')
pygame.display.set_icon(icon)
white = (255,255,255)

uH = 0
uT = 0
flag = 0
cAnsChoice = ['Heads','Tails']
cChoice = random.choice(cAnsChoice)

color = (128, 246, 255)
run = True
screen.fill(color)  
while run:
    screen.blit(bg, (0,0))
    mx,my = pygame.mouse.get_pos()
    for event in pygame.event.get():
        uH = 0
        uT = 0
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (mx>=hX and mx<=hX+70) and (my>=hY and my<=hY+70):
                cAnsChoice = ['Heads','Tails']
                cChoice = random.choice(cAnsChoice) 
                print( 'computer:',cChoice)
                red = (255,0,0)
                uH +=1
                if (uH==1 and cChoice=='Heads') or (uT == 1 and cChoice=='Tails'):
                    print('U Win!')
                    screen.fill(color)
                    screen.blit(uWINH, (5,50))
                    # screen.blit(uLOSTT,(50,50))
                    
                else:
                    screen.fill(color)
                    screen.blit(uLOSTT,(30,50))
                    print('You Lost !')
                # print(uH)
            else:
                red = (255,0,0)
            if (mx>=tX and mx<=tX+70) and (my>=tY and my<=tY+70):
                cAnsChoice = ['Heads','Tails']
                cChoice = random.choice(cAnsChoice)
                print( 'computer:', cChoice)
                blue = (200,200,200)
                uT += 1
                if (uH==1 and cChoice=='Heads') or (uT == 1 and cChoice=='Tails'):
                    print('U Win!')
                    screen.fill(color)
                    screen.blit(uWIN,(10,50))
                    
                else:
                    print(  'you lost !')
                    screen.fill(color)
                    screen.blit(uLOST,(10,50))
            else:
                blue = (0,0,255)
            
            
    pygame.draw.rect(screen,color,(hX,hY,70,70))
    screen.blit(h,(110,550))
    pygame.draw.rect(screen,color,(tX,tY,70,70))
    screen.blit(t,(550,550))
    pygame.draw.rect(screen,(150,190,150),(rX-65,rY,200,70))
    screen.blit(headsCOIN,(hX,hY))
    screen.blit(tailsCOIN,(tX,tY))
    screen.blit(RESET,(rX-70,rY))
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (mx>=rX and mx<=rX+70) and (my>=rY and my<=rY+70):
            print('Done Resetting')
            screen.fill(color)
        



    pygame.display.update()


#let me run it
#this is the game, thanks for watching my game, it uses the random lib, to make a choice as for the computer :D  thanks...