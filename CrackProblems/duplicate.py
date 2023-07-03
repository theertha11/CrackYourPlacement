strings = input("Enter the string: " )
count = dict()

for i in range(0, len(strings)):
	
	if strings[i] in count.keys():
		count[strings[i]] += 1
	else:
		count[strings[i]] = 1
for key, value in count.items():
	print(f'{key} is {value} times') 
		