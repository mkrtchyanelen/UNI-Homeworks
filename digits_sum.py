import sys

number = int(sys.argv[1])

sum_of_dig = 0
while number > 0:
	dig = number % 10
	sum_of_dig = sum_of_dig + dig
	number = number // 10

print('The sum of digites is: ', sum_of_dig)

