import math
from collections import Counter
from datetime import datetime, timedelta

from AppClasses.Connexion import Connexion
from AppScripts.methodesUtiles import *


def est_puissance_de_2(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0


def calcul_duree_poule(taille_poule, nb_table):
    return math.ceil(taille_poule * (taille_poule - 1) / 2 / nb_table * 5)


def determine_poule(nb_participants, nb_poule):
    return [nb_participants // nb_poule + (j and nb_participants % 2) for j in range(2)] if nb_poule == 2 else [
        nb_participants // nb_poule + j for j in [nb_participants / nb_poule % 1 >= 0.25 * k for k in range(1, 5)]]


def genere_format(nb_participants, nb_table, temps_max):
    choix = []
    duree_championat = calcul_duree_poule(nb_participants, nb_table)
    if nb_participants <= 8 and duree_championat <= temps_max:
        choix += [("RONDE", duree_championat)]

    duree_championat = sum(
        nb_participants / (2 ** x) for x in range(1, int(math.log2(nb_participants) + 1))) * 5 / nb_table
    if est_puissance_de_2(nb_participants) and duree_championat <= temps_max:
        choix += [("BRAQUET", duree_championat)]

    nb_joueurs_brackets = 4
    if nb_participants < nb_joueurs_brackets:
        return choix

    for nb_poule in [2, 4]:
        poules = determine_poule(nb_participants, nb_poule)
        if 2 in poules or 1 in poules:
            continue
        temp_tournoi = 5 * (3 if nb_table == 1 else 2) + sum(calcul_duree_poule(p, nb_table) for p in poules)
        if temp_tournoi <= temps_max:
            choix += [(f"POULE :{poules}", temp_tournoi)]
    return choix


def joue_deja_a_cette_heure(joueur_1: str, heure_match: datetime, liste_matchs: list):
    if not liste_matchs:
        return False
    for match in liste_matchs:
        if (joueur_1 == match[0] or joueur_1 == match[1]) and match[3] == heure_match.strftime(
                "%H:%M le %d.%m.%Y"):
            return True
    return False


def horaire_complet(nb_table: int, liste_matchs: list, heure_match: datetime):
    if not liste_matchs:
        return False
    compteur = 0
    for match in liste_matchs:
        if match[3] == heure_match.strftime("%H:%M le %d.%m.%Y"):
            compteur += 1
    return True if compteur == nb_table else False


def calcul_nb_phase(nb_joueurs):
    while nb_joueurs > 0:
        return


def nb_match_a_cette_heure(liste_match: list, heure_match: datetime):
    """
    Ici, on calcule le nombre de matchs à
    un horaire donné, mais la fonction a
    pour finalité d'attribuer un numéro
    de table à chaque match
    """

    if not liste_match:
        return 1
    compteur = 1
    for match in liste_match:
        if heure_match.strftime("%H:%M le %d.%m.%Y") == match[3]:
            compteur += 1
    return compteur


class Tournoi(Connexion):

    def __init__(self):
        Connexion.__init__(self)

    def inserer_tournoi(self, nom_tournoi: str,
                        date_debut_tournoi: str,
                        heure_debut_tournoi: str,
                        nombre_de_table: int,
                        liste_des_joueurs: list,
                        format: list):

        if not (nom_tournoi and date_debut_tournoi and heure_debut_tournoi and nombre_de_table and liste_des_joueurs):
            return "Certains paramètres sont vides ou nuls"

        if not liste_des_joueurs:
            return "La liste des joueurs est vide"

        liste_de_matchs = self.generer_tournoi_2(liste_des_joueurs, nombre_de_table,
                                                 datetime.strptime(date_debut_tournoi + " " + heure_debut_tournoi,
                                                                   "%Y-%m-%d %H:%M"), format)

        # liste_de_matchs = self.generer_tournoi(liste_des_joueurs, len(liste_des_joueurs), nombre_de_table,
        #                                        datetime.strptime(date_debut_tournoi + " " + heure_debut_tournoi,
        #                                                          "%Y-%m-%d %H:%M"))
        #
        coll = self.db.tournoi
        if self.tournoi_existe(nom_tournoi):
            return "Un tournoi ayant ce nom existe déjà"
        else:
            coll.insert_one(
                {"nom_tournoi": nom_tournoi, "date_debut_tournoi": date_debut_tournoi,
                 "heure_debut_tournoi": heure_debut_tournoi, "nombres_de_tables": nombre_de_table,
                 "liste_des_joueurs": liste_des_joueurs, "liste_des_matchs": liste_de_matchs})
            return "Tournoi inséré"

    def tournoi_existe(self, nom_tournoi: str):
        coll = self.db.tournoi
        requete = coll.find_one({"nom_tournoi": nom_tournoi})
        if requete is not None:
            return True
        else:
            return False

    def modifier_dateheure_tournoi(self, nom_tournoi: str, date_debut_tournoi: str, heure_debut_tournoi: str):
        coll = self.db.tournoi

        if self.tournoi_existe(nom_tournoi):
            tournoi_existant = coll.find_one({"nom_tournoi": nom_tournoi})
            liste_des_joueurs = tournoi_existant.get("liste_des_joueurs")
            nombre_de_table = tournoi_existant.get("nombres_de_tables")

            liste_de_matchs = self.generer_tournoi(liste_des_joueurs, nombre_de_table,
                                                   datetime.strptime(date_debut_tournoi + " " + heure_debut_tournoi,
                                                                     "%Y-%m-%d %H:%M"))

            coll.update_one({"nom_tournoi": nom_tournoi}, {"$set": {
                "date_debut_tournoi": date_debut_tournoi,
                "heure_debut_tournoi": heure_debut_tournoi,
                "liste_des_matchs": liste_de_matchs
            }})

            return "La date et l'heure du tournoi ont été mis à jour"
        else:
            return "Le tournoi n'existe pas"

    def afficher_match(self, nom_tournoi: str):
        coll = self.db.tournoi
        tournoi = coll.find_one({"nom_tournoi": nom_tournoi})
        if tournoi:
            matches = tournoi.get('liste_des_matchs', [])
            return matches
        else:
            return []

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

    def generer_tournoi_2(self, joueurs: list, nb_table: int, date_heure_debut: datetime, format: list):
        if "RONDE" in format[0]:
            pass
        else:  # avec poules
            _, poules = format[0].split(':')
            poules = [int(x) for x in poules.replace('[', '').replace(']', '').split(',')]
            matchs_poules = [
                [(joueurs[x + sum(poules[:i])], joueurs[y + + sum(poules[:i])]) for x in range(k) for y in range(x)] for
                i, k in enumerate(poules)]
            matchs_ordoner = []
            nb_match_poules = sum(x * (x - 1) / 2 for x in poules)
            index_poule = 0
            compteur_table = 0
            while len(matchs_ordoner) < nb_match_poules:
                if matchs_poules[index_poule]:
                    t = matchs_poules[index_poule].pop(0)
                    matchs_ordoner.append([
                        t[0],
                        t[1],
                        "Table " + str(compteur_table + 1),
                        date_heure_debut.strftime("%H:%M le %d.%m.%Y"),
                        date_heure_debut,
                        "Poule " + str(index_poule)
                    ])
                    compteur_table = (compteur_table + 1) % nb_table
                    if not compteur_table:
                        date_heure_debut += timedelta(minutes=8)
                index_poule = (index_poule + 1) % len(poules)
            return matchs_ordoner

    # def generer_tournoi(self, joueurs: list, nb_table: int, date_heure_debut: datetime):
    #     global liste_matchs
    #     nb_joueur = len(joueurs)
    #     format_tournoi = self.definir_format_tournoi(nb_joueur)
    #     liste_joueurs = joueurs.copy()
    #     heure_match = date_heure_debut
    #     if format_tournoi == "Elimination Simple":
    #         liste_matchs = []
    #         for i in range(nb_joueur // 2):
    #             while horaire_complet(nb_table, liste_matchs, heure_match):
    #                 heure_match += timedelta(minutes=6)
    #             numero_table = nb_match_a_cette_heure(liste_matchs, heure_match)
    #             liste_matchs.append([liste_joueurs.pop(randint(0, liste_joueurs.__len__() - 1)),
    #                                  liste_joueurs.pop(randint(0, liste_joueurs.__len__() - 1)),
    #                                  "Table " + str(numero_table),
    #                                  heure_match.strftime("%H:%M le %d.%m.%Y"), heure_match])
    #             heure_match = date_heure_debut
    #     elif format_tournoi == "Tournoi à la ronde":
    #         liste_matchs = []
    #         for i in range(joueurs.__len__()):
    #             for j in range(i + 1, joueurs.__len__()):
    #                 while (horaire_complet(nb_table, liste_matchs, heure_match)
    #                        or joue_deja_a_cette_heure(joueurs[i], heure_match, liste_matchs)
    #                        or joue_deja_a_cette_heure(joueurs[j], heure_match, liste_matchs)):
    #                     heure_match += timedelta(minutes=6)
    #                     print(date_heure_debut.strftime("%H.%M.%d.%m.%Y"))
    #                 numero_table = nb_match_a_cette_heure(liste_matchs, heure_match)
    #                 liste_matchs.append([joueurs[i], joueurs[j], "Table " + str(numero_table),
    #                                      heure_match.strftime("%H:%M le %d.%m.%Y"), heure_match])
    #                 heure_match = date_heure_debut
    #     return liste_matchs

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

    def mettre_a_jour_tournoi(self, nom_tournoi: str, gagnants: list):
        coll = self.db.tournoi
        tournoi = coll.find_one({"nom_tournoi": nom_tournoi})

        if len(gagnants) > 1:
            nombre_de_joueurs = len(tournoi.get("liste_des_joueurs", []))
            format_tournoi = self.definir_format_tournoi(nombre_de_joueurs)

            if format_tournoi == "Elimination Simple":
                match_dates = [datetime.strptime(match[3], "%H:%M le %d.%m.%Y") for match in
                               tournoi.get("liste_des_matchs")]
                nouv_date = max(match_dates) + timedelta(minutes=12)
                nouv_match = self.generer_tournoi(gagnants, len(gagnants), tournoi.get("nombres_de_tables"), nouv_date)
                coll.update_one({"nom_tournoi": nom_tournoi}, {"$set": {"liste_des_matchs": nouv_match}})
            elif format_tournoi == "Tournoi à la ronde":
                victoires_par_joueur = Counter(gagnants)
                gagnant = victoires_par_joueur.most_common(1)[0][0]
                coll.update_one({"nom_tournoi": nom_tournoi}, {"$set": {"gagnant": gagnant}, })
                coll.update_one({"nom_tournoi": nom_tournoi}, {"$unset": {"liste_des_matchs": ""}})

            elif format_tournoi == "POULE":
                for i in gagnants:
                    coll.insert_one({"nom_tournoi": nom_tournoi})
        else:
            gagnant_unique = gagnants[0]
            coll.update_one({"nom_tournoi": nom_tournoi}, {"$set": {"gagnant": gagnant_unique}})
            coll.update_one({"nom_tournoi": nom_tournoi}, {"$unset": {"liste_des_matchs": ""}})

    def retour_gagnant(self, nomTournoi: str):
        coll = self.db.tournoi
        tournoi = coll.find_one({"nom_tournoi": nomTournoi})

        if tournoi:
            gagnant = tournoi.get("gagnant")
            if gagnant is not None:
                return gagnant
        return "null"
