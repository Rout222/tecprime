import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})

export class CadastrosService {

	contatosUrl = 'http://127.0.0.1:5000/'

  constructor(private http: HttpClient) { }

  listar(page, per_page) {
  	return this.http.get<any[]>(`${this.contatosUrl}users?page=${page}&per\_page=${per_page}`)
  	// return this.http.get<any[]>(`${this.contatosUrl}users?page=${page}&per_page=&{per_page}`)
  }
}
