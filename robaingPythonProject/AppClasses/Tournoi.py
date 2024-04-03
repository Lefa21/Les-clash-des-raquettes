from datetime import datetime, timedelta

from ProjetS4.robaingPythonProject.AppClasses.Connexion import Connexion
from ProjetS4.robaingPythonProject.AppScripts.methodesUtiles import *
from random import randint


class Tournoi(Connexion):

    def __init__(self):
        Connexion.__init__(self)

    # def inserer_tournoi(self):

    def definir_format_tournoi(self, nb_joueur: int) -> str:
        if est_puissance_de_2(nb_joueur) and nb_joueur <= 32:
            return "Elimination Simple"  # Des tournois à élimination simple: pour 32 joueurs par exemple on aura 16
            # matchs, 16 survivants puis 8 matchs 8 survivants, etc...
        elif nb_joueur < 10:
            return "rienpourlemoment"  # Un format de tournoi rapide ou tout le monde rencontre tout le monde et la
            # personne avec le plus de victoires gagne.
        elif nb_joueur < 32:
            return "rienpourlemoment"  # Comme le tournoi à élimination simple mais certains joueurs auront
            # la chance de passer directement en deuxième phase.
        else:
            return "rienpourlemoment"  # Des poules de 3 à 4 joueurs qui élimineront 1 joueur si
            # 3 joueurs dans la poule et 2 joueurs si 4 joueurs dans la poule.

    def generer_tournoi(self, joueurs : list, nb_joueur: int, nb_table: int, date_heure_debut : datetime):
        format_tournoi = self.definir_format_tournoi(nb_joueur)
        liste_joueurs = joueurs.copy()
        heure_match = date_heure_debut
        compteur_table = 0
        if format_tournoi == "Elimination Simple":
            liste_matchs = []
            for i in range(nb_joueur // 2):
                liste_matchs.append([liste_joueurs.pop(randint(0, liste_joueurs.__len__()-1)), liste_joueurs.pop(randint(0, liste_joueurs.__len__()-1)), heure_match.strftime("%H.%M.%d.%m.%Y")])
                compteur_table = compteur_table + 1
                if compteur_table == nb_table:
                    heure_match = heure_match.replace(year= heure_match.year, month= heure_match.month, day=heure_match.day, hour=heure_match.hour, minute=heure_match.minute + 6)
                    compteur_table = 0
        return liste_matchs




    def calcul_nb_phase(self, nb_joueurs):
        while nb_joueurs > 0:
            return


if __name__ == '__main__':
    tournoi = Tournoi()
    print(tournoi.generer_tournoi(["Robin", "Faraz", "Thomas", "Arthur", "Huseyin", "Thibault", "Sarah", "Esteban"],8, 1, datetime.now()))