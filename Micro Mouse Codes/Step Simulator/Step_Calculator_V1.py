


print (" ")
print ("Give me The values")

distance = int(input("Enter the Distance:"))
step_angle = int(input("Enter the Step Angle:"))
diameter_of_whell = int(input("Enter the Diameter of the Wheel:"))

radius = diameter_of_whell / 2
py = 22/7
circumference = 2 * py * radius
rev_step = 360 / step_angle
div_distance = distance / circumference
total_steps = div_distance * rev_step
    
print(" ")
print("Total number of steps required to cover given distance = " +str(total_steps))