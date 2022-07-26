from secure_pwd_gen_api import *
import json
from math import log
from os import get_terminal_size

config = {}
default_uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
default_lowers = "abcdefghijklmnopqrstuvwxyz"
default_ints = "0123456789"
default_special_chars = "@%+\\/'!#$^?:(){[}]~-_."
default_uncommon_special_chars = "`&*=|;\"<,>§£øéèàçùαβγδεζηΘθλμνξΠπρΣτυΦφΨψΩω"

simple_config = {
    "uppers": default_uppers,
    "lowers": default_lowers,
    "ints": default_ints,
    "special_chars": default_special_chars,
    "uncommon_special_chars": default_uncommon_special_chars,
    "default": "yyynn",
    "range_min": 8,
    "range_max": 15,
    "passphrase_separator": '-',
    "passphrase_lenght": 4,
    "acronyms": 'n'
}

usual_config = {
    "uppers": default_uppers,
    "lowers": default_lowers,
    "ints": default_ints,
    "special_chars": default_special_chars,
    "uncommon_special_chars": default_uncommon_special_chars,
    "default": "yyyyn",
    "range_min": 12,
    "range_max": 30,
    "passphrase_separator": '-',
    "passphrase_lenght": 6,
    "acronyms": 'y'
}

strong_config = {
    "uppers": default_uppers,
    "lowers": default_lowers,
    "ints": default_ints,
    "special_chars": default_special_chars,
    "uncommon_special_chars": default_uncommon_special_chars,
    "default": "yyyyn",
    "range_min": 30,
    "range_max": 50,
    "passphrase_separator": '-',
    "passphrase_lenght": 8,
    "acronyms": 'y'
}

very_strong_config = {
    "uppers": default_uppers,
    "lowers": default_lowers,
    "ints": default_ints,
    "special_chars": default_special_chars,
    "uncommon_special_chars": default_uncommon_special_chars,
    "default": "yyyyy",
    "range_min": 50,
    "range_max": 100,
    "passphrase_separator": '-',
    "passphrase_lenght": 12,
    "acronyms": 'y'
}


def print_separator():
    print('-' * get_terminal_size().columns)

def get_config():
    global config

    try:
        with open("config.json", "r") as f:
            config = json.load(f)
            print("Config successfully loaded !")
    except Exception:
        print("No config file found, or missing permissions to read it. Setting up default configuration (usual config, see settings section for more details).")

        global usual_config
        config = usual_config

def clean_string(str_input, allowed_chars, to_upper = False, to_lower = False):
    if to_upper:
        str_input = str_input.upper()
    if to_lower:
        str_input = str_input.lower()

    return ''.join(char for char in str_input if char in allowed_chars)

def convert_duration(seconds):
    one_year = int(365.25 * 24 * 60 * 60)
    one_month = int(60 * 60 * 24 * 365.25 / 12)
    one_week = 7 * 24 * 60 * 60
    one_day = 24 * 60 * 60

    human_readable = ""
    if seconds == 0:
        human_readable = "Less than a second. Not nice, change your settings !!"
    elif seconds > one_year:
        years = round(seconds / one_year)
        str_years = '{:,}'.format(years)
        human_readable = f"{str_years} year{'s' if years != 1 else ''}. {'You should be safe your whole life.' if seconds >= 100 * one_year else 'Your should change your settings.'}"
    elif seconds > one_month:
        months = round(seconds / one_month)
        human_readable = f"{str(months)} month{'s' if months != 1 else ''}. Not nice, change your settings !!"
    elif seconds > one_week:
        weeks = round(seconds / one_week)
        human_readable = f"{str(weeks)} week{'s' if weeks != 1 else ''}. Not nice, change your settings !!"
    elif seconds > one_day:
        days = round(seconds / one_day)
        human_readable = f"{str(days)} day{'s' if days != 1 else ''}. Not nice, change your settings !!"
    elif seconds > 3600:
        hours = round(seconds / 3600)
        human_readable = f"{str(hours)} hour{'s' if hours != 1 else ''}. Not nice, change your settings !!"
    elif seconds > 60:
        minutes = round(seconds / 60)
        human_readable = f"{str(minutes)} minute{'s' if minutes != 1 else ''}. Not nice, change your settings !!"
    else:
        human_readable = f"{str(seconds)} second{'s' if seconds != 1 else ''}. Not nice, change your settings !!"

    return human_readable


def edit_chain(old_set, data):
    new_set = old_set
    for char in data:
        if char in new_set:
            new_set = new_set.replace(char, '')
        else:
            new_set += char

    return new_set

def change_config():
    global config
    global default_ints
    global default_lowers
    global default_special_chars
    global default_uncommon_special_chars
    global default_uppers

    print_separator()
    print("CONFIG")
    print("1. Quick setup")
    print("2. Edit uppercases")
    print("3. Edit lowercases")
    print("4. Edit digits")
    print("5. Edit special characters")
    print("6. Edit uncommon special characters")
    print("7. Edit default password settings")
    print("8. Edit range for randomly sized passwords option")
    print("9. Edit default random passphrase settings")
    print("10. Edit default quote-based passphrase settings")
    print_separator()

    try:
        choice = int(input("Choice ? "))
    except Exception:
        print("This choice is not valid.")
        return

    if choice == 1:
        global simple_config
        global usual_config
        global strong_config
        global very_strong_config

        print("""
READ THIS BEFORE MAKING YOUR CHOICE

Several configurations are available :
1.  Simple config : passwords will not contain special characters.
    Choosing r when size is asked will generate a password of a lenght between 8 and 15.
    Default number of words in a passphrase : 4.
    THIS CONFIGURATION IS NOT RECOMMENDED.

2.  Usual config : passwords will contain special characters.
    Choosing r when size is asked will generate a password of a lenght between 12 and 30.
    Default number of words in a passphrase : 6.
    This config is the default one.

3.  Strong config : passwords will contain special characters.
    Choosing r when size is asked will generate a password of a lenght between 30 and 50.
    Default number of words in a passphrase : 8.
    When long passwords are accepted, this configuration is recommended.

4.  Very strong config : passwords will contain special characters and uncommon special characters (e.g. greek letters).
    Choosing r when size is asked will generate a password of a lenght between 50 and 100.
    Default number of words in a passphrase : 12.
    Please note that many systems will not accept such long passwords, and uncommon special characters.
        """)

        try:
            config_choice = int(input("Choice ? (configuration number) : "))
        except Exception:
            print("This choice is not valid.")
            return

        if config_choice == 1:
            if input("""
---------------------------------------------------------------------------------------
| WARNING : THE PASSWORDS GENERATED WITH THIS CONFIGURATION SHOULD BE CONSIDERED WEAK |
| AND THEREFORE SHOULD NOT BE USED IF BRUTE-FORCE ATTACK MAY BE PERFORMED.            |
---------------------------------------------------------------------------------------
Set anyway ? (y/n)
            """) == 'y':
                config = simple_config
            else:
                return
        elif config_choice == 2:
            config = usual_config
        elif config_choice == 3:
            config = strong_config
        elif config_choice == 4:
            config = very_strong_config
        else:
            print("Invalid choice !")
            return

    elif choice == 2:
        print("""
READ THIS BEFORE EDITING

Please note that :
- This input is not case-sensitive.
- If a character is in the current set, it will be removed.
- If a character is not in the current set, it will be added.
- Any non-related character will be ignored.
- A character can be put multiple time but will not be inserted two times, they will be computed as explained above.

Example : the current set is ABCD.
The user input is aAE!5Def.
The new set will be : BCAF.

To exit this menu : enter *exit
To reset the set to its default value : *reset
        """)

        while 1:
            print("The current set of uppercases is :   " + config["uppers"])
            data = input("Edit : ")

            if data.find("*exit") > -1:
                break
            elif data.find("*reset") > -1:
                config["uppers"] = default_uppers
            else:
                config["uppers"] = edit_chain(config["uppers"], clean_string(data, default_uppers, to_upper=True))
    elif choice == 3:
        print("""
READ THIS BEFORE EDITING

Please note that :
- This input is not case-sensitive.
- If a character is in the current set, it will be removed.
- If a character is not in the current set, it will be added.
- Any non-related character will be ignored.
- A character can be put multiple time but will not be inserted two times, they will be computed as explained above.

Example : the current set is abcd.
The user input is aAE!5Def.
The new set will be : bcaf.

To exit this menu : enter *exit
To reset the set to its default value : *reset
        """)

        while 1:
            print("The current set of lowercases is :   " + config["lowers"])
            data = input("Edit : ")

            if data.find("*exit") > -1:
                break
            elif data.find("*reset") > -1:
                config["lowers"] = default_lowers
            else:
                config["lowers"] = edit_chain(config["lowers"], clean_string(data, default_lowers, to_lower=True))
    elif choice == 4:
        print("""
READ THIS BEFORE EDITING

Please note that :
- If a character is in the current set, it will be removed.
- If a character is not in the current set, it will be added.
- Any non-related character will be ignored.
- A character can be put multiple time but will not be inserted two times, they will be computed as explained above.

Example : the current set is 123.
The user input is aE53326.
The new set will be : 1536.

To exit this menu : enter *exit
To reset the set to its default value : *reset
        """)

        while 1:
            print("The current set of digits is :   " + config["ints"])
            data = input("Edit with : ")

            if data.find("*exit") > -1:
                break
            elif data.find("*reset") > -1:
                config["ints"] = default_ints
            else:
                config["ints"] = edit_chain(config["ints"], clean_string(data, default_ints))
    elif choice == 5:
        print("""
READ THIS BEFORE EDITING

Please note that :
- If a character is in the current set, it will be removed.
- If a character is not in the current set, it will be added.
- Any character which is not a lower/uppercase or digit will be accepted, but some may not be compatible with the sites or apps you may use.
- A character can be put multiple time but will not be inserted two times, they will be computed as explained above.

Example : the current set is ~!+@#
The user input is aAE!!??+5Def%
The new set will be : ~@#!%

To exit this menu : enter *exit
To reset the set to its default value : *reset
        """)

        while 1:
            print("The current set of special characters is :   " + config["special_chars"])
            data = input("Edit with : ")

            if data.find("*exit") > -1:
                break
            elif data.find("*reset") > -1:
                config["special_chars"] = default_special_chars
            else:
                edited_data = ""
                for char in data:
                    if char not in default_ints + default_lowers + default_uppers:
                        edited_data += char

                config["special_chars"] = edit_chain(config["special_chars"], edited_data)
    elif choice == 6:
        print("""
READ THIS BEFORE EDITING

Please note that :
- If a character is in the current set, it will be removed.
- If a character is not in the current set, it will be added.
- Any character which is not a lower/uppercase or digit will be accepted, but some may not be compatible with the sites or apps you may use.
- A character can be put multiple time but will not be inserted two times, they will be computed as explained above.
- Some characters in this set may not be accepted by websites/systems. It's highly possible, actually.

Example : the current set is >§£øéèàçùαβγδ
The user input is Bp8"!éàà+5µ
The new set will be : >§£øèçùαβγδàµ

To exit this menu : enter *exit
To reset the set to its default value : *reset
        """)

        while 1:
            print("The current set of special characters is :   " + config["uncommon_special_chars"])
            data = input("Edit with : ")

            if data.find("*exit") > -1:
                break
            elif data.find("*reset") > -1:
                config["uncommon_special_chars"] = default_uncommon_special_chars
            else:
                edited_data = ""
                for char in data:
                    if char not in default_ints + default_lowers + default_uppers + default_special_chars:
                        edited_data += char

                config["uncommon_special_chars"] = edit_chain(config["uncommon_special_chars"], edited_data)
    elif choice == 7:
        choices = ["uppercases", "lowercases", "digits", "special characters", "uncommon sepcial characters"]
        new_settings = ""

        for i in range(len(choices)):
            res = input(f"Should your password contain {choices[i]} ? (y/n) ")
            if res not in ['y', 'n']:
                print("Invalid answer.")
                return
            new_settings += res

        config["default"] = new_settings
    elif choice == 8:
        print("""
Give the minimum lenght and the maximum lenght like this : min-max, or reset to set the default values.
A password of less than 8 characters may be a concern, even for a common/everyday use.
This program only accepts a minimum of 3 (for viability) and a maximum of 200 (a lot of services don't accept such long passwords !).
The default values are : 8-40.
    """)
        res = input("Enter the min-max : ")
        min = 8
        max = 40

        if res != "reset":
            try:
                res = res.split('-')
            except Exception:
                print("Invalid input.")
                return

            if len(res) != 2:
                print("Invalid input.")
                return

            try:
                min = int(res[0])
                max = int(res[1])
            except Exception:
                print("Invalid input.")
                return

            if min < 3:
                print("The minimum size has to be greater or equal to 3. Canceled.")
                return

            if max > 200:
                print("The maximum size has to be less or equal to 200. Canceled.")
                return

            if min == max:
                print("Using this function with the same min and max is useless... Canceled.")
                return

        config["range_min"] = min
        config["range_max"] = max
    elif choice == 9:
        print(f"Current : separator is {config['passphrase_separator']}, number of words is {config['passphrase_lenght']}")
        separator = input("Separator ? ")
        lenght = input("How many words do you want in your passphrase ? ")

        try:
            lenght = int(lenght)
        except Exception:
            print("Invalid lenght.")
            return

        if lenght > 200 or lenght < 3:
            print("The lenght must be between 3 and 200 (included).")
            return

        config['passphrase_separator'] = separator
        config['passphrase_lenght'] = lenght
    elif choice == 10:
        print("Do you want acronyms in your quote based passphrases ?")
        print("If enabled, 2 quotes are used, one is turned into an acronym and is randomly placed in the first one.")
        print("IF YOU CHOOSE TO USE A PASSPHRASE MADE OF A PUBLIC OR FAMOUS QUOTE, IT IS STRONGLY RECOMMENDED TO USE THIS TECHNIQUE, AS SUCH PASSPHRASE IS VULNERABLE TO DICTIONARY ATTACK")
        print(f"Current : {config['acronyms']}")
        choice = input("Use acronyms ? (y/n) ")

        if choice not in ['y', 'n']:
            print("Invalid lenght.")
            return

        config["acronyms"] = choice
    else:
        print("This choice is not valid.")
        return

    try:
        with open("config.json", "w+") as f:
            json.dump(config, f)
        print("Settings saved !")
    except Exception as e:
        print("Failed to save changes. It may be because : \"" + str(e) + "\"")


def generate_passwords():
    global config

    choice = input(f"Should I use the default settings ? Current {config['default']} (in order : use uppercases, lowercases, digits, special character, uncommon special characters) : (y/n) ")
    settings = ""
    if choice == 'y':
        settings = config["default"]
    else:
        choices = ["uppercases", "lowercases", "digits", "special characters", "uncommon special characters"]

        for choice in choices:
            res = input(f"Should your password contain {choice} ? (y/n) ")
            if res not in ['y', 'n']:
                print("Invalid answer.")
                return
            settings += res

    chars = ""
    if settings[0] == 'y':
        chars += config["uppers"]
    if settings[1] == 'y':
        chars += config["lowers"]
    if settings[2] == 'y':
        chars += config["ints"]
    if settings[3] == 'y':
        chars += config["special_chars"]
    if settings[4] == 'y':
        chars += config["uncommon_special_chars"]

    if len(chars) == 0:
        print("You must choose at least one type of characters.")
        return

    amount = 6

    size = input("How long do you want your password ? (r for randomly sized passwords) : ")
    sizes = []
    if size != "r":
        try:
            size = int(size)
        except Exception:
            print("Invalid size.")
            return

        if size > 200 or size < 3:
            print("The size must be between 3 and 200 (included).")
            return

        sizes = [size for i in range(amount)]
    else:
        sizes = [random_range(config["range_min"], config["range_max"]) for i in range(amount)]

    passwords = new_passords(sizes, chars)
    line_size = max(len(x) for x in passwords)

    print('-'*line_size)
    for password in passwords:
        print(password)
        print('-'*line_size)

def generate_passphrases():
    global config

    wordlist = load_wordlist('wordlist.json')

    choice = input(f"Should I use the default settings ? Current : separator is {config['passphrase_separator']}, number of words is {config['passphrase_lenght']} : (y/n) ")
    seperator = ""
    lenght = 0

    if choice == 'y':
        separator = config["passphrase_separator"]
        lenght = config["passphrase_lenght"]
    else:
        separator = input("Separator ? ")
        lenght = input("How many words do you want in your passphrase ? ")

        try:
            lenght = int(lenght)
        except Exception:
            print("Invalid lenght.")
            return

        if lenght > 200 or lenght < 3:
            print("The lenght must be between 3 and 200 (included).")
            return

    amount = 6

    passphrases = new_passphrases(wordlist, lenght, separator, amount)
    line_size = max([len(x) for x in passphrases])

    print('-'*line_size)
    for passphrase in passphrases:
        print(passphrase)
        print('-'*line_size)

def generate_quotephrases():
    global config

    quote_dict = load_wordlist('quotes.json')

    choice = input(f"Should I use the default settings ? Current : separator is {config['passphrase_separator']}, use acronyms : {config['acronyms']} : (y/n) ")
    seperator = ""
    lenght = 0

    if choice == 'y':
        separator = config["passphrase_separator"]
        use_acronym = config["acronyms"]
    else:
        separator = input("Separator ? ")
        use_acronym = input("Use acronyms ? (y/n) ")

    use_acronym = True if use_acronym == 'y' else False

    amount = 6

    quotesphrases = new_quotephrases(quote_dict, separator, use_acronym, amount)
    line_size = max(len(x['quote']) for x in quotesphrases)

    print('-'*line_size)
    for q_phrase_dict in quotesphrases:
        print(q_phrase_dict['quote'])
        print()
        print("Original : " + q_phrase_dict['original'])
        print("From : " + q_phrase_dict['from'])

        if "acronym_original" in q_phrase_dict:
            print("Acronym : " + q_phrase_dict['acronym_original'])
            print("From : " + q_phrase_dict['acronym_from'])

        print('-'*line_size)


def calculus():
    global config

    choice = input("Password (1) or passphrase (2) ? ")
    if choice not in ['1', '2']:
        print("Invalid answer.")
        return

    if choice == '1':
        choice = input(f"Should I use the default settings ? Current : {config['default']} (in order : use uppercases, lowercases, digits, special characters, uncommon special characters) : (y/n) ")
        settings = ""

        if choice == 'y':
            settings = config["default"]
        else:
            choices = ["uppercases", "lowercases", "digits", "special characters", "uncommon special characters"]

            for i in range(len(choices)):
                res = input(f"Should your password contain {choices[i]} ? (y/n) ")
                if res not in ['y', 'n']:
                    print("Invalid answer.")
                    return
                settings += res

        chars_len = 0
        if settings[0] == 'y':
            chars_len += len(config["uppers"])
        if settings[1] == 'y':
            chars_len += len(config["lowers"])
        if settings[2] == 'y':
            chars_len += len(config["ints"])
        if settings[3] == 'y':
            chars_len += len(config["special_chars"])
        if settings[4] == 'y':
            chars_len += len(config["uncommon_special_chars"])

        if chars_len == 0:
            print("You must choose at least one type of characters.")
            return

        size = 0
        try:
            size = int(input("How long would your password be ? "))
        except Exception:
            print("Invalid size.")
            return

        if size > 400 or size <= 0:
            print("The size must be between 1 and 400 (included).")
            return

        bits_of_entropy = round(size * log(chars_len, 2), 1)

        print(f"Strenght of your password : {bits_of_entropy} bits of entropy.")
        print("What does it means ?")
        print(f"That the possible number of passwords according your settings is about 2^{bits_of_entropy}.")

        print("How long would it be to crack such a password ? Assuming the attacker can perfom a billion check per seconds, your password may last...")
        print(convert_duration(round(2**(bits_of_entropy-1) / (10 ** 9))))
    else:
        wordlist = load_wordlist('wordlist.json')

        choice = input(f"Should I use the default settings ? Current : number of words is {config['passphrase_lenght']} : (y/n) ")
        lenght = 0

        if choice == 'y':
            lenght = config["passphrase_lenght"]
        else:
            lenght = input("How many words do you want in your passphrase ? ")

            try:
                lenght = int(lenght)
            except Exception:
                print("Invalid lenght.")
                return

            if lenght > 200 or lenght < 3:
                print("The lenght must be between 3 and 200 (included).")
                return

        bits_of_entropy = round(lenght * log(len(wordlist), 2), 1)

        print(f"Strenght of your passphrase : {bits_of_entropy} bits of entropy.")
        print("What does it means ?")
        print(f"That the possible number of passphrases according your settings is about 2^{bits_of_entropy}.")

        print("How long would it be to crack such a passphrase ? Assuming the attacker can perfom a billion check per seconds, your passphrase may last...")
        print(convert_duration(round(2**(bits_of_entropy-1) / (10 ** 9))))


def main():
    splash = """
███████╗████████╗██████╗  ██████╗ ███╗   ██╗ ██████╗     ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗
██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗████╗  ██║██╔════╝     ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗
███████╗   ██║   ██████╔╝██║   ██║██╔██╗ ██║██║  ███╗    ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║
╚════██║   ██║   ██╔══██╗██║   ██║██║╚██╗██║██║   ██║    ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║
███████║   ██║   ██║  ██║╚██████╔╝██║ ╚████║╚██████╔╝    ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝
╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝     ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝

 ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗
 ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
 ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
 ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
 ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
  ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
    """

    version = "1.3"

    print(splash)
    print()
    print(version)
    print()


    get_config()

    while 1:
        print("MAIN MENU")
        print_separator()
        print("1. Generate password")
        print("2. Generate passphrase (random words)")
        print("3. Generate passphrase (from a quote)")
        print("4. Edit settings")
        print("5. A bit of math")
        print("6. Exit")
        print_separator()

        try:
            choice = int(input("Choice ? "))
        except Exception:
            print("This choice is not valid.")

        if choice == 1:
            generate_passwords()
        elif choice == 2:
            generate_passphrases()
        elif choice == 3:
            generate_quotephrases()
        elif choice == 4:
            change_config()
        elif choice == 5:
            calculus()
        elif choice == 6:
            print("Goodbye !")
            break
        else:
            print("This choice is not valid.")


main()
