# Greenduino

## Participants

- Jean-Christophe MELIKIAN
- Antoine PELLETIER

Les projets android et api utilisent des fichiers de configuration de services Google pour Firebase.
Ils ne sont pas présent dans les dépôts car ces derniers sont publics.
Nous pouvons vous les envoyer directement par email s'il le faut.

## Sommaire

- [Sous-modules](#sous-modules)
- [Documentation](#documentation)
  - [Récupérer les sous-modules après clonage du dépôt](#récupérer-les-sous-modules-après-clonage-du-dépôt)
  - [Schéma d'architecture technique](#schéma-darchitecture-technique)
  - [Composants électroniques](#composants-électroniques)

## Sous-modules

- [greenhouse-iot](https://github.com/ozonePowered/greenhouse-iot)
- [greenhouse-api](https://github.com/ozonePowered/greenhouse-api)
- [greenhouse-android](https://github.com/ozonePowered/greenhouse-android)

## Documentation

### Récupérer les sous-modules après clonage du dépôt

Récupération des sous-modules:
```
git submodule update --init
```

### Postman

Vous pouvez importer la collection Postman [greenhouse-iot.postman_collection.json](greenhouse-iot.postman_collection.json) présente à la racine de ce dépôt.

Vous devrez définir la variable d'environnement `host`=`http://greenduino.info/`

### Schéma d'architecture technique
![Schéma d'architecture technique](doc/greenhouse-iot-architecture-technique.png)

### Composants électroniques

- 86duino EduCake + carte SD CL10 4Go
- Hygromètre YL-69 et son module YL-38
- Photorésistance + résistance 7.5 kOhms
- Led RGB cathode commune + 3 résistances 180 Ohms
