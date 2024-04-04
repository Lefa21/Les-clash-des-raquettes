import { Component, OnInit } from '@angular/core';
import {ActivatedRoute, RouterLink, RouterOutlet} from '@angular/router';
import { ApiService } from '../api.service';
import {Matchs, nameTournament} from '../Tournament';
import {NgFor, NgIf} from "@angular/common";

@Component({
  selector: 'app-detail-tournoi',
  templateUrl: './detail-tournoi.component.html',
  imports:[RouterOutlet, RouterLink, NgIf, NgFor],
  styleUrls: ['./detail-tournoi.component.css'],
  standalone: true
})
export class DetailTournoiComponent implements OnInit {
  data: Matchs[] = [];
  nomTournoi: nameTournament = { name: '' };


  constructor(private route: ActivatedRoute, private apiService: ApiService) { }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      let nomTournoi = params['nomTournoi'];
      this.loadMatches();
    });
  }

  loadMatches() {
    this.apiService.getAffichageMatchTournament(this.nomTournoi).subscribe(response => {
      this.data = response;
      console.log(this.data);
    });
  }
}
