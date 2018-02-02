#Collatz序列计算
print('请输入任何一个整数')
number = int(input())  #从键盘获取该数字
while number != 1:
    if number % 2 == 0:#验证是否为偶数
        number = number // 2
        print(number)
        continue       #返回所得值
    if number % 2 == 1:
        number = 3 * number + 1
        print(number)
        continue

