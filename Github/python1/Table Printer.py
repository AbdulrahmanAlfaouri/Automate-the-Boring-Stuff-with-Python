def Table_Printer(table):
    w = []
    for i in range(len(table)):
        innerTable = table[i]
        for j in range(len(innerTable)):
            w.append(len(innerTable[j]))
            a = max(w)

    for i in range(len(table)):
        innerTable = table[i]
        print()
        for j in range(len(innerTable)):
            print(innerTable[j].rjust(a + 2), end='')
    return ''

