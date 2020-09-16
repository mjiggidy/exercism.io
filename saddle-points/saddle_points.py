def saddle_points(matrix):

	points = []
	
	# Verify there is at least one row
	row_count = len(matrix)
	if row_count == 0:
		return []

	# Verify no empty columns
	col_count = len(matrix[0])
	if col_count == 0:
		return []
	
	# Verify no rows with unequal column count
	elif any(len(row) != col_count for row in matrix):
		raise ValueError("Matrix cannot be irregular")

	# Find saddle points
	for row_idx, row in enumerate(matrix):
		for col_idx, val in enumerate(row):
			if val == max(row) and val == min(y[col_idx] for y in matrix):
				points.append({"row":row_idx+1, "column": col_idx+1})
	
	return points