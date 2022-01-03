# Tutorial 5: Classes and Algorithms
# Due: Friday, April 9 @ 11:55 PM
# Hosna Hamdieh
# A5: This assignment had 5 questions and in order to run each uncomment the function at the end of each

############################################# 1: TV Shows #######################
def TVS():
    """a) Create a class to represent a TV show that you’d like to recommend to your friends and
    family. Your class should implement the following methods:
    __init__(self, title, genre, rating, noEpisodes, noSeasons, … etc...) Creates a TV show with
    relevant information such as title, genre, number of episodes, your “star rating”, and any other
    data you want to include.
    __str__(self) Returns a string that names the tv show and the genre, for example: "Friends,
    Comedy"
    b) Test your class by creating a TV show object based on your favourite TV show."""
    class TV_Shows:
        def __init__(self, title, genre, rating, noEpisodes, noSeasons, summary, cast):
            self.title = title
            self.genre = genre
            self.rating = rating
            self.noEpisodes = noEpisodes
            self.noSeasons = noSeasons
            self.summary = summary
            self.cast = cast
        def __str__(self):
            output=f"""The name of the TV_Show is,{self.title}, and it belongs to {self.genre}'s genre.
Its rating is {self.rating} it has {self.noEpisodes}, in the total of {self.noSeasons} seasons."""
            print(output)
    TVS1 = TV_Shows("She-Ra: Princess of Power","Fantasy TV shows","7.8/10 IMDb","54", "5", """She-Ra and the Princesses of Power is set on the planet Etheria and follows the stories of Adora and Catra, orphans who were raised to be soldiers in the Horde.
One day, after getting lost in the woods, Adora finds a magic sword that transforms her into the legendary Princess of Power, She-Ra""",{"Adora":"Aimee Carrero","Bow":"Marcus Scribner","Glimmer":"Karen Fukuhara","Catra":"AJ Michalka"})
    print(TVS1.genre)
    print("-----------------------") # Outcome=> Fantasy TV shows
    TVS1.__str__()
    print("-----------------------") # Outcome=> The name of the TV_Show is,She-Ra: Princess of Power, and it belongs to Fantasy TV shows's genre. Its rating is 7.8/10 IMDb it has 54, in the total of 5 seasons.
    print(TVS1.cast["Adora"])
    print("-----------------------") # Outcome=> Aimee Carrero
    print(TVS1.summary)
    print("-----------------------") # Outcome=> She-Ra and the Princesses of Power is set on the planet Etheria and follows the stories of Adora and Catra, orphans who were raised to be soldiers in the Horde. One day, after getting lost in the woods, Adora finds a magic sword that transforms her into the legendary Princess of Power, She-Ra
    TVS2 = TV_Shows("Locke & Key", "Supernatural horror","7.4/10 IMDb", "10","1","""After Rendell Locke is murdered at the hands of former student Sam Lesser, his wife Nina decides to move with her three children, Tyler, Kinsey, and Bode, from Seattle to Matheson, Massachusetts, and take residence in Rendell's family home, Keyhouse. 
The children soon discover a number of mysterious keys throughout the house that can be used to unlock various doors in magical ways. 
They soon become aware, though, of a demonic entity that is also searching for the keys for its own malevolent purposes.""",{"Nina Locke":"Darby Stanchfield ","Tyler Locke":"Connor Jessup","Kinsey Locke":"Emilia Jones","Bode Locke":"Jackson Robert Scott"})
    print(TVS2.genre)
    print("-----------------------")
    TVS2.__str__()
    print("-----------------------")
    print(TVS2.cast["Tyler Locke"])
    print("-----------------------")
    print(TVS2.summary)
    print("-----------------------")
################################################## To run uncomment the line below #########################
#TVS()
"""Test results:
Fantasy TV shows
-----------------------
The name of the TV_Show is,She-Ra: Princess of Power, and it belongs to Fantasy TV shows's genre.
Its rating is 7.8/10 IMDb it has 54, in the total of 5 seasons.
-----------------------
Aimee Carrero
-----------------------
She-Ra and the Princesses of Power is set on the planet Etheria and follows the stories of Adora and Catra, orphans who were raised to be soldiers in the Horde.
One day, after getting lost in the woods, Adora finds a magic sword that transforms her into the legendary Princess of Power, She-Ra
-----------------------
Supernatural horror
-----------------------
The name of the TV_Show is,Locke & Key, and it belongs to Supernatural horror's genre.
Its rating is 7.4/10 IMDb it has 10, in the total of 1 seasons.
-----------------------
Connor Jessup
-----------------------
After Rendell Locke is murdered at the hands of former student Sam Lesser, his wife Nina decides to move with her three children, Tyler, Kinsey, and Bode, from Seattle to Matheson, Massachusetts, and take residence in Rendell's family home, Keyhouse. 
The children soon discover a number of mysterious keys throughout the house that can be used to unlock various doors in magical ways. 
They soon become aware, though, of a demonic entity that is also searching for the keys for its own malevolent purposes.
-----------------------"""
############################################# 2: Scrabble 2 #######################
def Scrabble():
    """In class we created a program to calculate the value of scrabble letters, however we did not use
    the actual scrabble tile values. Update the scrabble program with the correct values for the
    letters. Please solve this problem using the Python dictionary data structure.
    https://wordfinder.yourdictionary.com/blog/scrabble-letter-values-list/
    """
    scrabbleSum = 0
    letter = input("Enter a scrabble letter: ").lower()
    SLV={"a":1,"b":3,"c":3,"d":2,"e":1,"f":4,"g":2,"h":4,"i":1,"j":8,"k":5,"l":1,"m":3,"n":1,"o":1,"p":3,"q":10,"r":1,"s":1,"t":1,"u":1,"v":4,"w":4,"x":8,"y":4,"z":10,"":0}
    i=0
    SL={}
    while letter != "":  # while the user doesn't just press the enter key
        scrabbleSum += SLV[letter]  # math part
        i+=1
        SL[letter]=SLV[letter]
        letter = input("Enter a scrabble letter: ").lower()
    print(f"""You have entered {i} letters in total and your score is {scrabbleSum}
Letters played with their values: {SL}""")
################################################## To run uncomment the line below #########################
#Scrabble()
"""Test results:
Enter a scrabble letter: a
Enter a scrabble letter: d
Enter a scrabble letter: w
Enter a scrabble letter: x
Enter a scrabble letter: b
Enter a scrabble letter: 
You have entered 5 letters in total and your score is 18
Letters played with their values: {'a': 1, 'd': 2, 'w': 4, 'x': 8, 'b': 3}"""
############################################# 3: Decorators and Docstrings #######################
"""Decorators and Docstrings(/10)
a) Create a function called hexConvert that converts an integer into its hexadecimal
representation.
Example: hexConvert(15) = “F”
hexConvert(100) = 64
b) Provide a docstring to explain the function.
c) Create a decorator called info that provides information about a function by printing the
function’s docstring. Test the function by using it with the hexConvert function from part
a)."""
def decorator():
    import time
    def info(func):
        def wrapper(*args, **kwargs):
            print("Info:")
            print(func.__doc__)
            value = func(*args, **kwargs)
            return value
        return wrapper
    def timer(func):
        def wrapper(*args, **kwargs):
            tic = time.perf_counter()
            value = func(*args, **kwargs)
            toc = time.perf_counter()
            elapsed_time = toc - tic
            print(f"Elapsed time: {elapsed_time:0.4f} seconds")
            return value
        return wrapper

    @timer
    @info
    def hexConvert(X):
        "This function will convert an integer into its hexadecimal representation."
        Y="{0:x}".format(X)
        return Y
    x=int(input("Please type in an integer to convert into hexadecimal: "))
    print(hexConvert(x))
    # print(hexConvert(10))
    #print(hexConvert.__doc__)
################################################## To run uncomment the line below #########################
#decorator()
"""Test results:
Please type in an integer to convert into hexadecimal: 15 
This function will convert an integer into its hexadecimal representation.
Elapsed time: 0.0001 seconds
f 
----------------------------------------------------------------------
Please type in an integer to convert into hexadecimal: 12
Info:
This function will convert an integer into its hexadecimal representation.
Elapsed time: 0.0001 seconds
c
----------------------------------------------------------------------
Please type in an integer to convert into hexadecimal: 8695484737979
Info:
This function will convert an integer into its hexadecimal representation.
Elapsed time: 0.0001 seconds
7e8934769bb
"""
############################################# 4: Card Player #######################
"""a) During the lectures we created classes for a PlayingCard and for a Deck. A next step
could be to create a class to represent a Player in the card game. The Player class
should have variables for a player name, and a representation of their card hand.
Create a Player class that includes the following methods:
__init__(self, name): Creates a card game Player with a name, and assigns the player
an empty card hand.
drawCard(self, deck): Draws a card from the top of a card deck object.
playCard(self, card): Removes the specified card from the player’s hand.
getHand(self): Returns the cards in the player’s hand.
sortHand(self): Sorts the player’s hand based on rank and then based on suit.
b) Demonstrate that your code works by creating a Player object and testing each method.
"""
import random

class PlayingCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def value(self):
        if self.rank > 9:
            return 10
        else:
            return self.rank

    def convertRank(self):
        if self.rank < 12:
            hexRank = '{0:x}'.format(self.rank)
        else:
            hexRank = '{0:x}'.format(self.rank + 1)
        return hexRank

    def convertSuit(self):
        suitDictHex = {"h": "b", "d": "c", "c": "d", "s": "a"}
        return suitDictHex[self.suit]

    def __str__(self):
        hexValue = "1f0" + self.convertSuit() + self.convertRank()
        decValue = int(hexValue, 16)
        return chr(decValue)

class Deck:
    def __init__(self):
        # make a list of 52 playing cards
        self.cardDeck = []
        for r in range(1, 14):  # ranks
            for s in 'c', 'd', 'h', 's':  # suits
                self.cardDeck.append(PlayingCard(r, s))

    def shuffle(self):
        random.shuffle(self.cardDeck)

    def dealCard(self):
        card = self.cardDeck.pop(0)
        return card

    def cardsLeft(self):
        return len(self.cardDeck)

    def printDeck(self):
        # need to print out every card in the list
        for card in self.cardDeck:
            print(card, end=" ")

    def sortbySuit(self):
        self.cardDeck.sort(key=PlayingCard.getSuit)

    def sortbyRank(self):
        self.cardDeck.sort(key=PlayingCard.getRank)

class player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.hand = []
    def drawCard(self,deck):
        card = deck.dealCard()
        self.hand.append(card)
        return self
    def playCard(self, card):
        if card in self.hand:
            i = self.hand.index(card)
            card = self.hand.pop(i)
        else:
            print("You do not have this card in your hand so the first card in your hand will be played")
            card = self.hand.pop(0)
            print("The played card:")
            print(card)
        return card
    def getHand(self):
        # need to print out every card in the list
        for card in self.hand:
            print(card, end=" ")
    def sortHand(self):
        self.hand.sort(key=PlayingCard.getSuit)
        self.hand.sort(key=PlayingCard.getRank)
        return self.hand
def playing_Card():
    # Testing the features
    deck = Deck()
    deck.shuffle()
    # deck.sortbyRank()
    print("The deck: ")
    deck.printDeck()
    print()
    name = input("What is your name? ")
    player1 = player(name)
    print()
    print(f"Welcome '{player1.player_name}' you can start playing")
    noc = int(input("How many cards do you need to play? "))
    # # player1.drawCard(deck)
    print()
    # print(player1.getHand())
    for i in range(0,noc):
        player1.drawCard(deck)
    print("This is your hand")
    player1.getHand()
    print()
    player1.sortHand()
    print("This is your hand sorted")
    player1.getHand()
    print()
    print("If you want to play a card, type in the rank and the suit of your card")
    r=input("rank (1-13): ")
    s=input("suit (c, d, h, or s): ")
    player1.playCard(PlayingCard(r,s))
    # print()
    print("Your hand after playing the card")
    # PlayingCard.__str__(self)
    player1.getHand()
    print("You have tested this function by getting a hand, sorting it, and playing a card")
################################################## To run uncomment the line below #########################
#playing_Card()
"""Test result:
The deck: 
🂷 🃍 🂪 🃔 🂣 🃛 🃂 🃖 🃉 🃆 🃃 🃑 🂹 🂨 🂤 🂡 🂮 🃓 🂺 🂽 🃗 🃒 🃝 🃚 🃊 🂵 🂩 🂸 🃎 🂴 🃈 🂦 🂶 🃕 🂾 🂥 🂱 🃙 🃇 🂳 🃋 🃘 🃄 🃞 🂭 🂻 🂫 🃅 🂢 🂧 🂲 🃁 
What is your name? Honsa

Welcome 'Honsa' you can start playing
How many cards do you need to play? 5

This is your hand
🂷 🃍 🂪 🃔 🂣 
This is your hand sorted
🂣 🃔 🂷 🂪 🃍 
If you want to play a card, type in the rank and the suit of your card
rank (1-13): 1
suit (c, d, h, or s): h
You do not have this card in your hand so the first card in your hand will be played
The played card:
🂣
Your hand after playing the card
🃔 🂷 🂪 🃍 
You have tested this function by getting a hand, sorting it, and playing a card"""
############################################# 5: Spell Checker #######################
"""Automated spell-checkers are used to analyze documents and locate words that might be
misspelled. These programs work by comparing each word in the document to a large dictionary
(in the non-Python sense) of words. Any word not found in the dictionary is flagged as
potentially incorrect. Write a program to perform spell-checking on a text file. To do this, you will
need to get a large file of English words in alphabetical order. Your program should prompt for a
file to analyze and then try to look up every word in the file using a binary search. If a word is
not found in the dictionary, print it on the screen as potentially incorrect.
Example dictionary:
https://github.com/dwyl/english-words"""
import re
def remove_urls(TEXT):
    vTEXT0 = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%\@\#\;\!\$\,\:)*\b', '', TEXT, flags=re.MULTILINE)
    vTEXT = re.sub("[^a-zA-Z\s]", " ", vTEXT0)
    # print("Text no urls: ",vTEXT)
    return vTEXT

def load_words(filename):
    file = open(filename,"r")
    words = ((remove_urls(file.read().lower())).split())
    return words
def selectionSort(l):
    for n in range(0, len(l) - 1):
        # 1) find index of the smallest element in the list
        ind_min = n
        for i in range(n + 1, len(l)):
            if l[i] < l[ind_min]:
                ind_min = i
        # 2) swap the smallest element with the first element of the list
        l[n], l[ind_min] = l[ind_min], l[n]
    return l
def binarySearch(l,x):
    low = 0
    high = len(l)-1
    while low <= high:
        mid = (low+high)//2
        item = l[mid]
        if item == x:
            return mid
        elif item > x:
            high = mid-1
        else:
            low = mid+1
    return -1
################################################### Solution 1: #############################################
def misspelling(valid_words):
    words = (remove_urls(input("Type the text you want to check the spelling for: ")).lower()).split()
    misspell = 0
    i=0
    misspellings = {}
    for w in words:
        if w not in valid_words:
            print(f"Misspelling: {w}")
            misspell += 1
            misspellings[i] = w
            i += 1
    if misspell == 0:
            print("No Misspellings")
    else:
        print(f"There were {misspell} misspelled words and are listed along with their position in the text: {misspellings}")
################################################## To run uncomment the line below #########################
# misspelling(load_words('words.txt'))
"""Test results:
Type the text you want to check the spelling for: I am hapy to be herer
Misspelling: hapy
Misspelling: herer
There were 2 misspelled words and are listed along with their position in the text: {0: 'hapy', 1: 'herer'}"""
################################################### Solution 2: #############################################
from gingerit.gingerit import GingerIt
def spellcheck():
    text = input("Enter text to be corrected: ")
    result = GingerIt().parse(text)
    corrections = result['corrections']
    correctText = result['result']
    if text==correctText:
        print("The text dose not have a misspelling")
    else:
        print("Correct Text:", correctText)
        print()
        print("CORRECTIONS")
        n = len((corrections))
        print(f"The text has {n} misspelled words")
        for d in corrections:
            print("________________")
            print("Previous:", d['text'])
            print("Correction:", d['correct'])
            print("`Definiton`:", d['definition'])
################################################## To run uncomment the line below #########################
spellcheck()
"""Test result:
Enter text to be corrected: I am hapy to be here with u since it is my gool
Correct Text: I am happy to be here with you since it is my goal

CORRECTIONS
________________
Previous: gool
Correction: goal
`Definiton`: the state of affairs that a plan is intended to achieve and that (when achieved) terminates behavior intended to achieve it
________________
Previous: u
Correction: you
`Definiton`: second person pronoun; the person addressed
________________
Previous: hapy
Correction: happy
`Definiton`: enjoying or showing or marked by joy or pleasure
"""
################################################### Solution 3: #############################################
def SpellChecker():
    # valid_words = load_words('words_alpha.txt')
    # The list is not sorted so we must sort it first using 'sorted()' function
    valid_words = sorted(load_words('words.txt'))
    print(type(valid_words))
    A = int(input("""Do you want to process a text file or you just want to type in a sentence or two? 
type either 1 or 2 (1. Typing sentences, 2. Entering a text file)
Answer= """))
    if A == 1:
        words = (remove_urls(input("Type the text you want to check the spelling for: ")).lower()).split()
        print(words)
    else:
        filename = input("""Please type in the name of your text file to be validated based on spelling: 
""")
        words = load_words(filename)
        print(words)

    misspell = 0
    i = 0
    misspellings = {}
    for w in words:
        outcome = binarySearch(valid_words, w)
        if outcome == -1:
            print(f"The word '{w}' dose not exist in the dictionary of words so it might be misspelled")
            misspell += 1
            misspellings[i] = w
        i += 1
    if misspell == 0:
        print("No spelling mistakes found based on the dictionary")
    else:
        print(f"There were {misspell} misspellings and here is the words that are wrong along with their position (index) in the text {misspellings}")
################################################## To run uncomment the line below #########################
#SpellChecker()
"""Test result:
Do you want to process a text file or you just want to type in a sentence or two? 
type either 1 or 2 (1. Typing sentences, 2. Entering a text file)
Answer= 1
Type the text you want to check the spelling for: What a greete day it is, and I am hapy to be with you
['what', 'a', 'greete', 'day', 'it', 'is', 'and', 'i', 'am', 'hapy', 'to', 'be', 'with', 'you']
The word 'greete' dose not exist in the dictionary of words so it might be misspelled
The word 'hapy' dose not exist in the dictionary of words so it might be misspelled
There were 2 misspellings and here is the words that are wrong along with their position (index) in the text {2: 'greete', 9: 'hapy'}"""