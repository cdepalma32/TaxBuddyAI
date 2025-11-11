import { Injectable } from '@angular/core';
import { CanActivate, CanMatch, Router, UrlTree } from '@angular/router';

@Injectable({ providedIn: 'root' })
export class AuthGuard implements CanActivate, CanMatch {
  constructor(private router: Router) {}

  private isAuthed(): true | UrlTree {
    const token = localStorage.getItem('access_token');
    return token ? true : this.router.parseUrl('/login');
  }

  canActivate(): true | UrlTree { return this.isAuthed(); }
  canMatch(): true | UrlTree { return this.isAuthed(); }
}
