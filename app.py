"""
Read string as input

For each character that IS NOT " " OR IS NOT punctuation OR IS NOT a number
    pass character through switchboard
    if character is to be swapped, swap character
    set new value to character

    pass character through rotor_1
    alphabet[0] goes to rotor_1[0] etc
    set new value to character
    move rotor_1 values by 1 position

    pass new character through rotor_2
    alphabet[0] goes to rotor_2[0] etc
    set new value to character
    move rotor_2 values by 1 position

    go backwards to rotor_2 and repeat those steps

    go backwards to rotor_1 and repeat those steps

    go backwards to switchboard and repeat those steps

    return new character

Print encrypted string
"""

def main():
    switchboard = {
        "g": "o",
        "p": "z",
        "d": "b",
        "w": "j"
    }

    rotor_1 = "wgsdtolkpcrxyhzujnbvieaqfm"
    rotor_2 = "yshgdxzwbpoatejvqlfcirknum"

    input_string = "example text"

    output_string = ""

    print(f"Input string:\n{input_string}\nOutput string:\n{output_string}")


if __name__ == "__main__":
    main()
