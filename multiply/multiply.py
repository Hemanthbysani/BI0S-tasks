input_string = input()
userList = input_string.split()
mul1 = 1
for num in userList:
    mul1 *= int(num)
print(mul1)