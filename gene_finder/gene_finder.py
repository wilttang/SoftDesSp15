# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: Wilson Tang

"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons, aa_table
import random
from load import load_seq
import re
def shuffle_string(s):
    """ Shuffles the characters in the input string
        NOTE: this is a helper function, you do not have to modify this in any way """
    return ''.join(random.sample(s,len(s)))

### YOU WILL START YOUR IMPLEMENTATION FROM HERE DOWN ###


def get_complement(nucleotide):
    """ Returns the complementary nucleotide

        nucleotide: a nucleotide (A, C, G, or T) represented as a string
        returns: the complementary nucleotide
    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    >>> get_complement('T')
    'A'
    >>> get_complement('G')
    'C'
    """
    if nucleotide == 'A':
         return 'T'
    elif nucleotide == 'T':
         return 'A'
    elif nucleotide == 'G':
         return 'C'
    else:

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    >>> get_reverse_complement("ATGCCCGCTTT")
    'AAAGCGGGCAT'
    >>> get_reverse_complement("CCGCGTTCA")
    'TGAACGCGG'
    >>> get_reverse_complement("C")
    'G'
    """
    #added a test to check that it works for a string of length 1
    reverse_string = ''
    for x in range(len(dna)):
        reverse_string = get_complement(dna[x]) + reverse_string
    return reverse_string

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    >>> rest_of_ORF("ATGTGAA")
    'ATG'
    >>> rest_of_ORF("ATGAGATAGG")
    'ATGAGA'
    >>> rest_of_ORF("ATGAAAAAA")
    'ATGAAAAAA'
    """
    #added a test to check that it returned whole string with no in frame stop codon
    '''
    '''
    dna_split = [dna[i:i+3] for i in range(0,len(dna),3)]
    x = 0
    inidicies = 0
    while x < len(dna_split):
        if dna_split[x] == 'TAG' or dna_split[x] == 'TGA' or dna_split[x] == 'TAA':
            inidicies = x +1 
            break
        else:
            x = x + 1
    if inidicies > 0:
        return dna[0:x*3]
    else: 

def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")
    ['ATGCATGAATGTAGA', 'ATGTGCCC']
    """
    index = 0
    possible_ORFS_oneframe = []
    while index < len(dna) - 3:
        if (index%3 == 0):
            if(dna[index:index+3] == 'ATG'):
                x = rest_of_ORF(dna[index:])
                possible_ORFS_oneframe.append(x)
                index += len(x)
            else:
                index += 3
        else: 
            index += 3
    return possible_ORFS_oneframe

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs

    >>> find_all_ORFs("ATGCATGAATGTAG")
    ['ATGCATGAATGTAG', 'ATGAATGTAG', 'ATG']
    """
    all_ORFs = []
    first_ORF =  find_all_ORFs_oneframe(dna)  
    second_ORF = find_all_ORFs_oneframe(dna[1:])
    third_ORF = find_all_ORFs_oneframe(dna[2:])
    all_ORFs = first_ORF + second_ORF + third_ORF
    return all_ORFs

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """
    all_nonnested_ORFS_in_both = find_all_ORFs(dna) + find_all_ORFs(get_reverse_complement(dna))
    return all_nonnested_ORFS_in_both

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    >>> longest_ORF("ATGATGAAAAGGCCAT")
    'ATGATGAAAAGGCCAT'
    """
    #added test to check if there is no stop codon it will return the entire string
    return max(find_all_ORFs_both_strands(dna),key = len)

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    test_list = []
    for i in range(num_trials):
        temp_string = shuffle_string(dna)
        test_list.append(longest_ORF(temp_string))
    return len(max(test_list, key = len))

def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment

        >>> coding_strand_to_AA("ATGCGA")
        'MR'
        >>> coding_strand_to_AA("ATGCCCGCTTT")
        'MPA'
    """
    amino_acid_string = ''
    dna_split = [dna[i:i+3] for i in range(0,len(dna),3)]
    for i in range(len(dna_split)):
        if len(dna_split[i]) == 3:
            amino_acid_string += aa_table[ dna_split[i] ]
    return amino_acid_string

def gene_finder(dna):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    final_list = []
    all_possible_ORFS = find_all_ORFs_both_strands(dna)
    threshhold = longest_ORF_noncoding(dna,1500)
    for i in range(len(all_possible_ORFS)):
        if len(all_possible_ORFS[i]) >= threshhold:
            final_list.append( coding_strand_to_AA(all_possible_ORFS[i]) )
    return final_list        


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
dna = load_seq("./data/X73525.fa")
print gene_finder(dna)
