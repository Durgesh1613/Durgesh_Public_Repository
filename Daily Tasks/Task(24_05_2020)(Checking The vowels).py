print(" ")
print("IN THIS PROGRAM WE WILL FIND THE VOWEL IN THE WORD")
print(" ")
print("YOU CAN ENTER MULTIPLE NAMES")
def Check_Vow(string, vowels): 
    final = [each for each in string if each in vowels] 
    print(len(final)) 
    print(final) 
      
# Driver Code 
NAME = input("WHAT IS YOUR NAME?PLEASE ENTER:")
vowels = "AaEeIiOoUu"
Check_Vow(NAME, vowels);
    