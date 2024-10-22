import tkinter as tk
from random import choice
from tkinter import messagebox


def play(user_choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = choice(options)
    
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    
    messagebox.showinfo("Result", f"You chose: {user_choice}\nComputer chose: {computer_choice}\n\n{result}")


window = tk.Tk()
window.title("Rock, Paper, Scissors")
window.geometry("300x200")


tk.Label(window, text="Choose your option:", font=('Helvetica', 14)).pack(pady=10)

tk.Button(window, text="Rock", width=15, height=2, command=lambda: play("Rock")).pack(pady=5)
tk.Button(window, text="Paper", width=15, height=2, command=lambda: play("Paper")).pack(pady=5)
tk.Button(window, text="Scissors", width=15, height=2, command=lambda: play("Scissors")).pack(pady=5)


window.mainloop()
