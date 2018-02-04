def collatz(number):  
    if number % 2 == 1 and number > 1:  
        num = 3*number + 1  
        print(num)  
        return num  
    elif number % 2 == 0:  
        num = number // 2  
        print(num)  
        return num    
n = int(input('Enter a number: \n'))  
while True:  
    n = collatz(n)  
    if n == 1:  
        break 
