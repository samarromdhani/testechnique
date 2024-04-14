import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AcceuilComponent } from './acceuil/acceuil.component';
import { ProduitComponent } from './gestion-produit/produit/produit.component';

const routes: Routes = [
  { path: '', component: AcceuilComponent},
  { path: 'produit',
  loadChildren: () => import('./gestion-produit/gestion-produit.module').then(m => m.GestionProduitModule)}

  //{ path: '/categorie', component: ProduitComponent},

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
