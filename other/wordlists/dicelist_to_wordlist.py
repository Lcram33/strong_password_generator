"""
Wordlists are usually found as "dicelists" (designed to be used with a dice to generate passphrases).
E.g. 12534 cow will be picked up if you obtain 1,2,5,3,4 on 5 dices.
We however here don't need the numbers !
So let's remove then with this simple script.

WARNING : it overwrites the inputed file !
"""

dice_list_path = 'fr_wordlist.txt'

f = open(dice_list_path, 'r')
lines = [x.replace('\n', '') for x in f.readlines()]
f.close()

words = [line.split(' ')[1] for line in lines]

f = open(dice_list_path, 'w')
f.write("\n".join(words))
f.close()

print("Done.")
