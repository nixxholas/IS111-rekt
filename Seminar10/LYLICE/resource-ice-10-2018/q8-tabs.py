
def rot (sentence, offset):
	result = ''
	for ch in                       sentence:
		if ch == ' ':
			result += ' '
		else:
			result += chr( (ord(ch) - ord('a') + offset) % 26  + ord('a'))

	return result

print (rot('xyz',2))
print (rot2('xyz',2))


students = [('Alwyn', 12), ('Tim', 12)]
students[1] = ('Jerry',13)
print(students[1])
