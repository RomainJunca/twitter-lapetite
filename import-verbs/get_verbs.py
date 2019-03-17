import requests
import json
import time
import random

BASE_URL="https://fr.wiktionary.org/w/api.php?action=query&cmtitle=Cat%C3%A9gorie:Verbes_du_premier_groupe_en_fran%C3%A7ais&list=categorymembers&format=json&cmlimit=500&cmtype=page&cmnamespace=0"
#BASE_URL="https://fr.wikipedia.org/w/api.php?action=query&cmtitle=Catégorie:Fruit_alimentaire&list=categorymembers&format=json&cmlimit=500&cmtype=page&cmnamespace=0"

with open("verbs.txt","w", encoding='utf8') as file:
	r = None
	tot = 0
	while True:
		url = BASE_URL
		if r is not None and "continue" in r and "cmcontinue" in r["continue"]:
			url += "&cmcontinue="+r["continue"]["cmcontinue"]

		r = requests.get(url = url).json()


		for member in r["query"]["categorymembers"]:
			file.write(member["title"]+"\n")

		if not ("continue" in r and "cmcontinue" in r["continue"]):
			break;
		tot += len(r["query"]["categorymembers"])
		print(str(tot)+" mots")	
		time.sleep(1)


with open('verbs.txt','r', encoding='utf8') as src:
	data = [ (random.random(), line) for line in src ]
	data.sort()
with open('verbs_random.txt','w', encoding='utf8') as trgt:
	for _, line in data:
		trgt.write( line )



