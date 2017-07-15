# greenhouse-iot

## Sommaire

- [Participants](#participants)
- [Sous-modules](#sous-modules)
- [Documentation](#documentation)
  - [Récupérer les sous-modules après clonage du dépôt](#récupérer-les-sous-modules-après-clonage-du-dépôt)
  - [Schéma d'architecture technique](#schéma-darchitecture-technique)
- [Composants électroniques](#composants-électroniques)

## Participants

- Jean-Christophe MELIKIAN
- Antoine PELLETIER

## Sous-modules

- greenhouse-iot
- greenhouse-api
- greenhouse-android

## Documentation

### Récupérer les sous-modules après clonage du dépôt

Récupération des sous-modules:
```
git submodule update --init
```

### Schéma d'architecture technique
![Schéma d'architecture technique](doc/greenhouse-iot-architecture-technique.png)

### Composants électroniques

- 86duino EduCake + carte SD CL10 4Go
- Hygromètre YL-69 et son module YL-38
- Photorésistance + résistance 7.5 kOhms
- Led RGB cathode commune + 3 résistances 180 Ohms
