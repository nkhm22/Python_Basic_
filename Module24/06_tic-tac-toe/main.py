class Cell:
    def __init__(self, number, busy = False):
        self.number = str(number)
        self.busy = busy


class Board:
    def __init__(self):
        self.board = [Cell(i) for i in range(1, 10)]
    def draw_board(self):
        print('+' * 13)
        for i in range(3):
            print('|', self.board[i * 3].number, '|', self.board[1 + i * 3].number, '|', self.board[2 + i * 3].number, '|')
            print('+' * 13)
    def check_win(self):
        combination_win = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6], [0, 3, 6], [1, 4, 7], [2, 5, 8]]
        for comb in combination_win:
            if self.board[comb[0]].number == self.board[comb[1]].number == self.board[comb[2]].number:
                if player_1.symb == self.board[comb[0]].number:
                    print('Победил {}'.format(player_1.name))
                else:
                    print('Победил {}'.format(player_2.name))
                return True
        return False
    def check_busy(self, number):
        if self.board[number - 1].busy:
            return True
        return False
class Player:
    def __init__(self, name, symb, win = False):
        self.name = name
        self.symb = symb
        self.win = win
    def go_cell(self, number, Board):
        Board.board[number - 1].busy = False
        Board.board[number - 1].number = self.symb
class Game:
    def start(self, player, board):
        number = int(input('Куда ходит, {}?'.format(player.name)))
        if board.check_busy(number):
            print('Клетка занята')
            Game.start(self, player, board)
        else:
            player.go_cell(number, board)
player_1 = Player('Игрок 1', 'X')
player_2 = Player('Игрок 2', 'O')
board = Board()
game = Game()
count = 0
while True:
    board.draw_board()
    if count % 2 == 0:
        game.start(player_1, board)
        if board.check_win():
            break
    else:
        game.start(player_2, board)
        if board.check_win():
            break
    count += 1
    if count == 9:
        print('Ничья')
        break