  
import pygame
import time
import rotateImage as rotator
import pygame.font
pathInput = ''
run = ''
pygame.init()

size = (1259,677)
screen = pygame.display.set_mode(size)




pygame.display.set_caption("Step Simulator")


background = pygame.image.load("Images/Step_Markings_V2.png")
screen.blit(background,(0,0))
bot = pygame.image.load("Images/Grid BOt.png")
image1 = pygame.image.load("Images/Stepper Motor Symbol.png")
image1 = pygame.transform.scale(image1,(210,210))
image2 = pygame.image.load("Images/Stepper Motor Symbol 2.png")
image2 = pygame.transform.scale(image2,(210,210))


done = True



while pathInput != 'x':
    path = input('Enter your path or stop it by typing x:- ')


a = float(input('Enter the Distance the bot wants to travel (in cm):- '))
b = int(input("Enter the Step Angle of the robot's first stepper motor:- "))
b1 = b
b2 = b
c = float(input('Enter the Diameter of the first wheel of the bot (in cm) :- '))
y = int(input("Enter the Step Angle of the robot's second stepper motor:- "))
y1 = y
y2 = y
z = float(input('Enter the Diameter of the second wheel of the bot (in cm) :- '))

# finding the circumference
pi = 3.14
circum = pi * c

# finding the length of the steps
step_len = (circum * b) / 360

# finding the number of steps
step_num = a / step_len


circum2 = pi * z

# finding the length of the steps
step_len2 = (circum * y) / 360
step_num2 = a / step_len2
while run:
    screen.blit(background, (0,0))
    
    #win.blit(bot, (700, 0))
    rotator.blitRotate(screen, bot, (700, 2), 180)
    font = pygame.font.SysFont('SHOWCARD GOTHIC', 45)
    sa1 = font.render(str(b), True, (0, 0, 0))
    screen.blit(sa1, (550, 200))
    sa2 = font.render(str(y), True, (0, 0, 0))
    screen.blit(sa2, (550, 465))
    sn1 = font.render(str(int(step_num)), True, (0, 0, 0))
    screen.blit(sn1, (580, 270))
    sn2 = font.render(str(int(step_num2)), True, (0, 0, 0))
    screen.blit(sn2, (580, 535))
    wd1 = font.render(str(int(c)), True, (0, 0, 0))
    screen.blit(wd1, (670, 310))
    wd2 = font.render(str(int(z)), True, (0, 0, 0))
    screen.blit(wd2, (675, 580))

    if step_num >= 0:
        rotator.blitRotate(screen, image1, (90,200), b1)
        step_num = step_num - 1
        time.sleep(1)
    if step_num2 >= 0:
        rotator.blitRotate(screen, image2, (0,380), y1)
        step_num2 = step_num2 - 1
        time.sleep(1)

    b1 = b1 - b2
    y1 = y1 - y2
# finding the number of steps
step_num2 = a / step_len2
def decideAngle(turn,currentAngle):
    global currentDirection
    
    if turn=="L":
        currentAngle=currentAngle+90
        
        if currentDirection==4:
            currentDirection=1
        else:
            currentDirection=currentDirection+1
        
    elif turn=="R":
        currentAngle=currentAngle-90
        if currentDirection==1:
            currentDirection=4
        else:
            currentDirection=currentDirection-1
        
    return currentAngle,currentDirection

def UpdateBackground():
    """ Set the Dimension of the Screen"""
    Width = 483
    Height = 484
    
    """ Set the Screen"""
    
    screen = pygame.display.set_mode((Width,Height))
    
    """ Set The Title of Screen"""
    
    pygame.display.set_caption("Display Text")
    
    """ Load the Image"""
    screenImg = pygame.image.load("Images/MicroMouse Grid.jpg")
    
    """ Display Image at Specific Co-Ordinate"""
    
    screen.blit(screenImg,(0,0))
    
def Move(angle,cellX,cellY):
    UpdateBackground()
    
    
    """Load the Bot Image"""
    botImg= pygame.image.load("Images/Grid BOt.png")
    # screen.blit(botImg,(15,15))
    rotator.blitRotate(screen,botImg,(cellX,cellY),angle)

def getCoordinates(steps,cellX,cellY,currentDirection,currentAngle):
    
    if steps==0:
        if currentDirection==1:
            cellX=cellX+(steps*30)
        if currentDirection==2:
            cellY=cellY-(steps*30)
        if currentDirection==3:
            cellX=cellX-(steps*30)
        if currentDirection==4:
            cellY=cellY+(steps*30)
        Move(currentAngle,cellX,cellY)
              
    else:
        for i in range (steps):
            time.sleep(1)
            print("Taking Step ", i)
            if currentDirection==1:
                cellX=cellX+(30)
                Move(currentAngle,cellX,cellY)
            if currentDirection==2:
                cellY=cellY-(30)
                Move(currentAngle,cellX,cellY)
            if currentDirection==3:
                cellX=cellX-(30)
                Move(currentAngle,cellX,cellY)
            if currentDirection==4:
                cellY=cellY+(30)
                Move(currentAngle,cellX,cellY)
            pygame.display.update()
             
            
    return cellX,cellY
        
        

def parsePath(element,currentAngle):
    global state
    global steps
    global currentDirection
    global cellX
    global cellY
    
    
   #Check each element in the List
    if element =="L":
        
       currentAngle,currentDirection= decideAngle("L",currentAngle)
       steps=0
       cellX,cellY=getCoordinates(steps,cellX,cellY,currentDirection,currentAngle)
       state="NotReached"
       print("Taking Left Turn with angle ", currentAngle)
       
    elif element =="R":
       currentAngle,currentDirection= decideAngle("R",currentAngle)
       steps=0
       cellX,cellY=getCoordinates(steps,cellX,cellY,currentDirection,currentAngle)
       state="NotReached"
       print("Taking Right Turn with angle ", currentAngle)
      
    elif element=='x':
        state="Reached"
        
    else:
        steps=int(element)
        print("currentAngle ",currentAngle)
        cellX,cellY=getCoordinates(steps,cellX,cellY,currentDirection,currentAngle)
        
        state="NotReached" 
        

       
    return state,currentAngle    
            

while pathInput!='x':
    pathInput=input("Enter the Path Step "+ str(stepNum))
    stepNum+=1
    path.append(pathInput)


while state !="Reached" :
    # pygame.display.update()
    for element in path:
        pygame.display.update()
        state,currentAngle=parsePath(element,currentAngle)
        time.sleep(2)
# pygame.display.update()


done = False
count=0
distanceTravelled = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    

        time.sleep(0.01)

    else:

        pygame.display.update()

print("Reached")
pygame.quit()
