import pyperclip
import re

text = pyperclip.paste()

s = []

searchphone = re.compile(r'[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}',re.VERBOSE)
searchEmail = re.compile(r'09\d{8}')

phone = searchphone.findall(text)
Email = searchEmail.findall(text)

for j in Email:
    # print("Email addres found:",j)
    s.append(j)

for i in phone:
    # print("phone number found :",i)
    s.append(i)


emailsanPhones = '\n'.join(s)

pyperclip.copy(emailsanPhones)
print("Copied to Clipboard:\n"+emailsanPhones)




