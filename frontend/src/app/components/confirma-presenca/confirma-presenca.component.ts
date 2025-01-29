import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule, FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ApiService } from '../../services/api.service';
import { SimpleNavBarComponent } from "../shared/simple-nav-bar/simple-nav-bar.component";
import { FooterComponent } from "../shared/footer/footer.component";

@Component({
  selector: 'app-confirma-presenca',
  standalone: true,
  imports: [CommonModule, FormsModule, ReactiveFormsModule, SimpleNavBarComponent, FooterComponent],
  templateUrl: './confirma-presenca.component.html',
  styleUrl: './confirma-presenca.component.scss'
})
export class ConfirmaPresencaComponent {
  searchForm: FormGroup;
  isLoading = false;
  showResults = false;
  showNotFound = false;
  guests: Array<{id: string, name: string, confirmed: boolean}> = [];

  constructor(
    private apiService: ApiService,
    private formBuilder: FormBuilder
  ) {
    this.searchForm = this.formBuilder.group({
      searchType: ['code'],
      searchTerm: ['', Validators.required]
    });
  }

  onSearchTypeChange(type: 'code' | 'name'): void {
    this.searchForm.patchValue({ searchType: type, searchTerm: '' });
    this.showResults = this.showNotFound = false;
  }

  search(): void {
    if (this.searchForm.invalid) return;

    this.isLoading = true;
    this.showResults = this.showNotFound = false;

    const { searchType, searchTerm } = this.searchForm.value;
    const searchMethod = searchType === 'code' ?
      this.apiService.buscarPorConvite(searchTerm) :
      this.apiService.buscarPorNome(searchTerm);

    searchMethod.subscribe({
      next: (response) => {
        this.guests = response.map((guest: any) => ({
          id: guest.id,
          name: guest.nome,
          confirmed: false
        }));
        this.showResults = this.guests.length > 0;
        this.showNotFound = this.guests.length === 0;
        this.isLoading = false;
      },
      error: (error) => {
        console.error(`Erro ao buscar ${searchType === 'code' ? 'convite' : 'por nome'}:`, error);
        this.showNotFound = true;
        this.isLoading = false;
      }
    });
  }

  confirmPresence(): void {
    const confirmedGuests = this.guests.filter(guest => guest.confirmed);
    console.log('Convidados confirmados:', confirmedGuests);
  }
}
