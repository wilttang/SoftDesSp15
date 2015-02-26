""" Mini Project 3: Text Mining:
	This Project whill compare two Machiavelli books:
	(The Prince and Discourses on Livy) 
	that have two very different messages

	Create a new Markov text from these two books

	Then compare the new text and see which original 
	is it more similar to.
"""
import pickle
import math
import string
import matplotlib.pyplot as plt 

def process_file(filename,percentage):
	"""
		Adapted from ThinkPython book, create histogram of words in 
		a text up to a certain point in the book
		inputs: file and percentage of book to stop at
		returns: dictionary histogram
	"""
	hist = dict()
	#open file safely
	with open(filename) as fp:
		for line in range(0,percentage):
			process_line(fp.readline(), hist )
	return hist


def process_line(line,hist):
	"""
		Taken from ThinkPython book, takes a line, strips it, updates histogram
		inputs: a line and histogram object
		returns: none
	"""
	line = line.replace('-', ' ')
	for word in line.split():
		word = word.strip(string.punctuation + string.whitespace)
		word = word.lower()
		hist[word] = hist.get(word, 0) +1


def summation_AiBi(Ai,Bi):
	"""
		Iterates through corresponding given data sets Ai and Bi
		For every possible key will multiply value together(if only found in one multiplies by 0)
		
		inputs: Ai - histogram dictionary ,Bi - histogram dictionary
		returns  an int - SummationofAiBi

	"""
	summation = 0
	#sum Ai*Bi
	for i in Ai:
		if i in Bi:
			summation += Ai[i] * Bi[i]
	return summation

def summation_squared(Ai):
	"""
		Iterates through the given data and sums the square of each value

		inputs:Ai - histogram dictionary
		returns an int - SummationofAi^2
	"""
	summation = 0
	for i in Ai:
		summation += Ai[i]**2
	return summation


def cos_comparison(input_text1,input_text2):
	"""
		Takes two input text files and applies cosine similarity analysis on it
		inputs: two text files
		outputs: graph of cosine similarity at various points in the book
	"""
	theta_list = []
	for i in range(1,11):
		percentage = i*0.1
		hist1 = process_file(input_text1,int(percentage  * 4207))
		hist2 = process_file(input_text2,int(percentage  * 13245))
		top = summation_AiBi(hist1,hist2)
		bot1 = math.sqrt( summation_squared(hist1) )
		bot2 = math.sqrt( summation_squared(hist2) )
		theta = math.acos( top/(bot1 * bot2) )
		theta_list.append(theta)
	plt.plot(['10','20','30','40','50','60','70','80','90','100'],theta_list, 'go-')
	plt.xlabel('Percentage of Book')
	plt.ylabel('Cosine Similarity')
	plt.title('Cosine Similarity of "The Prince" and "The Discourses" at various points')
	plt.show()


cos_comparison('prince.txt','discourses.txt')

