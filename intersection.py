num1 = []
num2 = []

n1 = int(input('Enter the length of the first list: '))
n2 = int(input('Enter the length of the second list: '))

for i in range(n1):
	num = int(input('Enter a number for the first list: '))
	num1.append(num)

for i in range(n2):
	num = int(input('Enter a number for the second list: '))
	num2.append(num)

def intersection(num1, num2):
	set1 = set(num1)
	set2 = set(num2)
	return list(set1.intersection(set2))

print( intersection(num1, num2) )
