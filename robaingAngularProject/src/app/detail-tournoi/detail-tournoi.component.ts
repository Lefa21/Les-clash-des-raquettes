import { Component, OnInit } from '@angular/core';
import {RouterLink, RouterOutlet} from '@angular/router';
import { ApiService } from '../api.service';
import {Matchs, nameTournament} from '../Tournament';
import {NgFor, NgIf} from "@angular/common";
import { ActivatedRoute } from '@angular/router';


@Component({
  selector: 'app-detail-tournoi',
  templateUrl: './detail-tournoi.component.html',
  imports:[RouterOutlet, RouterLink, NgIf, NgFor],
  styleUrls: ['./detail-tournoi.component.css'],
  standalone: true
})
export class DetailTournoiComponent implements OnInit {
  data: Matchs[] = [];
  nomTournoi: string | null = '';


  constructor(private route: ActivatedRoute, private apiService: ApiService) { }

  ngOnInit(): void {
    this.route.paramMap.subscribe(params => {
      this.nomTournoi = params.get('nomTournoi');
      if (this.nomTournoi != null) {
        this.apiService.getAffichageMatchTournament(this.nomTournoi).subscribe(matchs => {
          this.data = matchs;
        });
      }
    });
  }
}
