import pygame
import pygame.font
import time
import rotateImage as rotator

# Py Game Initialization
pygame.init()
size = (1121,545)
screen = pygame.display.set_mode(size) # Setting the Screen
clock = pygame.time.Clock()




# Display the Background Image

backImg = pygame.image.load("Images/Step Markings 2.png")

screen.blit(backImg,(0,0))

pygame.display.update()

#--------------------------------------------

#Display the Image of the Wheel at its position
image= pygame.image.load("Images/Final Left 2.png")
""" Display Image at Specific Co-Ordinate"""

screen.blit(image,(30,160))
w, h = image.get_size()
#----------------------------------------------
angle = 0
done = True

# Take user Input for StepAngle, Diameter & Distance
stepAngle= float(input("Enter the Step Angle: "))
diameter=int(input("Enter the Diameter: "))
distance=int(input("Enter the Distance to be covered: "))
#------------------------------------------------

#Calculations of Dist. in 1 Step and Total number of Steps
distIn1Step = ((3.14*diameter)*stepAngle)/360
print("Distance in One Step: "+str(distIn1Step))
steps = distance / distIn1Step

print("Steps: "+str(steps))
#------------------------------------------------

#Show the Quantities entered by the user on the display

#To Display Text: Wheel Diameter
font = pygame.font.SysFont('Times New Roman', 35)
text = font.render(str(diameter), False, (255, 255, 255))
image1 = pygame.Surface((text.get_width()+1, text.get_height()+1))
pygame.draw.rect(image1, (0, 0, 255), (1, 1, *text.get_size()))
screen.blit(text, (1070, 165))

#To Display Text: Step Angle
font = pygame.font.SysFont('Times New Roman', 35)
text = font.render(str(stepAngle), False, (255, 255, 255))
image1 = pygame.Surface((text.get_width()+1, text.get_height()+1))
pygame.draw.rect(image1, (0, 0, 255), (1, 1, *text.get_size()))
screen.blit(text, (1070, 230))

#To Display Text: Steps
font = pygame.font.SysFont('Times New Roman', 35)
text = font.render(str(round(distance,3)), False, (255, 255, 255))
image1 = pygame.Surface((text.get_width()+1, text.get_height()+1))
pygame.draw.rect(image1, (0, 0, 255), (1, 1, *text.get_size()))
screen.blit(text, (1070, 295))
#------------------------------------------------------------

#Display Status as Travelling....

#To Display Text: "Travelling"
font = pygame.font.SysFont('Times New Roman', 45)
text = font.render("Travelling...", False, (0, 0, 255))
image1 = pygame.Surface((text.get_width()+1, text.get_height()+1))
pygame.draw.rect(image1, (0, 0, 255), (1, 1, *text.get_size()))
screen.blit(text, (850, 420))

#-------------------------------------------------------------

done = False
count=0

distanceTravelled=0

while not done:
    
   # To Exit 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                done = True
#------------------------------------------------------
                
    pos = (screen.get_width()//2, screen.get_height()//2)
    pos = (200, 200)

# Check whether stepsCount has reached the number of steps calculated
    if count<steps: # If not reached then Rotate the wheel by 1 step angle
        
        #To Display Text: StepCount
       
        font = pygame.font.SysFont('Times New Roman', 35)
       
        text = font.render(str(count+1), False, (255, 255, 255))
        
        # To Clear the previous number of Step Count
        screen.fill(pygame.Color(85,49,133), (1070,495,*text.get_size()))
        
        #To Display new number
        image1 = pygame.Surface((text.get_width()+1, text.get_height()+1))
        pygame.draw.rect(image1, (0, 0, 255), (1, 1, *text.get_size()))
        screen.blit(text, (1070, 495))
        time.sleep(0.3)
        
        #To Rotate Wheel
        rotator.blitRotate(screen, image, pos, (w//2,h//2), angle)
        
        #Update StepAngle , StepCount and Distance Travelled
        angle -= stepAngle
        count+=1
        
        distanceTravelled= distanceTravelled + round(distIn1Step,3)
        
        distanceTravelled=round(distanceTravelled,3)
        
        #To Show Text: Distance Travelled
        font = pygame.font.SysFont('Times New Roman', 35)
        text = font.render(str(distanceTravelled), False, (255, 255, 255))
         
        # To Clear the previous distance travelled value
        screen.fill(pygame.Color(85,49,133), (1070,560,*text.get_size()))
        
        image1 = pygame.Surface((text.get_width()+1, text.get_height()+1))
        pygame.draw.rect(image1, (0, 0, 255), (1, 1, *text.get_size()))
        screen.blit(text, (1070, 560))
        pygame.display.flip()
        pygame.display.update()
        time.sleep(0.01)

    else:
        #To Display status as Reached
        
          # To Clear the previous status
        font = pygame.font.SysFont('Times New Roman', 45)
        text = font.render("Travelling", False, (255, 0, 0))
        
      
        screen.fill(pygame.Color(204,204,204), (850,420,*text.get_size()))
        
        #Show the new status as Reached
        text = font.render("Reached", False, (255, 0, 0))
        image1 = pygame.Surface((text.get_width()+1, text.get_height()+1))
        pygame.draw.rect(image1, (0, 0, 255), (1, 1, *text.get_size()))
        screen.blit(text, (850, 420))
        pygame.display.update()
        time.sleep(1)
        
    

    # pygame.draw.line(screen, (0, 255, 0), (pos[0]-20, pos[1]), (pos[0]+20, pos[1]), 3)
    # pygame.draw.line(screen, (0, 255, 0), (pos[0], pos[1]-20), (pos[0], pos[1]+20), 3)
    # pygame.draw.circle(screen, (0, 255, 0), pos, 7, 0)

        

pygame.quit()