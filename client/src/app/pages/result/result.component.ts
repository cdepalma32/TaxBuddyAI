// client/src/app/pages/result/result.component.ts
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { TaxService, TaxEntry } from '../../services/tax.service';

@Component({
  selector: 'app-result',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './result.component.html',
  styleUrls: ['./result.component.scss']
})
export class ResultComponent {
  loading = true;
  errorMsg = '';
  data: TaxEntry | null = null;

  constructor(private route: ActivatedRoute, private tax: TaxService) {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.tax.getTax(id).subscribe({
      next: (entry) => { this.data = entry; this.loading = false; },
      error: (err) => { this.errorMsg = err?.error?.detail || 'Not found'; this.loading = false; }
    });
  }
}
