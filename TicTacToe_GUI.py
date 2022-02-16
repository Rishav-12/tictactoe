from tkinter import Tk, Button, Label, NORMAL, DISABLED, messagebox

root = Tk()
root.title("Rishav's TIC-TAC-TOE")

class TicTacToeButton(Button):
	def __init__(self, idx):
		self.idx = idx
		self.button = Button(root, text = " ", height = 5, width = 14, command = lambda: make_move(self.button))

def make_move(b):
	global player, moves, flag

	# If the button is empty, put current token in
	if b['text'] == " ":
		b['text'] = player

		check_win(player)
		if flag == 1: # If any player has won
			info['text'] = "Game Over"
			info_2['text'] = f"{player} wins"
		else:
			moves += 1

			if moves == 9: # If 9 moves have been played, declare a TIE
				info['text'] = "Game Over"
				info_2['text'] = "Tied"
				messagebox.showinfo("TIE", "You tied the game!\nPlay another...")
				# configure_buttons([])
				reset_game()
			else: # If game is not over, just switch the tokens
				if player == 'X':
					player = 'O'
					info['text'] = f"Move: {player}"
				else:
					player = 'X'
					info['text'] = f"Move: {player}"

def check_win(player):
	global flag

	# Various conditions for a win to occur
	win_conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
	for c in win_conditions:
		x, y, z = c
		if (list_buttons[x].button['text'] == list_buttons[y].button['text'] == list_buttons[z].button['text'] == player):
			configure_buttons([list_buttons[x].button, list_buttons[y].button, list_buttons[z].button])
			flag = 1
			break

def configure_buttons(buttons):
	for b in buttons:
		b.config(bg = "lightgreen") # Mark the line where the win has occured

	# Disable all buttons
	for button in list_buttons:
		button.button.config(state = DISABLED)

def reset_game():
	global player, moves, flag
	for button in list_buttons:
		button.button['text'] = " "
		button.button.config(state = NORMAL, bg = btn_default_color)
	player = 'X'
	moves = 0
	flag = 0
	info['text'] = f"Move: {player}"
	info_2['text'] = "Running..."

global player, moves, flag
player = 'X'
moves = flag = 0

# Setting up the buttons and labels
list_buttons = []
for i in range(1, 10):
	button = TicTacToeButton(idx = i)
	if 1 <= i <= 3:
		row = 0
	if 4 <= i <= 6:
		row = 1
	if 7 <= i <= 9:
		row = 2
	if i == 1 or i == 4 or i == 7:
		column = 0
	if i == 2 or i == 5 or i == 8:
		column = 1
	if i == 3 or i == 6 or i == 9:
		column = 2

	list_buttons.append(button)
	button.button.grid(row = row, column = column)

info = Label(root, text = f"Move: {player}")
info.grid(row = 3, column = 0)

info_2 = Label(root, text = "Running...")
info_2.grid(row = 3, column = 2)

reset_btn = Button(root, text = "Reset Game", height = 2, width = 12, command = reset_game)
reset_btn.grid(row = 4)
btn_default_color = reset_btn.cget("background")

root.mainloop()
