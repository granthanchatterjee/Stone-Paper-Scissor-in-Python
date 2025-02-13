import tkinter as tk
import random

root = tk.Tk()
root.title("Stone Paper Scissors")

player_choice = ["pst.png", "pp.png", "psc.png"]
bot_choice = ["bst.png", "bp.png", "bsc.png"]
player_images = [tk.PhotoImage(file=img) for img in player_choice]
computer_images = [tk.PhotoImage(file=img) for img in bot_choice]

player_score = 0
computer_score = 0


def play(choice):
    global player_score, computer_score

    player_index = choice
    player_image_label.config(image=player_images[player_index])

    computer_index = random.randint(0, 2)
    computer_image_label.config(image=computer_images[computer_index])

    if player_index == computer_index:
        result_label.config(text="Tie!")
    elif (player_index == 0 and computer_index == 2) or \
            (player_index == 1 and computer_index == 0) or \
            (player_index == 2 and computer_index == 1):
        player_score += 1
        result_label.config(text="You Win!")
    else:
        computer_score += 1
        result_label.config(text="Bot Wins!")

    player_score_label.config(text=f"Player: {player_score}")
    computer_score_label.config(text=f"Bot: {computer_score}")


def reset_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    player_score_label.config(text=f"Player: {player_score}")
    computer_score_label.config(text=f"Bot: {computer_score}")
    player_image_label.config(image=default_image)
    computer_image_label.config(image=default_image)
    result_label.config(text="")


frame = tk.Frame(root)
frame.pack(pady=20)

player_label = tk.Label(frame, text="Player")
player_label.grid(row=0, column=0)

computer_label = tk.Label(frame, text="Bot")
computer_label.grid(row=0, column=2)

default_image = tk.PhotoImage(file="default.png")
player_image_label = tk.Label(frame, image=default_image)
player_image_label.grid(row=1, column=0)

vs_label = tk.Label(frame, text="VS")
vs_label.grid(row=1, column=1)

computer_image_label = tk.Label(frame, image=default_image)
computer_image_label.grid(row=1, column=2)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

score_frame = tk.Frame(root)
score_frame.pack(pady=10)

player_score_label = tk.Label(score_frame, text=f"Player: {player_score}")
player_score_label.grid(row=0, column=0)

computer_score_label = tk.Label(score_frame, text=f"Bot: {computer_score}")
computer_score_label.grid(row=0, column=1)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

stone_button = tk.Button(button_frame, text="Stone", command=lambda: play(0))
stone_button.grid(row=0, column=0)

paper_button = tk.Button(button_frame, text="Paper", command=lambda: play(1))
paper_button.grid(row=0, column=1)

scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: play(2))
scissors_button.grid(row=0, column=2)

reset_button = tk.Button(root, text="Reset", command=reset_game)
reset_button.pack(pady=10)

root.mainloop()