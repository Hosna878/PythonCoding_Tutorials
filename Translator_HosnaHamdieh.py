
from tkinter import *
from translate import Translator

Screen = Tk()
Screen.title("Language Translator with GUI")

InputLanguageChoice = StringVar()
TranslateLanguageChoice = StringVar()
LanguageChoices = {'Persian','English','French','German','Spanish',"Italian"}
InputLanguageChoice.set('French')
TranslateLanguageChoice.set('English')

def Translate():
    translator = Translator(from_lang= InputLanguageChoice.get(),to_lang=TranslateLanguageChoice.get())
    Translation = translator.translate(TextVar.get())
    OutputVar.set(Translation)


# choice for input language
InputLanguageChoiceMenu = OptionMenu(Screen, InputLanguageChoice, *LanguageChoices)
Label(Screen, text="Choose a Language").grid(row=0, column=0)
InputLanguageChoiceMenu.grid(row=1, column=0)

# choice in which the language is to be translated
NewLanguageChoiceMenu = OptionMenu(Screen, TranslateLanguageChoice, *LanguageChoices)
Label(Screen, text="Translated Language").grid(row=0, column=3)
NewLanguageChoiceMenu.grid(row=1, column=3)

Label(Screen, text="Enter Text",).grid(row=2, column=0)
TextVar = StringVar()
TextBox1 = Entry(Screen, textvariable=TextVar).grid(row=3, column=0)

Label(Screen, text="Output Text").grid(row=2, column=3)
OutputVar = StringVar()
TextBox2 = Entry(Screen, textvariable=OutputVar).grid(row=3, column=3)

# Button for calling function
B = Button(Screen, text="Translate", command=Translate, relief=GROOVE).grid(row=1, column=1, columnspan=1)

mainloop()
