import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Player, NewNamePlayer} from "./Player";
import {Tournament} from "./Tournament";

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  constructor(private http: HttpClient) { }
  getAffichage(): Observable<Player[]> {
    return this.http.get<Player[]>(`/api/personnes/`)
  }

  addJoueur(player: Player): Observable<string> {
    return this.http.post('/api/personnes/inserer_joueur', player, { responseType: 'text' })
  }

  addTournoi(tournament : Tournament): Observable<string>{
    return this.http.post('/api/tournois/inserer_tournoi', tournament, { responseType: 'text' })
  }

  sendFile(fichier: File): Observable<string> {
    const formData = new FormData();
    formData.append('fichier', fichier);
    return this.http.post('/api/personnes/inserer_les_joueurs', formData, { responseType: 'text' });
  }

  modifierJoueurPseudo(formData: NewNamePlayer): Observable<string> {
    return this.http.post('/api/personnes/modifier_joueur', formData, { responseType: 'text' });
  }
}

