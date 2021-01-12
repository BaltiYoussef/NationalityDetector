#%% Preprocessing

# on crée un code couleur pour l'affichage des résultats
class bcolors:
    WIN = "\033[32m" # Vert
    FAIL = "\033[91m" # Rouge
    KPI = "\033[93m" # Jaune

# on importe les libraries nécessaires
import pytesseract as tess
from PIL import Image
from passporteye import read_mrz
import glob
import pandas as pd
from translate import Translator

# on instancie la base de donnée des code ISO 3
iso = pd.read_csv("./../src/Data/ISO.csv", sep=";")

# on instancie l'outil de traduction
translator = Translator(to_lang="fr")

# %% On utilise passportEye pour les Passeports

# on va chercher l'ensemble des fichiers concernant les passeports
liste_fichiers = glob.glob("./../src/Data/Passeport interieur/*.jpg")
# on instancie un kpi de réussite
res = 0

# pour chaque fichier dans la liste des fichiers
for i in range(len(liste_fichiers)):
    
    # on lit l'image et identifie les informations du Machine Readable Zone
    mrz = read_mrz(liste_fichiers[i])
    # on identifie le nom du fichier qui expose le résultat attendue du programme
    nom_fichier = liste_fichiers[i].split("\\")[-1]

    # on essaye de le transformer en dictionnaire de données
    try:
        mrz_data = mrz.to_dict()
        # si la transformation a fonctionné, on relève le code ISO 3 du document
        country = mrz_data['country']
        # on identifie le nom complet du pays grâce à la base de données des codes ISO 3
        pays = iso.loc[iso["code"]==country, "nationality"].values[0]
        # on traduit le nom du pays en français
        pays_fr = translator.translate(pays)
        
        # on affiche le résultat
        print(f"{bcolors.WIN}{nom_fichier} vient de {pays_fr} car {country}")
        # on incrémente le kpi
        res += 1
    
    # si une erreur apparait, on affiche l'échec
    except:
        print(f"{bcolors.FAIL}{nom_fichier} n'a pas été identifié")

# on affiche le taux de réussite
kpi = (res / len(liste_fichiers)) * 100
print(f"{bcolors.KPI}{kpi}% de réussite")

# %% On fait passporteye pour les Visa

# on va chercher l'ensemble des fichiers concernant les passeports
liste_fichiers = glob.glob("./../src/Data/Fichier_de_donnees/Visa/*.jpg")
# on instancie un kpi de réussite
res = 0

# pour chaque fichier dans la liste des fichiers
for i in range(len(liste_fichiers)):
    
    # on lit l'image et identifie les informations du Machine Readable Zone
    mrz = read_mrz(liste_fichiers[i])
    # on identifie le nom du fichier qui expose le résultat attendue du programme
    nom_fichier = liste_fichiers[i].split("\\")[-1]

    # on essaye de le transformer en dictionnaire de données
    try:
        mrz_data = mrz.to_dict()
        # si la transformation a fonctionné, on relève le code ISO 3 du document
        country = mrz_data['country']
        # on identifie le nom complet du pays grâce à la base de données des codes ISO 3
        pays = iso.loc[iso["code"]==country, "nationality"].values[0]
        # on traduit le nom du pays en français
        pays_fr = translator.translate(pays)
        
        # on affiche le résultat
        print(f"{bcolors.WIN}{nom_fichier} vient de {pays_fr} car {country}")
        # on incrémente le kpi
        res += 1
    
    # si une erreur apparait, on affiche l'échec
    except:
        print(f"{bcolors.FAIL}{nom_fichier} n'a pas été identifié")

# on affiche le taux de réussite
kpi = (res / len(liste_fichiers)) * 100
print(f"{bcolors.KPI}{kpi}% de réussite")

# %% On fait passporteye pour les Carte d'identité

# on va chercher l'ensemble des fichiers concernant les cartes d'identité
liste_fichiers = glob.glob("./../src/Data/Carte ID/*.jpg")
# on instancie un kpi de réussite
res = len(liste_fichiers)

# pour chaque fichier dans la liste des fichiers
for i in range(len(liste_fichiers)):
    # on lit l'image et identifie les informations du Machine Readable Zone
    img = Image.open(liste_fichiers[i])
    # on la transforme en chaine de caractère
    text = tess.image_to_string(img)
    # on identifie le nom du fichier qui expose le résultat attendue du programme
    nom_fichier = liste_fichiers[i].split("\\")[-1]

    # on test la présence des mots clés et on affiche le résultat
    if "BELGIË" in text or "BELGIQUE" in text or "BELGIEN" in text or "BELGIUM" in text:
        print(f"{bcolors.WIN}{nom_fichier} est belge")
    elif "National Identity Card" in text or "British" in text:
        print(f"{bcolors.WIN}{nom_fichier} est anglais")
    elif "IDFRA" in text or "FRANÇAISE" in text:
        print(f"{bcolors.WIN}{nom_fichier} vient de France")
    elif "DEUTSCH" in text:
        print(f"{bcolors.WIN}{nom_fichier} vient d'Allemagne")
    elif "ITALIANA" in text:
        print(f"{bcolors.WIN}{nom_fichier} vient d'Italie")
    elif "Reeczpospolita" in text or "Polska" in text:
        print(f"{bcolors.WIN}{nom_fichier} vient de Pologne")
    elif "PORTUGAL" in text or "PRT" in text:
        print(f"{bcolors.WIN}{nom_fichier} vient du Portugal")
    elif "ESPANA" in text:
        print(f"{bcolors.WIN}{nom_fichier} vient d'Espagne")
    
    # sinon on affiche l'échec
    else:
        print(f"{bcolors.FAIL}{nom_fichier} n'a pas été identifié")
        # on décrémente le kpi
        res -= 1

# on affiche le taux de réussite
kpi = (res / len(liste_fichiers)) * 100
print(f"{bcolors.KPI}{kpi}% de réussite")

# %%