<a name="top"></a>
# 21-Day Python Challenge

Welcome to the 21-Day Python Challenge! This project is designed to help you master Python programming in just three weeks. Each day, you will explore new concepts, complete practical exercises, and strengthen your coding skills.

## Table of Contents

- [📖 Introduction](#-introduction)
- [🚀 Getting Started](#-getting-started)
- [📅 Daily Structure](#-daily-structure)
- [💪 Challenges](#-challenges)
- [🧪 Unit Tests](#-unit-tests)

## 📖 Introduction
[🔝 Back to Top](#top)

The 21-Day Python Challenge is an intensive program aimed at beginners who want to learn Python programming from the ground up. Whether you're a complete novice or have some coding experience, this challenge will guide you through a structured curriculum to build a solid foundation in Python.

## 🚀 Getting Started
[🔝 Back to Top](#top)

To get started with the challenge, follow these steps:

1. Clone this repository to your local machine.
2. Make sure you have Python installed (version X.X recommended).
3. Open your terminal and navigate to the project directory.
4. Execute the daily exercises for the next 21 days.

## 📅 Daily Structure
[🔝 Back to Top](#top)

Each day of the challenge follows this structure:

1. **Concept Exploration**: Learn a new Python concept through interactive examples.
2. **Practical Exercise**: Apply what you've learned by completing a coding exercise.
3. **Code Review**: Review the provided solution and compare it with your own.
4. **Challenge Yourself**: Take on an optional extra challenge to push your skills further.

## 💪 Challenges
[🔝 Back to Top](#top)

|  #  |                                       Challenge                        |  ES  | Difficulty |               Solution                  |
| :-: | :--------------------------------------------------------------------: | :--: | :--------: | :-------------------------------------: |
| 01  | [✅ Return the Type](./day_01/README.md) | [![Español](./assets/flag_es.png)](./day_01/README.es.md) | Easy  | [Solution](./day_01/exercise_01.py) |
| 02  | [✅ Calculate the Tip](./day_02/README.md) | [![Español](./assets/flag_es.png)](./day_02/README.es.md) | Easy  | [Solution](./day_02/exercise_02.py) |
| 03  | [✅ Determine if a Year is a Leap Year](./day_03/README.md) | [![Español](./assets/flag_es.png)](./day_03/README.es.md) | Easy  | [Solution](./day_03/exercise_03.py) |
| 04  | [✅ Draw a Triangle Using Loops](./day_03/README.md#-exercise-04---draw-a-triangle-using-loops) | [![Español](./assets/flag_es.png)](./day_03/README.es.md) | Easy  | [Solution](./day_03/exercise_04.py) |

## 🧪 Unit Tests
[🔝 Back to Top](#top)

To run the unit tests you have provided, you need to follow these steps:

1. **Install pytest**: If you do not have the `pytest` module installed, you will need to install it. You can do this using the `pip` package manager. Open your terminal or command line and run:

```bash
pip install pytest
```

2. Organize your files: Make sure the file with the tests (the code snippet you provided) is saved in a file with the .py extension. For example, save it as test_exercise.py.

3. File location: Ensure that the exercise_01.py file (from which you import the found_type function) is in the same directory as your test file (test_exercise.py).

4. Run the tests: Open the terminal or command line and navigate to the directory where your files are located. Then, run the following command:

```bash
pytest test_exercise.py
```

This will run the tests defined in test_exercise.py and display the results in the console. If all tests pass successfully, you will see a message indicating that everything is fine. If any test fails, you will get detailed information about which test failed and how.
