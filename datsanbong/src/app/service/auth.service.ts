// auth.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private baseUrl = 'http://127.0.0.1:8000';

  constructor(private http: HttpClient) {}

  login(email: string, password: string) {
    const body = { email, password };
    return this.http.post<any>(`${this.baseUrl}/login`, body);
  }
  
  register(userData: any) {
    return this.http.post<any>(`${this.baseUrl}/register`, userData);
  }

  info(){
    return this.http.get<any>(`${this.baseUrl}/users/me`,);
  }
}
