# Stone Paper Scissors Game

## Description
The **Stone Paper Scissors** game is a simple yet interactive graphical game built using **Python** and the **Tkinter** library. This game is based on the classic hand game played between two participants, where each player simultaneously forms one of three shapes: **Stone (Rock)**, **Paper**, or **Scissors**. The rules of the game are straightforward:  
- **Stone beats Scissors** (Stone crushes Scissors).  
- **Scissors beats Paper** (Scissors cut Paper).  
- **Paper beats Stone** (Paper covers Stone).  
- If both players choose the same shape, the game results in a **Tie**.  

In this implementation, the player competes against a **bot**, which makes random selections. The game is visually enhanced by displaying images corresponding to each choice. The interface consists of three buttons for player selection and a **Reset** button to restart the game at any time. The score is continuously updated, allowing the player to track their performance against the bot.  

This project provides a simple demonstration of using Python for building **graphical user interfaces (GUIs)** with Tkinter. It is beginner-friendly and serves as a great example of event-driven programming. The game logic is implemented efficiently, and the code structure is easy to follow, making it a useful learning resource for Python programmers.  

Additionally, this game can be customized by modifying the images or adding more features like sound effects or animations. Since Tkinter is a built-in module in Python, no additional installation of external libraries is required, making it highly accessible for users across different platforms.  

## How It Works
- The player selects an option by clicking one of the **Stone**, **Paper**, or **Scissors** buttons.  
- The bot randomly selects one of the three choices.  
- Both selections are displayed with corresponding images.  
- The winner is determined based on the standard game rules.  
- The result is displayed on the screen, indicating whether the player won, lost, or if it was a tie.  
- Scores are updated accordingly.  
- The **Reset** button can be used to reset the game to its initial state.  

## Code Overview
The game is implemented using Python and Tkinter, following an event-driven approach. Below is a breakdown of the key components of the code:  

### **Packages Used**
- **tkinter**: Used for creating the graphical user interface.  
- **random**: Used for generating the bot's random selection.  

### **Key Components**
- **GUI Elements**:  
  - `Tk()` initializes the main game window.  
  - `Label` is used for displaying images and text.  
  - `Button` allows user interaction for selecting a move and resetting the game.  
  - `Frame` helps in structuring the layout of elements inside the window.  

- **Functions**:  
  - `play(choice)`:  
    - Updates the player's selection.  
    - Randomly selects a choice for the bot.  
    - Updates the displayed images.  
    - Compares choices to determine the winner.  
    - Updates the score accordingly.  
  - `reset_game()`:  
    - Resets player and bot scores.  
    - Restores default images.  
    - Clears the result display.  

- **Game Logic**:  
  - The bot’s move is determined using `random.randint(0, 2)`.  
  - The game rules are implemented using conditional statements to compare the player’s choice with the bot’s choice.  
  - Score labels are dynamically updated using the `config()` method.  

## Installation & Running
1. Ensure that **Python** is installed on your system.  
2. Place the required image files (`pst.png`, `pp.png`, `psc.png`, `bst.png`, `bp.png`, `bsc.png`, `default.png`) in the same directory as `main.py`.  
3. Run `main.py`.

## Screenshots
1. **Default window: **We choose between Stone, Paper, Scissors<br>
   ![Image](https://github.com/user-attachments/assets/7c9f1308-4415-43e3-8854-c0ca10a9e264) <br>
2. **Player winning**<br>
   ![Image](https://github.com/user-attachments/assets/0991d803-8367-4a4c-b4b0-e727588fa1c4) <br>
3. **Bot winning**<br>
   ![Image](https://github.com/user-attachments/assets/a41a911f-d070-44b3-afe8-212152b0c6e7) <br>
4. **Tie** <br>
   ![image](https://github.com/user-attachments/assets/10d2a866-c413-4873-9d44-4c7363aae34b)
