class Rotor:
    def __init__(self, letters):
        self.letters = letters
        self.rotations = 0
        self.alphabet_lower = list("abcdefghijklmnopqrstuvwxyz")
        self.alphabet_upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def rotate(self):
        self.letters = self.letters[1:] + self.letters[:1]
        self.rotations = self.rotations + 1