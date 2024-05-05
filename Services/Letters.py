class Letter:
    def __init__(self):
        pass

    def letter_to_number(self, letter:str) -> int:
        if len(letter) != 1:
            raise ValueError("Input must be a letter a-z, A-Z")
        letters = "abcdefghijklmnopqrstuvwxyz"
        return letters.index(letter.lower()) + 1
    
    def get_word_value(self, word:str) -> int:
        return sum([self.letter_to_number(c) for c in word])