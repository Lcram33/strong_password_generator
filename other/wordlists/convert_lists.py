import json


def load_wordlist_raw_txt(path):
    wordlist = list()
    with open(path, 'r') as f:
        wordlist = [x.replace('\n', '') for x in f.readlines()]

    return wordlist


def txt_wordlist_to_json(path, save_path):
    data = load_wordlist_raw_txt(path)
    with open(save_path, 'w+') as f:
        json.dump(data, f)


#convert to json, if not done yet
txt_wordlist_to_json('en_wordlist.txt', 'wordlist.json')
