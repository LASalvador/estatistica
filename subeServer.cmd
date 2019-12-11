pip install Flask
pip install -U flask-cors

cd server/venv/Scripts
activate

set FLASK_ENV=development
set FLASK_APP=app.py

flask run