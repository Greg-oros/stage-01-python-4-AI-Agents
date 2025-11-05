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

How to Run
```bash
git clone https://https://github.com/Greg-oros/stage-01-python-4-AI-Agents/
cd stage-01-python-4-AI-Agents
python src/prime_checker.py
