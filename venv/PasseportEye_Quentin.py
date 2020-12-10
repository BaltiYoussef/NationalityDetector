# %%
import pytesseract as tess
from PIL import Image
import glob

listeChemin = glob.glob("C:/Users/qlachaussee/Documents/CNAM 2/Python/Fichier_de_donnees/Passeport interieur/*.jpg")

for i in range(len(listeChemin)):
    img = Image.open(listeChemin[i])
    text = tess.image_to_string(img)
    if "PCBEL" in text or "P<BEL" in text:
        print(listeChemin[i].split("\\")[-1] + " est belge")
    if "PCGBR" in text or "P<GBR" in text:
        print(listeChemin[i].split("\\")[-1] + " est anglais")
    if "PCFRA" in text or "P<FRA" in text:
        print(listeChemin[i].split("\\")[-1] + " est français")
    if "PCDCC" in text or "P<D<<" in text:
        print(listeChemin[i].split("\\")[-1] + " est allemand")
    if "PCITA" in text or "P<ITA" in text:
        print(listeChemin[i].split("\\")[-1] + " est italien")
    if "PCPOL" in text or "P<POL" in text:
        print(listeChemin[i].split("\\")[-1] + " est polonais")
    if "PCPRT" in text or "P<PRT" in text:
        print(listeChemin[i].split("\\")[-1] + " est portugais")
    if "PCESP" in text or "P<ESP" in text:
        print(listeChemin[i].split("\\")[-1] + " est espagnol")

#%%
class bcolors:
    HEADER = '\033[95m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# %% On fait passporteye pour les Passeports
import pytesseract as tess
from PIL import Image
from passporteye import read_mrz
import glob
import pandas as pd

iso = pd.read_csv("C:/Users/qlachaussee/Documents/CNAM 2/Python/Fichier_de_donnees/ISO.csv", sep=";")

listeChemin = glob.glob("C:/Users/qlachaussee/Documents/CNAM 2/Python/Fichier_de_donnees/Passeport interieur/*.jpg")

for i in range(len(listeChemin)):
    mrz = read_mrz(listeChemin[i])
    try:
        mrz_data = mrz.to_dict()
        print(bcolors.WARNING + listeChemin[i].split("\\")[-1] + " est " + iso.loc[iso["code"]==mrz_data['country'], "nationality"].values[0] + " car " + mrz_data['country'])
    except:
        print(bcolors.FAIL + listeChemin[i].split("\\")[-1] + " n'est pas identifié")

# %% On fait passporteye pour les Visa
import pytesseract as tess
from PIL import Image
from passporteye import read_mrz
import glob
import pandas as pd

iso = pd.read_csv("C:/Users/qlachaussee/Documents/CNAM 2/Python/Fichier_de_donnees/ISO.csv", sep=";")

listeChemin = glob.glob("C:/Users/qlachaussee/Documents/CNAM 2/Python/Fichier_de_donnees/Visa/*.jpg")

for i in range(len(listeChemin)):
    mrz = read_mrz(listeChemin[i])
    try:
        mrz_data = mrz.to_dict()
        print(bcolors.WARNING + listeChemin[i].split("\\")[-1] + " est " + iso.loc[iso["code"]==mrz_data['nationality'], "nationality"].values[0] + " car " + mrz_data['country'])
    except:
        print(bcolors.FAIL + listeChemin[i].split("\\")[-1] + " n'est pas identifié")

# %% J'essaye une library pour la carte d'identité
from id_card_extractor import *
import glob
import pandas as pd

iso = pd.read_csv("C:/Users/qlachaussee/Documents/CNAM 2/Python/Fichier_de_donnees/ISO.csv", sep=";")

listeChemin = glob.glob("C:/Users/qlachaussee/Documents/CNAM 2/Python/Fichier_de_donnees/Carte ID/*.jpg")

for i in range(len(listeChemin)):
    try:
        print(get_card_from_image(listeChemin[i]))
    except:
        print("e")
# %%
