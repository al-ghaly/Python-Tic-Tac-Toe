from PyQt5 import QtWidgets as Widget
import sys, startwindow, random


class MainWindow(Widget.QMainWindow):
    def __init__(self, parent=None):
        self.app = Widget.QApplication(sys.argv)
        super().__init__(parent)
        self.ui = startwindow.Ui_StartWindow()
        self.ui.setupUi(self)
        self.ui.com_mode.clicked.connect(lambda: self.open(self, self.ui.diff_window))
        self.ui.ply_mode.clicked.connect(lambda: self.open(self, self.ui.players_window))
        self.ui.ui_players.new_game_player_mode.clicked.connect(lambda: self.open(self.ui.players_window, self))
        self.ui.ui_diff.easyButton.clicked.connect(lambda: self.open(self.ui.diff_window, self.ui.ui_diff.easyWindow))
        self.ui.ui_diff.med_button.clicked.connect(lambda: self.open(self.ui.diff_window, self.ui.ui_diff.medium_window))
        self.ui.ui_diff.hard_button.clicked.connect(lambda: self.open(self.ui.diff_window, self.ui.ui_diff.hard_window))
        self.ui.ui_diff.ui_easy.new_game_player_mode.clicked.connect(lambda: self.open(self.ui.ui_diff.easyWindow, self))
        self.ui.ui_diff.ui_med.new_game_player_mode.clicked.connect(lambda: self.open(self.ui.ui_diff.medium_window, self))
        self.ui.ui_diff.ui_hard.new_game_player_mode.clicked.connect(lambda: self.open(self.ui.ui_diff.hard_window, self))
        self.connect(self.ui.ui_players, self.player_click)
        self.board = [" "] * 9

        self.ui.ui_diff.hard_button.clicked.connect(self.hard)
        self.com_connect(self.ui.ui_diff.ui_hard, self.com_click)
        self.connect_no_params(self.ui.ui_diff.ui_hard, self.play_hard)

        self.ui.ui_diff.med_button.clicked.connect(self.medium)
        self.com_connect(self.ui.ui_diff.ui_med, self.com_click)
        self.connect_no_params(self.ui.ui_diff.ui_med, self.play_med)

        self.ui.ui_diff.easyButton.clicked.connect(self.easy)
        self.com_connect(self.ui.ui_diff.ui_easy, self.com_click)
        self.connect_no_params(self.ui.ui_diff.ui_easy, self.play_easy)

        self.winner = False

    def player_click(self, button, num):
        if button.text() != " ":
            self.message("Error", "Invalid Place!!", Widget.QMessageBox.Warning)
            return
        button.setText(f"{self.ui.ui_players.current[1]}")
        self.board[num] = self.ui.ui_players.current[1]
        self.ui.ui_players.current, self.ui.ui_players.coming = self.ui.ui_players.coming, self.ui.ui_players.current
        self.ui.ui_players.label2.setText(f"{self.ui.ui_players.current[0]} turn ({self.ui.ui_players.current[1]})")
        if self.detect(self.ui.ui_players):
            self.message("Winner !!!", "The game has ended")
            self.ui.ui_players.label2.setText(f"{self.ui.ui_players.coming[0]} Won the game.")
            return

    def com_click(self, ui, button, num):
        if button.text() != " ":
            self.message("Error", "Invalid Place!!", Widget.QMessageBox.Warning)
            return
        button.setText(f"{self.current[1]}")
        self.board[num] = self.current[1]
        if self.detect(ui):
            self.message("Winner !!!", "The game has ended")
            ui.label2.setText(f"{self.current[0]} Won the game.")
            self.winner = True
            return
        self.current, self.coming = self.coming, self.current
        ui.label2.setText(f"{self.current[0]} turn ({self.current[1]})")

    def message(self, title, message, typeof=Widget.QMessageBox.Information):
        msg = Widget.QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(typeof)
        msg.exec_()
        
    def detect(self, ui):
        board = self.board
        if board[0] == board[1] == board[2] != ' ':
            return True
        elif board[3] == board[4] == board[5] != ' ':
            return True
        elif board[6] == board[7] == board[8] != ' ':
            return True
        elif board[0] == board[3] == board[6] != ' ':
            return True
        elif board[1] == board[4] == board[7] != ' ':
            return True
        elif board[2] == board[5] == board[8] != ' ':
            return True
        elif board[0] == board[4] == board[8] != ' ':
            return True
        elif board[6] == board[4] == board[2] != ' ':
            return True
        elif ' ' not in board:
            self.message("Draw", "We have a Tie !!")
            ui.label2.setText('      Draw')
            return False
        return False

    def open(self, old, new):
        self.reset(self.ui.ui_players)
        self.reset(self.ui.ui_diff.ui_easy)
        self.reset(self.ui.ui_diff.ui_med)
        self.reset(self.ui.ui_diff.ui_hard)
        old.close()
        new.show()

    def show2(self):
        self.show()
        sys.exit(self.app.exec_())

    def reset(self, ui):
        self.winner = False
        self.board = [" "] * 9
        ui.box1.setText(" ")
        ui.box2.setText(" ")
        ui.box3.setText(" ")
        ui.box4.setText(" ")
        ui.box5.setText(" ")
        ui.box6.setText(" ")
        ui.box7.setText(" ")
        ui.box8.setText(" ")
        ui.box9.setText(" ")

    def connect(self, ui, func):
        ui.box1.clicked.connect(lambda: func(ui.box1, 0))
        ui.box2.clicked.connect(lambda: func(ui.box2, 1))
        ui.box3.clicked.connect(lambda: func(ui.box3, 2))
        ui.box4.clicked.connect(lambda: func(ui.box4, 3))
        ui.box5.clicked.connect(lambda: func(ui.box5, 4))
        ui.box6.clicked.connect(lambda: func(ui.box6, 5))
        ui.box7.clicked.connect(lambda: func(ui.box7, 6))
        ui.box8.clicked.connect(lambda: func(ui.box8, 7))
        ui.box9.clicked.connect(lambda: func(ui.box9, 8))

    def com_connect(self, ui, func):
        ui.box1.clicked.connect(lambda: func(ui, ui.box1, 0))
        ui.box2.clicked.connect(lambda: func(ui, ui.box2, 1))
        ui.box3.clicked.connect(lambda: func(ui, ui.box3, 2))
        ui.box4.clicked.connect(lambda: func(ui, ui.box4, 3))
        ui.box5.clicked.connect(lambda: func(ui, ui.box5, 4))
        ui.box6.clicked.connect(lambda: func(ui, ui.box6, 5))
        ui.box7.clicked.connect(lambda: func(ui, ui.box7, 6))
        ui.box8.clicked.connect(lambda: func(ui, ui.box8, 7))
        ui.box9.clicked.connect(lambda: func(ui, ui.box9, 8))

    def connect_no_params(self, ui, func):
        ui.box1.clicked.connect(func)
        ui.box2.clicked.connect(func)
        ui.box3.clicked.connect(func)
        ui.box4.clicked.connect(func)
        ui.box5.clicked.connect(func)
        ui.box6.clicked.connect(func)
        ui.box7.clicked.connect(func)
        ui.box8.clicked.connect(func)
        ui.box9.clicked.connect(func)

    def win(self, symbol, ui):
        all_moves = [ui.box1, ui.box2, ui.box3, ui.box4, ui.box5, ui.box6, ui.box7, ui.box8, ui.box9]
        if self.board.count(" ") == 1:
            all_moves[self.board.index(" ")].click()
        for move in all_moves:
            if move.text() == " ":
                self.board[all_moves.index(move)] = symbol
                if self.detect(ui):
                    move.click()
                    return True
                else:
                    self.board[all_moves.index(move)] = " "
        return False

    def hard(self):
        start_key = random.randint(0, 1)
        if start_key:
            self.current, self.coming = ("Computer", "X"), ("Player", "O")
            self.ui.ui_diff.ui_hard.box5.click()
        else:
            self.ui.ui_diff.ui_hard.label2.setText("Player turn (X)")
            self.current, self.coming = ("Player", "X"), ("Computer", "O")

    def play_hard(self):
        ui = self.ui.ui_diff.ui_hard
        if self.current[0] == "Player" or self.winner:
            return
        symbol = self.current[1]
        if self.win(symbol, ui):
            return
        symbol = self.coming[1]
        if self.win(symbol, ui):
            return
        if self.board[4] == " ":
            ui.box5.click()
            return
        priorities = [ui.box5, ui.box1, ui.box3, ui.box7, ui.box9, ui.box2, ui.box4, ui.box6, ui.box8]
        random.shuffle(priorities)
        corners = self.board[0] + self.board[2] + self.board[6] + self.board[8]
        if corners.count(self.coming[1]) == 2:
            priorities = [ui.box2, ui.box6, ui.box4, ui.box8, ui.box5, ui.box1, ui.box3, ui.box7, ui.box9]
        for move in priorities:
            if move.text() == " ":
                move.click()
                break

    def medium(self):
        start_key = random.randint(0, 1)
        if start_key:
            ui = self.ui.ui_diff.ui_med
            priorities = [ui.box5, ui.box1, ui.box3, ui.box7, ui.box9, ui.box2, ui.box4, ui.box6, ui.box8]
            random.shuffle(priorities)
            self.current, self.coming = ("Computer", "X"), ("Player", "O")
            priorities[5].click()
        else:
            self.ui.ui_diff.ui_med.label2.setText("Player turn (X)")
            self.current, self.coming = ("Player", "X"), ("Computer", "O")

    def play_med(self):
        ui = self.ui.ui_diff.ui_med
        if self.current[0] == "Player" or self.winner:
            return
        symbol = self.current[1]
        if self.win(symbol, ui):
            return
        priorities = [ui.box5, ui.box1, ui.box3, ui.box7, ui.box9, ui.box2, ui.box4, ui.box6, ui.box8]
        for move in priorities:
            if move.text() == " ":
                move.click()
                break

    def easy(self):
        start_key = random.randint(0, 1)
        if start_key:
            self.current, self.coming = ("Computer", "X"), ("Player", "O")
            self.ui.ui_diff.ui_easy.box2.click()
        else:
            self.ui.ui_diff.ui_easy.label2.setText("Player turn (X)")
            self.current, self.coming = ("Player", "X"), ("Computer", "O")

    def play_easy(self):
        ui = self.ui.ui_diff.ui_easy
        priorities = [ui.box5, ui.box1, ui.box3, ui.box7, ui.box9, ui.box2, ui.box4, ui.box6, ui.box8]
        if self.current[0] == "Player" or self.winner:
            return
        random.shuffle(priorities)
        for move in priorities:
            if move.text() == " ":
                move.click()
                break


test = MainWindow()
test.show2()


