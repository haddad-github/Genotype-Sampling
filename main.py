from tp1_data import samples, phenotypes, genotypes
from collections import Counter

#On print la longueur de la liste et des 2 dictionnaires, pour s'assurer que le nombre d'echantillion concorde
if (len(samples)) == (len(phenotypes)) == len((genotypes)):
    print("\nIl y a bien 2000 sujets dans chaque liste/dictionnaire\n")
else:
    print("Le nombre d'echantillions ne concorde pas. Revalider la base de donnees.\n")

#Question 1
#"len" compte le nombre d'objets dans la liste "samples"
print("Il y a", len(samples) ,"echantillons")

#Question 2
#"Counter" compter la valeur "1" dans le dictionaire "phenotypes", representant le nombre de malades
malade = Counter(phenotypes.values())
print("Il y a", malade[1], "cas")

#Question 3
#Meme fonction et logique que la question 2, mais avec la valeur "0" dans le dictionnaire "phenotypes", representant le nombre de controles
controles = Counter(phenotypes.values())
print("Il y a", controles[0], "controles\n")

#Question 4
#Regrouper les valeurs de genotypes et phenotypes dans un nouveau dictionaire
genotypesCopie = genotypes.copy() #copie du dictionnaire pour conserver l'original (pour utilisation apres la boucle)

for valeur in genotypesCopie:
    if valeur in phenotypes and valeur in genotypesCopie:
        genotypesCopie[valeur] = genotypesCopie[valeur], phenotypes[valeur] #a l'index respectif x, on y ajoute la valeur du phenotype
cas = {**phenotypes, **genotypesCopie} #nouveau dictionnaire

#compte le nombre de combinaisons "genotype, infectee"
GG_cas = Counter(cas.values())["G/G",1]
print("Il y a", GG_cas, "cas pour les genotypes G/G")

AG_cas = Counter(cas.values())["A/G",1]
print("Il y a", AG_cas, "cas pour les genotypes A/G")

AA_cas = Counter(cas.values())["A/A", 1]
print("Il y a", AA_cas, "cas pour les genotypes A/A\n")

#Question BONUS
GG_total = Counter(genotypes.values())["G/G"]
AG_total = Counter(genotypes.values())["A/G"]
AA_total = Counter(genotypes.values())["A/A"]

GG_cas_proportion = GG_cas/GG_total*100
AG_cas_proportion = AG_cas/AG_total*100
AA_cas_proportion = AA_cas/AA_total*100

print("La portion des cas pour le genotype GG est:", round(GG_cas_proportion), "%")
print("La portion des cas pour le genotype AG est:", round(AG_cas_proportion), "%")
print("La portion des cas pour le genotype AA est:", round(AA_cas_proportion), "%")