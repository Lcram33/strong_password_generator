import secrets
import json

config = {}
default_uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
default_lowers = "abcdefghijklmnopqrstuvwxyz"
default_ints = "0123456789"
default_special_chars = "~`! @#$%^&*()_-+={[}]|\\:;\"'<,>.?/"


def get_config():
    global config

    try:
        with open("config.json", "r") as f:
            config = json.load(f)
            print("Config successfully loaded !")
    except Exception:
        print("No config file found, or missing permissions to read it. Setting up default configuration.")

        global default_ints
        global default_lowers
        global default_special_chars
        global default_uppers

        config = {
            "uppers": default_uppers,
            "lowers": default_lowers,
            "ints": default_ints,
            "special_chars": default_special_chars,
            "default": "yyyy",
            "range_min": 8,
            "range_max": 60
        }


def clean_string(str_input: str, allowed_chars: str, to_upper: bool = False, to_lower: bool = False):
    if to_upper:
        str_input = str_input.upper()
    if to_lower:
        str_input = str_input.lower()

    str_output = ""
    for i in range(len(str_input)):
        if str_input[i] in allowed_chars:
            str_output += str_input[i]

    return str_output


def convert_duration(seconds: int):
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
        human_readable = f"{str_years} year{'s' if years != 1 else ''}. {'You should be safe your whole life, but you may change your password after some times anyway.' if seconds >= 100 * one_year else 'Your should change your settings.'}"
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


def edit_chain(old_set: str, data: str):
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
    global default_uppers

    print("----------------------------------------------------------")
    print("CONFIG")
    print("1. Edit uppercases")
    print("2. Edit lowercases")
    print("3. Edit digits")
    print("4. Edit special characters")
    print("5. Edit default password settings")
    print("6. Edit range for randomly sized passwords option")
    print("----------------------------------------------------------")

    try:
        choice = int(input("Choice ? "))
    except Exception:
        print("This choice is not valid.")
        return

    if choice == 1:
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
    elif choice == 2:
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
    elif choice == 3:
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
    elif choice == 4:
        print("""
READ THIS BEFORE EDITING

Please note that :
- If a character is in the current set, it will be removed.
- If a character is not in the current set, it will be added.
- Any character which is not a lower/uppercase or digit will be accepted, but some may not be compatible with the sites or apps you may use.
- A character can be put multiple time but will not be inserted two times, they will be computed as explained above.

Example : the current set is ~`! @#
The user input is aAE!!??5Def%£
The new set will be : ~` @#!%£

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
    elif choice == 5:
        choices = ["uppercases", "lowercases", "digits", "special characters"]
        new_settings = ""

        for i in range(len(choices)):
            res = input("Should your password contain {} ? (y/n) ".format(choices[i]))
            if res not in ['y', 'n']:
                print("Invalid answer.")
                return
            new_settings += res

        config["default"] = new_settings
    elif choice == 6:
        print("""
Give the minimum lenght and the maximum lenght like this : min-max, or reset to set the default values.
A password of less than 8 characters may be a concern, even for a common/everyday use.
This program only accepts a minimum of 3 (for viability) and a maximum of 200 (a lot of services don't accept such long passwords !).
The default values are : 8-60.
    """)
        res = input("Enter the min-max : ")
        min = 8
        max = 60

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
    else:
        print("This choice is not valid.")
        return

    try:
        with open("config.json", "w+") as f:
            json.dump(config, f)
        print("Settings saved !")
    except Exception as e:
        print("Failed to save changes. It may be because : \"" + str(e) + "\"")

    return


def permutation(str_input: str):
    l = len(str_input)
    str_input = list(str_input)
    str_output = ""

    for i in range(l):
        ind = secrets.randbelow(len(str_input))
        str_output += str_input[ind]
        del str_input[ind]

    return str_output


def secrets_random_range(min: int, max: int):
    new = 0
    while new < min:
        new = secrets.randbelow(max)
    return new


def new_pass(size: int, chars: str):
    newpass = ""
    for i in range(size):
        newpass += secrets.choice(chars)

    return newpass


def generate_passwords():
    global config

    choice = input(
        "Should I use the default settings ? Current : {} (in order : use uppercases, lowercases, digits, special characters) : (y/n) ".format(
            config["default"]))
    settings = ""
    if choice == 'y':
        settings = config["default"]
    else:
        choices = ["uppercases", "lowercases", "digits", "special characters"]

        for i in range(len(choices)):
            res = input("Should your password contain {} ? (y/n) ".format(choices[i]))
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

    if len(chars) == 0:
        print("You must choose at least one type of characters.")
        return

    chars = permutation(chars)

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
        sizes = [size for i in range(6)]
    else:
        sizes = [secrets_random_range(config["range_min"], config["range_max"]) for i in range(6)]

    print("----------------------------------------------------------")
    for i in range(6):
        print("     " + new_pass(sizes[i], chars))
    print("----------------------------------------------------------")
    return


def calculus():
    print("""
Curious about the strenght of your password ?
You came to the right place !
You can find here the number of possible passwords assuming your actual settings.
    """)

    choice = input(
        "Should I use the default settings ? Current : {} (in order : use uppercases, lowercases, digits, special characters) : (y/n) ".format(
            config["default"]))
    settings = ""
    if choice == 'y':
        settings = config["default"]
    else:
        choices = ["uppercases", "lowercases", "digits", "special characters"]

        for i in range(len(choices)):
            res = input("Should your password contain {} ? (y/n) ".format(choices[i]))
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

    if len(chars) == 0:
        print("You must choose at least one type of characters.")
        return

    size = 0
    try:
        size = int(input("How long do you want your password ? "))
    except Exception:
        print("Invalid size.")
        return
    if size > 400 or size <= 0:
        print("The size must be between 1 and 400 (included).")
        return

    number_of_passwords = len(chars) ** size

    comment = ""
    if number_of_passwords > 10 ** 80:
        comment = "Oof. That's bigger than the number of particles in the universe, which is about 10^80."
    elif number_of_passwords > 5 * 10 ** 51:
        comment = "It's bigger than the mass of Earth in nucleons, about 4x10^51."
    elif number_of_passwords > 5 * 10 ** 37:
        comment = "It's bigger than the total number of DNA base pairs within the entire biomass on Earth (estimated at 5.3x10^37)"
    elif number_of_passwords > 10 ** 26:
        comment = "It's bigger than 13.8 billion light years (more than 10^26 m) which is the radius of the observable universe."
    elif number_of_passwords > 6 * 10 ** 23:
        comment = "It's bigger than the Avogadro constant which is the number of atoms in 12 grams of carbon-12 (approximately 6.022×10^23)."
    elif number_of_passwords > 10 ** 14:
        comment = "It's bigger than the number of neuronal connections in the human brain (estimated at 10^14)."
    elif number_of_passwords > 3 * 10 ** 13:
        comment = "It's bigger than the number of cells in the human body (estimated at 3.72 × 10^13)."
    elif number_of_passwords > 3 * 10 ** 8:
        comment = "It's bigger than the speed of light, which is a bit less than 300,000,000 m/s."

    print("And the number of possible passwords according to your settings is...")
    print("{:,} (about 10^{})".format(number_of_passwords, str(len(str(number_of_passwords)) - 1)))
    if len(comment) != 0:
        print(comment)

    print(
        "How long would it be to crack such a password ? Assuming the attacker can perfom a billion check per seconds, your password may last...")
    print(convert_duration(round(number_of_passwords / (10 ** 9))))

    return


def main():
    print("""
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

  v1.1
    """)
    get_config()

    while 1:
        print("MAIN MENU")
        print("----------------------------------------------------------")
        print("1. Generate password !")
        print("2. Edit settings")
        print("3. A bit of math")
        print("4. Exit")
        print("----------------------------------------------------------")

        try:
            choice = int(input("Choice ? "))
        except Exception:
            print("This choice is not valid.")

        if choice == 1:
            generate_passwords()
        elif choice == 2:
            change_config()
        elif choice == 3:
            calculus()
        elif choice == 4:
            break
            return
        else:
            print("This choice is not valid.")


main()