# Tide Data Analysis using SQLite & Socket Programming

This project reads tidal data from a structured text file and stores it in a SQLite database. A socket-based server allows a client to request calculated tide statistics such as extreme tides and tidal ranges. The implementation combines file handling, SQL queries, and client–server communication in Python.

---

## Project Structure

- **TIDES.TXT** – Raw tidal data (tab-delimited)
- **tide.db** – SQLite database generated from the text file
- **Tide_DATABASE.ipynb** – Reads the text file and populates the database
- **Tide_SERVER.py** – Socket server that processes tide queries
- **Tide_CLIENT.py** – Client program that communicates with the server

---

## Features

- Parses structured text data
- Stores data in a SQLite relational database
- Performs SQL-based aggregation and analysis
- Implements TCP socket communication
- Supports remote querying via a menu-based client interface

---

## How to Run

### 1. Create the Database
```bash
python Tide_DATABASE.ipynb
```
### 2. Run Server side
```bash
python TASK4_DATABASE_YourName.py
```
### 3. Run Client side
```bash
python TASK4_DATABASE_YourName.py
```

