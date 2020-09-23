def Collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

while True:
    try:
        num = int(input('Enter a number :'))

        while True:
                 num = Collatz(num)
                 if num == 1:
                    print(num)
                    break
                 else:
                    print(num)

    except ValueError:
        print('please Enter a number')
        continue
