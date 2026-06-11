# Library Management System

This is a Python-based Library Management System designed to handle book records, manage inventory, and process loans. The project focuses on data persistence, modular code structure, and efficient user interaction through a command-line interface (CLI).

## Key Features
- **Data Persistence**: Uses CSV files (`acervo.csv`, `usuarios.csv`) and TXT files (`emprestimos.txt`) as a lightweight database to store and retrieve records.
- **Search & Filter**: Advanced search functionality allowing users to find books by Title, Author, Year, or Category.
- **Inventory Control**: Real-time tracking of book stock and availability.
- **Loan Management**: Implements loan logic with automatic due date calculation (14-day limit).
- **Robust Navigation**: Intuitive menu system with error handling and "back" navigation options.

## Technical Details
- **Language**: Python 3.x
- **Data Format**: CSV, TXT
- **Core Modules**: `csv`, `datetime`, `os` (standard library)

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/kiraDarthur/Biblioteca.git
