# This code determines the easter day
# Developer: Hosna Hamdieh
# Calculating the date of Easter Sunday

from datetime import date

def easter():
    year = int(input("What is the year you want to find the easter day in? "))
    "Returns Easter as a date object."
    a = year % 19
    b = year // 100
    c = year % 100
    d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
    e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
    f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
    month = f // 31
    day = f % 31 + 1
    return date(year, month, day)
def EasterDay():
    "Returns Easter day printed in the terminal."
    Month = ["Jan.","Feb.","Mar.","Apr.","May","Jun.","Jul.","Aug.","Sep.","Oct.","Nov.","Dec."]
    Easter_day = easter().strftime('%Y-%m-%d')
    ED = Easter_day.split("-")
    i = int(ED[1])-1
    ED[1]=Month[i]
    Easterday = f"The easter day for the year {ED[0]}: {ED[1]} {ED[2]}th"
    print(Easterday)
EasterDay()
# Sample result:
"""What is the year you want to find the easter day in? 2021
The easter day for the year 2021: Apr. 04th"""