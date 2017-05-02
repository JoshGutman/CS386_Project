class Game:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __eq__(self, x):
        assert type(x) == Game
        if self.name == x.name:
            return True
        else:
            return False
