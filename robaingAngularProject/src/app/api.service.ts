import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Player} from "./afficher-joueur/afficher-joueur.component";

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

  modifPseudo(): void {
    this.http.get('/api/personnes/modifier_joueur')
  }
}
