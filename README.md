### ============ Name of the repo : economic_research ============ ###
Problématique : Comment l’efficacité des chocs de politique monétaire en Suisse a-t-elle évoluée entre le régime pré-plancher (1990–2011), le régime du plancher de change (2011–2015) et l’ère des taux négatifs (2015–2022) ?

### Participants :
Dorian 
Ryan 
Veljko 
Timéo 

### Lien vers le google doc du projet :
https://docs.google.com/document/d/14NkQ9kOfRvtMvt0urUogPzFW_W_OlQbyQNy4H52IoLU/edit?tab=t.0

### Téléchargement de git en local 
dans le terminal : **xcode-select --install**
Ce qui va faire apparaitre un pop up pour download les dépendances dont git, que vous accepterez.

### Première intitialisation de VScode ( Pas lié directement à GIT )
- Téléchargez VsCode : https://code.visualstudio.com/download
- Ouvrez VsCode des applications et installez le raccourceis "code .", pour se faire :
  - maj + cmd + p ( un menu s'ouvre )
  - tapez dans ce menu : **Shell command : Install 'code' command in PATH**
  - Voila ! maintenant quand vous écrivez dans un fichier de votre terminal **code .**, le fichier s'ouvre dans vscode.

### Clonage du repo : 
Dans votre terminal entrez "ls" afin de visualiser tous les fichiers locaux de votre ordinateur. 
Clonez au même endroit le repository ( projet ) github en éxecutant : **git clone "https://github.com/TimmGRT/economic_research"**. L'URL ici mentionné est l'url de la barre de recherche 
lorsque vous allez sur le repository du projet sur github. 

### Création du venv : 
Nous utiliserons un environement virtuel afin que le code puisse s'éxecuter sans problème de la même façon sur notre 4 ordinateurs. Si cela n'était pas le cas, certains modules et applications que j'ai installé personnellement en local qui me permette de faire tourner certains programmes ne seront pas disponibles pour un de vous... Ce qui fera que certains bout de code éxécutable chez moi grâce à mes dépendances ne le sera pas chez vous ( ou inversement ). 

__Cook list__ : 
- creez le Virtual environement :
  - Rendez vous au clone du repo en local : **cd economic_research**
  - Créez un virtual environement : **python3 -m venv venv** 
  - Activez le virtual environement : **source venv/bin/activate**
  - Installez les dépendances nécessaires au code de notre projet : **pip install -r requirements.txt**
 
Génial, le clone du Repo Git est bien intialisé vous pouvez coder ! 

### Quelques explications liés à Git et son fonctionnement 
Git est un répertoire de versions de notre code. Il stock chacune de nos upgrades dans un cloud, mais forcément un grand pouvoir implique de grandes résponsabilités... Certaines règles sont à respecter : 
- Codez toujours sur votre fichier assigné ! Un datalake est commun à tout le monde, vous pouvez l'importer dans votre script mais ne modifiez pas de fichiers non contenus dans votre fichier personel !! Ce fonctionnement nous évitera de devoir fonctionner avec les branch, pull request et merge, plus lourds à comprendre. 
- Lorsque des modifications significatives sont faites sur votre fichier, allez dans l'onglet sur la gauche de Vscode représentant le logo de git et faites un push de vos modifications. C'est ici que vous y trouverez votre bonheur.

Uniquement deux fonctionnalités seront utilisés dans notre structure:
  - **push** : c'est l'action qui vous permettra de pousser votre code sur github, il actualisera ce que vous avez fais sur le cloud.
  - **pull** : Vous tirez les dernières modifications qui ont étés réalisés par les membres. Elles seront donc actualisés sur votre clone local du github ( le fichier quoi ).
 
### Routine d'initialisation : 
- Ouvrez votre terminal
- **cd economic_research** -> dirigez vous vers le fichier du projet
- **git pull economic_research main** -> actualisez les modifications qui ont étés faites en votre absence
- **source venv/bin/activate** -> activez votre environement virtuel
- **code .** -> ouvrir vscode

Magnifique ! Vous êtes prêts à utiliser git et le projet, une vidéo est jointe à cela pour l'installation de toutes ces choses. 



