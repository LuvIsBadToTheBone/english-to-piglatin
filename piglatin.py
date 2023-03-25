import sys
import re

liste = (sys.argv)
tmpliste = []
neueliste = []
vowels = "aeiou"
stringp = "!#$%&'()*+, -./:;<=>?@[\]^_`{|}~"

liste = liste[1:]
	
def piglatin(wort):
	if wort[0].lower() in vowels:
		return wort.lower() + "way"
	else:
		return wort[1:] + wort[0].lower() + "ay"
        
for i in liste:
    ding = re.findall(r"\w+|[^\w\s]", i)
    tmpliste.extend(ding)
    
for j in tmpliste:
	if j in stringp:
		neueliste.append(j)
	else:
		neueliste.append(piglatin(j))

print("Here is your translation in Piglatin :\n\n", " ".join(neueliste))
