import { Component } from '@angular/core';
import {RouterLink, RouterOutlet} from "@angular/router";
@Component({
  selector: 'app-home-player',
  standalone: true,
  imports: [RouterLink, RouterOutlet],
  templateUrl: './home-player.component.html',
  styleUrl: './home-player.component.css'
})
export class HomePlayerComponent {

}
