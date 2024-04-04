import { Component } from '@angular/core';
import {ApiService} from "../api.service";
import {AffichageTournament} from "../Tournament";
import {RouterLink} from "@angular/router";
import {NgForOf} from "@angular/common";


@Component({
  selector: 'app-afficher-tournoi',
  standalone: true,
  imports: [
    RouterLink,
    NgForOf
  ],
  templateUrl: './afficher-tournoi.component.html',
  styleUrl: './afficher-tournoi.component.css'
})

export class AfficherTournoiComponent {
  data: AffichageTournament[] = [];
  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.apiService.getAffichageTournament().subscribe(response => {
      this.data = response;
      console.log(this.data)
    });
  }
}
