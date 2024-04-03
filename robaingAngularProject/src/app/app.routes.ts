import { Routes } from '@angular/router';
import {ProjetS4Component} from "./projet-s4/projet-s4.component";
import {AfficherJoueurComponent} from "./afficher-joueur/afficher-joueur.component";
import {InsererJoueurComponent} from "./inserer-joueur/inserer-joueur.component";
import {ModifierJoueurComponent} from "./modifier-joueur/modifier-joueur.component";
import {SupprimerJoueurComponent} from "./supprimer-joueur/supprimer-joueur.component";
import {HomePlayerComponent} from "./home-player/home-player.component";
import {HomeTournamentComponent} from "./home-tournament/home-tournament.component";
import {InsererTournoiComponent} from "./inserer-tournoi/inserer-tournoi.component"

export const routes: Routes = [
  {path: '', component: ProjetS4Component},
  {path: 'projet-s4', component: ProjetS4Component},
  {path: 'afficher-joueur', component: AfficherJoueurComponent},
  {path: 'inserer-joueur', component: InsererJoueurComponent},
  {path: 'modifier-joueur', component: ModifierJoueurComponent},
  {path: 'supprimer-joueur', component: SupprimerJoueurComponent},
  {path: 'home-tournament', component: HomeTournamentComponent},
  {path: 'home-player', component: HomePlayerComponent},
  {path: 'inserer-tournoi', component: InsererTournoiComponent}
];
