import re
import pyperclip


text = "if you were born in 08/05/2000 you will propably live till 06/04/3000 ,YOU HAVE TIME"
detector = re.compile(r'\d\d/\d\d/\d\d\d\d')

date = detector.findall(text)

for i in date:
    print('Date detected:',i)
    day = int(i[0:2])
    month = int(i[3:5])
    year = int(i[6:])
    if day > 31 or day < 1:
        print('Error ,days in a month cant be more than 31 days or les than 1')
    if month > 12 or month < 1:
        print("Error , there can't be more than 12 months a year or less than 1")
    if year > 3000 or year < 1000:
        print(f"Error, The year {year} is Out of range")







