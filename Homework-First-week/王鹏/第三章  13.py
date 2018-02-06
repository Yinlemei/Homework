def collatz(number):
    if number%2==0:
        return number//2
    else:
        return 3*number+1

while True:
    try:
        num = int(input('Enter number: '))
        while num!=1:
            num=collatz(num)
            print(num)
        if num==1:
            break
    except ValueError:
        print('请输入正整数')
    
