# library_tracker
Local Library Book Checkout & Overdue Tracker

A Python command-line utility designed to audit daily community library transactions, calculate average checkout durations, and automatically flag overdue book loans.

Developed as part of practical programming coursework following robust PEP 8 standards, file I/O best practices, and defensive error handling.

Features

Dynamic File Ingestion: Uses pathlib and csv.DictReader to safely locate and parse CSV datasets regardless of column reordering.

Defensive Error Handling: Intercepts missing files (FileNotFoundError) to exit cleanly and skips corrupted or non-numeric rows (ValueError) without crashing.

Immutable Data Grouping: Utilizes immutable tuples (borrower_name, book_title) to group related loan data efficiently.

Pythonic Filtering: Leverages list comprehensions to isolate records exceeding the configured maximum loan threshold.

Automated Unit Testing: Includes built-in assert checks verifying calculation accuracy against test datasets.

Project Structure

├── library_tracker.py      # Main script containing business logic, testing, and file I/O
├── library_checkouts.csv   # Raw input data file containing daily transactions
└── library_audit.txt       # Generated output audit report (created upon execution)


Input File Format (library_checkouts.csv)

The input file must follow a comma-separated format with a header row:

book_title,borrower_name,checkout_date,days_kept
The Hobbit,Alice,2025-11-01,14
Python Programming,Bob,2025-11-03,21
Data Structures,Charlie,2025-11-04,7
Clean Code,Alice,2025-11-05,30


Constants & Configuration

MAX_LOAN_DAYS = 14: Defines the maximum allowed borrowing period before a transaction is flagged as overdue.

How to Run

Ensure Python 3.10+ is installed on your system.

Place library_tracker.py and library_checkouts.csv in the same working directory.

Execute the script from your terminal:

python3 library_tracker.py


Review the printed console output and check library_audit.txt for the 