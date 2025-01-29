import { Routes } from '@angular/router';

export const routes: Routes = [
  {
    path: '',
    loadComponent: () => import('./components/home/home.component').then(m => m.HomeComponent)
  },
  {
    path: 'confirmacao',
    loadComponent: () => import('./components/confirma-presenca/confirma-presenca.component').then(m => m.ConfirmaPresencaComponent)
  },
  {
    path: 'lista-presentes',
    loadComponent: () => import('./components/lista-presentes/lista-presentes.component').then(m => m.ListaPresentesComponent)
  },
];
