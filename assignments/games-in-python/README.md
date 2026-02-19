```markdown
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a playable command-line Hangman game using Python to practice string manipulation, control flow, and user input handling. The finished program should be clear, robust to invalid input, and provide a friendly play experience.

## 📝 Tasks

### 🛠️ Implement the core Hangman game

#### Description
Use the provided starter code at [assignments/games-in-python/starter-code.py](assignments/games-in-python/starter-code.py) as a base. Implement the game loop so a player can guess letters, see progress, and win or lose based on a limited number of incorrect attempts.

#### Requirements
Completed program should:

- Randomly select a secret word from a built-in list.
- Display the secret word as underscores for unknown letters (e.g. `_ _ a _ _`).
- Accept single-letter guesses (case-insensitive) and reveal correct letters.
- Track and display letters already guessed.
- Track remaining incorrect attempts and end the game when attempts reach zero.
- Show a clear win or lose message with the full secret word.
- Ignore repeated guesses (they should not deduct attempts).
- Validate input and only accept single alphabetic characters.


### 🛠️ Add enhancements (optional)

#### Description
Add extra features to improve playability and demonstrate deeper Python skills.

#### Requirements
Completed enhancements may include any of the following:

- Difficulty levels affecting allowed attempts or word length.
- Load words from an external `words.txt` file if present, otherwise fall back to the built-in list.
- ASCII-art hangman stages that progress on incorrect guesses.
- Allow the player to attempt a full-word guess.
- Persist a simple high-score or stats file tracking wins/losses.

## Files

- Starter code: [assignments/games-in-python/starter-code.py](assignments/games-in-python/starter-code.py)

## How to run

Run the game with Python 3 from the assignment folder:

```bash
python3 assignments/games-in-python/starter-code.py
```

## Submission

When you're done, submit your modified `starter-code.py` (and any additional files) following course instructions.

```
