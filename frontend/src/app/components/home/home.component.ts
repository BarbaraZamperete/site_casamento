import { Component, HostListener } from '@angular/core';
import { ApiService } from '../../services/api.service';

import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { FooterComponent } from '../shared/footer/footer.component';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss',
  standalone: true,
  imports: [CommonModule, HttpClientModule, FooterComponent]
})
export class HomeComponent {

  convidados: any[] = [];
  presentes: any[] = [];

  // Data do evento
  eventDate: Date = new Date('2027-27-03T18:00:00'); // Data do seu casamento
  days: number = 0;
  hours: number = 0;
  minutes: number = 0;
  seconds: number = 0;
  countdownInterval: any;

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {

  }

  @HostListener('window:scroll', ['$event'])
  onWindowScroll() {
    const navbar = document.querySelector('.navbar');
    if (navbar) {
      if (window.scrollY > window.innerHeight - 100) {
        navbar.classList.add('scrolled');
        navbar.classList.remove('bg-transparent');
      } else {
        navbar.classList.remove('scrolled');
        navbar.classList.add('bg-transparent');
      }
    }
  }

}
