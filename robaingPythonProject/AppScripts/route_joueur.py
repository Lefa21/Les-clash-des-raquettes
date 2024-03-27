from flask import Blueprint, jsonify, request

from robaingPythonProject.AppClasses.Joueur import Joueur

joueur = Joueur()
personnes_bp = Blueprint('routes', __name__)


@personnes_bp.route('/', methods=['GET'])
def get_personnes():
    return jsonify(joueur.display_player())


@personnes_bp.route('/inserer_joueur', methods=['POST'])
def inserer_joueur():
    id = request.form.get('id')
    prenom = request.form.get('prenom')
    nom = request.form.get('nom')
    date_naissance = request.form.get('date_naissance')
    sexe = request.form.get('sexe')
    pseudo = request.form.get('pseudo')
    return joueur.inserer_joueur(id, prenom, nom, date_naissance, sexe, pseudo)


@personnes_bp.route('/supprimer_joueur', methods=['POST'])
def supprimer_joueur():
    pseudo = request.form.get('pseudo')
    return joueur.supprimer_joueur_par_nom(pseudo)


@personnes_bp.route('/modifier_joueur', methods=['POST'])
def modifier_joueur():
    pseudo = request.form.get('ancienPseudo')
    newpseudo = request.form.get('nouveauPseudo')
    return joueur.modifier_joueur_par_nom(pseudo, newpseudo)
