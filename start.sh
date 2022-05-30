python manage.py migrate
cd frontend && yarn build && cd ..
python manage.py runserver 0.0.0.0:8765
