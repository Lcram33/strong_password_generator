import secrets
import json


#in case the random library has to be changed
def random_below(max):
    """Return a random int in the range [0, max)."""
    return secrets.randbelow(max)

def random_range(min, max):
    """Return a random int in the range [min, max)."""
    new = 0
    while new < min:
        new = random_below(max)

    return new

def random_int(max):
    return secrets.randbelow(max)

def random_choice(items):
    return secrets.choice(list(items))

def permutation(items):
    l = len(items)
    items_list = list(items)
    output = list()

    for i in range(l):
        ind = random_int(len(items_list))
        output.append(items_list[ind])
        del items_list[ind]

    return "".join(output) if type(items) == str else output


#passwords
def new_password(size, chars):
    newpass = ""
    chars = permutation(chars)

    for i in range(size):
        newpass += random_choice(chars)

    return newpass

def new_passords(sizes, chars):
    passwords = list()
    for i in range(len(sizes)):
        passwords.append(new_password(sizes[i], chars))

    return passwords


#passphrases (picking random words)
def load_wordlist(path):
    #making this function in case another method/file format is needed. See perf_test.py for raw import.
    data = None
    with open(path, 'r') as f:
        data = json.load(f)
    return data


def new_passphrase(wordlist, number_of_words, separator):
    wordlist = permutation(wordlist)
    return separator.join([random_choice(wordlist) for i in range(number_of_words)])

def new_passphrases(wordlist, number_of_words, separator, amount):
    passphrases = list()
    for i in range(amount):
        passphrases.append(new_passphrase(wordlist, number_of_words, separator))

    return passphrases


#quotephrases (picking random quote)
def new_quotephrase(quotedict, separator, use_acronym, only_quotephrase = False):
    picked = random_choice(quotedict)
    acronym_picked = random_choice(quotedict)
    final = picked.replace('-', separator)

    if use_acronym:
        words = picked.split('-')
        pos = random_below(len(words))
        final = '-'.join(words[:pos] + [quotedict[acronym_picked]['reduced']] + words[pos:]).replace('-', separator)

    output = {
        'quote': final,
        'from': quotedict[picked]['from'],
        'original': quotedict[picked]['original']
    }

    if use_acronym:
        output['acronym_original'] = quotedict[acronym_picked]['original']
        output['acronym_from'] = quotedict[acronym_picked]['from']
    
    return output['quote'] if only_quotephrase else output

def new_quotephrases(quotedict, separator, use_acronym, amount, only_quotephrase = False):
    quotephrases = list()
    for i in range(amount):
        quotephrases.append(new_quotephrase(quotedict, separator, use_acronym, only_quotephrase))

    return quotephrases