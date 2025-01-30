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
  isConfirming = false;
  confirmationSuccess = false;
  confirmationError = '';

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
    if (this.isConfirming) return;

    const guestsToConfirm = this.guests.map(guest => ({
      id: Number(guest.id),
      presenca_confirmada: guest.confirmed
    }));

    if (guestsToConfirm.length === 0) {
      this.confirmationError = 'Por favor, selecione pelo menos um convidado.';
      return;
    }

    this.isConfirming = true;
    this.confirmationError = '';
    this.confirmationSuccess = false;

    this.apiService.confirmarPresenca(guestsToConfirm).subscribe({
      next: (response) => {
        this.confirmationSuccess = true;
        this.isConfirming = false;
        this.showResults = false;
        this.searchForm.reset({ searchType: 'code' });
      },
      error: (error) => {
        console.error('Erro ao confirmar presença:', error);
        this.confirmationError = 'Ocorreu um erro ao confirmar a presença. Por favor, tente novamente.';
        this.isConfirming = false;
      }
    });
  }

  clearMessages(): void {
    this.confirmationSuccess = false;
    this.confirmationError = '';
  }
}
