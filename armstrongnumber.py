print('enter a number')
number = int(input())
temp = number
digitsum = 0
print("Armstrong number Checking")
while temp != 0:
    digit = temp % 10
    digitsum += pow(digit, 3)
    temp = temp//10
if digitsum == number:
    print(f'{number} is a ARMSTRONG Number')
else:
    print(f'{number} is not an ARMSTRONG Number')
