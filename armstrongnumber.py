print('enter a number')
number = int(input())
temp = number
digitsum = 0
while temp != 0:
    digit = temp % 10
    digitsum += pow(digit, 3)
    temp = temp//10
if digitsum == number:
    print(f'{number} is a Armstrong Number')
else:
    print(f'{number} is not an Armstrong Number')
