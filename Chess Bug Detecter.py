u = 0
c = 0
j = 0
h = ''
BoardTiles = []
shitIn = []
bking = '8c'
bqueen = '8e'
wqueen = '1e'
wking = '1c'
kingsCount = 0
aaa =()


ChessBoard = {'wknight':('1g','1b'),'wbishop':('1f','1c'),'wrook':('1h','1a'),'wqueen':'1d','wking':'1e','wpawn':('2a','2b','2c','2d','2e','2f','2g','2h'),\
             'bknight':('8g','8b'),'bbishop':('8f','8c'),'brook':('8h','8a'),'bqueen':"8e",'bking':"7e",'bpawn':('7a','7b','7c','7d','7e','7f','7g','7h')}


for charecter in range(ord('a'), ord('h') + 1):
    for number in range(9):
        BoardTiles.append((str(number) +chr(charecter)))

print(BoardTiles)

shitIn =ChessBoard.keys()

for w in shitIn:
    print(ChessBoard[w])
    if ChessBoard[w] in BoardTiles:
        print('good ')
    else:
        print('bad')



for i,s in ChessBoard.items():
    for n in s:
        c += 1
    for q in i:
        if q == 'wking'or q == 'bking':
            kingsCount += 1
            if kingsCount == 2:
                print('ther is 2 king"s and that is good')
            if kingsCount > 2:
                print("error , ther is more than 2 kings ")

            #  or q == 'wqueen ' or q == 'bqueen':


for w in ChessBoard['wpawn']:
    j += 1

for t in ChessBoard['bpawn']:
    u += 1

if c > 32:
    print(c)
    print('error there must not be more that 32 pieces on the board')
else:
    print('All clear')


if (j or u) > 8:
    print('error you cant have more that 8 pawns')
else:
    print('All clear')
