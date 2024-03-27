import { Component } from '@angular/core';
import {RouterLink, RouterOutlet} from "@angular/router";

@Component({
  selector: 'app-supprimer-joueur',
  standalone: true,
  imports: [RouterOutlet, RouterLink],
  templateUrl: './supprimer-joueur.component.html',
  styleUrl: './supprimer-joueur.component.css'
})
export class SupprimerJoueurComponent {

}
