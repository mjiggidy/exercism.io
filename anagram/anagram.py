def find_anagrams(word, candidates):
	"""Return words that are anagrams of the original"""
	anas = []

	word = word.casefold()
	
	for idx, cand in enumerate(candidates):
		cand = cand.casefold()

		# Skip if word is identical
		if word == cand:
			continue
		
		# Word is identical if list of sorted letters are the same
		elif sorted(word) == sorted(cand):
			anas.append(candidates[idx])
	
	return anas