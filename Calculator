import tkinter as tk
from tkinter import messagebox

# Function to calculate
def calculate():
    try:
        number1 = float(entry1.get())
        number2 = float(entry2.get())
        operator = operator_var.get()

        if operator == "+":
            result = number1 + number2

        elif operator == "-":
            result = number1 - number2

        elif operator == "*":
            result = number1 * number2

        elif operator == "/":
            if number2 != 0:
                result = number1 / number2
            else:
                messagebox.showerror("Error", "Cannot divide by zero")
                return

        else:
            messagebox.showerror("Error", "Invalid operator")
            return

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")


# Main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x300")
root.config(bg="#1e1e1e")

# Heading
title = tk.Label(
    root,
    text="Simple Calculator",
    font=("Arial", 18, "bold"),
    bg="#1e1e1e",
    fg="white"
)
title.pack(pady=10)

# Number 1
entry1 = tk.Entry(root, font=("Arial", 14))
entry1.pack(pady=10)

# Number 2
entry2 = tk.Entry(root, font=("Arial", 14))
entry2.pack(pady=10)

# Operator selection
operator_var = tk.StringVar()
operator_var.set("+")

operator_menu = tk.OptionMenu(
    root,
    operator_var,
    "+",
    "-",
    "*",
    "/"
)
operator_menu.config(font=("Arial", 12))
operator_menu.pack(pady=10)

# Calculate button
calc_button = tk.Button(
    root,
    text="Calculate",
    font=("Arial", 14, "bold"),
    bg="green",
    fg="white",
    command=calculate
)
calc_button.pack(pady=15)

# Result label
result_label = tk.Label(
    root,
    text="Result:",
    font=("Arial", 16),
    bg="#1e1e1e",
    fg="white"
)
result_label.pack(pady=10)

# Run app
root.mainloop()
