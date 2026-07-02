# Project Setup

This guide explains how to create a Python virtual environment on different operating systems and install the project's dependencies.

## Prerequisites

* Python 3.10 or newer
* `pip`
* Git (optional)

Clone the repository:

```bash
git clone <repository-url>
cd ai_expense_tracker
```

---

## Linux (Ubuntu, Linux Mint, Debian, Fedora, etc.)

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

Install project dependencies:

```bash
pip install -r requirements.txt
```

Deactivate when finished:

```bash
deactivate
```

---

## macOS

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Deactivate:

```bash
deactivate
```

---

## Windows (PowerShell)

Create a virtual environment:

```powershell
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Deactivate:

```powershell
deactivate
```

---

## Windows (Command Prompt)

Create a virtual environment:

```cmd
python -m venv venv
```

Activate it:

```cmd
venv\Scripts\activate.bat
```

Install dependencies:

```cmd
pip install -r requirements.txt
```

Deactivate:

```cmd
deactivate
```

---

## Windows (Git Bash)

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

```bash
source venv/Scripts/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Deactivate:

```bash
deactivate
```

---

## Verify the Virtual Environment

Confirm that Python and pip are being used from the virtual environment:

Linux/macOS:

```bash
which python
which pip
```

Windows:

```cmd
where python
where pip
```

The paths should point to the project's `venv` directory.

---

## Installing New Packages

Whenever you install a new package:

```bash
pip install <package-name>
```

Update the dependency file:

```bash
pip freeze > requirements.txt
```

Commit the updated `requirements.txt` so others can install the same package versions.

---

## Running the Application

Start the FastAPI development server:

```bash
uvicorn main:app --reload
```

The API will be available at:

* http://127.0.0.1:8000
* Swagger UI: http://127.0.0.1:8000/docs
* ReDoc: http://127.0.0.1:8000/redoc

---

## Running Tests

Execute the test suite:

```bash
python -m pytest
```

Generate a coverage report:

```bash
python -m pytest --cov=. --cov-report=html
```

Open the generated report:

```text
htmlcov/index.html
```
