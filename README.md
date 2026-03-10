# 🎮 Hangman Game (Python)

A terminal-based Hangman game written in Python with multiple categories, difficulty modes, and descriptive hints.

## How to Play

Make sure you have **Python 3.10+** installed (the game uses `match/case`).

```bash
python game.py
```

## Features

- **4 Word Categories:**
  - `1` — Animals (wildlife from around the world)
  - `2` — World Places (countries & cities)
  - `3` — India (Indian cities & states)
  - `5` — General Words (vocabulary challenge)

- **2 Difficulty Modes:**
  - `1` — Normal: hint/description shown *after* the game ends
  - `2` — Easy: hint/description shown *before* you start guessing

- **5 lives** per game
- Duplicate guess detection
- Win/loss detection with the answer revealed on loss

## Project Structure

```
hangman/
├── game.py              # Main game logic
├── input1_game.txt      # Word list: Animals
├── input2_game.txt      # Word list: World Places
├── input3_game.txt      # Word list: India
├── input4_game.txt      # Word list: (reserved)
├── input5_game.txt      # Word list: General Words
├── description1.txt     # Hints: Animals
├── description2.txt     # Hints: World Places
├── description3.txt     # Hints: India
├── description4.txt     # Hints: (reserved)
├── description5.txt     # Hints: General Words
└── README.md
```

## Requirements

- Python 3.10 or higher (for `match/case` syntax)
- No external libraries needed

## Example Gameplay

```
Enter
 1 for "Animals"
 2 for "places:both countries and cities"
 3 for places in INDIA
 5 or any other number for general play

> 1

Enter 1 for normal play; with hints,
Enter 2 for easy play
> 1

_ _ _ _ _ _

Enter guess
> a
_ a _ _ _ _
Number of lifelines left  5

Enter guess
> e
_ a _ _ e _
...
```
