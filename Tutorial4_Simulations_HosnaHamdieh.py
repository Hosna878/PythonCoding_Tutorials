# Tutorial 4: Simulations
# Due: Tuesday, March 23 @ 11:55 PM
# Hosna Hamdieh
#    A4: This assignment had 5 questions pluse an extra and in order to run each uncomment the function at the end of each
############################ 1. Blood Pressure #########################
# High blood pressure can require immediate medical attention. Write a program that allows a
# doctor to identify a patient's blood pressure category given the systolic and diastolic blood
# pressure.
class Doctor:
    def __init__(self,Systolic_Blood_Pressure,Diastolic_Blood_Pressure):
        self.Systolic_Blood_Pressure=Systolic_Blood_Pressure
        self.Diastolic_Blood_Pressure=Diastolic_Blood_Pressure

    def Blood_Pressure_Category(self):
        if self.Systolic_Blood_Pressure<120 and self.Diastolic_Blood_Pressure<80:
            self.Category="Normal"
        elif self.Systolic_Blood_Pressure<129 and self.Diastolic_Blood_Pressure<80:
            self.Category = "Elevated"
        elif self.Systolic_Blood_Pressure<139 or self.Diastolic_Blood_Pressure<89:
            self.Category = "Hypertension Stage 1 "
        elif self.Systolic_Blood_Pressure<180 or self.Diastolic_Blood_Pressure<120:
            self.Category = "Hypertension Stage 2 "
        elif self.Systolic_Blood_Pressure>180 or self.Diastolic_Blood_Pressure>120:
            self.Category = "Hypertensive crisis "
        return self.Category

def Blood_Pressure():
    print("Welcome")
    Systolic_Blood_Pressure = int(input("What is your Systolic_Blood_Pressure? "))
    Diastolic_Blood_Pressure = int(input("What is your Diastolic_Blood_Pressure "))
    BP=Doctor(Systolic_Blood_Pressure,Diastolic_Blood_Pressure)
    BPC = BP.Blood_Pressure_Category()
    print(f"Based on the information you have shared your blood pressure category is {BPC}")

# Blood_Pressure()

############################################## 2. Yahtzee ##############################
# In the game of Yahtzee, players roll 5 dice, and score different points depending on the dice
# they roll. A player rolls a “Yahtzee” when all 5 of the dice have the same value. Develop a Monte
# Carlo simulation in Python to estimate the probability of rolling a Yahtzee.

#roll the dice
def roll():
    import random
    Values = []
    for i in range(0, 5):
        Value = random.randint(1,6)
        Values.append(Value)
    return Values

# Yahtzee win
def play():
    Values = roll()
    Game=""
    if Values[0]==Values[1]==Values[2]==Values[3]==Values[4]:
        Game = "win"
        print("You have won in Yahtzee")
    else:
        print("Maybe next time")
    return Game

# Monte Carlo simulation of Yahtzee
def Yahtzee():
    n=int(input("How many times do you want to run the simulation? "))
    win=0
    for i in range(n):
        Game = play()
        if Game == "win":
            win += 1
    probability_of_win = win/n
    print(f"Out of {n} times you have won {win} which means the probability of winning this game is {probability_of_win} which is not that high")

#Yahtzee() # needs n
# Some results
# Yahtzee() # for n=100 =>  Out of 100 times you have won 1 which means the probability of winning this game is 0.01 which is not that high
# Yahtzee() # for n=1000 =>  Out of 1000 times you have won 1 which means the probability of winning this game is 0.001 which is not that high
# Yahtzee() # for n=10000=> Out of 10000 times you have won 6 which means the probability of winning this game is 0.0006 which is not that high
# Yahtzee() # for n=100000 => Out of 100000 times you have won 75 which means the probability of winning this game is 0.00075 which is not that high
# Yahtzee() # for n=1000000 => Out of 1000000 times you have won 777 which means the probability of winning this game is 0.000777 which is not that high

###################################################### 3. Birthdays ####################
# The birthday problem concerns the probability that within a group of n randomly selected
# people, two people will have the same birthday. For example, in a group of 70 random people,
# there is a 99.9% chance that two people will share the same birthday.
# https://en.wikipedia.org/wiki/Birthday_problem
# Develop a Monte Carlo simulation in Python to estimate the probability that in our class of 30
# students, at least two students share a birthday.
def Duplicate_Birthdays(n):
    global yes
    from random import randint
    BD=[]
    d=0
    for i in range(n):
        bd=randint(1,365)
        if bd not in BD:
            BD.append(bd)
        else:
            d+=1
    if d!=0:
        yes += 1
    probability_of_duplicates = d/n
    print(f"Out of {n} people in the room same birthdays happened {d} times")
    return d

def Birthdays():
    m=int(input("How many times do you like to run the simulation: "))
    global yes
    yes=0
    n = int(input("How many people are in the class? "))
    D=0
    for i in range(m):
        d = Duplicate_Birthdays(n)
        D += d
    Pyes = yes/(m)
    # probability_of_duplicates=D/(m*n)
    print(f"The chances of at least two people having the same birthday in a room with {n} people after repeting the simulation {m} times is {Pyes} and in this run same birthdays happened {D} times")
# Birthdays_Simulation() # inputs needed n,m
# some results
# Birthdays_Simulation() # for n=30,m=10000 => The chances of at least two people having the same birthday in a room with 30 people after repeting the simulation 10000 times is 0.7059 and in this run same birthdays happened 11523 times
# Birthdays_Simulation() # for n=30,m=100000=> The chances of at least two people having the same birthday in a room with 30 people after repeting the simulation 100000 times is 0.70681 and in this run same birthdays happened 116114 times

###################################################################### 4. Craps ############################
# Craps is a dice game played at many casinos. A player rolls a pair of normal six-sided dice. If
# the initial roll is 2, 3, or 12, the player loses. If the roll is 7 or 11, the player wins. Any other initial
# roll causes the player to "roll for point." That is, the player keeps rolling the dice until either
# rolling a 7 or re-rolling the value of the initial roll. If the player re-rolls the initial value before
# rolling a 7, it's a win. Rolling a 7 first is a loss.
# Write a program to simulate multiple games of craps and estimate the probability that the player
# wins. For example, if the player wins 249 out of 500 games, then the estimated probability of
# winning is 249/500 = 0.498.
import random

rng = range
inp = input

def makeNSidedDie(n):
    _ri = random.randint
    return lambda: _ri(1,n)

class Craps_Play(object):
    def __init__(self):
        super(Craps_Play,self).__init__()
        self.die = makeNSidedDie(6)
        self.firstRes = (0, 0, self.lose, self.lose, 0, 0, 0, self.win, 0, 0, 0, self.win, self.lose)
        self.reset()

    def reset(self):
        self.wins   = 0
        self.losses = 0

    def win(self):
        self.wins += 1
        return True

    def lose(self):
        self.losses += 1
        return False

    def roll(self):
        return self.die() + self.die()

    def play(self):
        first = self.roll()
        res   = self.firstRes[first]
        if res:
            return res()
        else:
            while True:
                second = self.roll()
                if second == 7:
                    return self.lose()
                elif second == first:
                    return self.win()

    def times(self, n):
        wins = sum(self.play() for i in rng(n))
        return wins, n-wins

def craps():
    import random
    c = Craps_Play()
    m = 0
    while True:
        try:
            n = int(input("How many rounds of craps would you like to play? (0 to quit) "))
            m += n

            print("Won {0}, lost {1}".format(*(c.times(n))))
            print("Based on the outcome the game probability of wining is {1} after {0} rounds""".format(n, (c.wins)/n))

        except:
            print("You have chosen to finish the game")
            break
    print("""In Total number of wins are {0}, and losses are {1}
The probability of wining in total after playing the game {2} times is {3}""".format(c.wins, c.losses, m, (c.wins)/m))

#craps()

# Result
"""How many rounds of craps would you like to play? (0 to quit) 10
Won 5, lost 5
Based on the outcome the game probability of wining is 0.5 after 10 rounds
How many rounds of craps would you like to play? (0 to quit) 100
Won 43, lost 57
Based on the outcome the game probability of wining is 0.48 after 100 rounds
How many rounds of craps would you like to play? (0 to quit) 1000
Won 505, lost 495
Based on the outcome the game probability of wining is 0.553 after 1000 rounds
How many rounds of craps would you like to play? (0 to quit) 
You have chosen to finish the game
In Total number of wins are 553, and losses are 557
The probability of wining in total after playing the game 1110 times is 0.4981981981981982"""

########################################################## 5. Gaming ######################
# In a computer-based trading card game, players use in-game currency to draw cards. The
# probability of drawing each card type is as follows:
# Common: 94.3%
# Rare: 5.1%
# Legendary: 0.6%
# However, because the rates for rare and legendary cards are so low, the game also includes the
# following rules:
# 1. If a Rare card is not drawn after 9 attempts, a Rare card is guaranteed on the 10th
# attempt.
# 2. If a Legendary card is not drawn after 75 attempts, the probability of drawing a
# Legendary card on subsequent attempts increases to 30%.
# 3. If a Legendary card is not drawn after 89 attempts, a Legendary card is guaranteed on
# the 90th attempt.
# Develop a Monte Carlo simulation to estimate the effective probabilities of drawing Rare and
# Legendary cards.
import random
def drawCard(pc,pr,pl):
    r = random.random()
    if r < (pc/100):
        card = 'Common'
    elif r < (pc+pr)/100:
        card = "Rare"
    elif r >= (1-pl)/100:
        card = "Legendary"
    return card

def Gaming():
# testing
    A = int(input("""Which one would you like: 1. Testing with the probabilities avaiable in the program or test it with the numbers you want?
Answer (1 or 2): """))
    if A == 1:
        pc, pr, pl = 94.3, 5.1, 0.6
    elif A == 2:
        pc = int(input("What is the probability of getting a common card? pc= "))
        pr = int(input("What is the probability of getting a rare card? pr= "))
        pl = int(input("What is the probability of getting a legendary card? pl= "))
    else:
        print("Your input is not valid")
    cards = []
    rare = 0
    legendary = 0
    common = 0
    i = 1
    P = (input("How many times do you want to simulate the card function: "))
    try:
        play = int(P)
        for i in range(play):
            # If a Legendary card is not drawn after 89 attempts, a Legendary card is guaranteed on the 90th attempt.
            if "Legendary" not in cards[-89:]:
                card = "Legendary"
            # If a Rare card is not drawn after 9 attempts, a Rare card is guaranteed on the 10th attempt.
            elif "Rare" not in cards[-9:]:
                card = "Rare"
            # If a Legendary card is not drawn after 75 attempts, the probability of drawing a Legendary card on subsequent attempts increases to 30%.
            elif "Legendary" not in cards[-75:]:
                pcn = pc - (30 - pl)
                pln = 30
                card = drawCard(pcn, pr, pln)
            else:
                card = drawCard(pc, pr, pl)
            cards.append(card)
            if card == 'Common':
                common += 1
            elif card == "Rare":
                rare += 1
            else:
                legendary += 1
            # play = input(
            #     f"""You have randomly selected {i} cards up to now enter if you do not want to continue otherwise type more """)
            i += 1
        # Probabilities after doing the simulation
        print(f"""You have randomly selected {i} cards and the list of cards is {cards}
The total number of common cards is {common}, rare cards is {rare}, and you got {legendary} legendary cards
Based on the simulation the probabilities are:
The probability of getting a common card is {common/play}, 
The probability of getting a rare card is {rare/play}, 
The probability of getting a legendary card is {legendary/play}
We can see that new roles have increased the probability of getting rare cards and legendary cards a bit""")
    except:
        print("Your input is not valid")
#Gaming() # the number of sumilation is needed there is also a chance of changing the probabilities
"""outcome after trying the simulation for n=1000 is:
You have randomly selected 1000 cards
The total number of common cards is 861, rare cards is 124, and you got 15 legendary cards
Based on the simulation the probabilities are:
The probability of getting a common card is 0.861, 
The probability of getting a rare card is 0.124, 
The probability of getting a legendary card is 0.015
We can see that new roles have increased the probability of getting rare cards and legendary cards a bit"""
"""outcome after trying the simulation for n=100 is:
The total number of common cards is 84, rare cards is 13, and you got 3 legendary cards
Based on the simulation the probabilities are:
The probability of getting a common card is 0.84, 
The probability of getting a rare card is 0.13, 
The probability of getting a legendary card is 0.03
We can see that new roles have increased the probability of getting rare cards and legendary cards a bit"""

########################################## Bonus ####################################
"""An E. coli bacterium is swimming in a porous circular bag with a radius of 1 mm. Every second,
the bacterium randomly changes the direction that it is swimming in. If the bacterium starts in
the centre of the bag, and swims at a rate of 0.06 mm per second, how long, on average, will it
take the bacterium to escape the bag? """
"""To make things visible the scales were change and multiplied by 50 that is why the speed was changed from 0.06 to 3 and similarly to make things go faster the time step was changed from 1 second to 0.001 but each step is counted and the time is calculated based on each movement happening in one second.
One problem was that the bag size had to be converted and it was not obvious at first. 
"""

from math import *
import graphics
from random import *
import time
def Brownian_Motion():
    win = graphics.GraphWin("Brownian", 500, 500)
    p0 = graphics.Point(250, 250)
    # converting the bage size based on the fact that each pixel is 26 mm in each side
    # making dimentions bigger to be visiable so all sizes are multiplied by 50
    bag = graphics.Circle(p0, 5000/(26*(2**0.5)))
    bag.setFill("lightsteelblue")
    bag.draw(win)
    particle = graphics.Circle(p0, 10)
    particle.setFill("yellow")
    particle.draw(win)
    i = 1
    x = [500]
    y = [500]
    while win.checkMouse() == None:
        # making the simulations faster by 1000 times
        time.sleep(0.001)
        p = particle.getCenter()
        angle = random() * 2 * pi
        x.append(x[i-1] + cos(angle))
        y.append(y[i-1] + sin(angle))
        #line = graphics.Line(p, p0).draw(win)
        d = (((((x[i] - x[0])/50) ** 2) + (((y[i] - y[0])/50) ** 2)) ** 0.5)
        if d <= 1:
            particle.move(sin(angle) * 0.06*50, cos(angle) * 0.06*50)
            pn = particle.getCenter()
            line = graphics.Line(p, pn).draw(win)
            print(f"the new point is located in x={x[i]} and y={y[i]} and is {d} far from the start point")
            # since each step should have been 1 second we can assume that the number of times we repeat it would be the time taken in seconds
            i += 1
        else:
            print(f"It took {i} seconds for the Brownian to reach the bag's border and go out of it")
            break
    win.getMouse()
    win.close()
    return i
def Bonous():
    n = int(input("How many times do you want to simulate this function: "))
    Ttime = 0
    Times = []
    for i in range(n):
        t = Brownian_Motion()
        Times.append(t)
        Ttime += t
    ta = Ttime/n
    print(f"""After repeating the process {n} times the average time of scape is {ta}
List of scape times is: {Times}""")
Bonous() # number of symulation is needed
""" 
It took 6925 seconds for the Brownian to reach the bag's border and go out of it
It took 2121 seconds for the Brownian to reach the bag's border and go out of it
It took 5222 seconds for the Brownian to reach the bag's border and go out of it
It took 3062 seconds for the Brownian to reach the bag's border and go out of it
It took 1106 seconds for the Brownian to reach the bag's border and go out of it
After repeating the process 5 times the average time of scape is 3687.2"""

"""After repeating the process 10 times the average time of scape is 1907.0
List of scape times is: [4283, 2568, 1651, 504, 2335, 1537, 1099, 2957, 1565, 571]"""

############################################## The End ##################################
