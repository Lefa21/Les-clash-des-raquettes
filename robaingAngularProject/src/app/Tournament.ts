
export interface Tournament {
    nom_tournoi: string;
    date_tournoi: string;
    heure_debut_tournoi: string;
    joueurs_participants: string[]
    nombre_tables: number;
    liste_matchs: Matchs[]
  }

export interface AffichageTournament {
  date_tournoi: string;
  heure_debut_tournoi: string;
  nom_tournoi: string;
  nombre_participants: number;
}


export interface Matchs {
    joueur_1: string;
    joueur_2: string;
    table : string;
    horaire : string;
  }

  export interface newDateAndHourTournament {
    nom_tournoi: string;
    date_tournoi: string;
    heure_debut_tournoi: string;
  }

  export class nameTournament{
    name: string;
    constructor(name: string) {
  this.name = name;
}
  }
