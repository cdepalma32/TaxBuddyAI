import { Injectable } from '@angular/core';
import {
  HttpInterceptor, HttpRequest, HttpHandler, HttpEvent, HttpErrorResponse,
  HTTP_INTERCEPTORS
} from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { Router } from '@angular/router';
import { Auth } from '../services/auth.service';

// optional: use environment.apiBase like 'http://127.0.0.1:8000'
const API_BASE = 'http://127.0.0.1:8000';

@Injectable()
export class AuthInterceptor implements HttpInterceptor {
  constructor(private auth: Auth, private router: Router) {}

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    let request = req;

    const token = this.auth.token; // read from localStorage or service getter
    const url = req.url;

    // Only attach to calls going to your backend
    const isApiCall =
      url.startsWith(API_BASE) || url.startsWith('/api') || url.startsWith('/tax') || url.startsWith('/auth');

    // Skip auth endpoints
    const isAuthEndpoint = /\/auth\/(login|register)\b/.test(url);

    if (token && isApiCall && !isAuthEndpoint && !req.headers.has('Authorization')) {
      request = req.clone({
        setHeaders: { Authorization: `Bearer ${token}` }
      });
    }

    return next.handle(request).pipe(
      catchError((err: any) => {
        if (err instanceof HttpErrorResponse && err.status === 401) {
          // Token invalid/expired → clear and go to login
          this.auth.logout?.(); // if you have a logout() that clears storage
          this.router.navigate(['/login']);
        }
        return throwError(() => err);
      })
    );
  }
}
