import re

phoneNumRegex = re.compile(r'09\d{8}')
text = "my phone num 0956959035, . 0932596773, . 09av598743 . 0932591234564, 0956956035, 0932596763 "
phoneNumbersFinder = phoneNumRegex.findall(text)

for i in phoneNumbersFinder:
    if len(i) == 10:
        print("Phone number found ",str(i))






