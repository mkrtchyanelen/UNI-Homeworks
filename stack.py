s = input('Enter any brackets: ')

def is_valid(s, str) -> bool:
	stack = []
	for char in s:
		if char in '([{':
			stack.append(char)
		elif char in ')]}':
			if not stack:
				return false
			elif char == ')' and stack[-1] == '(':
				stack.pop()
			elif char == ']' and stack[-1] == '[':
				stack.pop()
			elif char == '}' and stack[-1] == '{':
				stack.pop()
			else:
				return false
	return not stack

print(is_valid(s, str))
