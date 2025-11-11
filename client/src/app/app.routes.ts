import { Routes } from '@angular/router';
import { LoginComponent } from './pages/login/login.component';
import { TaxFormComponent } from './pages/tax-form/tax-form.component';
import { ResultComponent } from './pages/result/result.component';
import { AuthGuard } from './guards/auth.guard';

export const appRoutes: Routes = [
  // Only show login if NOT authenticated
  { path: 'login', component: LoginComponent },

  // Protected routes (token required)
  { path: 'tax-form', component: TaxFormComponent, canActivate: [AuthGuard], canMatch: [AuthGuard] },
  { path: 'result/:id', component: ResultComponent, canActivate: [AuthGuard], canMatch: [AuthGuard] },

  // Default
  { path: '', pathMatch: 'full', redirectTo: 'login' },
  { path: '**', redirectTo: 'login' },
];
