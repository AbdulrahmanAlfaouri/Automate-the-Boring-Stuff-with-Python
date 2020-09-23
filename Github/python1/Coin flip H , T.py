import random

HorT = ''
ListOFHorT = []
N1 = 0
N2 = 0
numberOfStrickes = 0

for SampleNumber in range(100):
    Chance = random.randint(0,1)
    if Chance == 1:
        HorT = 'H'
        N1 += 1
        N2 = 0
    else:
        HorT = 'T'
        N2 += 1
        N1 = 0

    if N1 == 6 or N2 == 6:
        numberOfStrickes +=1

    ListOFHorT.append(HorT)

print(numberOfStrickes)
print(ListOFHorT)


