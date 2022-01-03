######################### Tutorial 2: Numbers and Graphics #######################################################

########################### Created by Hosna Hamdieh #############################################################
#Q1:
import math
#Q2 & Q3
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
#Q4 & Q5 & Q6
from graphics import *
from colordict import *
##########################  1. Nernst Equation ###################################################################
##################################################################################################################
# The Nernst Equation is a famous equation in chemistry that finds the reduction potential (E) of a
# chemical reaction.
# Constants : R = universal gas constant (8.3145 J/mol/K) F = Faraday constant (96485.33 C/mol)
# Variables (inputs) : E0= standard potential for the reaction, T = temperature in Kelvin, z = ion charge, Q = reaction quotient
'''a) Write a program that allows a user to find the reduction potential of any chemical reaction. 
The output should be rounded to two decimal places. (/5)
b) Use your program to find the reduction potential (E) for a chemical reaction with the following properties: 
standard potential = 1.25 V, temperature = 273 K, ion charge = 2, Q = 0.077. (/2)'''
############  Reduction potential function: Calculates the E having R and F and asking for four other variables  ####################

def Reduction_Potential(E0,T,z,Q):
    R = 8.3145
    F = 96485.33
    E=E0-(R*T)/(z*F)*math.log1p(Q)
    return E

###########################   Nernst Equation's main code  ##########################################################################

# There are two ways to use the function first asking for each variable from the user
# or giving the fixed test variables from the question

def Nernst_Equation():
    A=int(input("""Which one do you like to try: (enter either 1 or 2)
    1. Testing with the variables you like
    2. Testing the function with the variables provided in the program
    (standard potential = 1.25 V, temperature = 273 K, ion charge = 2, Q = 0.077)

    Answer: """))

########################     First way: Asking the user to give us the variables:   ###################################

    if A==1:
        E0=float(input("What is the standard potential? "))
        T=float(input("What is the temperature in Kelvin? "))
        z=float(input("What is the ion change? "))
        Q=float(input("What is the reaction quotient? "))

#######################    Second way: Testing the function using fixed variables     #################################

    elif A==2:
        E0=1.25
        T=273
        z=2
        Q=0.077
    else:
        print("The number you have entered is not valid try again, choosing 1 or 2")

##########################  Calling the function having the variables #################################

    E=Reduction_Potential(E0,T,z,Q)

##############################  Using round function to show only two decimal places  #################

    E=(round(E,2))
    print("""The reduction potential (E) for a chemical reaction with the following properties: 
    standard potential = %f V, temperature = %f K, ion charge = %f, Q = %f is""" %(E0, T, z, Q), E)

#################################  To Call the Nernst_Equation function uncomment the next line ###################################

#Nernst_Equation()

###################################################################################################################################
################################  2. Pendulum Swing  ##############################################################################

# The period (time it takes a pendulum to swing back and forth) of a pendulum (T) given its length
# (l) is provided
# Constant: g = acceleration due to gravity (9.8 m/s^2)
# Variable:l= length of the pendulum string (m)
'''Create a plot of the pendulum period vs. length for pendulums with string lengths of 10 cm to 2 m.'''

def Pendulum_Swing():
    A=int(input("""Which one do you like to try: (Put either 1 or 2)
    1. Testing with the variables you like
    2. Testing the function with the variables provided in the program
    (length for pendulums with string lengths of 10 cm to 2 m)

    Answer: """))

    if A == 1:
        lMax = float(input("What the Maximum length of the pendulum string (cm): "))
        lMin = float(input("What the Minimum length of the pendulum string (cm): "))
    elif A == 2:
        lMax = 200
        lMin = 10
    else:
        print("The number you have entered is not valid try again, choosing 1 or 2")
    l = np.arange(lMin/100,lMax/100,0.001)
    g = 9.8
    T = 2*np.pi*(l/g)**0.5
    fig, ax= plt.subplots()
    ax.plot(l,T)
    ax.set(xlabel="Length for pendulums", ylabel="The pendulum period", title="The pendulum period vs. length for pendulums with string lengths in the range")
    ax.grid()
    fig.savefig("Pendulum_Swing.png")
    plt.show()

#################################  To Call the Pendulum_Swing function uncomment the next line ###################################

#Pendulum_Swing()

###################################################################################################################################
#################################### 3. : Supply and Demand #######################################################################

# In economics, there are two relationships between the quantity of a product, and the price.
# Demand:
# As the price (P) of an item increases, the quantity people are willing to buy (Qd) decreases. Qd=20-2*P
# Supply:
# As the price (P) of an item increases, the quantity that suppliers will want to supply (Qs)increases. Qs=-10+2*P
"""a) Plot the supply and demand curves on the same graph for prices of $0 to $20.
Remember to label the axes of the graph. 
b) In economic theory, the economy will sit at the equilibrium of the two curves (the point
where the two curves intersect). What is the equilibrium price?"""

def Supply_and_Demand():
    A = int(input("""Which one do you like to try: (Put either 1 or 2)
        1. Testing with the variables you like
        2. Testing the function with the variables provided in the program
        (prices of $0 to $20)

        Answer: """))

    if A == 1:
        PMax = float(input("What the Maximum price (P) of the item in $: "))
        PMin = float(input("What the Minimum price (P) of the item in $: "))
    elif A == 2:
        PMax = 20
        PMin = 0
    else:
        print("The number you have entered is not valid try again, choosing 1 or 2")
    P = np.arange(PMin, PMax, 0.001)
    Qd = 20 - 2 * P
    Qs = -10 + 2 * P

########################## The equilibrium price happens when Qd=Qs #########################

    E=30/4
    print("The equilibrium price is %f $" %E)
    fig, axs = plt.subplots(2, 1)

    axs[0].plot(P,Qd,P, Qs)
    axs[0].set(xlabel="Price of the item ($)", ylabel="Supply and Demand",
           title="Supply and Demand in a price range for an item")
    axs[0].grid(True)
    axs[0].annotate('E(7.5, 6)', (7.5, 6),
                xytext=(0.5, 0.25), textcoords='axes fraction',
                arrowprops=dict(facecolor='black', shrink=0.05),
                fontsize=10, horizontalalignment='right', verticalalignment='top')
    axs[0].legend(["Qd","Qs"])
    cxy, f = axs[1].cohere(Qd, Qs, 256, 1. / 0.001)
    axs[1].set_ylabel('coherence')

    fig.tight_layout()
    plt.show()
    fig.savefig("Supply_and_Demand.png")

#################################  To Call the Supply_and_Demand function uncomment the next line ###################################

#Supply_and_Demand()

#####################################################################################################################################
################################## 4: Iceland  ######################################################################################

def Iceland():
    win=GraphWin("Iceland",250,200)
    #win.getMouse()
    win.setBackground("green")
    message = Text(Point(win.getWidth()/2, 10), 'Click anywhere to start.')
    message.draw(win)
    win.getMouse()
    message.undraw()
    Blue=Rectangle(Point(0,20),Point(250,200))
    Blue.setFill(color_rgb(2, 85, 156))
    Blue.setOutline(color_rgb(2, 85, 156))
    #win.getMouse()
    Blue.draw(win)
    white1=Rectangle(Point(0,90),Point(250,130))
    white1.setFill(color_rgb(255, 255, 255))
    white1.setOutline(color_rgb(255, 255, 255))
    #win.getMouse()
    white1.draw(win)
    white2=Rectangle(Point(70,20),Point(110,200))
    white2.setFill(color_rgb(255, 255, 255))
    white2.setOutline(color_rgb(255, 255, 255))
    #win.getMouse()
    white2.draw(win)
    Red1=Rectangle(Point(0,100),Point(250,120))
    Red1.setFill(color_rgb(220, 30, 53))
    Red1.setOutline(color_rgb(220, 30, 53))
    #win.getMouse()
    Red1.draw(win)
    Red2=Rectangle(Point(80,20),Point(100,200))
    Red2.setFill(color_rgb(220, 30, 53))
    Red2.setOutline(color_rgb(220, 30, 53))
    #win.getMouse()
    Red2.draw(win)
    # findPixel = win.getPixel(250, 200)
    # print(findPixel)

    message = Text(Point(win.getWidth()/2, 10), 'Click anywhere to quit.')
    message.draw(win)
    # It would be cool if I could add sth to save the win
    win.getMouse()
    win.close()

#################################  To Call the Iceland function uncomment the next line ###################################

#Iceland()

#####################################################################################################################################
#################################  5.  Pentagon  ####################################################################################

'''Write a program that allows a user to create a pentagon of their choice by clicking on 5 points on the graphics window.'''

def Pentagon():
    win=GraphWin("Your Pentagon", 1000,1000)
    # win.getMouse()
    win.setBackground("blue")
    message = Text(Point(win.getWidth() / 2, 10), """Click 5 times anywhere on the screen to form the pentagon.""")
    message.draw(win)
    p=[]
    for i in range(0,5):
        P=win.getMouse()
        Po=Point(P.getX(),P.getY())
        MP=Text(P,"(%f,%f)"%(P.getX(),P.getY()))
        MP.draw(win).setSize(10)
        Po.draw(win)
        p.append(P)
        print("You clicked at:",p[i].getX(),p[i].getY())
    message.undraw()
    message=Text(Point(win.getWidth() / 2, 10), """Your points are ready click once more to see your pentagon.""")
    message.draw(win)
    win.getMouse()
    message.undraw()
    Pentagon=Polygon(p)
    Pentagon.draw(win)
    Pentagon.setFill("red")
    Pentagon.setOutline("red")
    message = Text(Point(win.getWidth() / 2, 10), 'Click anywhere to quit.')
    message.draw(win)
    # It would be cool if I could add sth to save the win
    win.getMouse()
    win.close()

#################################  To Call the Pentagon function uncomment the next line ###################################

#Pentagon()

############################################################################################################################
################################# 6.  Polygon Colour #######################################################################

"""Write a program that prompts a user for their favourite colour. Then have the program draw the following polygon on the graphics window filled with the user’s favourite colour."""

def Color_RGB():
    Rc = int(input("How much red do you want in your color? "))
    Gc = int(input("How much green do you want in your color? "))
    Bc = int(input("How much blue do you want in your color? "))
    Name = color_rgb(Rc, Gc, Bc)
    return Name

def Polygon_Colour():
    win = GraphWin("Color with your favorite color", 450, 400)
    A = int(input("""Choose the way you want to color: put 1 or 2
    1. giving a color name (note some colors might not exist in the system)
    2. Giving the color using RGB (the amount of red, green and blue existing in the color you want
    Answer: """))
    if A == 1:
        bc = input("What is the color you would like for the background (Do not choose black!) ").lower()
        pc = input("What is the color you would like for the polygon ").lower()
        poc = input("What is the color you would like for the outline of the polygon ").lower()
    elif A == 2:
        print("Give RGB for the color you want for the background (Do not choose black!): ")
        bc = Color_RGB()
        print("Give RGB for the color you want for the polygon (separate the numbers using comma): ")
        pc = Color_RGB()
        print("Give RGB for the color you want for the outline of the polygon (separate the numbers using comma): ")
        poc = Color_RGB()
    else:
        print("The number you have entered is not valid try again, choosing 1 or 2")
    # win.getMouse()

    message = Text(Point(win.getWidth() / 2, 10), """Click anywhere on the screen to see the polygon.""")
    message.draw(win)
    win.getMouse()
    p1=Point(150,150)
    p2=Point(200,200)
    p3=Point(150,250)
    p4=Point(250,250)
    p5=Point(300,200)
    p6=Point(250,150)
    poly=Polygon(p1,p2,p3,p4,p5,p6)
    poly.draw(win)
    message.undraw()
    message = Text(Point(win.getWidth() / 2, 10), """Click anywhere on the screen to see everything colored.""")
    message.draw(win)
    win.getMouse()
    win.setBackground(bc)
    poly.setFill(pc)
    poly.setOutline(poc)
    message.undraw()
    message = Text(Point(win.getWidth() / 2, 10), 'Click anywhere to quit.')
    message.draw(win)
    # It would be cool if I could add sth to save the win
    win.getMouse()
    win.close()

#################################  To Call the Pentagon function uncomment the next line ###################################

#Polygon_Colour()

############################################################################################################################
###################################### Numbers and Graphics ################################################################

def Numbers_and_Graphics():
    A=int(input("""Welcome dear user
     Please determine which of the function you are interested in by selecting the number associated with it
     1. Nernst Equation 
     2. Pendulum Swing 
     3. Supply and Demand
     4. Iceland 
     5. Pentagon 
     6. Polygon Colour
     Answer: """))
    if A == 1:
        Nernst_Equation()
    elif A == 2:
        Pendulum_Swing()
    elif A == 3:
        Supply_and_Demand()
    elif A == 4:
        Iceland()
    elif A == 5:
        Pentagon()
    elif A == 6:
        Polygon_Colour()
    else:
        print("""The number you have typed is not defined in the system "
              try again using a number between 1 to 6""")
    final_text="""
    It was nice seeing you take care"""
    print(final_text)
Numbers_and_Graphics()

########################################### Finished ##########################################################################