from datetime import datetime, timedelta

from robaingPythonProject.AppClasses.Connexion import Connexion
from robaingPythonProject.AppScripts.methodesUtiles import *
from random import randint


def joue_deja_a_cette_heure(joueur_1: str, heure_match: datetime, liste_matchs: list):
    if liste_matchs == []:
        return False
    for match in liste_matchs:
        if (joueur_1 == match[0] or joueur_1 == match[1]) and match[3] == heure_match.strftime(
                "%H.%M.%d.%m.%Y"):
            return True
    return False


def horaire_complet(nb_table: int, liste_matchs: list, heure_match: datetime):
    if liste_matchs == []:
        return False
    compteur = 0
    for match in liste_matchs:
        print(match)
        if match[3] == heure_match.strftime("%H.%M.%d.%m"):
            compteur += 1
    return True if compteur == nb_table else False


def calcul_nb_phase(nb_joueurs):
    while nb_joueurs > 0:
        return


class Tournoi(Connexion):

    def __init__(self):
        Connexion.__init__(self)

    def inserer_tournoi(self, nom_tournoi: str, date_debut_tournoi: str, heure_debut_tournoi: str, nombre_de_table: int,
                        liste_des_joueurs: list):

        if not (nom_tournoi and date_debut_tournoi and heure_debut_tournoi and nombre_de_table and liste_des_joueurs):
            return "Certains paramètres sont vides ou nuls"

        if not liste_des_joueurs:
            return "La liste des joueurs est vide"

        liste_de_matchs = self.generer_tournoi(liste_des_joueurs, len(liste_des_joueurs), nombre_de_table,
                                               datetime.strptime(date_debut_tournoi + " " + heure_debut_tournoi,
                                                                 "%Y-%m-%d %H:%M"))

        coll = self.db.tournoi
        if self.tournoi_existe(nom_tournoi):
            return "Un tournoi ayant ce nom existe déjà "
        else:
            coll.insert_one(
                {"nom_tournoi": nom_tournoi, "date_debut_tournoi": date_debut_tournoi,
                 "heure_debut_tournoi": heure_debut_tournoi, "nombres_de_tables": nombre_de_table,
                 "liste_des_joueurs": liste_des_joueurs, "liste_des_matchs": liste_de_matchs})
            return "Tournoi inséré"

    def tournoi_existe(self, nom_tournoi: str):
        coll = self.db.tournoi
        requete = coll.find_one({"nom_tournoi": nom_tournoi})
        if (requete != None):
            return True
        else:
            return False

    def afficher_match(self, nom_tournoi: int):
        coll = self.db.tournois
        matches = []
        tournois = coll.find_one({"nom": nom_tournoi})
        for tournoi in tournois:
            if 'matches' in tournoi:
                matches.extend(tournoi['matches'])
        return matches



    def definir_format_tournoi(self, nb_joueur: int) -> str:
        if est_puissance_de_2(nb_joueur) and nb_joueur <= 32:
            return "Elimination Simple"  # Des tournois à élimination simple: pour 32 joueurs par exemple on aura 16
            # matchs, 16 survivants puis 8 matchs 8 survivants, etc...
        elif nb_joueur < 10:
            return "Tournoi à la ronde"  # Un format de tournoi rapide ou tout le monde rencontre tout le monde et la
            # personne avec le plus de victoires gagne.
        elif nb_joueur < 32:
            return "rienpourlemoment"  # Comme le tournoi à élimination simple mais certains joueurs auront
            # la chance de passer directement en deuxième phase.
        else:
            return "rienpourlemoment"  # Des poules de 3 à 4 joueurs qui élimineront 1 joueur si
            # 3 joueurs dans la poule et 2 joueurs si 4 joueurs dans la poule.

    def generer_tournoi(self, joueurs: list, nb_joueur: int, nb_table: int, date_heure_debut: datetime):
        global liste_matchs
        format_tournoi = self.definir_format_tournoi(nb_joueur)
        liste_joueurs = joueurs.copy()
        heure_match = date_heure_debut
        if format_tournoi == "Elimination Simple":
            liste_matchs = []
            for i in range(nb_joueur // 2):
                while horaire_complet(nb_joueur, liste_matchs, heure_match):
                    heure_match += timedelta(minutes=6)
                liste_matchs.append([liste_joueurs.pop(randint(0, liste_joueurs.__len__() - 1)),
                                     liste_joueurs.pop(randint(0, liste_joueurs.__len__() - 1)), "Table ",
                                     heure_match.strftime("%H.%M.%d.%m.%Y")])
                heure_match = date_heure_debut
        elif format_tournoi == "Tournoi à la ronde":
            liste_matchs = []
            for i in range(joueurs.__len__()):
                for j in range(i + 1, joueurs.__len__()):
                    while (horaire_complet(nb_joueur, liste_matchs, heure_match)
                           or joue_deja_a_cette_heure(joueurs[i], heure_match, liste_matchs)
                           or joue_deja_a_cette_heure(joueurs[j], heure_match, liste_matchs)):
                        heure_match += timedelta(minutes=6)
                        print(date_heure_debut.strftime("%H.%M.%d.%m.%Y"))
                    liste_matchs.append([joueurs[i], joueurs[j], "Table ", heure_match.strftime("%H.%M.%d.%m.%Y")])
                    heure_match = date_heure_debut
        return liste_matchs

    def display_tournament(self):
        coll = self.db.tournoi
        found = []
        request = coll.find()

        for tournoi in request:
            filtered_tournament = {
                'nom_tournoi': tournoi.get('nom_tournoi', ''),
                'date_tournoi': tournoi.get('date_debut_tournoi', ''),
                'heure_debut_tournoi': tournoi.get('heure_debut_tournoi', ''),
                'nombre_participants': len(tournoi.get('liste_des_joueurs', []))
            }
            found.append(filtered_tournament)

        return found

    def supprimer_tournoi_par_nom(self, tournoi: str):
        coll = self.db.tournoi
        joueur = coll.find_one({"nom_tournoi": tournoi})
        if joueur:
            coll.delete_one({"nom_tournoi": tournoi})
            return " Ce tournoi a été supprimé ! :)"
        else:
            return "Le tournoi avec le nom donné n'existe pas dans la base de données."


if __name__ == '__main__':
    tournoi = Tournoi()
    print(
        tournoi.generer_tournoi(["Robin", "Faraz", "Thomas", "Arthur"], 4, 3,
                                datetime.now()))
