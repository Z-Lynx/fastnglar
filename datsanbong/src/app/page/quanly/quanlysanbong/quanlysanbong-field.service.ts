// football-field.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import {
  SanBongField,
  SanBongPostField,
  SanBongPutField,
  SanBongResponseField,
} from './quanlysanbong-field.model';

@Injectable({
  providedIn: 'root',
})
export class SanBongFieldService {
  private apiUrl = 'http://127.0.0.1:8000/sanbongs'; // Replace 'YOUR_API_URL' with the actual API endpoint.
  private apiUrlPost = 'http://127.0.0.1:8000/sanbong'; // Replace 'YOUR_API_URL' with the actual API endpoint.

  constructor(private http: HttpClient) {}

  getSanBongFields(): Observable<SanBongField[]> {
    return this.http.get<SanBongField[]>(this.apiUrl);
  }

  postSanBongField(
    sanBongField: SanBongPostField
  ): Observable<SanBongResponseField> {
    return this.http.post<SanBongResponseField>(this.apiUrlPost, sanBongField);
  }

  putSanBongField(
    id: number,
    sanBongField: SanBongPutField
  ): Observable<SanBongResponseField> {
    const url = `${this.apiUrlPost}/${id}`;
    return this.http.put<SanBongResponseField>(url, sanBongField);
  }

  deleteSanBongField(id: number): Observable<SanBongField> {
    const url = `${this.apiUrlPost}/${id}`;
    return this.http.delete<SanBongField>(url);
  }
}
