#Установка

1. docker build . --tag kpopbot
1. docker run --restart unless-stopped -v /var/docker_volumes/IceAnna/kpopbot/:/var/kpopbot kpopbot