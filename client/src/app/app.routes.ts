// client/src/app/app.routes.ts
import { Routes } from '@angular/router';
import { LoginComponent } from './pages/login/login.component';
import { TaxFormComponent } from './pages/tax-form/tax-form.component';
import { ResultComponent } from './pages/result/result.component';

export const appRoutes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: 'tax-form', component: TaxFormComponent },  // <-- add this
  { path: 'result', component: ResultComponent },
  { path: '', redirectTo: 'login', pathMatch: 'full' },
];
