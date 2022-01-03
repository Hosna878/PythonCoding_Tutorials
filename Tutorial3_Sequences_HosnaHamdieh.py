# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 22:43:13 2021

@author: Hosna Hamdieh 
"""

##################################### Tutorial 3: Sequences #####################################################
# This program includes 6 functions around sequences and it is automatically run asking the user to choose one of them by entering a number
# IT will continue while the user is entering a number and when they just press Enter it will stop
########################################  Q1:  Birth Trees  ########################################

def Birth_trees():
    print("""Do you want to know what your birth tree is?
          You are in the right place
          """)
    Month=input("""What is your month of birth?
Month of birth: """)
    BT={"January": "Apple",
"February": "Willow",
"March": "Maple",
"April": "Elm",
"May": "Fig",
"June": "Cherry",
"July": "Walnut",
"August": "Oak",
"September": "Palm",
"October": "Olive",
"November": "Citrus",
"December": "Spruce"}
    try:
        UBT = BT[Month]
        print("Your birth tree is {} since you have entered {} as your month of birth".format(UBT,Month))
        print()
    except:
        print("Your answer is not valid try again")
    
#Birth_trees()  

#######################################  Q2: Hello World  ###########################################

def Hello_World():
    print("Lets say hi to the world together")
    textFile=open("countries.txt","r")
    textRead=textFile.read()
    HWord=open("helloword.txt","a")
    text=textRead.split("\n")
    HW=[]
    for i in text:
        hc="Hello "+i
        HW.append(hc)
    HelloWord="""
    """.join(HW)
    print("""Hello word: 
""", HelloWord)
    print(HelloWord,file=HWord)
    textFile.close() 
    HWord.close()
#Hello_World()
 
#####################################  Q3:  Vocabulary  #############################################

def  Vocabulary():
    Answer = int(input("""Enter 1 or 2 for to calculate the average word lenght
1. The average lenght of english words 
2. The average word lenght in one text file
Answer: """))
    if Answer == 1:
        FileName = "English_Words.txt"
    elif Answer == 2:
        FileName = input("""What is the name of your text file? (FileName.txt)
FileName: """)
    else:
        print("Error: Your input is not valid, try again")
    WL = []
    WDL = {}
    textFile = open(FileName,"r")
    text = textFile.read()
    SWL = 0
    words = text.split()
    for word in words:
        wl = len(word)
        WL.append(wl)
        SWL += wl
        WDL[word] = wl
    AWL = SWL/len(words)
    print(f"The average word length is {AWL}")
    textFile.close()
#Vocabulary()

################################### Q4: Password Generator  #####################################
def Password():
    Answer = input('''Do you like to have only one password generated or more? (type 1 or more)
Answer: ''')
    if Answer == "1":
        Password_Generator()
    else:
        Password_save()

def Password_Generator():
    
    import string
    special_letters = string.punctuation
    #print(special_letters)
    letters = string.ascii_letters
    #print(letters)
    numbers = string.digits
    #print(numbers)
    from random import choice,randint
    characters = letters + special_letters  + numbers
    print("Your password will include different characters randomly picked")
    password = "".join(choice(characters) for x in range(randint(10, 16)))
    print ("Your password is: ",password)
    return password
#Password_Generator()

def Password_save():
    PassFile = open("passwords.txt","a")
    try:
        n = int(input("""How many passwords do you need? 
        n= """))
        Password_list = []
        for i in range(n):
            Pass = Password_Generator()
            Password_list.append(Pass)
        PassText=str(Password_list)
        print(PassText,file=PassFile)
        PassFile.close()
    except:
        print("Your answer is not valid try again")
    PassFile.close()
#Password_save()

##################################  Q5: Caesar Cipher #########################
# By running the decipher code testing all keys we can find the answer for part c of the question (Deciphering SIOBUPYWLUWEYXNBTWIXY):
# Decoded massage using 20 as the key is:  YOUHAVECRACKEDTHECODE
# or in another words YOU HAVE CRACKED THE CODE
# So even when we do not have the key we can simply test it with all keys and check to see which one makes sense
def Caesar_cipher(letter,n):
    pos = ord(letter)-65 #position for mod math
    e = (pos + n)%26
    #convert back to unicode value and get new character
    new_chr = chr(e+65)
    return new_chr
def Coding():
    Textin = input("Enter a message: ").upper()
    n = int(input("Enter a value for n: "))
    M = Textin.split()
    NM = []
    for word in M:
        NW = ""
        for ch in word:
          NW += Caesar_cipher(ch,n)
        NM.append(NW)
    new_massage = "".join(NM)
    print("The massage is coded into: ", new_massage)
    print()

def Decriptor_Ceasar_cipher(letter,n):
    pos = ord(letter)-65
    e = (pos - n)%26
    new_chr = chr(e+65)
    return new_chr
def DeCoding():
    Textin = input("Enter a message: ").upper()
    A=input("""Do you have the key to decode the text? (yes/no)
Answer= """).lower()
    if A == "yes":
        n = int(input("Enter a value for n: "))
        NM = Textin.split()
        NME=[]
        for word in NM:
            NWE = ""
            for ch in word:
                NWE += Decriptor_Ceasar_cipher(ch,n)
            NME.append(NWE)
        new_massageE =" ".join(NME)
        print("Lets see if we can change it back: ",new_massageE)
    elif A == "no":
        print("""Not having the key makes things a bit harder 
We can give you all possible choices using different keys
It is up to you to find the one that makes sense""")
        for n in range(1,26):
            NM = Textin.split()
            NME=[]
            for word in NM:
                NWE = ""
                for ch in word:
                    NWE += Decriptor_Ceasar_cipher(ch,n)
                NME.append(NWE)
            new_massageE =" ".join(NME)
            
            print("Decoded massage using {} as the key is: ".format(n),new_massageE)
def Coding_Decoding():
    Answer=input("""Do you want to code or decode a massage: (Type c for code and d for decode)
    Answer: """).lower()
    if Answer == "c":
        Coding()
    elif Answer == "d":
        DeCoding()
    else:
        print("Error: Your answer is not valid try again")
        
#Coding_Decoding()

################################################# Q6: Latin Keyboard ##########################################
from collections import Counter
import re
def Latin_Keyboard():
    infile = open("CeasarBook.txt","r")
    String = infile.read().lower()
    Words = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%\@\#\;\!\$\,\:)*\b', '', String, flags=re.MULTILINE)
    WordsC = re.sub("[^a-zA-Z\s]", " ", Words)
    # print(WordsC)
    listOfWords = WordsC.split()
    # print(listOfWords)
    LastLetter = [word[-1] for word in listOfWords]
    Common_LastLetters = Counter(LastLetter).most_common(80)
    print("""Common last letters in Latin:
    """,Common_LastLetters)
    text = String.replace(" ", "")
    # print(text)
    text = text.replace("\n","")
    Text = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%\@\#\;\!\$\,\:)*\b', '', text, flags=re.MULTILINE)
    TextC = re.sub("[^a-zA-Z\s]", " ", Text)
    AllLetters = [letter for letter in TextC]
    # alphabet = ["a","b","c",]
    Common_letters = Counter(AllLetters).most_common(80)
    print("""Common letters in Latin:
    """,Common_letters)
    Ceasar_keyboard = f""" I II III IV V VI VII VIII IX X XX - = <-
Tab  {Common_letters[19][0]}  {Common_letters[17][0]}  {Common_letters[11][0]}  {Common_letters[9][0]}  {Common_letters[8][0]}  {Common_letters[10][0]}  {Common_letters[16][0]}  {Common_letters[18][0]}  {Common_letters[20][0]}  {Common_letters[21][0]} [ ] slash 
CL   {Common_letters[15][0]}  {Common_letters[13][0]}  {Common_letters[7][0]}  {Common_letters[6][0]}  {Common_letters[5][0]}  {Common_letters[3][0]}  {Common_letters[4][0]}  {Common_letters[1][0]}  {Common_LastLetters[3][0]}  {Common_LastLetters[2][0]} ; ' Enter
Shift   {Common_letters[-1][0]}  {Common_letters[-2][0]}  {Common_letters[3][0]}  {Common_letters[3][0]}  {Common_letters[12][0]}  {Common_LastLetters[1][0]}  {Common_LastLetters[0][0]}  ,  .  /  Shift
Ctrl fn win Alt     space     Alt Car Ctr """
    print("""Ceasar Keyboard is designed based on having the most used letters in the middle row
having the most used last letters near the punctuation marks 
and less used letters far from reach:
""",Ceasar_keyboard)
    infile.close()
#Latin_Keyboard()

##################################### Tutorial 3: Sequences #####################################################
def Sequences():
    ListOfFunctions = [Birth_trees, Hello_World, Vocabulary, Password, Coding_Decoding, Latin_Keyboard]
    try:
        Answer = int(input("""Welcome to Sequences
We have 6 functions that you could test listed below. Chose the number related to the function so that you could test it
Have fun
Note: Please type one number at a time and press Enter if you want to quit
List of functions:
1= Birth_trees, 2= Hello_World, 3= Vocabulary, 4= Password, 5= Coding_Decoding, 6= Latin_Keyboard
Answer: """))
        while Answer != "":
            try:
                i = int(Answer) - 1
                Function = ListOfFunctions[i]
                Function()
                Answer = input("""Do you want to try another? type another number from 1 to 6 or Enter if you want to quit
Answer: """)
            except:
                print("Your answer is not valid try again")
    except:
        print("Your answer is not valid")

Sequences()
################################################ Finished #############################################

