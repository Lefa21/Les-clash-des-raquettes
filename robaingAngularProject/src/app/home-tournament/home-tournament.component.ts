import { Component } from '@angular/core';
import {RouterLink, RouterOutlet} from "@angular/router";
@Component({
  selector: 'app-home-tournament',
  standalone: true,
  imports: [RouterLink, RouterOutlet],
  templateUrl: './home-tournament.component.html',
  styleUrl: './home-tournament.component.css'
})
export class HomeTournamentComponent {

}
