"""Main module."""

def hamming(seq1, seq2, case = 0):
    """
    hamming(seq1, seq2): Prints the hamming distance between the two input sequences. 

    Parameters
    ----------
    seq1 : str
           The reference sequence.
    seq2 : str
           The query sequence.
    case: int
            case sensitivity 
            default = 0, sensitive
                    1, insensititve

    """

    if seq1 is None or seq2 is None:
       print("One or both input sequences missing: Cannot calculate Hamming distance")
       return None
    
    elif not isinstance(seq1, str) or not isinstance(seq2, str):
        print("One or both input sequences is not a string: Cannot calculate Hamming distance")
        return None
    
    elif len(seq1) != len(seq2):
        print("Othe given sequences are not of the same length: Cannot calculate Hamming distance")
        return None
    
    elif case !=0 and case !=1:
        print("case argument is not 0 or 1: Cannot calculate Hamming distance")
        return None

    else:
        hamming_distance = 0
        if case == 0:
             for i in range(len(seq1)):
                 if seq1[i] != seq2[i]:
                     hamming_distance += 1
        else:
             for i in range(len(seq1)):
                 if seq1.upper()[i] != seq2.upper()[i]:
                     hamming_distance += 1   
    print("The reference sequence is " + seq1)
    print("The query sequence is " + seq2 ) 
    print("The hamming distance is ")
    return(hamming_distance)


