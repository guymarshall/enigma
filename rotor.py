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
            print("lowercase swap")
        elif letter in self.alphabet_upper:
            print("uppercase swap")
        
        return letter