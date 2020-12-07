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
        annee = int(champs[0])
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
    fig, ax = plt.subplots()

    plt.xticks(rotation=0)

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


    with open('tournois_par_annee_ajuste.txt') as entree:
        annees, nombres = lire_entree(entree)


        ax.plot(annees, nombres, 'k-')

        annees_filtrees = [annee for annee in annees if int(annee)%5==0]
        plt.xticks(annees_filtrees, annees_filtrees)


    fig.savefig('tournois.pdf')
    #\pgfpathrectangle{\pgfqpoint{0.3in}{0in}}{\pgfqpoint{4.200000in}{3.800000in}}%

    #fig.savefig('tournois_par_annee_ajuste.pgf')
    #fig.savefig('tournois_par_annee_ajuste.pdf')

def graphe_joueurs_historique(files, nom_sortie):

    fig, ax = plt.subplots()

    for file_index, data_file in enumerate(files):
        with open(data_file) as entree_m:

            print(data_file)

            annees_m, nombres_m = lire_entree(entree_m)

            if data_file == 'joueurs1990.txt' and nom_sortie == 'joueurs1990.pdf':
                ax.set_ylim(top=20000)

            if data_file == 'joueurs1990.txt':
                ax.plot(annees_m, nombres_m, '-', color='black')

            elif data_file == 'joueursFictif.txt':
                ax.plot(annees_m, nombres_m, '--', color='black')

                ax.text(0.9,0.5, "?", size=20,
                        transform=ax.transAxes,
                        ha="center", va="center",
                        bbox=dict(boxstyle="round",
                                  ec='black',
                                  fc='white',))   

            elif data_file == 'joueursA.txt':
                ax.plot(annees_m, nombres_m, ':', color='green')

                ax.text(0.8,0.8, "A", size=20,
                        transform=ax.transAxes,
                        ha="center", va="center",
                        bbox=dict(boxstyle="round",
                                  ec='green',
                                  fc='white',))   

            elif data_file == 'joueursB.txt':
                ax.plot(annees_m, nombres_m, '-.', color='orange')

                ax.text(0.9,0.3, "B", size=20,
                        transform=ax.transAxes,
                        ha="center", va="center",
                        bbox=dict(boxstyle="round",
                                  ec='orange',
                                  fc='white',))   

            elif data_file == 'joueursC.txt':
                ax.plot(annees_m, nombres_m, '--', color='red')

                ax.text(0.65,0.1, "C", size=20,
                        transform=ax.transAxes,
                        ha="center", va="center",
                        bbox=dict(boxstyle="round",
                                  ec='red',
                                  fc='white',))   

            if file_index == 0:
                annees_filtrees = [int(annee) for annee in annees_m if int(annee)%10==0 or int(annee) == 1951]
                if data_file == 'joueursFictif.txt':
                    annees_filtrees.append(1990)
                    ax.set_xlim(right=1995)
                labels = [str(annee) for annee in annees_filtrees]
                plt.xticks(annees_filtrees, labels)


    ax.yaxis.set_label_position("right")
    ax.yaxis.tick_right()

    plt.xlabel(u'Année de naissance', fontsize=24, family='times')
    plt.ylabel(u'Joueurs cotés', fontsize=24, family='times')

    plt.xticks(rotation=0)

    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)

    ax.xaxis.labelpad = 10
    ax.yaxis.labelpad = 20

    ax.set_ylim(bottom = 5000)

    fig.set_size_inches(8, 5)

    plt.tight_layout()

    # hum... la boundingbox est trop petite!
    #        ajuster à la main


    fig.savefig(nom_sortie)
    #\pgfpathrectangle{\pgfpointorigin}{\pgfqpoint{4.500000in}{4.000000in}}%

if __name__ == '__main__':

    graphe_tournois()

    plt.clf() # clear figure

    graphe_joueurs_historique(['joueursFictif.txt', 'joueurs1990.txt'], 'joueurs1990.pdf')

    graphe_joueurs_historique(['joueursA.txt', 'joueursB.txt', 'joueursC.txt', 'joueurs1990.txt'], 'joueursABC.pdf')

    exit()

