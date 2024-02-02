## Запуск приложения
```shell
python -m venv venv
source ./venv/Scripts/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata tabs/fixtures/db.json
python manage.py runserver
```
