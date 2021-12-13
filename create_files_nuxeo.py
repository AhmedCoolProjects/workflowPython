from os import listdir
from os.path import join
import random
import shutil

files_dir_path = "C:\\Users\\ahmed\\Desktop\\here"
dir_dest_path = "C:\\Users\\ahmed\\Desktop\\zzzz"

e = [
    "talbi_amal",
    "badaoui_amira",
    "staili_houda",
    "boulkhir_nada",
    "motawakile_janate",
    "boulid_mohammed",
    "hachimi_said",
    "lamrani_adam",
    "sgire_zakaria",
    "darki_ayoub",
    "benfettah_ilyass",
    "sadiq_hamza",
    "behri_manal",
    "ramzi_marwa",
    "toubali_salwa",
]
php = {
    "index": "php",
    "counts": [8, 4, 3],
    "titles": ["cours", "tp", "projet"]
}
html = {
    "index": "html",
    "counts": [3, 1, 1],
    "titles": ["cours", "tp", "projet"]
}
archive = {
    "index": "archivistique",
    "counts": [5, 3, 2],
    "titles": ["cours", "td", "controle"]
}
eco = {
    "index": "economie",
    "counts": [6, 3, 2],
    "titles": ["cours", "td", "controle"]
}
l = [php, html, archive, eco]
k = []
kk = listdir(files_dir_path)
for f in kk:
    k.append(join(files_dir_path, f))

# the program

# copy origine file and past it in the dest dir


def createFiles(origine, name):
    shutil.copy(origine, join(dir_dest_path, name))


for subj in l:
    for i in range(len(subj["counts"])):
        for j in range(subj["counts"][i]):
            origine = random.choice(k)
            name = subj['index'] + "_" + subj['titles'][i] + \
                "_" + str(j + 1) + "." + origine.split(".")[-1]
            createFiles(origine, name)
        if i >= 1:
            for j in range(subj["counts"][i]):
                r = random.randint(5, len(e))
                eleves = random.sample(e, r)
                for ele in eleves:
                    origine = random.choice(k)
                    name = subj['index'] + "_rendue_" + subj['titles'][i] + \
                        "_" + str(j + 1) + "_" + ele + "." + \
                        origine.split(".")[-1]
                    createFiles(origine, name)
print("done")
