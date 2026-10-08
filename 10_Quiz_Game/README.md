# 📝 Quiz Game

A **console-based Quiz Game** built with Python where players answer randomly selected **True/False** questions. The game keeps track of the player's score, prevents duplicate questions, and displays the final result after all questions have been answered.

![Python](https://img.shields.io/badge/Python-3776AB?style=plastic&logo=python&logoColor=white) ![Console Application](https://img.shields.io/badge/Console-Application-blue?style=plastic) ![Object Oriented Programming](https://img.shields.io/badge/Object%20Oriented-Programming-success?style=plastic) ![Intermediate Project](https://img.shields.io/badge/Level-Intermediate-orange?style=plastic)

---

# 📖 Project Overview

This project was developed to practice **Object-Oriented Programming (OOP)** and working with structured data in Python.

The game randomly selects questions from a predefined question bank, validates user answers, updates the score, and ensures each question is asked only once.

---

# ✨ Features

- 📝 True/False quiz game
- 🎲 Random question selection
- 🚫 No repeated questions
- 🏆 Live score tracking
- 📚 Question bank using a list of dictionaries
- 🏗️ Object-Oriented Programming (OOP)
- 🎨 Custom ASCII game logo
- 📦 Modular project structure
- 💻 Interactive console interface

---

# 🎮 Gameplay

1. Start the Quiz Game.
2. Answer each True/False question.
3. The game checks your answer immediately.
4. Your current score is displayed after every question.
5. Questions never repeat during a game session.
6. After all questions have been answered, your final score is displayed.

---

# 📂 Project Structure

```text
10_Quiz_Game/
│
├── README.md
├── Quiz_Game.py
├── quiz_art.py
└── Screenshot/
    ├── 1.png
    └── 2.png
```

---

# 🛠️ Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Random Module
- Lists
- Dictionaries
- Classes & Objects
- Functions
- Loops
- Conditional Statements
- Console Input/Output

---

# 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/Harsh-Belekar/Python-Projects.git
```

### Navigate to the project folder

```bash
cd Python-Projects/10_Quiz_Game
```

### Run the program

```bash
python Quiz_Game.py
```

---

# 📸 Screenshots

## Game Start

![Game Start](Screenshot/1.png)

---

## Final Result

![Final Score](Screenshot/2.png)

---

# 🧠 Python Concepts Practiced

- Variables
- Classes & Objects
- Object-Oriented Programming
- Lists
- Dictionaries
- Functions
- Loops
- Conditional Statements
- Random Module
- Score Tracking
- State Management
- Modular Programming

---

# 📚 Files Description

## `Quiz_Game.py`

Contains the complete quiz game logic including:

- Quiz class implementation
- Random question selection
- Score management
- Answer validation
- Duplicate question prevention
- Final score calculation

---

## `quiz_art.py`

Contains all reusable project assets including:

- ASCII game logo
- Question bank
- Correct answers
- Question numbering

Separating the quiz data from the game logic keeps the application clean, modular, and easier to maintain.

---

# 📋 Quiz Workflow

```text
Start Game
     │
     ▼
Load Question Bank
     │
     ▼
Randomly Select Question
     │
     ▼
Already Asked?
     │
 ┌── Yes ───────────────┐
 │                      │
 ▼                      │
Choose Another          │
 │                      │
 └──────────────┬───────┘
                ▼
Display Question
        │
        ▼
Get User Answer
        │
        ▼
Check Answer
        │
        ▼
Update Score
        │
        ▼
Questions Remaining?
        │
   Yes ─┴─ No
    │       │
    ▼       ▼
Next Q   Final Score
```

---

# 🏆 Scoring System

- ✅ Correct Answer → +1 Point
- ❌ Incorrect Answer → No Point
- 📊 Current score is displayed after every question.
- 🎯 Final score is shown after all questions have been completed.

---

# 📊 Question Bank

Each quiz question is stored as a dictionary containing:

- Question Number
- Question Text
- Correct Answer

This structured format makes it easy to add, edit, or remove questions.

---

# 🔮 Future Improvements

Possible enhancements for future versions:

- 📂 Load questions from a JSON file
- 🌐 Online trivia API integration
- 🎚️ Multiple difficulty levels
- ⏱️ Timer for each question
- 🏅 High score leaderboard
- 📈 Performance statistics
- 🧠 Multiple-choice questions
- 🎵 Sound effects
- 🖥️ GUI version using Tkinter
- 🎮 Pygame version

---

# 🎯 Learning Outcomes

Through this project, I learned how to:

- Build applications using Object-Oriented Programming
- Work with lists of dictionaries
- Randomly select structured data
- Prevent duplicate data selection
- Track application state
- Build reusable classes and methods
- Create interactive quiz applications

---

# 📂 More Projects

This project is part of my **Python Projects Portfolio**, a collection of Python projects covering:

- 🎮 Games
- 🖥️ GUI Applications
- 🤖 Automation
- 🌐 API Integrations
- 📊 Data Processing
- 🧩 Python Fundamentals

*Explore the repository to discover more projects and follow my Python learning journey.*

***⭐ If you like this project, don't forget to star the repository!***