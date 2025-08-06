def int_to_roman(number):
	int_roman = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
				 10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
				 100: 'C', 400: 'CD',  500: 'D', 900: 'CM', 1000: 'M'}
	result = ''
	for n in (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1):
		while n <= number:
			result += int_roman[n]
			number -= n
	return result


print(int_to_roman(3749))
print(int_to_roman(58))
print(int_to_roman(1994))
