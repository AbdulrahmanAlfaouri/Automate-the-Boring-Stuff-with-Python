def CommaAndSpace(spam):
    for i in range(0,len(spam)):
        if i == len(spam)-1:
            print('and',spam[len(spam)-1])
        else:
            print(spam[i], end=', ')


shit = ['apples', 'bananas', 'tofu', 'cats','dogs','some random shit']

CommaAndSpace(shit)
