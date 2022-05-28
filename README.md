## fisheye_app

dev backend
```shell
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
setting super admin
```shell
docker ps
docker exec -it fisheye_app /bin/bash
./manage.py createsuperuser
```

