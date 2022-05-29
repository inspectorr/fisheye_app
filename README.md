## fisheye_app

dev backend
```shell
pip install -r requirements.txt
./start.sh
```

dev frontend
```shell
cd frontend && yarn install && yarn build
```

deployment
```shell
docker-compose up --build
```
logging into app container
```shell
docker ps
docker exec -it fisheye_app /bin/bash
```
setting super admin
```shell
./manage.py createsuperuser
```
backup
```shell
./manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 2 > backup/dump.json
```
import dump
```shell
./manage.py loaddata backup/dump.json
```
