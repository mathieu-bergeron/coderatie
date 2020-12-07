#!/usr/bin/python3
# vim: set fileencoding=utf8 :

import matplotlib

#matplotlib.use("pgf")

import matplotlib.pyplot as plt


import re


PATRON_COMMENTAIRE = '^\s*#.*$'
patron_commentaire = re.compile(PATRON_COMMENTAIRE)


ANNEE_FIN = 2006

def lire_entree(entree):
    annees = []
    nombres = []
    for ligne in entree:
        if patron_commentaire.match(ligne):
            continue

        ligne = ligne.rstrip()
        champs = ligne.split(' ')
        annee = champs[0]
        nombre = int(champs[1])

        annees.append(annee)
        nombres.append(nombre)

    return annees,nombres

def ecrire_sortie(annees, nombres, nom_sortie):
    with open(nom_sortie, 'w') as sortie:
        for i, annee in enumerate(annees):
            sortie.write(str(annee))
            sortie.write(' ')
            sortie.write(str(int(nombres[i])))
            sortie.write('\n')

def creerB(nom_entree, annee_pivot, nom_sortie):

    distance_max = ANNEE_FIN - annee_pivot

    with open(nom_entree) as entree:
        annees, nombres = lire_entree(entree)

        nouveaux_nombres = []

        for i, annee in enumerate(annees):
            nombre = nombres[i]

            if int(annee) > annee_pivot:

                distance = ANNEE_FIN - int(annee)

                facteur = 0.1 +  0.9*(float(distance) / float(distance_max))
                if facteur > 1.0:
                    facteur = 0.8
                elif facteur < 0.2:
                    facteur = 0.2

                nouveaux_nombres.append(int(nombre) * facteur)

            else:
                nouveaux_nombres.append(nombre)

        ecrire_sortie(annees, nouveaux_nombres, nom_sortie)

        return nouveaux_nombres

def creerC(nom_entree, annee_pivot, nombresB, nom_sortie):

    with open(nom_entree) as entree:
        annees, nombres = lire_entree(entree)

        nouveaux_nombres = []

        for i, annee in enumerate(annees):
            nombreA = nombres[i]

            if int(annee) > annee_pivot:

                nombreB = nombresB[i]

                nouveaux_nombres.append((nombreA + nombreB) / 2)

            else:
                nouveaux_nombres.append(nombreA)

        ecrire_sortie(annees, nouveaux_nombres, nom_sortie)


if __name__ == '__main__':

    nombresB = creerB('joueursA.txt', 1983, 'joueursC.txt')

    creerC('joueursA.txt', 1983, nombresB, 'joueursB.txt')

    exit()

