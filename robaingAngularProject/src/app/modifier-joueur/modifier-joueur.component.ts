import {Component, OnInit} from '@angular/core';
import {RouterLink, RouterOutlet} from "@angular/router";
import {ApiService} from "../api.service";
import {NgIf, NgFor} from "@angular/common";

@Component({
  selector: 'app-modifier-joueur',
  standalone: true,
  imports: [RouterOutlet, RouterLink, NgIf, NgFor],
  templateUrl: './modifier-joueur.component.html',
  styleUrl: './modifier-joueur.component.css'
})
export class ModifierJoueurComponent implements OnInit{

  constructor(private apiService: ApiService) {
  }
  ngOnInit(): void {
    let baliseAncienPseudo = document.getElementById("ancienPseudo")
    let baliseNouveauPseudo = document.getElementById("nouveauPseudo")


  }

}
