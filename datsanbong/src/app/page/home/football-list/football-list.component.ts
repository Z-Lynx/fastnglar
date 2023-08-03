import { Component, Input } from '@angular/core';
import { FootballField } from '../football-field.model';

@Component({
  selector: 'app-football-list',
  templateUrl: './football-list.component.html',
})
export class FootballListComponent {
  @Input() football: FootballField | undefined;
}
