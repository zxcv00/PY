import tkinter
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

        # set winner

        # 승자가 있거나 무승부일 경우 game over => 결과 출력

        # change turn

    def draw_board(self):
        pass

    def cordinate_to_position(self, x, y):
        # x = col, y = row
        return y // 100 + 1, x // 100 + 1

if __name__ == '__main__':
    ttt_GUI = TictactoeGUI()