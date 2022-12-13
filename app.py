from rotor import Rotor

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
    output = ""

    for character in input:
        for key, value in switchboard:
            if key == character:
                character = value
        
        # rotors

        for key, value in switchboard:
            if key == character:
                character = value
        
        output += character

    print(f"Input string:\n{input}\nOutput string:\n{output}")


if __name__ == "__main__":
    main()
