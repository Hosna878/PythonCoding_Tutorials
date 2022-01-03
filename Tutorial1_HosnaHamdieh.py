# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 06:43:14 2021

@author: Hosna Hamdieh 
"""

############################# Tutorial1- Creating Simple Programs #######################

print("Hosna Hamdieh: Welcome to Tutorial 1 there are 6 functions in this program")
print("""The main function will run automatically
You can also uncomment last line of each function to run it seperatly
Have fun
""")

#######################################  Hosna Hamdieh  #################################

### 1. Hello Doctor
def Hello_Doctor():
    print("This function is going to print your name with your title ")
    Name=input("What is your name? ")
    Title=input("What is your title? (e.g. (Dr.) ")
    print ("Hello %s %s" %(Title,Name))
  
#Hello_Doctor()

############################### 2. xxxCoolxxxNamexxx   ##################################
def xxxCoolxxxNamexxx():
    print("This function will give you a cool username based on 3 random words you type")
    output=""
    for i in range(0,3):
      word=input("Type a word: ")
      output+="xxx"
      output+=word
    print("Your user edgy Myspace username is: "+output)

#xxxCoolxxxNamexxx():
    
#################################### 3. Adding  #########################################
def Adding():
    print("This function is going to add the numbers from 1 to the number you want ")
    Sum=0
    n=int(input("Wht is the number you are interested in? "))
    for i in range(1,n+1):
        Sum+=i
    print("The sum of the numbers from 1 to %d is:" %n, Sum)
#Note: uncomment the following line to activate the function#
#Adding()

################################# 4. Stadium Area  ######################################
def Stadium_Area():
    Pi=3.14
    print("This function is going to give you the area of a stadium having r and a")
    r=float(input("Enter the radius (r) of semicircle half in m: "))
    a=float(input("Enter the length of rectangle in m: "))
    A=Pi*r**2+2*r*a
    print("The area of a stadium is", A,"m**2")
#Note: uncomment the following line to activate the function#
#Stadium_Area()

########################### 5. : Weight Tables   ########################################
def Weight_Tables():
    print("This function will let you convert the weight of your table from kg to either lbs or ounces")
    def kg_to_lbs(Wkg):
        Wlbs=Wkg*2.20462262
        return Wlbs
    def kg_to_ounces(Wkg):
        Wounces=Wkg*35.2739619
        return Wounces
    Table_weight=float(input("Please enter the weight of your table in kg: "))
    Wlbs=kg_to_lbs(Table_weight)
    Wounces=kg_to_ounces(Table_weight)
    print("Weight in kg", "Weight in lbs", "Weight in ounces", sep=" - ")
    outcome="      %d      -       %d       -        %d     " %(Table_weight, Wlbs, Wounces)
    print(outcome)
#Note: uncomment the following line to activate the function#
#Weight_Tables()

############################ 6. The King’s Gambit  ######################################
def The_Kings_Gambit():
    print("This function will show the number of grain of rice on each chess square of the chess board and the sum of them all")
    All_grains=0
    grains=[]
    for i in range(0,64):
        grains=2**i
        print("%d grains on the square number %d " %(grains,i+1))
        All_grains+=grains
    print("There are %d grains on the chess board." %All_grains)
#Note: uncomment the following line to activate the function#   
#The_Kings_Gambit()

####################################  The main program-Tutorial1  ############################################

def main():
    print("Running this function will let you, call any function out of 6 buy calling its number.")
    
    print( """
Hello_Doctor=1
xxxCoolxxxNamexxx=2
Adding=3
Stadium_Area=4
Weight_Tables=5
The_Kings_Gambit=6
""")
    N=(input("Which function do you want to call:(1-6) "))

    if N=="":
        print("Your input is not valid.You did not choose anything")
    else:
        n = eval(N)
        if type(n) != int:
            print("Your input is not valid.You did not choose an integer number")
        else:
            print("Your input is valid")
            if n==1:
              Hello_Doctor()
            elif n==2:
              xxxCoolxxxNamexxx()
            elif n==3:
              Adding()
            elif n==4:
              Stadium_Area()
            elif n==5:
              Weight_Tables()
            elif n==6:
              The_Kings_Gambit()
    # else:
    #     print("The number is not valid please try again buy running the program again")
#Note: uncomment the following line to activate the function#  
main()

#################################  Finish  ######################################################