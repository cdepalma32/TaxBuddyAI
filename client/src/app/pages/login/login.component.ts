// client/src/app/pages/login/login.component.ts
import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { Auth } from '../../services/auth.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
  standalone: true,
  imports: [CommonModule, FormsModule], // ngIf/ngFor + [(ngModel)]
})
export class LoginComponent {
  email = '';
  password = '';
  errorMsg = '';

  constructor(private auth: Auth, private router: Router) {}

  onSubmit() {
    this.auth.login(this.email, this.password).subscribe({
      next: () => this.router.navigate(['/tax-form']),
      error: () => (this.errorMsg = 'Invalid email or password'),
    });
  }
}
