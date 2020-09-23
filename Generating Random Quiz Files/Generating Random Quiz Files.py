import random
import pyinputplus as pyip


def WriteDate_Name_Period2File():
    with open('Quistoins and choices.txt', 'a') as QandC:
        QandC.write('''
Date:
    
Name :
    
Period:
    
            State Capitals Quiz (Form 1)
    
    
            ''')
def WriteRandom_QuistionsNChoinces():
    capitals = {'Alabama': 'Montgomery',
                'Alaska': 'Juneau',
                'Arizona': 'Phoenix',
                'Arkansas': 'Little Rock',
                'California': 'Sacramento',
                'Colorado': 'Denver',
                'Connecticut': 'Hartford',
                'Delaware': 'Dover',
                'Florida': 'Tallahassee',
                'Georgia': 'Atlanta',
                'Hawaii': 'Honolulu',
                'Idaho': 'Boise',
                'Illinois': 'Springfield',
                'Indiana': 'Indianapolis',
                'Iowa': 'Des Moines',
                'Kansas': 'Topeka',
                'Kentucky': 'Frankfort',
                'Louisiana': 'Baton Rouge',
                'Maine': 'Augusta',
                'Maryland': 'Annapolis',
                'Massachusetts': 'Boston',
                'Michigan': 'Lansing',
                'Minnesota': 'Saint Paul',
                'Mississippi': 'Jackson',
                'Missouri': 'Jefferson City',
                'Montana': 'Helena',
                'Nebraska': 'Lincoln',
                'Nevada': 'Carson City',
                'New Hampshire': 'Concord',
                'New Jersey': 'Trenton',
                'NewMexico': 'Santa Fe',
                'New York': 'Albany',
                'North Carolina': 'Raleigh',
                'North Dakota': 'Bismarck',
                'Ohio': 'Columbus',
                'Oklahoma': 'Oklahoma City',
                'Oregon': 'Salem',
                'Pennsylvania': 'Harrisburg',
                'Rhode Island': 'Providence',
                'South Carolina': 'Columbia',
                'South Dakota': 'Pierre',
                'Tennessee': 'Nashville',
                'Texas': 'Austin',
                'Utah': 'Salt Lake City',
                'Vermont': 'Montpelier',
                'Virginia': 'Richmond',
                'Washington': 'Olympia',
                'WestVirginia': 'Charleston',
                'Wisconsin': 'Madison',
                'Wyoming': 'Cheyenne'}
    values = list(capitals.values())
    for i in range(1,50):
        # Values
        random.shuffle(values)

        # keys
        a = random.randint(0,len(capitals)-1)
        theCapital = list(capitals.keys())[a]
        theRightAnswer = capitals[theCapital]

        #NO duplication in the list
        choicesAndAnswers, possibleAnswers = Choices_And_Answers(theRightAnswer, values)

        Writing_Data_To_Files(capitals, choicesAndAnswers, i, possibleAnswers, theCapital, theRightAnswer)
def Choices_And_Answers(theRightAnswer, values):
    while True:
        possibleAnswers = [theRightAnswer,
                           values[random.randint(0, len(values) - 1)],
                           values[random.randint(0, len(values) - 1)],
                           values[random.randint(0, len(values) - 1)]]
        if len(possibleAnswers) == len(set(possibleAnswers)):
            break
    random.shuffle(possibleAnswers)
    choicesAndAnswers = {possibleAnswers[0]: 'A', possibleAnswers[1]: 'B', possibleAnswers[2]: 'C',
                         possibleAnswers[3]: 'D'}
    return choicesAndAnswers, possibleAnswers
def Writing_Data_To_Files(capitals, choicesAndAnswers, i, possibleAnswers, theCapital, theRightAnswer):
    with open('Quistoins and choices.txt', 'a') as QandC:
        QandC.write(f'''
{i}.What is the Capitale of {theCapital}
    A:{possibleAnswers[0]}
    B:{possibleAnswers[1]}
    C:{possibleAnswers[2]}
    D:{possibleAnswers[3]}
                \n''')
    with  open('capitalsquiz_answers.txt', 'a') as CapitalesQA:
        CapitalesQA.write(f'{i}. {choicesAndAnswers[theRightAnswer]}\n')
    print(i)
    capitals.pop(theCapital)


WriteRandom_QuistionsNChoinces()