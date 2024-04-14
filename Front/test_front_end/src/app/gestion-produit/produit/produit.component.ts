import { Component, OnInit,ViewEncapsulation } from '@angular/core';
import { Produit } from 'app/models/produit.model';
import { ProduitService } from 'app/services/produit.service';
import { CdkDragDrop, moveItemInArray, transferArrayItem } from '@angular/cdk/drag-drop';
import { FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-produit',
  templateUrl: './produit.component.html',
  styleUrls: ['./produit.component.scss'],
  encapsulation: ViewEncapsulation.None

})
export class ProduitComponent implements OnInit {

  public listProduit:Produit[]=[];
  public list_fruit:Produit[]=[]
  public list_legumes:Produit[]=[]
  public list_viande:Produit[]=[]


  constructor(private produitService:ProduitService, 
       private formBuilder: FormBuilder
    ) { }

  public formGroup = this.formBuilder.group({
    produit_id:[],
    categories_Produit:[]
  })
  ngOnInit(): void {
    this.getListProduit();
  }
//Récupération de toute la liste des produits
  public getListProduit(){
    
    this.produitService.list_produit().subscribe(data=>{
      this.list_fruit=data.filter(item=>item.categories_Produit=='FRUIT')
      this.list_legumes=data.filter(item=>item.categories_Produit=='lEGUME')
      this.list_viande=data.filter(item=>item.categories_Produit=='VIANDE')


    })
  }
 //La fonction qui effectue le déplacement des élément
  drop(event: CdkDragDrop<string[]>) {
    if (event.previousContainer === event.container) {

      moveItemInArray(event.container.data,
         event.previousIndex,
          event.currentIndex);
    } else {
      //console.log('ok',event.previousContainer.data)
      let elementEnCoursDeChangement = event.container.data[event.currentIndex];

      transferArrayItem(event.previousContainer.data,
                        event.container.data,
                        event.previousIndex,
                        event.currentIndex);
    }
    //Vérifier le nouveau type ou l'élément est déplacé

if(this.verifelement(this.list_fruit,'FRUIT')){
}
 if(this.verifelement(this.list_viande,'VIANDE')){

}
 if( this.verifelement(this.list_legumes,'LEGUME')){
}


  }
  //Fonction pour vérifier la liste dans laquelle l'élement est déplacer
  verifelement(list:Produit[],categorie:string):Boolean{
   let index= list.findIndex(item=>item.categories_Produit!=categorie)
   if(index!=-1){
    //Remplir formGroup par l'élément à modifier
    this.formGroup.value['produit_id']=list[index]['produit_Id']
    this.formGroup.value['categories_Produit']=categorie
    //Mettre a jour l'élément
    this.miseAjour_produit();
    return true
   }
   return false;

  }
public miseAjour_produit(){
  this.produitService.update_produit(this.formGroup.value).subscribe(res=>{
  })
  
}

}
