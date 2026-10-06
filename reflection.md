# 💭 Reflection: Game Glitch Investigator

## 1. What was broken when you started?

When I first ran the game, the guessing interface loaded successfully and I was able to enter guesses. However, I noticed that some of the game logic did not behave as expected. The hints were backwards; for example, when the secret number was 49 and I guessed 99, the game told me to go higher instead of lower. I also found that after correctly guessing the number, the New Game button did not properly restart the game, and changing the difficulty did not properly start a new playable game.

### Bug Reproduction Log

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Secret = 49, Guess = 99 | The game should report that the guess is too high and tell the player to go lower. | The game displayed the opposite direction and told me to go higher. | No console error. |
| Correctly guess the secret number, then click New Game | A new game should start with a new secret number and reset the game state. | The game did not properly restart after the correct guess. | No console error. |
| Correctly guess the secret number, then change difficulty | The selected difficulty should start a playable game with its appropriate range and attempt limit. | The game did not properly allow me to play the newly selected difficulty. | No console error. |

---

## 2. How did you use AI as a teammate?

I used ChatGPT as an AI coding and debugging teammate during this project. I used it to help interpret the behavior I observed, identify likely causes in the code, plan the refactoring, and design tests for the repaired game logic.

One AI suggestion that was correct was to move the core `check_guess` logic from `app.py` into `logic_utils.py` and correct the reversed Higher/Lower comparisons. The AI explained that when the guess is greater than the secret, the result should be "Too High" and the player should be told to go lower. I reviewed the code and compared the suggested behavior with my manual test where the secret was 49 and the guess was 99. I accepted this suggestion because it made the game logic easier to test separately from the Streamlit interface.

One suggestion I did not accept exactly as written was to reset every piece of game state whenever the difficulty changed, including the score and guess history. I decided that automatically clearing all of that state on a difficulty change could make the behavior less predictable for a user because changing a setting does not necessarily mean the user intended to erase all game information. Instead, I chose to make the difficulty change explicitly start a fresh game and reset the state needed for the new round. I verified my modified approach by changing the difficulty and checking that the new difficulty used the correct range, attempt limit, and a new secret number.

---

## 3. Debugging and testing your fixes

I decided that a bug was fixed only after both automated tests and the live Streamlit application showed the expected behavior. For the Higher/Lower bug, I tested a guess greater than the secret and verified that the result was "Too High" with a "Go LOWER!" message. I also tested a guess lower than the secret and verified that the game returned "Too Low" with a "Go HIGHER!" message.

I added pytest cases for the core game logic. The tests cover a winning guess, a guess that is too high, and a guess that is too low. When I ran pytest, all three tests passed successfully.

The final pytest output was:

```text
============================= test session starts =============================
collected 3 items

tests/test_game_logic.py ...                                           [100%]

============================== 3 passed in 0.01s ===============================
---

## 4. What did you learn about Streamlit and state?

I learned that Streamlit reruns the Python script when a user interacts with widgets such as buttons and inputs. Because the script reruns, normal Python variables do not automatically preserve the state of the game between interactions. Streamlit's `st.session_state` allows values such as the secret number, score, attempts, history, and game status to survive those reruns. I also learned that resetting only one state variable is not always enough because related state variables can leave the application stuck in an old state.

---

## 5. Looking ahead: your developer habits

One habit I want to reuse in future projects is testing a bug before changing the code and then creating a specific automated test for that bug. This makes it easier to determine whether the fix actually solved the original problem instead of simply changing the behavior. I also want to continue using Git commits to save meaningful stages of my work rather than making one large commit at the end.

Next time I work with AI on a coding task, I will review the proposed changes carefully instead of accepting the entire change automatically. I will ask the AI to explain why a change is needed, inspect the diff, and test the result myself.

This project changed the way I think about AI-generated code because AI can identify problems and produce useful fixes, but its suggestions still require human judgment and verification. AI can make a confident suggestion that is over-engineered, incorrect, or unsuitable for the existing codebase, so the developer needs to remain in the loop.