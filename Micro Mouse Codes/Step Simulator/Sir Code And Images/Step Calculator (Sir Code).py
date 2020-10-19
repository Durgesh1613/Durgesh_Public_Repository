import pygame
import pygame.font
import time
import rotateImage as rotator

pygame.init()
size = (1262,680)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()



font = pygame.font.SysFont('Times New Roman', 35)
text = font.render('Step ', False, (255, 255, 255))
image1 = pygame.Surface((text.get_width()+1, text.get_height()+1))
pygame.draw.rect(image1, (0, 0, 255), (1, 1, *text.get_size()))
screen.blit(text, (680, 100))



backImg = pygame.image.load("Images/Step Markings.png")

screen.blit(backImg,(0,0))

pygame.display.update()


image= pygame.image.load("Images/Stepper Motor Symbol.png")
""" Display Image at Specific Co-Ordinate"""

screen.blit(image,(140,140))
w, h = image.get_size()

angle = 0
done = True

stepAngle= float(input("Enter the Step Angle"))
diameter=int(input("Enter the Diameter"))
distance=int(input("Enter the Distance to be covered"))

distIn1Step = ((3.14*diameter)*stepAngle)/360
print("Distance in One Step: "+str(distIn1Step))
steps = distance / distIn1Step

print("Steps: "+str(steps))

done = False
count=0
while not done:
    
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                done = True

    pos = (screen.get_width()//2, screen.get_height()//2)
    pos = (200, 200)

    if count<steps:
    # screen.fill(0)
        rotator.blitRotate(screen, image, pos, (w//2,h//2), angle)
        angle -= stepAngle
        count+=1
        pygame.display.flip()
        pygame.display.update()
        time.sleep(1)
    

    # pygame.draw.line(screen, (0, 255, 0), (pos[0]-20, pos[1]), (pos[0]+20, pos[1]), 3)
    # pygame.draw.line(screen, (0, 255, 0), (pos[0], pos[1]-20), (pos[0], pos[1]+20), 3)
    # pygame.draw.circle(screen, (0, 255, 0), pos, 7, 0)

        

pygame.quit()