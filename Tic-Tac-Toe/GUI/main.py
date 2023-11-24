# ------------------------------------------------------------------.
# Importing Libraries.
# ------------------------------------------------------------------.

import numpy as np

from tkinter import *

# ------------------------------------------------------------------.
# Setting the constants and colors. 
# ------------------------------------------------------------------.

size_of_board = 600
symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
symbol_thickness = 30
symbol_X_color = '#EE4035'
symbol_O_color = '#0492CF'
Green_color = '#7BC043'


# ------------------------------------------------------------------.
# Tic-Tac-Toe class initialization.  
# ------------------------------------------------------------------.

class Tic_Tac_Toe():

    # ------------------------------------------------------------------.
    # Initialization Functions:
    # ------------------------------------------------------------------.

    def __init__(self):
        self.window = Tk()
        self.window.title('Tic-Tac-Toe')

        # Set window size and position.
        window_width = size_of_board
        window_height = size_of_board

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.window.geometry(f'{window_width}x{window_height}+{x}+{y}')

        self.canvas = Canvas(self.window, width=size_of_board, height=size_of_board)
        self.canvas.pack()

        self.player1_name = ""
        self.player2_name = ""

        # Call a function to get player names and symbols.
        self.get_player_info()

        self.initialize_board()

        self.player_X_turns = True
        self.board_status = np.zeros(shape=(3, 3))

        self.player_X_starts = True
        self.reset_board = False

        self.gameover = False
        self.tie = False

        self.X_wins = False
        self.O_wins = False

        self.player1_score = 0
        self.player2_score = 0
        self.tie_score = 0


    def mainloop(self):
        self.window.mainloop()

    def enable_canvas_click_event(self, enabled=True):
        if enabled:
            self.window.bind('<Button-1>', self.click)
        else:
            self.window.unbind('<Button-1>')


    # Getting the players info and options to play. 
    def get_player_info(self): 
        self.current_frame = Frame(self.window)
        self.current_frame.pack()

        label1 = Label(self.current_frame, text="Enter Player 1's name:", font=("Helvetica", 12))

        label2 = Label(self.current_frame, text="Enter Player 2's name:", font=("Helvetica", 12))

        label1.pack()

        entry1 = Entry(self.current_frame, font=("Helvetica", 12))
        entry1.pack()

        label2.pack()

        entry2 = Entry(self.current_frame, font=("Helvetica", 12))
        entry2.pack()

        continue_button = Button(self.current_frame, text="Continue", command=lambda: self.set_player_names(entry1.get(), entry2.get()), font=("Helvetica", 12))
        continue_button.pack()

        # # Disabling canvas click event while the dialog boxes are open.
        # self.enable_canvas_click_event(False)


    def set_player_names(self, name1, name2):
        self.player1_name = name1
        self.player2_name = name2

        # Destroy the input frame.
        self.current_frame.destroy()  

        # Call initialize_board directly.
        self.initialize_board()

        # Reenabling canvas click event after dialog boxes are closed.
        self.enable_canvas_click_event(True)


    def initialize_board(self): 
        for i in range(2):
            x = (i + 1) * size_of_board / 3
            y = (i + 1) * size_of_board / 3

            self.canvas.create_line(x, 0, x, size_of_board)
            self.canvas.create_line(0, y, size_of_board, y)

        # Center the canvas in the window
        self.canvas.place(relx=0.5, rely=0.5, anchor=CENTER)


    def play_again(self):
        self.initialize_board()

        self.player_X_starts = not self.player_X_starts
        self.player_X_turns = self.player_X_starts

        self.board_status = np.zeros(shape=(3, 3))

        # Reset the reset_board flag to allow new moves.
        self.reset_board = False

        # Reinitialize the board to clear any drawings.
        self.initialize_board()

        # Enable canvas click event for the new game.
        self.enable_canvas_click_event(True)


    def restart_game(self, event):
        if self.reset_board:
            self.canvas.delete("all")
            self.play_again()
            self.reset_board = False

    # ------------------------------------------------------------------.
    # Canvas Rendering Functions:
    # Functions responsible for rendering game elements on the canvas.
    # ------------------------------------------------------------------.


    def draw_O(self, logical_position):
        logical_position = np.array(logical_position)
        grid_position = self.convert_logical_to_grid_position(logical_position)

        self.canvas.create_oval(
            grid_position[0] - symbol_size, 
            grid_position[1] - symbol_size, 
            grid_position[0] + symbol_size, 
            grid_position[1] + symbol_size, 
            width=symbol_thickness,
            outline=symbol_O_color)

    def draw_X(self, logical_position):
        grid_position = self.convert_logical_to_grid_position(logical_position)

        self.canvas.create_line(
            grid_position[0] - symbol_size, 
            grid_position[1] - symbol_size,
            grid_position[0] + symbol_size, 
            grid_position[1] + symbol_size, 
            width=symbol_thickness,
            fill=symbol_X_color)
        
        self.canvas.create_line(
            grid_position[0] - symbol_size, 
            grid_position[1] + symbol_size,
            grid_position[0] + symbol_size, 
            grid_position[1] - symbol_size, 
            width=symbol_thickness,
            fill=symbol_X_color)



    def display_gameover(self):
        winner_name = self.player1_name if self.X_wins else (self.player2_name if self.O_wins else "Tie")

        winner_text = "Result : " + winner_name + " wins \n"

        color = symbol_X_color if self.X_wins else (symbol_O_color if self.O_wins else 'gray')
        
        self.canvas.delete("all")
        self.canvas.create_text(size_of_board / 2, size_of_board / 3, font=("Helvetica", 40, "bold"), fill=color, text=winner_text)
    
        
        # Display Scores Tab.
        label_color = '#444444'

        self.canvas.create_text(
            size_of_board / 2, 
            size_of_board / 2 - 60, 
            font=("Helvetica", 24, "bold"), 
            fill=label_color, 
            text="\nScores Tab : \n")

        self.canvas.create_text(
            size_of_board / 2, 
            size_of_board / 2 - 20, 
            font=("Helvetica", 20, "bold"), 
            fill=Green_color, 
            text=f"{self.player1_name} (X) : {self.player1_score}")

        self.canvas.create_text(
            size_of_board / 2, 
            size_of_board / 2 + 20, 
            font=("Helvetica", 20, "bold"), 
            fill=Green_color, 
            text=f"{self.player2_name} (O): {self.player2_score}")

        self.canvas.create_text(
            size_of_board / 2, 
            size_of_board / 2 + 60, 
            font=("Helvetica", 20, "bold"), 
            fill=Green_color, 
            text=f"Tie : {self.tie_score}")
        
        self.reset_board = True

        score_text = 'Click to play again'
        
        self.canvas.create_text(
            size_of_board / 2, 
            15 * size_of_board / 16, 
            font=("Helvetica", 20, "bold"), 
            fill="gray", 
            text=score_text)

        # Bind the canvas click event to the restart_game method.
        self.canvas.bind("<Button-1>", self.restart_game)


    # ------------------------------------------------------------------.
    # Logical Functions:
    # The modules required to carry out game logic
    # ------------------------------------------------------------------.


    def convert_logical_to_grid_position(self, logical_position):
        logical_position = np.array(logical_position, dtype=int)
        return (size_of_board / 3) * logical_position + size_of_board / 6

    def convert_grid_to_logical_position(self, grid_position):
        grid_position = np.array(grid_position)
        return np.array(grid_position // (size_of_board / 3), dtype=int)

    def is_grid_occupied(self, logical_position):
        if self.board_status[logical_position[0]][logical_position[1]] == 0:
            return False
        else:
            return True


    def is_winner(self, player):
        player = -1 if player == 'X' else 1

        # Three in a row.
        for i in range(3):
            if self.board_status[i][0] == self.board_status[i][1] == self.board_status[i][2] == player:
                return True
            
            if self.board_status[0][i] == self.board_status[1][i] == self.board_status[2][i] == player:
                return True

        # Diagonals
        if self.board_status[0][0] == self.board_status[1][1] == self.board_status[2][2] == player:
            return True

        if self.board_status[0][2] == self.board_status[1][1] == self.board_status[2][0] == player:
            return True

        return False


    def is_tie(self):
        r, c = np.where(self.board_status == 0)
        tie = False
        if len(r) == 0:
            tie = True

        return tie


    def is_gameover(self):
        # Either someone wins or all grid occupied
        self.X_wins = self.is_winner('X')
        if not self.X_wins:
            self.O_wins = self.is_winner('O')

        if self.X_wins:
            self.player1_score += 1 

        elif self.O_wins:
            self.player2_score += 1

        else:
            self.tie = self.is_tie()
            if self.tie:
                self.tie_score += 1

        # game declared over only after a conclusive result.
        gameover = self.X_wins or self.O_wins or self.tie

        if self.X_wins:
            print('X wins.')
        if self.O_wins:
            print('O wins.')
        if self.tie:
            print('Its a tie.')

        return gameover


    def click(self, event):
        # Check if the game is over or player names are not entered
        if self.gameover or not self.player1_name or not self.player2_name:
            return

        grid_position = [event.x, event.y]
        logical_position = self.convert_grid_to_logical_position(grid_position)

        if self.player_X_turns:
            if not self.is_grid_occupied(logical_position):
                self.draw_X(logical_position)
                self.board_status[logical_position[0]][logical_position[1]] = -1
                self.player_X_turns = not self.player_X_turns

        else:
            if not self.is_grid_occupied(logical_position):
                self.draw_O(logical_position)
                self.board_status[logical_position[0]][logical_position[1]] = 1
                self.player_X_turns = not self.player_X_turns

        # Check if the game is over
        if self.is_gameover():
            self.display_gameover()

        # If the board is not fully occupied, it's not a tie yet, so continue playing.
        elif np.count_nonzero(self.board_status) < 9:
            pass

        else:
            # If the board is fully occupied and there's no winner, it's a tie.
            self.tie = True
            self.display_gameover()

# ------------------------------------------------------------------.

if __name__ == "__main__":
    game_instance = Tic_Tac_Toe()
    game_instance.mainloop()
