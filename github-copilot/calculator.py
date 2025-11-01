import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.expression = ""

        # Display area
        self.display = tk.Entry(root, font=("Arial", 20), borderwidth=2, relief="groove", justify='right')
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '.', '+',
            '='
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            tk.Button(root, text=button, width=5, height=2, font=("Arial", 18), command=action).grid(row=row_val, column=col_val, sticky="nsew")
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Configure grid weights for responsiveness
        for i in range(5):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.update_display()
        elif char == '=':
            try:
                result = str(eval(self.expression))
                self.expression = result
                self.update_display()
            except ZeroDivisionError:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                self.expression = ""
                self.update_display()
            except Exception as e:
                messagebox.showerror("Error", "Invalid input.")
                self.expression = ""
                self.update_display()
        else:
            self.expression += str(char)
            self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
