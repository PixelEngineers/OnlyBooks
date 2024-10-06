# OnlyBooks
OnlyBooks is a web service to browser through a vast collection of books

## Prereqisites
1. Python
2. Pip

## Setup

1. (Optional) Setup a virtual environment
### Windows
```
python -m venv .venv
".venv/Scripts/activate"
```
### MacOS
```
python -m venv .venv
source .venv/bin/activate
```
### Linux
With venv
```
python -m venv .venv
source .venv/bin/activate
```
With virtualenv (bash)
```
python -m virtualenv
source .venv/bin/activate
```
NixOS
```
python -m virtualenv
overlay use .venv/bin/activate.nu
```

2. Install dependencies
```
pip install -r requirements.txt
```

3. Run django server
```
python manage.py runserver
```