import numpy as np

def Decimal_To_Binary_Conversion(value):
    Value1 = []
    Value0 = []
    number = [np.modf(value)[0], np.modf(value)[1]]


    fractunalNumberPart = number[0]
    realNumberPart = number[1]

    while realNumberPart // 2 != 0:
        if realNumberPart % 2 == 1:
            Value1.append('1')
            realNumberPart = realNumberPart // 2
        else:
            Value1.append('0')
            realNumberPart = realNumberPart // 2
    else:
        if realNumberPart == 1:
            Value1.append('1')
        else:
            Value1.append('0')

    while fractunalNumberPart != 0.0:
        fractunalNumberPart = fractunalNumberPart * 2
        if fractunalNumberPart == 1.00:
            Value0.append('1')
            break
        elif fractunalNumberPart < 1:
            Value0.append('0')
        else:
            fractunalNumberPart = np.modf(fractunalNumberPart)[0]
            Value0.append('1')

    Value1.reverse()
    convertedRealPart = ''.join(Value1)
    convertedFractunalPart = ''.join(Value0)

    print(f'{value} in decimial = {convertedRealPart}.{convertedFractunalPart} in Binery')

while True:
    try:
        value = float(input('please input a  Number in Dicimal to convert it to Binary :'))
        Decimal_To_Binary_Conversion(value)
    except ValueError:
        print('Please Enter a number')