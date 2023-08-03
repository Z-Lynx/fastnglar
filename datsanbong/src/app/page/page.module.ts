import { NgModule } from '@angular/core';
import { HomeComponent } from './home/home.component';
import { CommonModule } from '@angular/common';
import { TopBarComponent } from '../top-bar/top-bar.component';
import { PageRoutingModule } from './page-routing.module';
import { FootballListComponent } from './home/football-list/football-list.component';
import { CarouselModule } from 'ngx-bootstrap/carousel';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { ProfileComponent } from './profile/profile.component';
import { ReactiveFormsModule } from '@angular/forms';

@NgModule({
  declarations: [HomeComponent, TopBarComponent, FootballListComponent, LoginComponent, RegisterComponent, ProfileComponent],
// Import the ReactiveFormsModule
  imports: [CommonModule, PageRoutingModule, CarouselModule.forRoot(), ReactiveFormsModule],
})
export class PageModule {}
