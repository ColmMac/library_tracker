import csv
import sys
import math

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