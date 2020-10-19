  
"""
Program for Image Movement
"""



""" Import Lib"""
import pygame
import rotateImage as rotator
import time


""" Initialize Pygame"""
pygame.init()


""" Set the Dimension of the Screen"""
Width = 483
Height = 484

""" Set the Screen"""

screen = pygame.display.set_mode((Width,Height))

""" Set The Title of Screen"""

pygame.display.set_caption("Moving Image")

""" Load the Image"""
screenImg = pygame.image.load("Images/MicroMouse Grid.png")

""" Display Image at Specific Co-Ordinate"""

screen.blit(screenImg,(0,0))


"""Load the Bot Image"""
botImg= pygame.image.load("Images/Grid BOt.png")
screen.blit(botImg,(0,0))
# rotator.blitRotate(screen,botImg,(15,15),180)

path=[]

pathInput = ""
v = int(input("Enetr"))
stepNum=1
EventStatus=""
cellX=0
cellY=v

cellYRotate = 15
cellXRotate = 15
angle=0

state=""
while True:
    
    
    pygame.display.flip()
    pygame.display.update()
    time.sleep(0.5)
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            EventStatus="Quit"
            break
       
        
    if EventStatus == "Quit":
        break
    
    
    screen.blit(screenImg,(0,0))
    
    #To Move Image in y direction till it reaches end and then move in x direction
    if cellY <=420:
        cellY=cellY+30
        
        
    elif cellX<=420:
        cellX=cellX+30
    else:
        state="done"
       
    
    
    screen.blit(botImg,(cellX,cellY))
    
    #-------------------------------------------
    
    #To Move as well as Rotate Image
    # if state=="done":
    #     if cellYRotate <=420:
    #         cellYRotate=cellYRotate+30
    #         angle=180
            
    #     else:
    #         cellXRotate=cellXRotate+30
    #         angle=270
            
    #     rotator.blitRotate(screen,botImg,(cellXRotate,cellYRotate),angle)