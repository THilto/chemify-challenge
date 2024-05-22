# Chemify Challenge
Chemify challenge task created for python 3.9 and 3.10

## Setup (windows)

### Create virtual environment + requirements install
```commandline
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### Create SQLAlchemy DB
```commandline
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

### Run Flask
```commandline
python app.py
```

### Run CLI
```commandline
python main.py
```
