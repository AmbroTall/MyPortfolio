Installation steps
git clone https://github.com/AmbroTall/MyPortfolio.git
cd Ambrose
mkdir virtualenv -p python 3.8.2 venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
