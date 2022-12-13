from rotor import Rotor

"""
Read string as input

For each character that IS NOT " " OR IS NOT punctuation OR IS NOT a number
    pass character through switchboard
    if character is to be swapped, swap character
    set new value to character

    for rotor in rotors:
        pass character through rotor
        alphabet[0] goes to rotor[0] etc
        set new value to character
        move rotor values by 1 position

    go backwards for rotor in rotors and repeat those steps

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

    rotors = [
        Rotor("wgsdtolkpcrxyhzujnbvieaqfm"),
        Rotor("yshgdxzwbpoatejvqlfcirknum")
    ]

    input = "example text"

    for character in input:
        for key, value in switchboard:
            if key == character:
                character = value
        
        # rotors

        for key, value in switchboard:
            if key == character:
                character = value

    output = ""

    print(f"Input string:\n{input}\nOutput string:\n{output}")


if __name__ == "__main__":
    main()
