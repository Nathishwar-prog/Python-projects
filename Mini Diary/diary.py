import json
import os
from datetime import datetime

file_name = "diary_DB.json"

def load_data():
    if not os.path.exists(file_name):
        return []
    with open(file_name, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_data(data):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)
    print("Saved Successfully")

def add_entries():
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    content = input(" What's on your mind: ")
    entries = load_data()
    entries.append({"Date": date, "Content": content})
    save_data(entries)

def view_entries():
    entries = load_data()
    command = input(" View all entries? (Yes/No): ").lower()
    if command == "yes":
        for entry in entries:
            print(f"\n {entry.get('Date')}\n {entry.get('Content')}\n{'-' * 40}")
    else:
        search_date = input("Enter date to search (YYYY-MM-DD): ")
        for entry in entries:
            if entry.get("Date", "").startswith(search_date):
                print(f"\n {entry.get('Date')}\n {entry.get('Content')}\n{'-' * 40}")

# Run loop
while True:
    print("\n1. Add Entry\n2. View Entries\n3. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        add_entries()
    elif choice == '2':
        view_entries()
    elif choice == '3':
        print("Exiting. Bye Nathish!")
        break
