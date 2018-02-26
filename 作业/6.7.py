
tableData = [['apples','oranges','cherries','banana'],
             ['Alice','Bob','Carol','David'],
             ['dogs','cats','moose','goose']]


def printTable(tableData):
    colWidths = []
    for row in range(0,len(tableData[0])):
        for col in range(0,len(tableData)):
            colWidths.append(len(tableData[col][row]))
    Maxlen = max(colWidths)
    for row in range(0,len(tableData[0])):
        for col in range(0,len(tableData)):
            print(tableData[col][row].rjust(Maxlen),end='')
        print()
    return ''
print(printTable(tableData))
