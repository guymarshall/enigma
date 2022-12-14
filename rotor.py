class Rotor:
    def __init__(self, letters):
        self.letters = letters
        rotate_count = 0
        alphabet_lower = list("abcdefghijklmnopqrstuvwxyz")
        alphabet_upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def rotate(self, letters):
        self.letters = letters[1:] + letters[:1]
        self.rotate_count += 1