#AutomaticMessages.py a multi clipboard program

Text = {'agree':"""Yes, I agree, that sounds fine to me.""",
        'busy':"""Sorry, can we do this later this week or next week?""",
        'upsell':"""Would you consider making this a monthly donation?"""}


import sys
import pyperclip


if len(sys.argv) < 2:
    print('Usage:python AutomaticMessage.py[keyphraze]- copy phrase text')
    sys.exit()

keyphrase = sys.argv[1] #first command line arg is the keyphrase

if keyphrase in Text:
    pyperclip.copy(Text[keyphrase])
    print('Text for ',keyphrase,'copied to clipboard.')
else:
    print('there is no text for',keyphrase)


