message = input('Enter teh English massage to translate into TheYLatin Latin:')

VOWELS = ('a','e','i','o','u','y')


TheYLatin = []
for word in message.split():
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]

    if len(word) == 0:
        TheYLatin.append(prefixNonLetters)
        continue

    #Separate the non letters at the end of this word:

    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]

    # Remember if the word was in uppercase of title case.
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower() # Make the word lowercase for translation

    # Separate the consonants at the start of this word.
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    # Adding the theYLattin ending to the word:
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

    # Set the word back to uppercase or title case:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # Add the non-letters vack to the start of end of the word.

    TheYLatin.append(prefixNonLetters + word + suffixNonLetters)

#join all the words back together into a single string:

print(' '.join(TheYLatin))
