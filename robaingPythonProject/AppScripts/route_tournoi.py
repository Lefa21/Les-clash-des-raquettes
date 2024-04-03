from flask import Blueprint, jsonify, request

from ProjetS4.robaingPythonProject.AppClasses.Tournoi import (Tournoi)

tournoi = Tournoi()

tournois_bp = Blueprint('routes', __name__)


@tournois_bp.route('/inserer_tournoi', methods=['POST'])
def inserer_tournoi():
    data = request.get_json()
    nom_tournoi = data['nom_tournoi']
    date_tournoi = data['date_tournoi']
    heure_debut_tournoi = data['heure_debut_tournoi']
    nombre_tables = data['nombre_tables']
    nombre_raquettes = data['nombre_raquettes']

    joueurs_participants = data['joueurs_participants']
    response = f"Nom du tournoi : {nom_tournoi}\nDate du tournoi : {date_tournoi}\nHeure de début du tournoi : {heure_debut_tournoi}\nNombre de tables : {nombre_tables}\nNombre de raquettes : {nombre_raquettes}\n\nParticipants :"
    for participant in joueurs_participants:
        response += f"\n- {participant}"

    return response
