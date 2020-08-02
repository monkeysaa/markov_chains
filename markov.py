"""Generate Markov text from text files."""
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text_string = open(file_path).read()


    return text_string

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    list_of_words = text_string.split()
    # print(list_of_words)
    for i in range(len(list_of_words) - 2):
        key = (list_of_words[i], list_of_words[i + 1])
        value = list_of_words[i + 2] 
        if key not in chains:
            chains[key] = []
        if key in chains:
            chains[key].append(value)   #all other values


        
    return chains

    
#chains = make_chains(open_and_read_file("green-eggs.txt"))

def make_text(chains):
    """Return text from chains."""

    words = []
    
    # creates first link in Markov chain
    first_tuple = next(iter(chains))
    words.append(first_tuple[0])
    words.append(first_tuple[1])
    link = first_tuple

    while link in chains: 
        rand_word = choice(chains[link])
        words.append(rand_word)
        link = (link[1], rand_word)

 
    return " ".join(words)

#print(make_text(chains))

input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)

