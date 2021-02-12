from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Rishav's TIC-TAC-TOE")

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
				configure_buttons([])
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
	if (b1['text'] == b2['text'] == b3['text'] == player):
		configure_buttons([b1, b2, b3])
		flag = 1

	elif (b4['text'] == b5['text'] == b6['text'] == player):
		configure_buttons([b4, b5, b6])
		flag = 1

	elif (b7['text'] == b8['text'] == b9['text'] == player):
		configure_buttons([b7, b8, b9])
		flag = 1

	elif (b1['text'] == b4['text'] == b7['text'] == player):
		configure_buttons([b1, b4, b7])
		flag = 1

	elif (b2['text'] == b5['text'] == b8['text'] == player):
		configure_buttons([b2, b5, b8])
		flag = 1

	elif (b3['text'] == b6['text'] == b9['text'] == player):
		configure_buttons([b3, b6, b9])
		flag = 1

	elif (b1['text'] == b5['text'] == b9['text'] == player):
		configure_buttons([b1, b5, b9])
		flag = 1

	elif (b3['text'] == b5['text'] == b7['text'] == player):
		configure_buttons([b3, b5, b7])
		flag = 1

def configure_buttons(buttons):
	for b in buttons:
		b.config(bg = "lightgreen") # Mark the line where the win has occured

	# Disable all buttons
	b1.config(state = DISABLED)
	b2.config(state = DISABLED)
	b3.config(state = DISABLED)

	b4.config(state = DISABLED)
	b5.config(state = DISABLED)
	b6.config(state = DISABLED)

	b7.config(state = DISABLED)
	b8.config(state = DISABLED)
	b9.config(state = DISABLED)

global player, moves, flag
player = 'X'
moves = flag = 0

# Setting up the buttons and labels
b1 = Button(root, text = " ", height = 5, width = 14, command = lambda: make_move(b1))
b2 = Button(root, text = " ", height = 5, width = 14, command = lambda: make_move(b2))
b3 = Button(root, text = " ", height = 5, width = 14, command = lambda: make_move(b3))

b4 = Button(root, text = " ", height = 5, width = 14, command = lambda: make_move(b4))
b5 = Button(root, text = " ", height = 5, width = 14, command = lambda: make_move(b5))
b6 = Button(root, text = " ", height = 5, width = 14, command = lambda: make_move(b6))

b7 = Button(root, text = " ", height = 5, width = 14, command = lambda: make_move(b7))
b8 = Button(root, text = " ", height = 5, width = 14, command = lambda: make_move(b8))
b9 = Button(root, text = " ", height = 5, width = 14, command = lambda: make_move(b9))

info = Label(root, text = f"Move: {player}")
info.grid(row = 3, column = 0)

info_2 = Label(root, text = "Running...")
info_2.grid(row = 3, column = 2)

b1.grid(row = 0, column = 0)
b2.grid(row = 0, column = 1)
b3.grid(row = 0, column = 2)

b4.grid(row = 1, column = 0)
b5.grid(row = 1, column = 1)
b6.grid(row = 1, column = 2)

b7.grid(row = 2, column = 0)
b8.grid(row = 2, column = 1)
b9.grid(row = 2, column = 2)

root.mainloop()
