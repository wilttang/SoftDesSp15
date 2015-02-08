def compare_numbers(x,y):
	""" checks Fermat's Theorem
    >>> compare_numbers(1,2)
    -1
    >>> compare_numbers(2,2)
    0
    >>> compare_numbers(2,1)
    1
    """
	if x > y:
		return 1
	elif x == y:
		return 0
	else: 
		return -1

def sum_of_squares(num):
	"""checks sum of squares of sequence
	>>> sum_of_squares(4)
	30
	"""
	x = 0
	for i in range(num+1):
		x += i**2
	return x

if __name__ == '__main__':
	import doctest
	doctest.testmod()