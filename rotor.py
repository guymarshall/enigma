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