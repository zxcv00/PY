class TictactoeGameEngine:
    def __init__(self):
        self.SIZE = 3
        self.board = list('.' * self.SIZE * self.SIZE)      # ['.', '.', '.', '.', '.', '.', '.', '.', '.']
        self.turn = 'X'

    def show_board(self):
        for a in range(len(self.board)):
            print(self.board[a], end=' ')
            if a % self.SIZE == self.SIZE - 1:   # 중요함 기말때보라함
                print()

    def set(self, row, col):
        self.board[self.SIZE * (row - 1) + (col - 1)] = self.turn

    def position_to_index(self, row, col):
        return self.SIZE * (row - 1) + (col - 1)

    def set_winner(self):
        # 가로
        for row in range(1, 3+1):   # row 1~3 반복
            if self.board[self.position_to_index(row, 1)] \
                    == self.board[self.position_to_index(row, 2)] \
                    == self.board[self.position_to_index(row, 3)] \
                    == self.turn:           # '.'일 때 끝나지 않게 하자
                return self.turn

        # 세로
        for col in range(1, 3+1):   # col 1~3 반복
            if self.board[self.position_to_index(col, 1)] \
                    == self.board[self.position_to_index(col, 2)] \
                    == self.board[self.position_to_index(col, 3)] \
                    == self.turn:           # '.'일 때 끝나지 않게
                return self.turn

        # \
        if self.board[self.position_to_index(1, 1)] \
                == self.board[self.position_to_index(2, 2)] \
                == self.board[self.position_to_index(3, 3)] \
                == self.turn:
            return self.turn

        # /
        if self.board[self.position_to_index(1, 3)]  \
                == self.board[self.position_to_index(2, 2)] \
                == self.board[self.position_to_index(3, 1)] \
                == self.turn:           # '.'일 때 끝나지 않게
            return self.turn

        # 무승부: 다 채워졌을 때 위의 것에 해당 안 됐을 때 => self.board 에 '.'이 없는 상테
        if not '.' in self.board:       # self.board 안에 '.'이 없다면
            return 'd'  # draw

    def change_turn(self):
        # self.turn 'X'면 'O'로, 'O'면 'X'로 바꾸자
        self.turn = 'O' if self.turn == 'X' else 'X'


if __name__ == '__main__':
    game_engine = TictactoeGameEngine()
    game_engine.show_board()    # ...\n...\n...
    game_engine.set(3, 2)
    game_engine.show_board()    # ['.', '.', '.', '.', '.', '.', '.', 'X', '.']
    game_engine.set(3, 1)
    game_engine.set(3, 3)
    print(game_engine.set_winner())     # 'X'
    game_engine.change_turn()
    print(game_engine.turn)      # 'O'

    game_engine.set(1, 3)
    game_engine.set(2, 2)
    game_engine.set(3, 1)
    print(game_engine.set_winner())# 'O'