from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.modalview import ModalView
from kivy.uix.floatlayout import FloatLayout

# Existing logic code
def sum(a, b, c):
    return a + b + c

def checkwin(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            return "X"
        if sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
            return "O"
    return None

class TicTacToeApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.xState = [0] * 9
        self.zState = [0] * 9
        self.turn = 1  # X starts first
        self.buttons = []

    def build(self):
        self.root = BoxLayout(orientation='vertical')

        # Add a label for status
        self.status_label = Label(text="Welcome to Tic Tac Toe! X's Turn", font_size=24)
        self.root.add_widget(self.status_label)

        # Create the grid layout for the board
        grid = GridLayout(cols=3, spacing=5, size_hint=(1, 0.8))
        for i in range(9):
            btn = Button(text="", font_size=32)  # Empty buttons initially
            btn.bind(on_press=self.on_button_click)
            grid.add_widget(btn)
            self.buttons.append(btn)
        self.root.add_widget(grid)
        
        return self.root

    def on_button_click(self, instance):
        idx = self.buttons.index(instance)
        if self.xState[idx] == 0 and self.zState[idx] == 0:  # Only allow empty cells
            if self.turn == 1:  # X's turn
                instance.text = "X"
                self.xState[idx] = 1
                self.status_label.text = "O's Turn"
            else:  # O's turn
                instance.text = "O"
                self.zState[idx] = 1
                self.status_label.text = "X's Turn"

            winner = checkwin(self.xState, self.zState)
            if winner:
                self.show_popup(f"{winner} wins the game!")
                return
            if self.check_draw():
                self.show_popup("The match is a draw!")
                return

            self.turn = 1 - self.turn  # Toggle turn

    def check_draw(self):
        return all(self.xState[i] or self.zState[i] for i in range(9))

    def show_popup(self, message):
        layout = FloatLayout()
        popup_label = Label(text=message, size_hint=(1, 0.5), pos_hint={"x": 0, "y": 0.3})
        restart_button = Button(text="Restart", size_hint=(0.3, 0.2), pos_hint={"x": 0.35, "y": 0.1})
        layout.add_widget(popup_label)
        layout.add_widget(restart_button)

        popup = Popup(title="Game Over", content=layout, size_hint=(0.6, 0.4), auto_dismiss=False)
        restart_button.bind(on_press=lambda *args: self.reset_game(popup))
        popup.open()

    def reset_game(self, popup):
        popup.dismiss()
        self.xState = [0] * 9
        self.zState = [0] * 9
        self.turn = 1
        self.status_label.text = "Welcome to Tic Tac Toe! X's Turn"
        for btn in self.buttons:
            btn.text = ""
            btn.disabled = False

if __name__ == "__main__":
    TicTacToeApp().run()
