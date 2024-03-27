from flask import Blueprint, jsonify, request

from robaingPythonProject.AppClasses.Joueur import Joueur

joueur = Joueur()
personnes_bp = Blueprint('routes', __name__)


@personnes_bp.route('/', methods=['GET'])
def get_personnes():
    return jsonify(joueur.display_player())


@personnes_bp.route('/inserer_joueur', methods=['POST'])
def inserer_joueur():
    data = request.get_json()
    prenom = data['prenom']
    nom =  data['nom']
    date_naissance = data['date_naissance']
    sexe = data['sexe']
    pseudo = data['pseudo']
    return joueur.inserer_joueur(prenom, nom, date_naissance, sexe, pseudo)




@personnes_bp.route('/supprimer_joueur', methods=['POST'])
def supprimer_joueur():
    pseudo = request.form.get('pseudo')
    return joueur.supprimer_joueur_par_nom(pseudo)


@personnes_bp.route('/modifier_joueur', methods=['POST'])
def modifier_joueur():
    pseudo = request.form.get('ancienPseudo')
    newpseudo = request.form.get('nouveauPseudo')
    return joueur.modifier_joueur_par_nom(pseudo, newpseudo)