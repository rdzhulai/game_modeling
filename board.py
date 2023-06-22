STARTING_POSITIONS = {
    'black': 0,
    'yellow': 10,
    'green': 20,
    'red': 30
}


class Board:
    def __init__(self):
        self.board = [None for _ in range(40)]

    def normalize_position(self, position, player_color):
        return 0

    def can_move_there(self, player, piece, position):
        return False

    def process_player_moves(self, player, targets):
        pass


if __name__ == '__main__':
    pass
