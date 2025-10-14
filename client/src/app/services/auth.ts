import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { tap } from 'rxjs/operators';
import { Observable } from 'rxjs';

interface LoginResponse {
  access_token: string;
  user: { email: string; role?: string };
}

@Injectable({ providedIn: 'root' })
export class Auth {
  private API = 'http://127.0.0.1:8000';

  constructor(private http: HttpClient) {}

  login(email: string, password: string): Observable<LoginResponse> {
    return this.http.post<LoginResponse>(`${this.API}/auth/login`, { email, password })
      .pipe(
        tap(res => {
          localStorage.setItem('access_token', res.access_token);
          localStorage.setItem('user_email', res.user?.email ?? '');
        })
      );
  }

  logout() {
    localStorage.removeItem('access_token');
    localStorage.removeItem('user_email');
  }

  get token(): string | null { return localStorage.getItem('access_token'); }
  isLoggedIn(): boolean { return !!this.token; }
}
