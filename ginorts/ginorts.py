input_string = input()

word = input_string

res_low = [char for char in word if char.islower()]
res_high = [char for char in word if char.isupper()]
res_digit = [int(char) for char in word if char.isdigit()]

zero = []
for i in list(res_digit):
    if i==0:
        res_digit.remove(i)
        zero.append(i)

def sortString(string): 
    return ''.join(sorted(string))

even = []
odd = []

def Split(res_digit): 
    global even
    global odd
    even =[]
    odd = [] 
    for i in res_digit: 
        if (i % 2 == 0): 
            even.append(i) 
        else: 
            odd.append(i) 

listToStr = ''.join([str(elem) for elem in res_digit])
Split(res_digit)
even.sort()
odd.sort()
listtostreven = ''.join([str(elem) for elem in even])   
listtostrodd = ''.join([str(elem) for elem in odd])
listtostrzero = ''.join([str(elem) for elem in zero])
print(sortString(res_low), sortString(res_high), listtostrodd, listtostrzero, listtostreven, sep='')