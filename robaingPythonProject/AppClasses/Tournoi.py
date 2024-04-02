from Connexion import Connexion
from robaingPythonProject.AppScripts.methodesUtiles import *
from robaingPythonProject.AppClasses import FormatTournoi


class Tournoi(Connexion):

    def __init__(self):
        Connexion.__init__(self)

    # def inserer_tournoi(self):

    def definir_format_tournoi(self, nb_joueur: int) -> FormatTournoi:
        if est_puissance_de_2(nb_joueur) and nb_joueur <= 32:
            return FormatTournoi.FormatTournoi.ELIMINATION_SIMPLE  # Des tournois à élimination simple: pour 32 joueurs par exemple on aura 16
            # matchs, 16 survivants puis 8 matchs 8 survivants, etc...
        elif nb_joueur < 10:
            return FormatTournoi.FormatTournoi.TOURNOI_A_LA_RONDE  # Un format de tournoi rapide ou tout le monde rencontre tout le monde et la
            # personne avec le plus de victoires gagne.
        elif nb_joueur < 32:
            return FormatTournoi.FormatTournoi.ELIMINATION_SIMPLE_SPECIAL  # Comme le tournoi à élimination simple mais certains joueurs auront
            # la chance de passer directement en deuxième phase.
        else:
            return FormatTournoi.FormatTournoi.ELIMINATION_SIMPLE_POULE  # Des poules de 3 à 4 joueurs qui élimineront 1 joueur si
            # 3 joueurs dans la poule et 2 joueurs si 4 joueurs dans la poule.

    def generer_tournoi(self, nbJoueur: int, nbTable: int, nbRaquettes: int):
        format_tournoi = self.definir_format_tournoi(nbJoueur)
        if format_tournoi == FormatTournoi.FormatTournoi.ELIMINATION_SIMPLE:
            nbPhases



    def calcul_nb_phase(self, nbJoueurs):
        while nbJoueurs > 0:
            