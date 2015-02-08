# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: Wilson Tang

"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids_less_structure import aa, codons
import random
from load import load_seq

### YOU WILL START YOUR IMPLEMENTATION FROM HERE DOWN ###
def create_complement_strand(dna):
    """Given a dna strand creates a complement strand of DNA
        returns: a string
    """
    complement = ''
    for x in dna:
        if dna(x) == 'A':
            complement = 'T' + complement
        elif dna(x) == 'T':
            complement = 'A' + complement
        elif dna(x) == 'G':
            complement = 'C' + complement
        else:
            complement = 'G' + complement
    return complement
    #TODO: implement this
    pass

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
    """
    '''
    use in operator chpt8TP
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
        return dna

    # TODO: implement this
    pass

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
    # start_codon_initial = [m.start() for m in re.finditer('ATG', dna)]
    # start_codon_list = [x for x in start_codon_initial if (x)%3 == 0]
    # start_codon_ending_positions = 0
    # possible_ORFS_oneframe = []
    # #find all possible orfs
    # if start_codon_list > 0:
    #     for x in start_codon_list:
    #         if len(possible_ORFS_oneframe) > 0:
    #             if start_codon_list[x] > start_codon_ending_positions:
    #                 possible_ORFS_oneframe.append(rest_of_ORF(dna[x:]))
    #                 start_codon_ending_positions = start_codon_list[x] + len(possible_ORFS_oneframe[-1])
    #         else:
    #             possible_ORFS_oneframe.append(rest_of_ORF(dna[x:]))
    #             start_codon_ending_positions = start_codon_list[x] + len(possible_ORFS_oneframe[-1])
    # else:
    #     return possible_ORFS_oneframe
    dna_split = [dna[i:i+3] for i in range(0,len(dna),3)]
    start_codon_initial = [m.start() for m in re.finditer('ATG', dna)]
    start_codon_initial = [x for x in start_codon_initial if (x)%3 == 0]
    ending_index = 0
    indexing = 0
    possible_ORFS_oneframe = []
    #test each start codon position against the end of the last known orf if it is longer add it, otherwise ignore b/c nested
    while indexes < len(start_codon_initial):
        if start_codon_initial[indexes] > ending_index:
            x = start_codon_initial[indexes]
            possible_ORFS_oneframe.append(x)
            ending_index += len(rest_of_ORF(dna[x:]))
            indexes += 1
        else:
            indexes += 2 
    return possible_ORFS_oneframe
    while index < len(dna) - 3:
        if (index%3 == 0):
            if(dna[index] == 'A'):
                if(dna[index+1] == 'T'):
                    if(dna[index+2] == 'G'):
                        x = rest_of_ORF(dna[index:])
                        possible_ORFS_oneframe.append(x)
                        index += len(x)
                    else:
                        index += 1
                else:
                    index += 1
            else:
                index += 1
        else: 
            index += 1
    # TODO: implement this
    pass

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
    dna_ORFs_alllist = find_all_ORFs_oneframe(dna[0:len(dna)-1]) + find_all_ORFs_oneframe(dna[0:len(dna)-1]) + find_all_ORFs_oneframe(dna[0:len(dna)-1])
    # TODO: implement this
    pass

def find_ORFs_one_strand(dna):
    """Finds the non-nested open reading frames in one dna strand
        return list of non-nested ORFs
    """

    #TODO: implement this
    pass

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
    # TODO: implement this
    pass


# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^Part 1^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    """
    # TODO: implement this
    pass


def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    # TODO: implement this
    pass

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
    # TODO: implement this
    pass

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    # TODO: implement this
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()