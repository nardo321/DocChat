import logging
import warnings

warnings.filterwarnings("ignore")
logging.disable(logging.WARNING)

from ingest import ingest
import os

# check if chroma_db exists
if not os.path.exists("./chroma_db"):
    print("No saved PDF document detected!\n")
    pdf_path = input("Please provide valid path to PDF document: ")
    try:
        ingest(pdf_path)
    except Exception as e:
        print(f"Can't load PDF: {e}\n")
        exit()
else:
    choice = input("Add new PDF (y/n) ")
    if choice.lower() == "y":
        pdf_path = input("Path to pdf document? ")
        try:
            ingest(pdf_path)
        except Exception as e:
            print(f"Can't load PDF: {e}\n")
            exit()

# importing after ingest so chroma_db exists
from query import query

user_question = input("\nQuestion (or Enter to exit)? ")
while user_question:
    response = query(user_question)

    print(f"\n{20 * '='} RESPONSE {20 * '='}\n")
    print(f"{response}\n")
    print(f"{20 * '='} USER {20 * '='}\n")
    user_question = input("\nQuestion (or Enter to exit)? ")

print("Exiting...")
