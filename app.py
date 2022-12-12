"""
Read string as input

For each character that IS NOT " " OR IS NOT punctuation OR IS NOT a number
    pass character through switchboard
    if character is to be swapped, swap character
    set new value to character

    foreach rotor in rotors:
        pass character through rotor
        alphabet[0] goes to rotor[0] etc
        set new value to character
        move rotor values by 1 position

    go backwards to rotor_2 and repeat those steps

    go backwards to rotor_1 and repeat those steps

    go backwards to switchboard and repeat those steps

    return new character

Print encrypted string
"""

def rotate(list, count):
    return list[count:] + list[:count]

def main():
    switchboard = {
        "g": "o",
        "p": "z",
        "d": "b",
        "w": "j"
    }

    rotors = [
        list("wgsdtolkpcrxyhzujnbvieaqfm"),
        list("yshgdxzwbpoatejvqlfcirknum")
    ]

    input = "example text"

    output = ""

    print(f"Input string:\n{input}\nOutput string:\n{output}")


if __name__ == "__main__":
    main()
