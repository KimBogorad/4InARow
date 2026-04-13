import token


class Board():

    def __init__(self, screen):
        # list of lists of square
        self.board_game = []
        for row in range(6):
            self.board_game.append([])
            lst = self.board_game[-1]  # last new list, now is empty
            for col in range(7):
                lst.append(token.Token(screen, row, col))
        self.lowest_spots = [5, 5, 5, 5, 5, 5, 5]

    def all_squares(self):
        squares = []
        for row in range(6):
            for col in range(7):
                squares.append(self.board_game[row][col])
        return squares

    def one_square(self, row, col):
        return self.board_game[row][col]

    def draw_board(self, screen):
        for sq in self.all_squares():
            sq.draw(screen)