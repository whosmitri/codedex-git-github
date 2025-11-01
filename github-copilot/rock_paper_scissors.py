"""Rock Paper Scissors

This file contains a small CLI implementation and a simple Tkinter GUI.
Run the script to open the GUI. The CLI logic is preserved in functions
and can be used programmatically or invoked separately.
"""

import random
import tkinter as tk
from tkinter import messagebox


def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def determine_winner(player, computer):
    """Return 'player', 'computer', or 'tie'. Inputs are expected lowercase."""
    if player == computer:
        return 'tie'
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        return 'player'
    else:
        return 'computer'


def run_cli():
    player_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play, or 'quit' to exit.")

    while True:
        player_choice = input("Your choice: ").strip().lower()
        if player_choice == 'quit':
            print("Thanks for playing!")
            break
        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(player_choice, computer_choice)
        if winner == 'player':
            player_score += 1
            print("You win this round!")
        elif winner == 'computer':
            computer_score += 1
            print("Computer wins this round!")
        else:
            print("It's a tie!")

        print(f"Score - You: {player_score}, Computer: {computer_score}")


class RPSGui:
    def __init__(self, root):
        self.root = root
        root.title("Rock Paper Scissors")
        root.resizable(False, False)

        self.player_score = 0
        self.computer_score = 0

        # Labels
        self.score_label = tk.Label(root, text=self._score_text(), font=(None, 12))
        self.score_label.pack(padx=10, pady=(10, 5))

        self.result_label = tk.Label(root, text="Make your move", font=(None, 11))
        self.result_label.pack(padx=10, pady=5)

        self.computer_label = tk.Label(root, text="Computer: -", font=(None, 10))
        self.computer_label.pack(padx=10, pady=(0, 10))

        # Buttons frame
        btn_frame = tk.Frame(root)
        btn_frame.pack(padx=10, pady=(0, 10))

        rock_btn = tk.Button(btn_frame, text="Rock", width=10, command=lambda: self.play('rock'))
        rock_btn.grid(row=0, column=0, padx=5)

        paper_btn = tk.Button(btn_frame, text="Paper", width=10, command=lambda: self.play('paper'))
        paper_btn.grid(row=0, column=1, padx=5)

        scissors_btn = tk.Button(btn_frame, text="Scissors", width=10, command=lambda: self.play('scissors'))
        scissors_btn.grid(row=0, column=2, padx=5)

        # Control buttons
        ctrl_frame = tk.Frame(root)
        ctrl_frame.pack(padx=10, pady=(0, 10))

        reset_btn = tk.Button(ctrl_frame, text="Reset", command=self.reset_scores)
        reset_btn.grid(row=0, column=0, padx=5)

        quit_btn = tk.Button(ctrl_frame, text="Quit", command=root.quit)
        quit_btn.grid(row=0, column=1, padx=5)

    def _score_text(self):
        return f"Score — You: {self.player_score}  Computer: {self.computer_score}"

    def play(self, player_move):
        computer_move = get_computer_choice()
        winner = determine_winner(player_move, computer_move)

        if winner == 'player':
            self.player_score += 1
            result_text = "You win this round!"
        elif winner == 'computer':
            self.computer_score += 1
            result_text = "Computer wins this round!"
        else:
            result_text = "It's a tie!"

        self.score_label.config(text=self._score_text())
        self.result_label.config(text=result_text)
        self.computer_label.config(text=f"Computer: {computer_move}")

    def reset_scores(self):
        self.player_score = 0
        self.computer_score = 0
        self.score_label.config(text=self._score_text())
        self.result_label.config(text="Make your move")
        self.computer_label.config(text="Computer: -")


def run_gui():
    root = tk.Tk()
    app = RPSGui(root)
    root.mainloop()


if __name__ == "__main__":
    # Start the GUI by default. To use the CLI instead, call run_cli().
    try:
        run_gui()
    except Exception as e:
        # If GUI fails for any reason, fallback to CLI so the game remains usable.
        print("GUI failed to start, falling back to CLI. Error:", e)
        run_cli()
