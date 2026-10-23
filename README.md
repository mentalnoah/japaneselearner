# Japanese Learner

A simple python program to help reinforce japanese words and characters.

[![Python](https://img.shields.io/badge/python-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

It aims to let users practice japanese content, and features 2 modes currently (no plans for more at this time), one gives a user the romaji, to let them write down what they think it is then reveal the answer, or the second mode which give the user characters and they can input the romaji. 

It currently uses a simple Tkinter GUI, nothing fancy but does the job.

> [!NOTE]
> The material in the program get updated as I learn the language, there is no guarantee that it will be correct and it will only contain information as i learn it, however the txt documents are there for if you want to add more content or alter current content

> [!IMPORTANT]
> This project was not originally going to be public, as a result, any poorly written code is due to the original plan for the project to be a quick solution to an issue i had that i wasnt going to share

## Features

- **Writing practice**, it gives user romaji and allows the user to write the character and then reveal the answer, it also allows users to press enter to reveal the answer and enter again to press next, allows for quick practice instead of having to move the mouse 
- **Memory practice**, gives the user a character and prompts them to type the romaji, then lets them know if it was correct or not, also features pressing enter to submit and go to the next one easily
- **Session customisation**, allows the user to select a mode, or even have a mix of each and also what things they want to practice (Hiragana, Katakana, etc.)
- **Prevents guessing**, instead of just looping through the list of characters, it has a 20% chance of giving you a character you already answered, this prevents the user from guessing a character based on what they havent done already, and also reinforces the learning
- **Always on top**, allows for the app to remain on the top even when clicked off, this is to allow users who use their device for writing notes, allowing them to use the Writing practice mode with more ease.

## Roadmap
- [x] Hiragana Support
- [ ] Katakana Support
- [ ] Kanji Support
- [ ] Words/Phrases/Concepts support 


## How to run

### Dependencies
This app uses **Python**, makes sure you have Python installed, the latest version should work but this was created for Python 3.13 

This app uses **UD Digi Kyokasho N**, a Japanese font available through Microsoft Windows.

1. Open **Settings → Personalisation → Fonts** and search for `UD Digi Kyokasho N`.
2. If the font is missing, open **Settings → Apps → Optional features**.
3. Select **View features**, search for `Japanese Supplemental Fonts`, and install it.
4. Restart the app.

<br>

For more information, see [Microsoft's official font documentation](https://learn.microsoft.com/en-us/typography/font-list/ud-digi-kyokasho).

If you cannot use this font then in the `main.py` file, under the `App` class you can find a `japaneseFont` class variable, change this to the font you would like to use

### Running the file
Download the files and put them in a folder and run the `main.py` file, make sure you have all the files, like the `groups` folder and the `main.py`
## Authors

- [@mentalnoah](https://www.github.com/mentalnoah)

