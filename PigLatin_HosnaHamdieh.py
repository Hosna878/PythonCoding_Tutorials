# creator: Hosna Hamdieh
############################################ PigLatin Translator ##############################

# The aim of this program is to convert english text into piglatin and to do so the text must be cleaned a bit
# since the punctuations will create noise in the words being attached to the end of the previous word
# Note: Looking at the piglatin version we can clearly undrestand the begining of the sentences as they have a capital letter inside them.
# The capital letters could have been easily changed to lower case letters but that way the begining of the sentences would not have been clear.

import re
########################################## Url remover function  ##############################

def remove_urls(TEXT):
    vTEXT0 = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%\@\#\;\!\$\,\:)*\b', '', TEXT, flags=re.MULTILINE)
    vTEXT = re.sub("[^a-zA-Z\s]", " ", vTEXT0)
    return (vTEXT)

################ This is a translator that converts English words to Pig Latin words ###########

# Pig Latin Translator for translating one English word to pig latin one

def pigLatinTranslate(english_word):
    pigLatin_word = english_word[1:]+english_word[0]+"ay"
    return pigLatin_word

############################################## Main program #####################################

###################################Reading the text file as an input ############################

print("""Welcom user
This program is a translator that changes english text into piglatin 
lets start""")
Answer=int(input("""Do you have a text in mine or do you just want to see how it works? 
(type 1 for the text file of your choice and 2 for testing the program with the book 'war and peace')
Answer= """))

if Answer==2:
    FName="War_and_Peace"
if Answer==1:
    FName=input("""What is the name of your text file? (Note: The text file must be in your active directory)
     File Name= """)

FileName=FName+".txt"
infile=open(FileName,"r")

##################################### Translating the input file line by line ###################

PigLatin_book = """ """
for line in infile:

############################Cleaning the text so that it would not have punctiuations ###########

    Clean_line=remove_urls(line)
    tokenized_line = Clean_line.split()
    PL_line = " "
    for word in tokenized_line:
        PL_word = pigLatinTranslate(word)
        print(PL_word, end=" ")
        PL_line += (" "+ PL_word)

    PigLatin_book += ("""
    """ + PL_line)

############################## Saving the translated book into a text file #######################

with open("%s_PigLatin.txt"%FName,"w") as text:
    text.write(PigLatin_book)

print("""

Your Book has been translated and stored under the name of %s_PigLatin.txt in your directory
Hint: To understand when the sentences are finished look for capital letters in the words
Thanks for trying PigLatin translator 
See you next time
Bests
Hosna Hamdieh""" %FName)

################################################ The end #########################################


