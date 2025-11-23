Projet : Application Python Conteneurisée (JokeAPI)

Ceci est une application Python 3 simple qui utilise la librairie requests pour interroger un service d'API public (JokeAPI) et afficher une blague de programmation aléatoire dans la console.

Le projet est conteneurisé à l'aide de Docker.

Fichiers Inclus

app.py: Le script Python principal qui exécute la requête API.

requirements.txt: Liste des dépendances Python (uniquement requests).

Dockerfile: Instructions pour construire l'image Docker.

🚀 Comment Lancer l'Application

Vous pouvez lancer l'application de deux manières : directement avec Python, ou via Docker (méthode recommandée).

Option 1 : Utilisation de Docker (Recommandée)

1. Cloner le Dépôt (si ce n'est pas déjà fait)

git clone [VOTRE_LIEN_GITHUB_ICI]
cd [NOM_DE_VOTRE_REPO]


2. Construire l'Image Docker

Exécutez cette commande dans le même répertoire que le Dockerfile. Nous nommons l'image joke-app.

docker build -t joke-app .


3. Exécuter le Conteneur

Une fois l'image construite, vous pouvez lancer l'application :

docker run joke-app


Le conteneur démarrera, exécutera app.py, affichera la blague, puis s'arrêtera.

Option 2 : Utilisation Locale avec Python

1. Installation des Dépendances

Assurez-vous d'avoir Python 3 installé. Ensuite, installez la librairie requests :

pip install -r requirements.txt


2. Exécution du Script

python app.py


Le script contactera l'API et affichera la blague.

Dépendances

Le projet utilise uniquement :

requests : pour effectuer les requêtes HTTP.

Ce projet a été réalisé dans le cadre de l'exercice ue19-lab-05.
