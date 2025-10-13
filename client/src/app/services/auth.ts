// client/src/app/services/auth.ts
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, tap } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class Auth {
  private apiUrl = 'http://127.0.0.1:8000/auth/login';

  constructor(private http: HttpClient) {}

  /** Perform login and store the JWT in localStorage */
  login(email: string, password: string): Observable<any> {
    const body = new URLSearchParams();
    body.set('username', email);      // FastAPI expects OAuth2 username
    body.set('password', password);

    const headers = new HttpHeaders({
      'Content-Type': 'application/x-www-form-urlencoded'
    });

    return this.http.post<{ access_token: string }>(this.apiUrl, body.toString(), { headers })
      .pipe(
        tap(response => {
          localStorage.setItem('access_token', response.access_token);
        })
      );
  }

  /** Remove JWT (logout) */
  logout(): void {
    localStorage.removeItem('access_token');
  }

  /** Retrieve stored JWT */
  getToken(): string | null {
    return localStorage.getItem('access_token');
  }

  /** Simple check for logged-in state */
  isAuthenticated(): boolean {
    return !!this.getToken();
  }
}
