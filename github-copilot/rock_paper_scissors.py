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
    ties = 0
    rounds = []  # list of tuples: (round_no, player_choice, computer_choice, result)

    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play, or 'quit' to exit.")

    round_no = 0
    while True:
        player_choice = input("Your choice: ").strip().lower()
        if player_choice == 'quit':
            print("Thanks for playing!")
            break
        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue

        round_no += 1
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(player_choice, computer_choice)
        if winner == 'player':
            player_score += 1
            result_text = "You win this round!"
        elif winner == 'computer':
            computer_score += 1
            result_text = "Computer wins this round!"
        else:
            ties += 1
            result_text = "It's a tie!"

        rounds.append((round_no, player_choice, computer_choice, winner))

        print(result_text)
        print(f"Score - You: {player_score}, Computer: {computer_score}, Ties: {ties}")

        # Print a concise per-round scoreboard (last 10 rounds to avoid flooding)
        print("Recent rounds:")
        for rn, p, c, w in rounds[-10:]:
            if w == 'player':
                res = 'You'
            elif w == 'computer':
                res = 'Computer'
            else:
                res = 'Tie'
            print(f"  Round {rn}: You ({p}) vs Computer ({c}) — {res}")


class RPSGui:
    def __init__(self, root):
        self.root = root
        root.title("Rock Paper Scissors")
        root.resizable(False, False)

        # Track detailed scoreboard
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0
        self.rounds = []  # list of tuples: (round_no, player_move, computer_move, result)
        self.round_no = 0

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

        # Detailed scoreboard (history)
        board_frame = tk.Frame(root)
        board_frame.pack(padx=10, pady=(0, 10), fill='both', expand=False)

        board_label = tk.Label(board_frame, text="Round History (most recent at bottom):", font=(None, 10))
        board_label.pack(anchor='w')

        self.history_listbox = tk.Listbox(board_frame, width=60, height=8)
        self.history_listbox.pack(side='left', fill='both', expand=True, pady=(4,0))

        scrollbar = tk.Scrollbar(board_frame, orient='vertical', command=self.history_listbox.yview)
        scrollbar.pack(side='right', fill='y')
        self.history_listbox.config(yscrollcommand=scrollbar.set)

    def _score_text(self):
        return f"Score — You: {self.player_score}  Computer: {self.computer_score}  Ties: {self.ties}"

    def play(self, player_move):
        computer_move = get_computer_choice()
        winner = determine_winner(player_move, computer_move)

        self.round_no += 1
        if winner == 'player':
            self.player_score += 1
            result_text = "You win this round!"
        elif winner == 'computer':
            self.computer_score += 1
            result_text = "Computer wins this round!"
        else:
            self.ties += 1
            result_text = "It's a tie!"

        # Record round
        self.rounds.append((self.round_no, player_move, computer_move, winner))
        # Update UI
        self.score_label.config(text=self._score_text())
        self.result_label.config(text=result_text)
        self.computer_label.config(text=f"Computer: {computer_move}")

        # Append a readable entry to the history listbox
        if winner == 'player':
            res_text = "You"
        elif winner == 'computer':
            res_text = "Computer"
        else:
            res_text = "Tie"

        entry = f"Round {self.round_no}: You ({player_move}) vs Computer ({computer_move}) — {res_text}"
        self.history_listbox.insert('end', entry)
        # keep the latest visible
        self.history_listbox.see('end')

    def reset_scores(self):
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0
        self.rounds.clear()
        self.round_no = 0
        self.score_label.config(text=self._score_text())
        self.result_label.config(text="Make your move")
        self.computer_label.config(text="Computer: -")
        self.history_listbox.delete(0, 'end')


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
