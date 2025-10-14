// client/src/app/pages/tax-form/tax-form.component.ts
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-tax-form',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './tax-form.component.html',
  styleUrls: ['./tax-form.component.scss']
})
export class TaxFormComponent {
  income = 0;
  deductions = 0;
  tip = '';
  loading = false;
  errorMsg = '';

  constructor(private http: HttpClient) {}

  submit() {
    this.loading = true;
    this.errorMsg = '';
    this.tip = '';

    this.http.post<{ tip: string }>('http://127.0.0.1:8000/tax/', {
      income: this.income,
      deductions: this.deductions
    }).subscribe({
      next: res => { this.tip = res.tip; this.loading = false; },
      error: err => { this.errorMsg = err?.error?.detail || 'Request failed'; this.loading = false; }
    });
  }
}
