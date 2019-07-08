import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {HttpClientModule} from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ListagemUsuariosComponent } from './listagem-usuarios/listagem-usuarios.component';
import { PaginationComponent } from './pagination/pagination.component';
import { CadastrosService } from './cadastros.service'
import {NgbModule} from '@ng-bootstrap/ng-bootstrap';
import { FormsModule } from '@angular/forms';


@NgModule({
  declarations: [
    AppComponent,
    ListagemUsuariosComponent,
    PaginationComponent
  ],
  imports: [
  	NgbModule,
  	FormsModule,
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [CadastrosService],
  bootstrap: [AppComponent]
})
export class AppModule { }
