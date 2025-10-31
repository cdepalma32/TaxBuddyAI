import { Injectable } from '@angular/core';
import {
  HttpEvent,
  HttpHandler,
  HttpInterceptor,
  HttpRequest
} from '@angular/common/http';
import { Observable } from 'rxjs';
import { Auth } from './auth';

@Injectable()
export class TokenInterceptor implements HttpInterceptor {
  constructor(private auth: Auth) {}

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    // Only attach for POST /tax requests
    const isPost = req.method.toUpperCase() === 'POST';
    const hitsTaxRoute = /\/tax(?:\/?$|\?)/.test(req.url);

    if (!isPost || !hitsTaxRoute || req.headers.has('Authorization')) {
      return next.handle(req);
    }

    const token = this.auth.token; // reads 'access_token' from localStorage
    if (!token) return next.handle(req);

    const authReq = req.clone({
      setHeaders: { Authorization: `Bearer ${token}` }
    });

    return next.handle(authReq);
  }
}
