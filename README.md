# Chemify Challenge
Chemify challenge task created for python 3.9 and 3.10

## Setup (windows)

### .env
```
SQLALCHEMY_DATABASE_URI='sqlite:///tasks.db'
SQLALCHEMY_TRACK_MODIFICATIONS=False
SECRET_KEY=secret_key

FLASK_URL=http://xxx.x.x.x:5000
```

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
