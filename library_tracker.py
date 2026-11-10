import csv
import sys
import math

MAX_LOAN_DAYS = 14

def load_checkouts() -> list[dict]:
    """Reads library_checkouts.csv and returns a list of checkout records.
    
    Expects:
        No arguments. Relies on library_checkouts.csv in the local directory.
        
    Returns:
        list[dict]: A list of rows parsed via DictReader.
    """
    checkouts = []
    try: 
        with open("library.checkouts.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    row["days_kept"] = int(row["days_kept"])
                    checkouts.append(row)
                except ValueError:
                    print(f"Skipping row with invalid data, value: {row}")
                    continue
#Converts days_kept to integer for calculation and appends row to list
    except FileNotFoundError:
        print("File not found!")
        sys.exit(1)
    return checkouts

def overdue_checkouts(checkouts: list[dict]) -> list[tuple[str, str, int]]:
    """Filters books kept longer than MAX_LOAN_DAYS and groups them as tuples.
    
    Expects:
        checkouts (list[dict]): List of checkout dictionaries.
        
    Returns:
        list[tuple[str, str, int]]: A list of (borrower_name, book_title, days_kept) tuples.
    """
    overdue = [(row["borrower_name"], row["book_title"], row["days_kept"])
               for row in checkouts
                if row["days_kept"] > MAX_LOAN_DAYS
                ]
    return overdue

def calculate_average_duration(checkouts: list[dict]) -> float:
    """Computes the average checkout duration across all records.
    
    Expects:
        checkouts (list[dict]): List of checkout dictionaries.
        
    Returns:
        float: Mean days kept, or 0.0 if empty.
    """
    if not checkouts:
        return 0.0

    total_days = sum(rows["days_kept"] for row in checkouts)
    return total_days / len(checkouts)

def build_audit_report(checkouts: list[dict]) -> str:
    """Generates the library overdue audit summary text.
    
    Expects:
        checkouts (list[dict]): List of checkout dictionaries.
        
    Returns:
        str: Formatted audit report text.
    """
    if not checkouts:
        print("No library checkouts available")

    total_records = len(checkouts)
    avg_duration = calculate_average_duration(checkouts)
    overdue_loans = overdue_checkouts(checkouts)

    overdue_lines = "\n".join(
        f"  - {borrower} borrowed '{title}' (kept for {days} days)" 
        for borrower, title, days in overdue_loans
    )
    report = f"""Community Library Audit Report:
----------------------------------
Total Active Transactions: {total_records}
Maximum Allowed Loan Period: {MAX_LOAN_DAYS} days
Average Checkout Duration: {avg_duration:.1f} days

Overdue Loans Flagged ({len(overdue_loans)} total):
{overdue_lines if overdue_lines else "  None"}
"""
    return report

def save_audit_report(report_text: str):
    """Saves the generated audit report text to library_audit.txt."""
    with open("library_audit.txt", "w") as file:
        file.write(report_text)