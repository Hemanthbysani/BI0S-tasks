usr_input = input().split()
list = usr_input
def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]
A, B = split_list(usr_input)
res1 = [ord(ele) for sub in A for ele in sub]
sum1 = 0
for num in res1:
    sum1 += int(num)
res2 = [ord(ele) for sub in B for ele in sub]
sum2 = 0
for num2 in res2:
    sum2 += int(num2)
if(sum1 == sum2):
    print("True")
else:
    print("False")
