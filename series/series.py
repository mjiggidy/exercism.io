def slices(series, length):

	if not 0 < length < len(series)+1:
		raise ValueError(f"Length {length} is greater than the series length {len(series)}")

	output = [series[x:length+x] for x in range(len(series) - length+1)]
	
	return output
