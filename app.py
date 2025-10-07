# app.py
"""
Main entry point for MEDTRACK Project
Author: muddapukrishnavamsee@gmail.com
"""
from display import main, view_summary

# Function to print header
def print_header():
    summary = view_summary()  # Get medicine summary from database
    print("\n" + "="*50)
    print("          Welcome to MedTrack")
    print("      Your Smart Medicine Reminder\n")
    print(f"Total medicines: {summary['total']} | Pending: {summary['pending']} | Taken: {summary['taken']}")
    print("="*50 + "\n")

# Function to print footer
def print_footer(message="Operation completed"):
    print("\n" + "-"*50)
    print(message)
    print("-"*50 + "\n")


if __name__ == "__main__":
    print_header()  # Print once at start
    try:
        main(print_footer)  # Pass print_footer to display.py
    except Exception as e:
        print_footer(f"An unexpected error occurred: {e}")
        print_footer() # print once a end 
    
