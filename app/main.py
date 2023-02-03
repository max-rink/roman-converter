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
    return roman_units_mapping[roman_string] if roman_string in roman_units_mapping.keys() else "no match"


def parse_roman_number_to_units(romannumber: str) -> list:
    parsing_units = []
    # loop from right to left, because subtraction needs the next "right" character
    for i in range(len(romannumber) - 1, 0, -1):
        print("aktuelle range i-1 bis i:", romannumber[i - 1:i + 1])
        #nächste Schritte:
        #prüfen, ob Zweisteller im Dict gematcht wird
        #ansonsten prüfen, ob Einsteller gematcht wird
        #danach Unit in Liste schreiben und nächste Unit betrachten
        if i > 0 and convert_roman_to_int(romannumber[i - 1:i + 1]):
            parsing_units.append(romannumber[i - 1:i + 1])
            print("parsing units:", parsing_units)
        else:
            parsing_units.append(romannumber[i])
            print("parsing units:", parsing_units)

    return parsing_units


if __name__ == '__main__':
    x = 'XIV'
    parse_roman_number_to_units(x)
    #convert_roman_to_int('PyCharm')

    # fehlerausgabe XI
    # Überlegung das Dictonary als Variable zu definieren?