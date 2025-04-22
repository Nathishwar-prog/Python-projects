```markdown
# Personal Diary CLI App

A simple command-line diary app to write and view your daily thoughts. Built with Python, this app stores entries locally in a JSON file.

## Features

- Add diary entries with date and time
- View all entries or search by date
- Automatically saves data in `diary_DB.json`

## How to Use

1. **Run the script**:
   ```bash
   python diary.py
   ```

2. **Options Available**:
   - `1`: Add a new entry
   - `2`: View all entries or search by date
   - `3`: Exit the app

3. **Sample Entry Flow**:
   - Add what's on your mind when prompted
   - To view entries, either list all or filter by specific date (format: YYYY-MM-DD)

## Data Storage

- All entries are stored in `diary_DB.json` in this format:
  ```json
  [
    {
      "Date": "2025-04-22 15:45",
      "Content": "Had a great coding session today!"
    }
  ]
  ```

## Author

Developed by **Nathishwar**

---
