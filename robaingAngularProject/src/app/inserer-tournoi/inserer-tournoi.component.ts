import { Component } from '@angular/core';
import {FormsModule} from "@angular/forms";
import {NgForOf, NgIf} from "@angular/common";
import {Tournament} from "../Tournament";
import {Player} from "../Player";
import {ApiService} from "../api.service";

@Component({
  selector: 'app-inserer-tournoi',
  standalone: true,
  imports: [
    FormsModule,
    NgIf,
    NgForOf
  ],
  templateUrl: './inserer-tournoi.component.html',
  styleUrl: './inserer-tournoi.component.css'
})
export class InsererTournoiComponent {
  tournoiData: Tournament = {
    nom_tournoi: '',
    date_tournoi: '',
    heure_debut_tournoi: '',
    joueurs_participants: [],
    nombre_tables: null as unknown as number,

  }
  joueurs: Player[] = [];
  messageFromServer : string = '';
  constructor(private tournoiService: ApiService) {}

  ngOnInit(): void {
    this.tournoiService.getAffichage().subscribe(
      (joueurs: Player[]) => {
        this.joueurs = joueurs;
      },
    );
  }
  selectedPlayer: Player | null = null;

  addPlayer() {
    if (this.selectedPlayer) {
      this.tournoiData.joueurs_participants.push(this.selectedPlayer.pseudo);
      this.joueurs = this.joueurs.filter(joueur => joueur !== this.selectedPlayer);
      this.selectedPlayer = null;
    }
  }
  onSubmit() {
    this.tournoiService.addTournoi(this.tournoiData).subscribe(
      (response : string) => {
        this.messageFromServer = response;
      },
    );
  }
}
