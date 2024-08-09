
class WordItem():
    def __init__(self, word, count, definition, translation):
        self.word = word
        self.count = count
        self.definition = definition
        self.translation = translation
        self.difficulty = None

    def __str__(self):
        return f'{self.word} ({self.count}) - {self.definition} - {self.translation} - {self.difficulty}'