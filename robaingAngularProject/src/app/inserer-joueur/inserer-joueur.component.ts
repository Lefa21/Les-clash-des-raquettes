import { Component } from '@angular/core';
import {RouterLink, RouterOutlet} from "@angular/router";
import {Player} from "../Player";
import {ApiService} from "../api.service";
import {FormsModule} from "@angular/forms";
import {NgIf} from "@angular/common";
@Component({
  selector: 'app-inserer-joueur',
  standalone: true,
  imports: [RouterOutlet, RouterLink, FormsModule, NgIf],
  templateUrl: './inserer-joueur.component.html',
  styleUrl: './inserer-joueur.component.css'
})
export class InsererJoueurComponent {
  joueurData: Player = {
    nom: '',
    prenom: '',
    date_naissance: '',
    sexe: '',
    pseudo: ''
  };

  messageFromServer : string | undefined

  constructor(private joueurService: ApiService) { }

  onSubmit() {
    this.joueurService.addJoueur(this.joueurData).subscribe(
      response => {
        this.messageFromServer = response;
      },
    );
  }
}
