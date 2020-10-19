import time

time.sleep(1)

done=0


print(" ")
print("IN THIS PROGRAM WE WOULD REVERSE THE NUMBER")
print(" ")
print("NOTE : ONLY 4-DIGIT NUMBER")
print(" ")
print("NOTE : THERE'S A 0 AT THOUSANDS PLACE THEN IN THHE REVERSING IT WOULD BE AT THE ONCE PLACE")



while done == 0:
    Conformation = input("DO YOU WANT TO START:")
    if Conformation == "Yes" or Conformation == "yes":
            
        
        TH = int(input("ENTER THE NUMBER OF THOUSANDS PLACE:"))
                
        H = int(input("ENTER THE HUNDREDS PLACE NUMBER:"))
                
        T = int(input("ENTER THE TENS PLACE NUMBER:"))
                
        O = int(input("ENTER THE ONES PLACE NUMBER:"))
                
        print(" ")
                
        print("FOLLOWING IS THE NUMBER YOU ENTERED:",(TH),(H),(T),(O))
                
                
        print(" ")
                
        print("FOLLOWING IN THE REVERSE OF THE NUMBER:",(O),(T),(H),(TH))
    
    More = input("DO YOU WANT TO TRY FOR MORE DIGITS ?:")
    
    if More =="Yes" or More =="yes":
        done = 0
    else:
        done = 1

        print("HAVE A NICE DAY")
            
    
            
     