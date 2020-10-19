import time

done = 0

print(" ")
print("IN THIS PROGRAM WE WOULD SE SOME INFORMATION ABOUT THE STATES IN THE SOUTH OF THE INDIA")
print(" ")

time.sleep(2)
print("STATES ARE AS THE FOLLOWING:")
time.sleep(2)
print(" ")
print("1.KERALA")
time.sleep(2)
print(" ")
print("2.ANDRA PRADESH")
time.sleep(2)
print(" ")
print("3.KARNATAKA")
time.sleep(2)
print(" ")
print("4.TAMIL NADU")
time.sleep(2)
print(" ")
print("5.TELANGANA")


print("------------------------------------------------------------------------")

while done == 0:
    State_Input = input("ENTER THE NAME OF THE STATE YOU WANT TO KNOW:")
    
    if State_Input == "Kerala":
        print(" ")
        print("SOME SOCIAL INFORMATIOM:Kerala, a state on India's tropical Malabar Coast, has nearly 600km of Arabian Sea shoreline. It's known for its palm-lined beaches and backwaters, a network of canals. Inland are the Western Ghats, mountains whose slopes support tea, coffee and spice plantations as well as wildlife. National parks like Eravikulam and Periyar, plus Wayanad and other sanctuaries, are home to elephants, langur monkeys and tigers.")
    
        print(" ")
        print("CAPITAL:Thiruvananthapuram")
       
        print(" ")
        print("LANGUAGE SPOKEN:Malayalam")
      
        print(" ")
        print("MOSTLY CROP GROWN:The main crops grown in the state are paddy, coconut, pepper, cashew, cassava, and plantation crops like rubber. Kerala is an Agrarian economy.")
     
        
    if State_Input == "Andhra Pradesh":
        print(" ")
        print("SOME SOCIAL INFORMATION:Andhra Pradesh, formerly known as Andhra State, is a state in the south-eastern coastal region of India. It is the seventh largest state by area covering an area of 162,975 km² and tenth-most populous state, with 49,386,799 inhabitants. It has the second-longest coastline after Gujarat of about 974 km")   
    
        print(" ")
        print("CAPITAL:Hyderabad")
    
        print(" ")
        print("LANGUAGE SPOKEN:Telugu,Urdu")
        
        print(" ")
        print("MOSTLY CROP GROWN:Agriculture is the main occupation of about 62 per cent of the people in Andhra Pradesh. Rice is a major food crop and staple food of the State contributing about 77 per cent of the food grain production. Other important crops are jowar, bajra, maize, ragi, small millets, pulses, castor, tobacco, cotton and sugarcane.")
        
    
    if State_Input == "Karnataka":
        print(" ")
        print("SOME SOCIAL INFORMATION:Karnataka is a state in southwest India with Arabian Sea coastlines. The capital, Bengaluru (formerly Bangalore), is a high-tech hub known for its shopping and nightlife. To the southwest, Mysore is home to lavish temples including Mysore Palace, former seat of the region’s maharajas. Hampi, once the medieval Vijayanagara empire’s capital, contains ruins of Hindu temples, elephant stables and a stone chariot.")
        
        print(" ")
        print("CAPITAL:Banglore")
        
        print(" ")
        print("LANGUAGE SPOKEN:Kannad")
        
        print(" ")
        print("MOSTLY CROP GROWN:The main crops grown are Rice, Ragi, Jowar (sorghum), maize, and pulses (Tur and gram) in addition to oilseeds and a number of other cash crops. Cashews, coconut, arecanut, cardamom, chillies, cotton, sugarcane and tobacco are also produced.")
    
    if State_Input == "Tamil Nadu":
        print(" ")
        print("SOME SOCIAL INFORMATION:Tamil Nadu, a South Indian state, is famed for its Dravidian-style Hindu temples. In Madurai, Meenakshi Amman Temple has high ‘gopuram’ towers ornamented with colourful figures. On Pamban Island, Ramanathaswamy Temple is a pilgrimage site. The town of Kanyakumari, at India’s southernmost tip, is the site of ritual sunrises. Capital Chennai is known for beaches and landmarks including 1644 colonial Fort St. George.")
        
        print(" ")
        print("CAPITAL:Chennai")
        
        print(" ")
        print("LANGUAGE SPOKEN:Tamil")
        
        print(" ")
        print("MOSTLY CROP GROWN:The major crops sown in Tamilnadu are rice, jowar, ragi, bajra, maize, and pulses. Few other crops that are highly cultivated in the regions of Tamilnadu are cotton, sugarcane, tea, coffee, and coconut.")
    
    if State_Input == "Telangana":
    
        print(" ")
        print("SOME SOCIAL INFORMATION:Telangana is a state in southern India. In the capital of Hyderabad, the Charminar is a 16th-century mosque with 4 arches supporting 4 towering minarets. The monument overlooks the city's long-running Laad Bazaar. Once the seat of the Qutb Shahi dynasty, the sprawling Golconda Fort is a former diamond-trading center. In the city of Warangal, the centuries-old Warangal Fort features carved stone towers and gateways.")
        
        print(" ")
        print("CAPITAL:Hyderabad")
        
        print(" ")
        print("LANGUAGE SPOKEN:Telugu,Urdu")
        
        print(" ")
        print("MOSTLY CROP GROEN:Crops that are grown in Telangana are Rice, Maize/ Corn, Red Gram, Green Gram, Jowar, Sesame, Castor, Cotton, Groundnut, Soyabean , Black Gram to mention a few.")
    
    
    More = input("DO YOU WANT TO TRY FOR MORE  ?:")
    
    if More =="Yes" or More =="yes":
        done = 0
    else:
        done = 1
        print("HAVE A NICE DAY")
        