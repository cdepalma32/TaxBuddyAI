// This file is where the Angular service logic is defined

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TaxService {
  private api = 'http://localhost:8000'; // Or the deployed FastAPI base URL

  constructor(private http: HttpClient) {}

  postTaxForm(data: any): Observable<any> {
    return this.http.post(`${this.api}/tax`, data);
  }
}
