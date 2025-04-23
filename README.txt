SearchIt - A Python GUI Search Tool

SearchIt is a Tkinter-based GUI application that allows users to search for a term and view real-time results from:
- Wikipedia
- Dictionary API (`dictionaryapi.dev`)
- Thesaurus (via synonyms and antonyms from the same Dictionary API)

This app uses live API calls and displays formatted results in a clean, user-friendly interface.

---

Features

- Tkinter-based multi-page interface
- Dynamic fetching of summaries and definitions
- Scrollable full-result view
- Real-time data from:
  - Wikipedia (via `wikipedia-api`)
  - Free Dictionary API
- Clickable sources with "← Back" navigation
- Clean separation of GUI and backend logic

---

Requirements

Ensure you have Python 3.11+ installed. Then install dependencies:

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:
```
requests
wikipedia-api
wonderwords
```

If you're missing `requirements.txt`, create it manually with the above packages.

---

Project Structure

```
pythonProject15/
│
├── API_PyTest.py        # Handles all API fetching logic
├── searchit.py          # Launches the GUI
├── requirements.txt     # Required packages
```

---

How to Run

Option 1: Command Line (Recommended)

```bash
cd path/to/location
python searchit.py
```

Option 2: In PyCharm or Visual Studio

- Open the folder as a project
- Right-click `searchit.py` → Run
- Or set it as your startup script in your IDE

---

Example Usage

1. Launch the GUI
2. Enter a search term like `apple`
3. Click Search
4. Click a source (e.g., Wikipedia) to read the full result
5. Click "← Back" to choose another source or start a new search

---

Optional: Run from API CLI

You can also test API calls directly from the command line by running:

```bash
python API_PyTest.py
```

It will prompt you for input and print live results from the APIs.

---


Developed by Melissa, Gabriel, and Zan
Tested with Python 3.11 and Tkinter
