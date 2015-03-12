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
	f = open(file_name,'r')
	lines = f.readlines()
	curr_line = 0
	while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
		curr_line += 1
	lines = lines[curr_line+1:]
	
	for word in lines.split():
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

	t = []
	final_list = []
	hist = create_histogram(word_list)
	
	#goes through the histogram and sorts in greatest to least
	for key, value in hist.items():
		t.append(key)
	t.sort(reverse = False)
	for word in t[0:n]:
		final_list.append(word)
	return final_list

get_word_list(filename)
print get_top_n_words(['balls','balls','hello','hello','hi'],2)