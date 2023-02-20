nums = []
n = int(input('Enter a length: '))
for i in range(n):
	num = int(input('Enter a number: '))
	nums.append(num)

k = int(input('Enter a non negative number: '))

def rotate(nums, k):
	k = k % n
	result = [0] * n
	for i in range(k):
		result[i] = nums[n-k+i]
	for i in range(n-k):
		result[k+i] = nums[i]
	return result

print(rotate(nums, k))
