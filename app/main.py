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


def parse_roman_number_to_units(romannumber: str) -> list:
    # loop from right to left, because subtraction needs the next "right" character
    for i in range(len(x) - 1, -1, -1):
        print(x[i - 1:i + 1])
        #nächste Schritte:
        #prüfen, ob Zweisteller im Dict gematcht wird
        #ansonsten prüfen, ob Einsteller gematcht wird
        #danach Unit in Liste schreiben und nächste Unit betrachten
        #if convert_roman_to_int(x[i - 1:i + 1])



if __name__ == '__main__':
    x = 'XIV'
    parse_roman_number_to_units(x)
    #convert_roman_to_int('PyCharm')

