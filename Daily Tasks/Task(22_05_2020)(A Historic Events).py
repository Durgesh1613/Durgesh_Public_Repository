#Importing Library
import time


#Creating the Lists
#Creating the Jumbled Of the Challenge List
Event_List = [
                ['1.The Dandi March'],
                ['2.The First Year Of India Became Republic '],
                ['3.The Quit India Movement'],
                ['4.The Jallianwala Bagh Massacre'],
                ['5.The India Got Independence Form Britishers']
                ]

#Creating the User List. When the user gives Input all at things store in this list
User_List = [0,0,0,0,0]
        
#Creating the List for  the correct sequence to compare with the User List
Correct_Sequence_List = [4,1,3,5,2]

#Creating the List For Creating the list for Showing The Solved Challenge
Years_Names_List = ["4. 1919 = The Jallianwala Bagh Massacre",
              "1. 1930 = The Dandi March",
              "3. 1942 = The Quit India Movement",
              "5. 1947 = The India Got Independence From Britishers ",
              "2. 1950 = The First Year Of India Became Republic "]

#Adding Some Veriables
score = 0
print(" ")
print("Intilizing")
time.sleep(5)
print(" ")
print("The Open Challenge!")
print(" ")

#Taking Conformation From The User

print("Please answer in the type of Y/N")

Confomation = input("Are You Ready For the Challenge:")



#If user say Yes 
if Confomation == 'Y': 
    print(" ")
    print("This challenge is made for cheking your brain power and how much you know about the history.")
    print(" ")
    print("All the Things are the based on the histroy of 1919 to 1950")
    print(" ")
    print("Clue:Time of the India's Independence")
    
    #Again the Conformation from the user
    
    print("Please answer in the type of Y/N")
    
    Conformation2 = input("Are You Ready For the Challenge?Are you sure you want to Continue:")
    
    #If user say Yes in the second conformation 
    if Conformation2 == "Y":
        print("Processing The Game....")
        
        time.sleep(2)
        
        #Printing the Jumbled Maze      
        for i in Event_List:        
            print(i)
            
        print(" ")
        print("Please enter the Sr.no of the Historic Event As the Entered in the upside.")         
        for y in range(5):
            
            #Asking the user for the input 
            User_List[y]=int(input("Please Enter Event " + str(y+1)+" : "))
            if User_List[y]==Correct_Sequence_List[y]:
                score=score+10
        #Calculating and printing the score    
        if score<=20:
            print(" ")
            print("You need Almonds Man!!")
            print("------------------------------------------------------------")
            
        elif score<=40:
            print(" ")
            print("You need to improve")
            print("------------------------------------------------------------")
        else:
            print(" ")
            print("You have sharp Memory!!")
            print("------------------------------------------------------------")
        
        print(" ")   
        print("Your Score is: " + str(score), "out of 50") 
        print("----------------------------------------------------------------")
        
        #Showing the Solved Challenge
        print(" ")
        print("Correct Order Of the Events Held From 1919 To 1950 are the following")
        print(" ")
        print("This is the correct Sequence")
        print("----------------------------------------------------------------")
        
        for a in Years_Names_List:
            print(a)
        print("----------------------------------------------------------------")    
            
            
#If the user input's No or any other thing the this is the output in second conformation        
    else:
        print("Have A Nice Day!")        
#If the user input's No or any other thing the this is the output in first conformation
else:
    print("Have A Nice Day!")
