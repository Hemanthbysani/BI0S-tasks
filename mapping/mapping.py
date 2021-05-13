input_string = input()
List = input_string
res = [int(i) for i in List.split() if i.isdigit()]
print(res)