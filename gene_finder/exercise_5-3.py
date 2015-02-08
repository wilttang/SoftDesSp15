def check_fermat(a,b,c,n):
	""" checks Fermat's Theorem
    >>> check_fermat(1,2,3,4)
    No, that doesn't work
    """
	if (a**n + b**n == c**n):
		print 'Holy Smokes, Fermat was wrong!'
	else:
		print "No, that doesn't work" 

def ask_fermat_Constants():
	""" Prompts user for 4 numbers to check Fermat's Theorem

    """
	a = raw_input('Please enter a number for a')
	b = raw_input('Please enter a number for b')
	c = raw_input('Please enter a number for c')
	n = raw_input('Please enter a number for n')
	check_fermat(a,b,c,n)

if __name__ == "__main__":
    import doctest
    doctest.testmod()