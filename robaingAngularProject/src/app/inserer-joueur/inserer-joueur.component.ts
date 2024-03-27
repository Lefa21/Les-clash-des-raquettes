import { Component } from '@angular/core';
import {RouterLink, RouterOutlet} from "@angular/router";

@Component({
  selector: 'app-inserer-joueur',
  standalone: true,
  imports: [RouterOutlet, RouterLink],
  templateUrl: './inserer-joueur.component.html',
  styleUrl: './inserer-joueur.component.css'
})
export class InsererJoueurComponent {

}
