tableData = [['apples','oranges','cherries','banana'],
             ['Alice','Bob','Carol','David'],
             ['dogs','cats','moose','goose']]

def printTable(data):
    str_data = ''
    col_len = []
    for row in range(0,len(data[0])):
        for col in range(0,len(data)):
            col_len.append(len(data[col][row]))
    max_col_len = max(col_len)
    for row in range(0,len(data[0])):
        for col in range(0,len(data)):
            print(data[col][row].rjust(max_col_len),end='')
        print()
    return str_data
f_data = printTable(tableData)
print(f_data)
