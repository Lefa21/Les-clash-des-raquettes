import { Component } from '@angular/core';
import {FormsModule} from "@angular/forms";
import {NgIf} from "@angular/common";
import {Tournament} from "../Tournament";
import {Player} from "../Player";
import {ApiService} from "../api.service";

@Component({
  selector: 'app-inserer-tournoi',
  standalone: true,
  imports: [
    FormsModule,
    NgIf
  ],
  templateUrl: './inserer-tournoi.component.html',
  styleUrl: './inserer-tournoi.component.css'
})
export class InsererTournoiComponent {
  tournoiData: Tournament = {
    nom_tournoi: '',
    date_tournoi: '',
    heure_debut_tournoi: '',
    nombre_joueurs: null as unknown as number,
    nombre_tables: null as unknown as number,
    nombre_raquettes: null as unknown as number,
  }

  messageFromServer : string = '';
  constructor(private tournoiService: ApiService) { }
  onSubmit() {
    this.tournoiService.addTournoi(this.tournoiData).subscribe(
      (response : string) => {
        this.messageFromServer = response;
      },
    );
  }
}
