import { Component, OnInit } from '@angular/core';

import {CadastrosService} from '../cadastros.service';

@Component({
  selector: 'app-listagem-usuarios',
  templateUrl: './listagem-usuarios.component.html',
  styleUrls: ['./listagem-usuarios.component.css']
})
export class ListagemUsuariosComponent implements OnInit {


  constructor(private cadastrosService: CadastrosService) { }
  users: Array<any>;
  ngOnInit() {
  	this.page = 1;
  	this.per_page = 3;
  	this.listar();
  }

  listar(){
  	this.cadastrosService.listar(this.page, this.per_page).subscribe(res => {
  														this.users = res['data']; 
  														this.page = res['page']; 
  														this.per_page = res['per_page']; 
  														this.total = res['total'];
  													});

  }

  carregarPagina(event){
  	this.cadastrosService.listar(event, this.per_page).subscribe(res => {
  														this.users = res['data']; 
  														this.page = res['page']; 
  														this.per_page = res['per_page']; 
  														this.total = res['total'];
  													});
  }

} 