def find_anagrams(word, candidates):
	"""Return words that are anagrams of the original"""
	return [candidate for candidate in candidates if candidate.casefold() != word.casefold() and sorted(candidate.casefold()) == sorted(word.casefold())]