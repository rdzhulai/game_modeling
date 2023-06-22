class Piece:
    def __init__(self, color):
        self.color = color
        self.active = False
        self.position = None

    def activate(self):
        pass

    def throw_out(self):
        pass

    def is_done(self):
        return False

    def move(self, steps):
        return 0

    def move_to_place(self, position):
        pass


if __name__ == '__main__':
    pass
