import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

// Define your interfaces for type safety
export interface CreateTaxPayload {
  income: number;
  deductions: number;
}

export interface CreateTaxResponse {
  tip: string;
  saved: boolean;
  id: number;
}

export interface TaxEntry {
  id: number;
  income: number;
  deductions: number;
  tip: string;
  created_at: string | null;
}

@Injectable({
  providedIn: 'root'
})
export class TaxService {
  private api = 'http://127.0.0.1:8000'; // your FastAPI base URL

  constructor(private http: HttpClient) {}

  // POST request — create new tax record
  createTax(body: CreateTaxPayload): Observable<CreateTaxResponse> {
    return this.http.post<CreateTaxResponse>(`${this.api}/tax/`, body);
  }

  // GET request — fetch single tax record by ID
  getTax(id: number): Observable<TaxEntry> {
    return this.http.get<TaxEntry>(`${this.api}/tax/${id}`);
  }
}
