def Temp(spam):
    spam[-1]='and'+' '+spam[-1]
    for i in range(len(spam)-1):
        print(spam[i],end=',')
    print(spam[-1])
    
spam=['apples','bananas','tofu','cats']
Temp(spam)
