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

  modifPseudo(): void {
    this.http.get('/api/personnes/modifier_joueur')
  }
}

