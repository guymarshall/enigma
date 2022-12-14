class Rotor:
    def __init__(self, letters):
        self.letters = letters
        rotations = 0
        alphabet_lower = list("abcdefghijklmnopqrstuvwxyz")
        alphabet_upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def rotate(self):
        self.letters = self.letters[1:] + self.letters[:1]
        self.rotations = self.rotations + 1