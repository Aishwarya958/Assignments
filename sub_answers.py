def max_subarray(array, size):
    '''
	 Finds the maximum sum of a contiguous subarray
	 input : [-2, -3, 4, -1, -2, 1, 5, -3]
			--> 4 + (-1) + (-2) + 1 + 5
	output : 7 

	'''
    if array is None:
        return 0
    
    max_sum = array[0]
    sum = array[0]
    for num in array[1:]:
        sum = max(num, sum+num)
        max_sum = max(max_sum, sum)
    
    print(max_sum)
  
array = [-2, -3, 4, -1, -2, 1, 5, -3]
max_subarray(array, len(array))
  