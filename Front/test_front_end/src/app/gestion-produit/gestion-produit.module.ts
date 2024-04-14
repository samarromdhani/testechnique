import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { DragulaModule } from 'ng2-dragula';
import { GestionProduitRoutingModule } from './gestion-produit-routing.module';
import { ProduitComponent } from './produit/produit.component';
import {MatCardModule} from "@angular/material/card";

import {DragDropModule} from '@angular/cdk/drag-drop';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

@NgModule({
  declarations: [ProduitComponent],
  imports: [
    CommonModule,
    GestionProduitRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    NgbModule,
    DragulaModule,
    DragDropModule,
    MatCardModule
  ]
})
export class GestionProduitModule { }
