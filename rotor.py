class Rotor:
    def __init__(self, letters):
        self.letters = letters
        rotate_count = 0

    def rotate(self, letters):
        self.letters = letters[1:] + letters[:1]
        self.rotate_count += 1