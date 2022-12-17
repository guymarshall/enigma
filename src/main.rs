/*
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
*/

mod user_input;

struct Rotor {
    letters: Vec<char>,
    rotations: i32,
    alphabet_lower: Vec<char>,
    alphabet_upper: Vec<char>
}

fn main() {
    let input: String = user_input::get_user_input("Enter text to encrypt:");
}

/*MAIN
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
*/

/*ROTOR
class Rotor:
    def __init__(self, letters):
        self.letters = letters
        self.rotations = 0
        self.alphabet_lower = list("abcdefghijklmnopqrstuvwxyz")
        self.alphabet_upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    @classmethod
    def rotate(self):
        self.letters = self.letters[1:] + self.letters[:1]
        self.rotations = self.rotations + 1
    
    @classmethod
    def use(self, letter):
        if letter not in self.alphabet_lower and letter not in self.alphabet_upper:
            return letter
        
        if letter in self.alphabet_lower:
            index = self.alphabet_lower.index(letter)
        elif letter in self.alphabet_upper:
            index = self.alphabet_upper.index(letter)
        
        letter = self.letters[index] # prevents rotate() changing return value

        self.rotate()
        
        return letter
*/