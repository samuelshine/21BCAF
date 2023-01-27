number = 153
temp = number
digitsum = 0
while temp != 0:
    digit = temp % 10
    digitsum += digit*digit*digit
    temp = temp//10
if digitsum == number:
    print(f'{number} is a three-digit Armstrong Number')
else:
    print(f'{number} is not an Armstrong Number')
