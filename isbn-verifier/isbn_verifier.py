import re

def is_valid(isbn):
	"""A valid ISBN-10 number"""
	if re.match(r"^\d\-?\d{3}\-?\d{5}\-?[\dX]$", isbn) is None:
		return False
	
	code  = [int(x) for x in re.sub("[^\d]","", isbn)[0:9]]
	code.append(10 if isbn[-1] == 'X' else int(isbn[-1]))

	check = 0
	for idx in range(10):
		check += code[idx] * (10-idx)
	
	return check % 11 == 0

