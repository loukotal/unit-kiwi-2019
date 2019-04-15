if ! [ -f .local ]; then
echo "You need to create .local file from .local.template and fill in your docker registry credentials" && exit
fi

echo ".local exists" && source .local
docker login -u $DOCKER_LOGIN -p $DOCKER_PASSWORD registry.thinkeasy.cz

docker-compose -f docker-compose.yml -f docker-compose.local.yml build

case "$1" in
"bash")
    docker-compose -f docker-compose.yml -f docker-compose.local.yml run host /bin/bash
    ;;

"migrate")
    docker-compose -f docker-compose.yml -f docker-compose.local.yml run host python manage.py migrate
    ;;

"makemigrations")
    docker-compose -f docker-compose.yml -f docker-compose.local.yml run host python manage.py makemigrations
    ;;

"test")
    docker-compose -f docker-compose.yml -f docker-compose.local.yml run host python manage.py test
    ;;

"csu")
    docker-compose -f docker-compose.yml -f docker-compose.local.yml run host python manage.py createsuperuser
    ;;

*)
    docker-compose -f docker-compose.yml -f docker-compose.local.yml up
    ;;
esac
