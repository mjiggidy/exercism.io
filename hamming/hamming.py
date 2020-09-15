def distance(strand_a, strand_b):
	"""Calculate hamming distance between two strands of DNA"""

	if len(strand_a) != len(strand_b):
		raise ValueError("Strands must be of equal length")

	errors = 0
	
	for a,b in zip(strand_a, strand_b):
		if a != b:
			errors+=1
	
	return errors