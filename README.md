# Tkinter Typing Speed Game

A Python-based desktop typing speed game built using Tkinter, featuring multiple
difficulty modes, real-time performance feedback, and local score persistence
using a MySQL database.

This project was originally developed as a standalone desktop application to
practice GUI development and GUI–database integration.

---

## Features

* User registration and login system
* Beginner, Intermediate, and Advanced typing modes
* Real-time typing speed (WPM) and accuracy evaluation
* Local leaderboard and score history
* Profile management for individual users
* Event-driven GUI built using Tkinter

---

## Tech Stack

* **Language:** Python
* **GUI:** Tkinter
* **Database:** MySQL (local, optional)

---

## Demo

A full walkthrough of the application—including user registration, gameplay
across difficulty levels, and leaderboard functionality—is available here:

**Demo Video:**
https://drive.google.com/file/d/12_StujZSdbkPyvqhRNQDcN2O7NzcvuEF/view?usp=sharing

---

## Database Notes

This project uses a local MySQL database to store user profiles and typing scores.
The provided SQL schema reflects the original design used during development and
may be incomplete.

The database layer is included for reference and learning purposes. Reviewers are
not expected to set up or run the database to understand the codebase.

---

## How to Run

1. Ensure Python is installed
2. (Optional) Set up a local MySQL database using the provided SQL schema
3. Run the application:

```bash
python SpeedTyping_v3.4.py
```

---

## Project Status

This repository contains the original implementation of the project with minimal
changes. Future improvements may include database refactoring, modularization,
and additional UI enhancements.

**Created** October 2023
