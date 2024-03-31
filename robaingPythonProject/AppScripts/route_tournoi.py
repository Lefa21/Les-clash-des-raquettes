from flask import Blueprint, jsonify, request

from robaingPythonProject.AppClasses.Tournoi import (Tournoi)

tournoi = Tournoi()

tournois_bp = Blueprint('routes', __name__)

@tournois_bp.route('/inserer_tournoi', methods=['POST'])
def inserer_tournoi():
    data = request.get_json()
    nom_tournoi = data['nom_tournoi']
    date_tournoi =  data['date_tournoi']
    heure_debut_tournoi = data['heure_debut_tournoi']
    nombre_joueurs = data['nombre_joueurs']
    nombre_tables = data['nombre_tables']
    nombre_raquettes = data['nombre_raquettes']

    return f"Nom du tournoi : {nom_tournoi}\nDate du tournoi : {date_tournoi}\nHeure de début du tournoi : {heure_debut_tournoi}\nNombre de joueurs : {nombre_joueurs}\nNombre de tables : {nombre_tables}\nNombre de raquettes : {nombre_raquettes}"