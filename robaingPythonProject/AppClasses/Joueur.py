from Connexion import Connexion
import json

class Joueur(Connexion):


    def __init__(self):
        Connexion.__init__(self)



    def inserer_joueur(self,id: int, prenom : str, nom : str, date_naissance : str, sexe : str, pseudo : str):
        """Insère un joueur avec tous les attributs entrés, ssi un joueur avec le même prénom,
         le même nom et la même date de naissance n'existe pas"""
        coll = self.db.personnes
        if self.joueur_existe(nom, prenom, date_naissance):
            return "Ce joueur existe déjà, il n'a pas été inséré"
        else:
            coll.insert_one(
                {"_id":id, "prenom": prenom, "nom": nom, "date_naissance": date_naissance, "sexe": sexe, "pseudo": pseudo})
            return "Ce joueur a été inséré ! "




    def joueur_existe(self,nom: str, prenom: str, dateDeNaissance: str):
        coll = self.db.personnes
        requete = coll.find_one({"nom": nom, "prenom": prenom, "date_naissance": dateDeNaissance})
        if (requete != None):
            return True
        else:
            return False



    def supprimer_joueur_par_pseudo(self, pseudo: str):
        coll = self.db.personnes
        coll.delete_one({"pseudo": pseudo})
        return "Si il existait, ce joueur a été supprimé ! :)"



    def modifier_joueur_par_pseudo(self, pseudo: str, nouveau_pseudo: str) -> None:
        coll = self.db.personnes
        coll.update_one({"pseudo": pseudo}, {"$set": {"pseudo": nouveau_pseudo}})
        return "Si il existe, ce joueur a été modifié !"



    def afficher_joueur(self):
        coll = self.db.personnes
        found = []
        requete = coll.find()

        for personne in requete:
            found.append(personne)
        return found


if __name__ == "__main__":
    j = Joueur()
    print(j.afficher_joueur())