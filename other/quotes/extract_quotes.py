"""
The 3 samples are extracted from :

https://github.com/dwyl/quotes/blob/main/quotes.json
https://github.com/vinitshahdeo/inspirational-quotes/blob/master/data/data.json
https://github.com/NikhilNamal17/popular-movie-quotes/blob/master/data/data.json

Thanks to the ones who compiled thoses lists :)
"""


import json


final_quote_list = {}


def format_quote(quote):
    for char_e in 'éèêë':
        quote = quote.replace(char_e, 'e')

    for char_a in 'àäâ':
        quote = quote.replace(char_a, 'a')

    for char_c in 'ç':
        quote = quote.replace(char_c, 'c')

    for char_o in 'òôðö':
        quote = quote.replace(char_o, 'o')

    for char_u in 'ûùûü':
        quote = quote.replace(char_u, 'u')

    return '-'.join(
        y for y in ''.join(
            x for x in quote.lower() if x in "abcdefghijklmnopqrstuvwxyz0123456789 "
        ).replace(' ', '-').split('-') if y != ''
    )

def reduce_quote(formatted_quote):
    return ''.join(x[0] for x in formatted_quote.split('-') if len(x) > 0)


def extract_quotes(file_path):
    global final_quote_list

    with open(file_path, 'r') as f:
        quotes = json.loads(f.read().encode().decode('utf-8-sig'))
    
    for quote_dict in quotes:
        quote = quote_dict["text"] if "text" in quote_dict else quote_dict["quote"]
        quote_from = quote_dict["author"] if "author" in quote_dict else (quote_dict["from"] if "from" in quote_dict else quote_dict["movie"])
        formatted = format_quote(quote)

        if formatted not in final_quote_list:
            final_quote_list[formatted] = {
                'reduced': reduce_quote(formatted),
                'original': quote,
                'from': quote_from
            }


quotes_files = ['quotes_sample_1.json', 'quotes_sample_2.json', 'quotes_sample_3.json']

for file in quotes_files:
    extract_quotes(file)

with open("quotes.json", 'w') as f:
    f.write(json.dumps(final_quote_list, sort_keys=True, indent=4))

print(f"Done. Dumped {len(final_quote_list)} quotes !")
