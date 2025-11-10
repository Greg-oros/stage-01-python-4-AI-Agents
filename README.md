Stage 1 — Python Fundamentals

Overview
This the first stage demonstrates my way to essential Python programming concepts through practical, portfolio-ready mini-projects from the scratch . The goal is to develop clean, structured, beginner-friendly Python code to build a strong base for AI and automation work and to develop my professional career.

---

Mini Projects Included

| Project | Description | File |
|--------|-------------|------|
| Swap Variables | Swap values without a temporary variable | `src/swap_variables.py` |
| Prime Checker | Determine if a number is prime | `src/prime_checker.py` |
| Word Frequency Analyzer | Count word occurrences in a paragraph | `src/word_frequency.py` |
| CSV Salary Sum | Read a CSV file and sum a numeric column | `src/sum_csv_salary.py` |

---
Parse and Time → Fetch 1 website and print response time
File: parse_and_time.py

This script performs a simple performance measurement of an HTTP request and processes data returned from the Wikipedia API.

What it does:
- Fetches the *"Climate change"* article using the MediaWiki API
- Prints the HTTP response time (how long the request took)
- Extracts readable text from HTML using **BeautifulSoup**
- Saves the article content into:
  - `Climate_change.txt` (plain text format)
  - `Climate_change.json` (structured JSON format)

Key concepts practiced:
- Making HTTP GET requests (`requests`)
- Handling API query parameters
- Response time measurement (`response.elapsed.total_seconds()`)
- Parsing HTML (`BeautifulSoup`)
- File saving (TXT + JSON)

Skills Learned
- Python syntax & control flow
- Functions & input handling
- Lists, dictionaries, and iteration patterns
- File I/O using `csv.DictReader`
- Basic problem-solving and debugging

---


This project contains a series of Python exercises that gradually build up to creating a simple "chat bot" using object-oriented programming concepts.

Learning Goals
- Understand classes and objects in Python  
- Use the `__init__()` constructor to create object attributes  
- Write and call methods (like `speak()` and `run()`)  
- Build a simple interactive bot capable of responding to user input

---

Exercises Overview

| Exercise | Focus | Description |
|-----------|--------|-------------|
| 1 | Class structure | Create your first class and object |
| 2 | Constructors | Learn how to use `__init__` and attributes like `name` |
| 3 | Methods | Add a `speak()` and `introduce()` method |
| 4 | Method arguments | Pass messages dynamically into methods |
| 5 | Bot project | Combine all skills to create a conversational bot |

---

 Running the Bot

Run the bot from your terminal:
```bash
python bot_and_exercises.py



