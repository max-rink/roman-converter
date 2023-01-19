def convert_roman_to_int(roman_string):
    roman_mapping = {
        '': 0,
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    return roman_mapping[roman_string]


if __name__ == '__main__':
    convert_roman_to_int('PyCharm')
