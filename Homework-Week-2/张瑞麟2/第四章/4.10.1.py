def list(spam):
    spam[-1] = 'and ' + spam[-1]
    list1 = ', '.join(spam)
    return list1
list2 = list(['apple','banana','tofu','cats'])
print("列表是:")
print(list2)
