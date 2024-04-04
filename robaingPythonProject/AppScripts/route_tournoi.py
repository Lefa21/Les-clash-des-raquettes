from flask import Blueprint, jsonify, request

from robaingPythonProject.AppClasses.Tournoi import (Tournoi)

tournoi = Tournoi()

tournois_bp = Blueprint('routes', __name__)

@tournois_bp.route('/', methods=['GET'])
def get_tournois():
    return tournoi.display_tournament()

@tournois_bp.route('/inserer_tournoi', methods=['POST'])
def inserer_tournoi():
    data = request.get_json()
    nom_tournoi = data['nom_tournoi']
    date_tournoi = data['date_tournoi']
    heure_debut_tournoi = data['heure_debut_tournoi']
    nombre_tables = data['nombre_tables']
    joueurs_participants = data['joueurs_participants']

    return tournoi.inserer_tournoi(nom_tournoi, date_tournoi, heure_debut_tournoi, nombre_tables, joueurs_participants)

@tournois_bp.route('/supprimer_tournoi', methods=['POST'])
def suppr_tournoi():
    data = request.get_json()
    nom_tournoi = data['name']
    return tournoi.supprimer_tournoi_par_nom(nom_tournoi)

@tournois_bp.route('/modifier_dateheure_tournoi', methods=['POST'])
def modif_dateheure_tournoi():
    data = request.get_json()
    nom_tournoi = data['nom_tournoi']
    print(nom_tournoi)
    date_tournoi = data['date_tournoi']
    heure_debut_tournoi = data['heure_debut_tournoi']

    return tournoi.modifier_dateheure_tournoi(nom_tournoi, date_tournoi, heure_debut_tournoi)

@tournois_bp.route('/afficher_match', methods=['GET'])
def affichage_match():
    nom_tournoi = request.args.get('nom_tournoi')
    return jsonify(tournoi.afficher_match(nom_tournoi))

