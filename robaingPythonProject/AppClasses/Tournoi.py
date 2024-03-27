from Connexion import Connexion
from robaingPythonProject.AppScripts.methodesUtiles import *


class Tournoi(Connexion):

    def __init__(self):
        Connexion.__init__(self)

    # def inserer_tournoi(self):

    def definir_format_tournoi(self, nb_joueur: int) -> str:
        if est_puissance_de_2(nb_joueur) and nb_joueur <= 32:
            return "Elimination Simple"  # Des tournois à élimination simple: pour 32 joueurs par exemple on aura 16 matchs, 16 survivants puis 8 matchs 8 survivants, etc...
        elif nb_joueur < 10:
            return "Tournoi à la ronde"  # Un format de tournoi rapide ou tout le monde rencontre tout le monde et la personne avec le plus de victoires gagne.
        elif nb_joueur < 32:
            return "Elimination Simple Spécial"  # Comme le tournoi à élimination simple mais certains joueurs auront la chance de passer directement en deuxième phase.
        else:
            return "Elimination Simple précédé de poules"  # Des poules de 3 à 4 joueurs qui élimineront 1 joueur si 3 joueurs dans la poule et 2 joueurs si 4 joueurs dans la poule.

    def generer_tournoi(self, nbJoueur: int, nbTable: int, nbRaquettes: int):
        formatTournoi = self.definir_format_tournoi(nbJoueur)
        return 0
