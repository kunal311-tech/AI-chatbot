import math
import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # Representation of the board
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        # Check column
        col_ind = square % 3
        col = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in col]):
            return True
        # Check diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

def minimax(game, maximizing_player, alpha, beta):
    if game.current_winner == 'O':
        return {'position': None, 'score': 1}
    elif game.current_winner == 'X':
        return {'position': None, 'score': -1}
    elif not game.empty_squares():
        return {'position': None, 'score': 0}

    if maximizing_player:
        max_eval = {'position': None, 'score': -math.inf} 
        for possible_move in game.available_moves():
            game.make_move(possible_move, 'O')
            evaluation = minimax(game, False, alpha, beta)
            game.board[possible_move] = ' '
            evaluation['position'] = possible_move
            if evaluation['score'] > max_eval['score']:
                max_eval = evaluation
            alpha = max(alpha, evaluation['score'])
            if alpha >= beta:
                break
        return max_eval
    else:
        min_eval = {'position': None, 'score': math.inf} 
        for possible_move in game.available_moves():
            game.make_move(possible_move, 'X')
            evaluation = minimax(game, True, alpha, beta)
            game.board[possible_move] = ' '
            evaluation['position'] = possible_move
            if evaluation['score'] < min_eval['score']:
                min_eval = evaluation
            beta = min(beta, evaluation['score'])
            if alpha >= beta:
                break
        return min_eval

def play(game, player, alpha=-math.inf, beta=math.inf):
    game.print_board_nums()
    while game.empty_squares():
        if player == 'X':
            square = int(input("Choose where to place X (0-8): "))
        else:
            square = minimax(game, True, alpha, beta)['position']
        if game.make_move(square, player):
            if game.current_winner:
                print(f"{player} wins!")
                return
            player = 'O' if player == 'X' else 'X'
        game.print_board()
    print("It's a tie!")

if __name__ == '__main__':
    game = TicTacToe()
    play(game, 'X')
