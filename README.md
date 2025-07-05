# py_exercise

## Project Overview
This repository contains Python exercises and projects, including:
- Playwright automation scripts
- PyAutoGUI automation
- Student grade calculator
- Simple Expense Tracker (with Streamlit frontend)

## Installation & Setup

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd py_exercise
```

### 2. Create and Activate Virtual Environment (Recommended)
```bash
python -m venv myenv
# On Windows:
myenv\Scripts\activate
# On Linux/Mac:
source myenv/bin/activate
```

### 3. Install Required Packages
Install dependencies for all projects:
```bash
pip install -r requirements.txt
```

For Playwright, also run:
```bash
playwright install
```

## Running the Projects

### Playwright Automation
- Navigate to `playwright_project` folder.
- Run the script:
```bash
python netjobsall_login.py
```

### Expense Tracker (Streamlit App)
- Navigate to `expense_tracker/frontend` folder.
- Start the Streamlit app:
```bash
streamlit run app.py
```
- Make sure the backend server (Flask or FastAPI) is running at `http://localhost:5000`.

### PyAutoGUI Scripts
- Navigate to `pyautogui_project` folder.
- Run the desired script:
```bash
python pixel-finder.py
```

### Student Grade Calculator
- Navigate to `Student_grade` folder.
- Run the script:
```bash
python student_grade.py
```

## Notes
- Ensure you have Python 3.11+ installed.
- Activate the virtual environment before running any scripts.
- For Playwright, Chrome/Chromium will be installed automatically with `playwright install`.

---
Feel free to explore each folder for more details and code examples.

