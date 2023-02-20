nums = []
n = int(input('Enter a length of list: '))
for i in range(n):
	num = int(input('Enter a number: '))
	nums.append(num)

def runningSum(nums):
	sum = 0
	result = []
	for num in nums:
		sum += num
		result.append(sum)
	return result

print( runningSum(nums) )
