  
import pygame
import time
import rotateImage as rotator
import pygame.font

pygame.init()

size = (1062,603)
screen = pygame.display.set_mode(size)

background = pygame.image.load("Images/Background.png")

screen.blit(background,(0,0))

pygame.display.set_caption("Step Simulator")

pygame.display.update()

image1 = pygame.image.load("Images/Stepper Motor Symbol.png")
image1 = pygame.transform.scale(image1,(210,210))


image2 = pygame.image.load("Images/Stepper Motor Symbol 2.png")
image2 = pygame.transform.scale(image2,(210,210))


done = True



stepAngle = stepAngle = float(input("Enter the Step Angle: "))
diameter=float(input("Enter the Diameter: "))
distance=int(input("Enter the Distance to be covered: "))



angle = stepAngle

distIn1Step = ((3.14*diameter)*stepAngle)/360
print("Distance in One Step: "+str(distIn1Step))
steps = distance / distIn1Step

print("Steps: "+str(steps))

#to display step angle for right wheel
font = pygame.font.SysFont("Comic Sans MS",40)
text1 = font.render(str(stepAngle),True,(255,255,255))
screen.blit(text1,(900,95))

#to display diameter for right wheel
text2 = font.render(str(diameter),True,(255,255,255))
screen.blit(text2,(925,175))

#to display step angle for left wheel
text3 = font.render(str(stepAngle),True,(255,255,255))
screen.blit(text3,(900,365))

#to display wheel diameter for left wheel
text4 = font.render(str(diameter),True,(255,255,255))
screen.blit(text4,(925,445))



done = False
count=0
distanceTravelled = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if count < steps:
        #To display steps
        font1 = pygame.font.SysFont('Bahnschrift', 42)
        text5 = font1.render(str(count + 1), False, (255, 255, 255), (	153, 0, 255))
        screen.blit(text5, (460, 160))

        text6 = font1.render(str(count+1),True,(255,255,255),(	153, 0, 255))
        screen.blit(text6,(460,406))

        time.sleep(0.3)
        #To rotate wheel
        rotator.blitRotate(screen,image1, (27, 10), angle)
        rotator.blitRotate(screen, image2, (27, 315), angle)

        angle -= stepAngle
        count += 1

        distanceTravelled = distanceTravelled + round(distIn1Step, 3)
        distanceTravelled = round(distanceTravelled, 3)

        # To Show Text: Distance Travelled
        font2 = pygame.font.SysFont('Comic Sans MS', 40)
        text7 = font2.render(str(distanceTravelled), False, (255, 255, 255),(	153, 0, 255))
        screen.blit(text7,(810,533))
        pygame.display.update()

        time.sleep(0.01)

    else:

        pygame.display.update()

print("Reached")
pygame.quit()
