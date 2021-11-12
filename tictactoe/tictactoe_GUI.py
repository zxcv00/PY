import tkinter
from tkinter import messagebox

from tictactoe_game_engine import TictactoeGameEngine

class TictactoeGUI:
    def __init__(self):
        self.game_engine = TictactoeGameEngine()
        self.init_GUI()

    def init_GUI(self):
        self.CANVAS_SIZE = 300
        self.root = tkinter.Tk()
        self.root.title('TICTACTOE')
        self.root.geometry(f'{self.CANVAS_SIZE}x{self.CANVAS_SIZE}')    # 300 x 300
        self.root.resizable(width = False, height = False)

        self.canvas = tkinter.Canvas(self.root, bg = 'white', width = self.CANVAS_SIZE, height = self.CANVAS_SIZE)
        self.canvas.pack()

        self.images = {}        # {'X' => PhotoImage 객체, 'O' => PhotoImage 객체}
        self.images['X'] = tkinter.PhotoImage(file = 'X.gif')
        self.images['O'] = tkinter.PhotoImage(file ='O.gif')

        self.canvas.bind('<Button-1>', self.click_handler)       # click_handler => 가로가 없고, 현재 실행하는 것이 아닌 버튼을 눌러야만 실행하는 것 (괄호 없애기)

        self.root.mainloop()

    def click_handler(self, event):
        # input event.x, event.y => row, col
        row, col = self.cordinate_to_position(event.x, event.y)

        # set row, col
        self.game_engine.set(row, col)

        # show board
        self.game_engine.show_board()
        self.draw_board()

        # set winner
        winner = self.game_engine.set_winner()

        # 승자가 있거나 무승부일 경우 game over => 결과 출력
        if winner == 'X' or winner == 'O':
            messagebox.showinfo('GAME OVER', f'{winner} WIN 🎊')
            self.root.quit()
        elif winner == 'd':
            messagebox.showinfo('GAME OVER', 'TIE 🙌')
            self.root.quit()

        # change turn
        self.game_engine.change_turn()

    def draw_board(self):
        TILE_SIZE = self.CANVAS_SIZE // self.game_engine.SIZE       # 100

        # clear
        self.canvas.delete('all')

        x = 0
        y = 0

        for i, v in enumerate(self.game_engine.board):
            if v == '.':
                pass
            else:       # elif v == 'X or v == 'O'
                self.canvas.create_image(x, y, anchor = 'nw', image = self.images[v])
            x += TILE_SIZE

            if i % self.game_engine.SIZE == self.game_engine.SIZE - 1:
                x = 0
                y += TILE_SIZE


    def cordinate_to_position(self, x, y):
        # x = col, y = row
        row = y // (self.CANVAS_SIZE // self.game_engine.SIZE) + 1
        col = x // (self.CANVAS_SIZE // self.game_engine.SIZE) + 1

        return row, col

if __name__ == '__main__':
    ttt_GUI = TictactoeGUI()