def longest_run(L):
	"""
	Assumes L is a list of integers containing at least 2 elements.
	Finds the longest run of numbers in L, where the longest run can
	either be monotonically increasing or monotonically decreasing. 
	In case of a tie for the longest run, choose the longest run 
	that occurs first.
	Does not modify the list.
	Returns the sum of the longest run. 
	"""
	longest_length = 1
	increasing_length = 1
	decreasing_length = 1
	for i in range(len(L) - 1):
		if L[i] >= L[i+1]:
			decreasing_length += 1
		else:
			decreasing_length = 1
		if L[i] <= L[i+1]:
			increasing_length += 1
		else:
			increasing_length = 1
		if increasing_length > longest_length:
			longest_length = increasing_length
			run_end = i + 1
		elif decreasing_length > longest_length:
			longest_length = decreasing_length
			run_end = i + 1

	return sum(L[run_end - longest_length + 1 : run_end+1])

#longest_run([10, 4, 3, 8, 3, 4, 5, 7, 7, 2])
#print(longest_run([5, 4, 10]))
