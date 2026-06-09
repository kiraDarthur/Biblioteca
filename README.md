# Library Management System

This is a Python-based Library Management System designed to handle book records, manage inventory, and process loans. The project focuses on data persistence, modular code structure, and efficient user interaction through a command-line interface (CLI).

## Key Features
- **Data Persistence**: Uses CSV files as a lightweight database to store and retrieve book information.
- **Search & Filter**: Advanced search functionality allowing users to find books by Title, Author, Year, or Category.
- **Inventory Control**: Real-time tracking of book stock and availability.
- **Loan Management**: Implements loan logic with a maximum limit of 2 books per user and dynamic due date calculation.
- **Robust Navigation**: Intuitive menu system with error handling and "back" navigation options.

## Technical Details
- **Language**: Python 3.x
- **Data Format**: CSV (Comma-Separated Values)
- **Object-Oriented Design**: Utilizes classes (`Livro`, `Usuario`) to encapsulate logic and state.
- **Dynamic Calculation**: Uses the `datetime` module to calculate loan expiration dates based on local time.

## How to Run
1. Ensure you have Python installed.
2. Place `main.py` and `acervo.csv` in the same directory.
3. Execute the following command in your terminal:
   ```bash
   python main.py
