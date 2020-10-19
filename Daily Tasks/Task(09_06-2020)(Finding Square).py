#importing Libraries
import time

#Assining The Variables
done = 0

#Some Information and Greeetings
print(" ")

print("In this Program We Would find the square of any NUmber")

print(" ")

print("Square Finder")

print(" ")

print("Welcome")

print(" ")

#inserting the loop for continuos Run
while done == 0:
    UserInput = int(input("Enter The Number Of The Square You Want To Know:"))
    
    #Finding the Square
    
    Sq = UserInput*UserInput
        
    print(" ")
    print("Processing")
    print(" ")
    time.sleep(3)
    print ("The Square of",UserInput,"is",Sq)
        
        
    More = input("DO YOU WANT TO TRY FOR MORE  ?:")
        
    if More =="Yes" or More =="yes":
        done = 0
    else:
        done = 1
        print("HAVE A NICE DAY")        
        
    