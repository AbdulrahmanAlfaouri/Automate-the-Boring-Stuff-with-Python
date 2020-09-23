import  random
import sys
numberOfWins = 0
numberOfLoss = 0
numberOfTies = 0
attack = ''
attacklist = ['rock','paper','scissors']
a = False
while True:
    a = False
    attack = attacklist[random.randint(0,2)]
    print('ROCK ,PAPER, SCISSORES ')
    print(str(numberOfLoss) + ' LOSS')
    print(str(numberOfTies) + ' Ties')
    print(str(numberOfWins) +  ' WINS')
    print('"Enter you move,rock .. paper .. scissores .. or Q to quit"')
    print(attack)
    move = input(':')
    if move == 'quit':
        break
    while attack != move:
        if attack == 'paper' and move == 'scissores':
            numberOfWins += 1
            a = True
        elif attack == 'rock' and move == 'paper':
            numberOfWins += 1
            a = True
        elif attack == 'scissores' and move == 'rock':
            numberOfWins += 1
            a = True
        elif a == False:
            print('LOOOOSER HAHAAA!: ')
            numberOfLoss += 1
            break

        if a == True:
            print('you won!!')
            break

    else:
        print("it's a tie")
        numberOfTies += 1

