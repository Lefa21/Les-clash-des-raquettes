import {Component, OnInit} from '@angular/core';
import {RouterLink, RouterOutlet} from "@angular/router";
import {ApiService} from "../api.service";
import {NgIf, NgFor} from "@angular/common";
import {resolve} from "node:path";

export interface Player {
  nom: string;
  prenom: string;
  date_naissance: string;
  sexe: string;
  pseudo: string;
}

@Component({
  selector: 'app-afficher-joueur',
  standalone: true,
  imports: [RouterOutlet, RouterLink, NgIf, NgFor],
  templateUrl: './afficher-joueur.component.html',
  styleUrl: './afficher-joueur.component.css'
})
export class AfficherJoueurComponent implements OnInit{
  data: Player[] = [];

  constructor(private apiService: ApiService) {
  }

  ngOnInit(): void {
    this.apiService.getAffichage().subscribe(response => {
      console.log(response);
      this.data = response;

    });
  }
}
