import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'environments/environment';
import { catchError, tap } from 'rxjs/operators';
import { from, Observable } from 'rxjs';
import { Produit } from 'app/models/produit.model';

@Injectable({
  providedIn: 'root'
})
export class ProduitService {
  public url:string=environment.urlAddress+"produit/";

  constructor(private http: HttpClient) { }

 list_produit(): Observable<Produit[]>{
    return this.http.get<[]>(this.url+"list/").pipe(
      tap(response => response ),
      catchError(ex => from([]))
  );
 }
 update_produit(produit){
  return this.http.put<[]>(this.url+"update/",produit);
}
}
