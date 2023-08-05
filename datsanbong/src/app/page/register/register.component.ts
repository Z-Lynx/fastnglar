// login.component.ts
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { CookieService } from 'ngx-cookie-service';
import { AuthService } from 'src/app/service/auth.service';
import { NgToastService } from 'ng-angular-popup';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
})
export class RegisterComponent implements OnInit {
  public registerForm!: FormGroup;

  constructor(
    private fb: FormBuilder,
    private cookieService: CookieService,
    private authService: AuthService,
    private toast: NgToastService,
    private readonly _router: Router
  ) {}

  ngOnInit(): void {
    this.createRegisterForm();
  }

  createRegisterForm(): void {
    this.registerForm = this.fb.group({
      ho_ten: ['', [Validators.required]],
      sdt: ['', [Validators.required]],
      ngay_sinh: ['', [Validators.required]],
      email: ['', [Validators.required, Validators.email]],
      dia_chi: ['', [Validators.required]],
      id_phuong_xa: [1],
      mat_khau: ['', [Validators.required]],
      id_phan_quyen_nguoi_dung: [0],
    });
  }
  onSubmit(): void {
    if (this.registerForm.invalid) {
      return;
    }
    if (this.registerForm.value['id_phan_quyen_nguoi_dung'] == true) {
      this.registerForm.value['id_phan_quyen_nguoi_dung'] = 1;
    }

    const formData = this.registerForm.value;

    this.authService.register(formData).subscribe(
      (response) => {
        this.toast.success({
          detail: 'SUCCESS',
          summary: 'Đăng nhập thành công',
          duration: 5000,
        });
        this.cookieService.set('token_jwt', response.access_token);
        this.authService.info().subscribe(
          (response) => {
            console.log(response);
            localStorage.setItem('user', JSON.stringify(response));
            this._router.navigate(['/home']);
          },  
          (error) => {}
        );
      },
      (error) => {
        // Handle error response here, e.g., show an error message
        this.toast.error({
          detail: 'ERROR',
          summary: error.error.detail,
          duration: 5000,
        });
      }
    );
  }
}
