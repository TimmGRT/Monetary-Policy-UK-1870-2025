# 💰📈📊 ==== Name of the repo : economic_research ==== 📊📈💰

### Monetary Theory • Macroeconomics • Economic Analysis



Problématique : Dans quelle mesure l’efficacité des chocs de politique monétaire au Royaume-Uni varie-t-elle selon le régime monétaire : Gold standard (1821–1931), Bretton Woods (1944–1971) et floating exchange rate (1971–présent) ?

## Participants 👥

- 🧑‍💻 **Dorian**  
- 🧑‍💻 **Ryan**  
- 🧑‍💻 **Veljko**  
- 🧑‍💻 **Timéo**

Explication fonctionnement github pour Ryan, Dorian et Veljko

### Lien vers le journal de bord du projet :
[https://docs.google.com/document/d/14NkQ9kOfRvtMvt0urUogPzFW_W_OlQbyQNy4H52IoLU/edit?tab=t.0](https://docs.google.com/document/d/1ArN4QLH1IzCfRL3MGWTbQbo_JbPDv8UI/edit)

### 1. Téléchargement de git en local 
dans le terminal : **xcode-select --install**

Ce qui va faire apparaitre un pop up pour download les dépendances dont git, que vous accepterez.

### 2. Première intitialisation de VScode ( Pas lié directement à GIT )

- Téléchargez VsCode : https://code.visualstudio.com/download
- Ouvrez VsCode des applications et installez le raccourceis "code .", pour se faire :
  - maj + cmd + p ( un menu s'ouvre )
  - tapez dans ce menu : **Shell command : Install 'code' command in PATH**
  - Voila ! maintenant quand vous écrivez dans un fichier de votre terminal **code .**, le fichier s'ouvre dans vscode.

### 3. Clonage du repo : 
Dans votre terminal entrez "ls" afin de visualiser tous les fichiers locaux de votre ordinateur. 

Clonez au même endroit le repository ( projet ) github en éxecutant : **git clone https://github.com/TimmGRT/economic_research**. L'URL ici mentionné est l'url du repository. 

Ceci clonera le projet sous le nom "economic_research" au sein de votre dossier main local.

lorsque vous allez sur le repository du projet sur github. 

### 4. Création du venv : 
Nous utiliserons un environement virtuel afin que le code puisse s'éxecuter sans problème de la même façon sur notre 4 ordinateurs. Si cela n'était pas le cas, certains modules et applications que j'ai installé personnellement en local qui me permette de faire tourner certains programmes ne seront pas disponibles pour un de vous... Ce qui fera que certains bout de code éxécutable chez moi grâce à mes dépendances ne le sera pas chez vous ( ou inversement ). 

__Cook list__ : 

- creez le Virtual environement :
  - Rendez vous au clone du repo en local : **cd economic_research**
  - Créez un virtual environement : **python3 -m venv venv** 
  - Activez le virtual environement : **source venv/bin/activate**
  - Installez les dépendances nécessaires au code de notre projet : **pip install -r requirements.txt**
 
Génial, le clone du Repo Git est bien intialisé vous pouvez coder ! 

### 5. ATTENTION :activez l'autosave des fichiers sans quoi vous devrez faire cmd + s tout le temps

Pour ce faire : en haut à gauche de l'écran lorsque VSCODE est ouvert cliquez sur ***file*** - > descendez et vous trouverez **autosave**

<img width="1467" height="956" alt="Capture d’écran 2026-03-13 à 13 26 38" src="https://github.com/user-attachments/assets/757d9791-3549-404d-a7ec-834fbc091e22" />


### 6. Quelques explications liés à Git et son fonctionnement 

Git est un répertoire de versions de notre code. Il stock chacune de nos upgrades dans un cloud, mais forcément un grand pouvoir implique de grandes résponsabilités... Certaines règles sont à respecter : 

- Codez toujours sur votre fichier assigné ! Un datalake est commun à tout le monde, vous pouvez l'importer dans votre script mais ne modifiez pas de fichiers non contenus dans votre fichier personel !! Ce fonctionnement nous évitera de devoir fonctionner avec les branch, pull request et merge, plus lourds à comprendre. 
- Lorsque des modifications significatives sont faites sur votre fichier, allez dans l'onglet sur la gauche de Vscode représentant le logo de git et faites un push de vos modifications. C'est ici que vous y trouverez votre bonheur.

### 7. Procédure pour push : 
  - premierement lorsque vous faites plusieurs changements mineur cliquez sur le bouton staged qui permettra de stacker tout vos changements mineurs
  - ensuite quand la quantités de changements mineur devient conséquente, __ENTREZ UN MESSAGE DE COMMIT AU DESSUS DU BOUTON BLEU__, et appuyez sur **commit changes**, ce qui pushera le code sur votre git LOCAL.
  - Lorsque vous voulez actualiser le code contenu dans github (le cloud), cliquez sur le bouton **sync changes**
 <img width="1661" height="1240" alt="image" src="https://github.com/user-attachments/assets/96ae6f63-0faf-42f9-9a6a-b8401dd9b156" />


Uniquement deux fonctionnalités seront utilisés dans notre structure:
  - **push** : c'est l'action qui vous permettra de pousser votre code sur github, il actualisera ce que vous avez fais sur le cloud.
  - **pull** : Vous tirez les dernières modifications qui ont étés réalisés par les membres. Elles seront donc actualisés sur votre clone local du github ( le fichier quoi ).

Pour push et pull se réferer à la vidéo.
 
### 8. Routine d'initialisation : 

- Ouvrez votre terminal
- **cd economic_research** -> dirigez vous vers le fichier du projet
- **git pull origin main** -> actualisez les modifications qui ont étés faites en votre absence
- **source venv/bin/activate** -> activez votre environement virtuel
- **code .** -> ouvrir vscode

Magnifique ! Vous êtes prêts à utiliser git et le projet, une vidéo est jointe à cela pour l'installation de toutes ces choses. 



