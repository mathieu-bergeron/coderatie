#!/usr/bin/python3
# vim: set fileencoding=utf8 :

import matplotlib

matplotlib.use("pgf")

import matplotlib.pyplot as plt


plt.rcParams.update({
    "font.family": "serif",  
    "font.serif": ["Times", "Times New Roman", "times"],
    "text.usetex": True,     # use inline math for ticks
    "pgf.rcfonts": False,    # don't setup fonts from rc parameters
    "pgf.preamble": [
        "\\usepackage{times}",
        #"\\setmainfont{times}",  # serif font via preamble
        #"\\usepackage{unicode-math}",   # unicode math setup
    #    r"\setmathfont{xits-math.otf}",
    ]
})

import re


PATRON_COMMENTAIRE = '^\s*#.*$'
patron_commentaire = re.compile(PATRON_COMMENTAIRE)

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



def afficher(entree, titre, titre_x, titre_y, step_x, nom_sortie):

    annees, nombres = lire_entree(entree)

    fig, ax = plt.subplots()
    ax.plot(annees, nombres)


    plt.xticks(rotation=-45)

    plt.xticks(annees, [annee if int(annee)%step_x==0 else '' for annee in annees])

    #ax.set(xlabel=titre_x, ylabel=titre_y,
                   #title=titre)

    ax.grid()

    fig.set_size_inches(8, 4)

    fig.savefig(nom_sortie)


def graphe_tournois():
    with open('tournois_par_annee_ajuste.txt') as entree:
        annees, nombres = lire_entree(entree)

        fig, ax = plt.subplots()


        ax.plot(annees, nombres, 'k-')

        plt.xticks(rotation=0)


        annees_filtrees = [annee for annee in annees if int(annee)%5==0]
        plt.xticks(annees_filtrees, annees_filtrees)

        ax.yaxis.set_label_position("right")
        ax.yaxis.tick_right()

        # police désirée x 5
        #plt.xlabel(u'Année', fontsize=60)
        #plt.ylabel(u'Tournois internationaux', fontsize=60)

        plt.xlabel(u'Année', fontsize=24, family='times')
        plt.ylabel(u'Tournois internationaux', fontsize=24, family='times')

        ax.yaxis.labelpad = 20
        ax.xaxis.labelpad = 10

        # ax.grid()

        # taille de 2.5in x 5
        #fig.set_size_inches(12, 8)
        fig.set_size_inches(5, 5)

        # taille désirée x 5
        plt.xticks(fontsize=16)
        plt.yticks(fontsize=16)

        #for tick in ax.yaxis.get_major_ticks():
            #tick.label.set_fontsize(50) 

        # hum... la boundingbox est trop petite!
        #        ajuster a la main

        plt.tight_layout()


        fig.savefig('graphe_deux.pdf')
        #\pgfpathrectangle{\pgfqpoint{0.3in}{0in}}{\pgfqpoint{4.200000in}{3.800000in}}%

        #fig.savefig('tournois_par_annee_ajuste.pgf')
        #fig.savefig('tournois_par_annee_ajuste.pdf')

def graphe_joueurs_historique():
    with open('joueurs_nes_cette_annee_M_ajuste.txt') as entree_m:
        annees_m, nombres_m = lire_entree(entree_m)

        fig, ax = plt.subplots()

        ax.plot(annees_m, nombres_m, 'k-')

        #plt.grid(b=False, which='minor')

        plt.xticks(rotation=0)

        annees_filtrees = [annee for annee in annees_m if int(annee)%20==0]


        plt.xticks(annees_filtrees, annees_filtrees)

        #ax.set(xlabel=titre_x, ylabel=titre_y,
                       #title=titre)

        ax.yaxis.set_label_position("right")
        ax.yaxis.tick_right()

        plt.xlabel(u'Année de naissance', fontsize=24, family='times')

        plt.ylabel(u'Joueurs cotés', fontsize=24, family='times')

        plt.xticks(fontsize=16)
        plt.yticks(fontsize=16)

        ax.xaxis.labelpad = 10
        ax.yaxis.labelpad = 20

        #ax.grid()

        fig.set_size_inches(5, 5)

        plt.tight_layout()

        # hum... la boundingbox est trop petite!
        #        ajuster à la main
        fig.savefig('graphe_un.pdf')
        #\pgfpathrectangle{\pgfpointorigin}{\pgfqpoint{4.500000in}{4.000000in}}%

if __name__ == '__main__':

    graphe_tournois()

    plt.clf() # clear figure


    graphe_joueurs_historique()

    exit()

