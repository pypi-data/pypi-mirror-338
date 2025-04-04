# impmagic
## Informations
Librairie pour l'importation optimis� de module python.
Fonctionne principalement avec des d�corateurs, ce qui permet de charger les modules uniquement lorsqu'ils sont n�cessaires.
Toutes ces fonctions se basent sur un syst�me de cache pour recharger plus rapidement les modules lorsqu'ils sont appel�s par d'autres fonctions.

### Pr�requis
- Python 3
<br>

# Installation
```console
pip install impmagic
```
<br>

# Utilisation
### Importer des modules avec un d�corateur
Cette option permet d'importer les modules n�cessaires � la fonction uniquement lorsque celle-ci est utilis�.
Pour son fonctionnement, il faut lui envoyer une liste ou un tuple contenant des dictionnaires d'informations.
Chaque dictionnaire doit contenir au minimum la cl� module, mais peut �galement contenir une liste de sous-module (submodule) ou encore l'option as (comme les import classique)
```python
@impmagic.loader(
        {'module':'zpp_args'},
        {'module':'os.path', 'submodule': ['exists']}, 
        {'module':'psutil', 'as': 'psfunction'}, 
        {'module':'toml_nxs.toml', 'submodule': ['TOML'], 'as': 'TOMLnxs'}
    )
    def function(self):
	    #MyCode
```
<br>

### Importer des modules dans une fonction
Il est �galement possible de charger des modules dans une fonction. Pour cela, on utilise la m�thode load.
Nous pouvons lui envoyer un simple str avec le nom du module, mais nous pouvons �galement lui envoyer les m�mes types de donn�es que le d�corateur loader.
```python
impmagic.load('os')
```
<br>

### Enlever un module import�
Il est possible de supprimer d'une fonction un module qui a �t� import� pr�c�demment.
Il suffit d'appeler la m�thode unload avec le nom du module en param�tre.
Par d�faut, le module restera dans le cache, il faut ajouter l'option uncache=True pour le supprimer �galement du cache.
```python
impmagic.unload('os')
```
<br>

### R�importer un module
Il est possible de r�importer un module d�j� import�. 
Cela peut �tre n�cessaire lorsque nous faisons des tests sur un module et que nous voulons voir les changements de suite sans avoir besoin de quitter le shell en cours.
```python
impmagic.reload('os')
```
<br>

### Utiliser un module sans l'importer
Il est possible d'utiliser un module sans avoir besoin de l'importer gr�ce � la m�thode get.
```python
module = impmagic.get('os')
module.mkdir(dir)
```
<br>

### Utiliser un module sans l'importer depuis un fichier
Il est possible d'utiliser un module sans avoir besoin de l'importer gr�ce � la m�thode get.
```python
module = impmagic.get_from_file('os.py')
module.mkdir(dir)
```