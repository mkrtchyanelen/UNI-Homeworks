import sys

n = int(sys.argv[1])
x = 1
for i in range(n-1,-1,-1):
	print('|' + ' ' * i + '#' * x)
	x += 1
