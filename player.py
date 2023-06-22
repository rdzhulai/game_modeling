from piece import Piece


class Player:
    def __init__(self, color, board):
        self.color = color
        self.board = board
        self.pieces = [
            Piece(color) for _ in range(4)
        ]

    def is_done(self):
        return False

    def has_active(self):
        return False

    def get_piece_positions(self):
        return list()

    def get_valid_moves(self, roll):
        return list()

    def prepare_targets(self, moves):
        return list()

    def get_move(self, roll):
        # DO NOT IMPLEMENT HERE
        return list()


class RandomPlayer(Player):
    def __init__(self, color, board):
        super().__init__(color, board)

    def get_move(self, roll):
        return list()


class SafePlayer(Player):
    def __init__(self, color, board):
        super().__init__(color, board)

    def get_move(self, roll):
        return list()


class MeanPlayer(Player):
    def __init__(self, color, board):
        super().__init__(color, board)

    def get_move(self, roll):
        return list()


class EagerPlayer(Player):
    def __init__(self, color, board):
        super().__init__(color, board)

    def get_move(self, roll):
        return list()


if __name__ == '__main__':
    pass
