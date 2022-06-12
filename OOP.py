import string


class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(self.letters)

    def letters_num(self):
        print(self.letters)


class EngAlphabet(Alphabet):
    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    __letters_num = 26

    def is_en_letter(self, letter):
        if letter.upper() in self.letters:
            return True
        return False

    def letters_num(self):
        return EngAlphabet.__letters_num

    @staticmethod
    def example():
        print("Hello world")



EngAlphabet = EngAlphabet()
EngAlphabet.print()
print(EngAlphabet.letters_num())
print(EngAlphabet.is_en_letter('F'))
print(EngAlphabet.is_en_letter('Щ'))
EngAlphabet.example()
