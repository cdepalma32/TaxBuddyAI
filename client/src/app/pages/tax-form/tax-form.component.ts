// client/src/app/pages/tax-form/tax-form.component.ts
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { TaxService, CreateTaxResponse } from '../../services/tax.service';

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
  loading = false;
  errorMsg = '';

  constructor(private tax: TaxService, private router: Router) {}

  submit() {
    this.loading = true;
    this.errorMsg = '';

    this.tax.createTax({ income: this.income, deductions: this.deductions })
      .subscribe({
        next: (res: CreateTaxResponse) => {
          this.router.navigate(['/result', res.id]); // deep-linkable result
        },
        error: (err) => {
          this.errorMsg = err?.error?.detail || 'Request failed';
          this.loading = false;
        },
        complete: () => { this.loading = false; }
      });
  }
}
