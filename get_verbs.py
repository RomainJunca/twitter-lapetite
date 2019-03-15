import requests
import json

with open("verbs.txt","w") as file:
    r = requests.get(url = "https://fr.wiktionary.org/w/api.php?action=query&cmtitle=Cat%C3%A9gorie:Verbes_du_premier_groupe_en_fran%C3%A7ais&list=categorymembers&format=json&cmlimit=500&cmtype=page&cmnamespace=0").json()
    i = 0

    nbr = len(r["query"]["categorymembers"])
    
    while i < nbr:
        file.write(r["query"]["categorymembers"][i]["title"]+"\n")
        i = i+1
