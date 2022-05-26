class Lexer:
    def __init__(self, source=None, source_file=None):
        self.source_file = source_file
        self.source = source
        self.tokens = []
