def convert_roman_to_int(roman_string):
    roman_units_mapping = {
        '': 0,
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900


    }
    return roman_units_mapping[roman_string]


#    def unitparser(number):


if __name__ == '__main__':
    convert_roman_to_int('PyCharm')

