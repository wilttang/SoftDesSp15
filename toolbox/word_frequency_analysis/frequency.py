""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string

filename = 'The_Adventures_of_Sherlock_Holmes.txt'

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	word_list = []

	#opens text file
	f = open(file_name,'r')
	lines = f.readlines()

	#skips past the header of the gutenberg book
	curr_line = 0
	while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
		curr_line += 1
	lines = lines[curr_line+1:]

	#goes through line by line and creads a list of all words
	for line in lines:
		for word in line.split():
			word = word.strip(string.punctuation + string.whitespace)
			word = word.lower()
			word_list.append(word)
	return word_list

def create_histogram(word_list):
	""" Takes a list of words and creates a dictionary histogram of all the words
	where the key is word and value is number of occurences
	"""
	hist = {}
	for word in word_list:
		hist[word] = hist.get(word, 0) +1
	return hist

def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	hist = create_histogram(word_list)

	#sort the dictionary from most frequent to least frequent
	ordered_by_frequency = sorted(hist, key = hist.get, reverse = True)
	
	return ordered_by_frequency

words_list = get_word_list(filename)
print get_top_n_words(words_list,100)