# 📧 Mail Merge

A simple **Mail Merge** project built using **Python File Handling**. This program automatically generates personalized letters by replacing a placeholder with names from a text file and creating a separate letter for each recipient.

![Python](https://img.shields.io/badge/Python-3776AB?style=plastic\&logo=python\&logoColor=white) ![File Handling](https://img.shields.io/badge/File_Handling-4CAF50?style=plastic) ![String Manipulation](https://img.shields.io/badge/String_Manipulation-FF9800?style=plastic) ![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=plastic\&logo=visualstudiocode\&logoColor=white) ![Git](https://img.shields.io/badge/Git-F05032?style=plastic\&logo=git\&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-181717?style=plastic\&logo=github\&logoColor=white)

---

## 📸 Screenshots

### Mail Files Generated

![Mail Created](Screenshot/1.png)

### Generated Mail

![Mail 1](Screenshot/2.png)

### Generated Mail

![Mail 2](Screenshot/3.png)

---

## ✨ Features

* 📄 Reads recipient names from a text file
* 📝 Uses a predefined letter template
* 🔄 Replaces placeholders with recipient names
* 📧 Automatically generates personalized letters
* 💾 Saves each letter as a separate text file
* 📂 Demonstrates Python file handling
* ⚡ Simple and efficient implementation

---

## 📂 Project Structure

```text
16_Mail_Merge/
│
├── Assets/
│   ├── main_mail.txt
│   ├── names.txt
│   ├── mail of Vaibhav.txt
│   ├── mail of Kunal.txt
│   ├── mail of Dhiraj.txt
│   ├── mail of Bunti.txt
│   └── mail of Meet.txt
│
├── Mail_Merge.py
│
├── Screenshot/
│   ├── 1.png
│   ├── 2.png
│   └── 3.png
│
└── README.md
```

---

## 🛠️ Technologies Used

* Python 3
* File Handling
* String Manipulation

---

## 🚀 How to Run

1. Clone this repository

```bash
git clone https://github.com/Harsh-Belekar/Python-Projects.git
```

2. Navigate to the project folder

```bash
cd Python-Projects/16_Mail_Merge
```

3. Run the program

```bash
python Mail_Merge.py
```

---

## ⚙️ How It Works

1. Reads all recipient names from `names.txt`.
2. Reads the email template from `main_mail.txt`.
3. Searches for the placeholder:

```text
[name]
```

4. Replaces the placeholder with each recipient's name.
5. Creates a new personalized text file for every recipient.

Example:

**Template**

```text
Dear [name],

You are Invited to my Birthday this Saturday.

Hope you Come.

Harsh
```

Generated Letter:

```text
Dear Vaibhav,

You are Invited to my Birthday this Saturday.

Hope you Come.

Harsh
```

---

## 📂 Source Files

### `Mail_Merge.py`

Main program responsible for generating personalized letters.

Features:

* Reads recipient names
* Reads the mail template
* Replaces placeholders
* Creates personalized text files
* Saves generated letters automatically

---

### `main_mail.txt`

Contains the template letter with a placeholder.

Example:

```text
Dear [name],

You are Invited to my Birthday this Saturday.

Hope you Come.

Harsh
```

---

### `names.txt`

Contains the list of recipients.

Example:

```text
Vaibhav
Kunal
Dhiraj
Bunti
Meet
```

---

## 📚 Concepts Practiced

* File Handling
* Reading Text Files
* Writing Text Files
* Context Managers (`with open`)
* String Manipulation
* String Replacement
* Loops
* Variables
* Automation
* Basic Python Scripting

---

## 🎓 Learning Outcomes

Through this project, I learned:

* Reading and writing files in Python
* Automating repetitive tasks
* Working with multiple text files
* Using string replacement for personalization
* Organizing project assets
* Building simple automation scripts

---

# 📂 More Projects

This project is part of my **Python Projects Portfolio**, a collection of Python projects covering:

- 🎮 Games
- 🎨 Graphics Programming
- 🖥️ GUI Applications
- 🤖 Automation
- 🌐 API Integrations
- 📊 Data Processing
- 🧩 Python Fundamentals

*Explore the repository to discover more projects and follow my Python learning journey.*

***⭐ If you like this project, don't forget to star the repository!***