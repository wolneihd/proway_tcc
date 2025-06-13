import { Component } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatDialogModule } from '@angular/material/dialog';
import { MatIconModule } from '@angular/material/icon';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-reset-senha',
  standalone: true,
  imports: [MatButtonModule, MatDialogModule, MatIconModule],
  templateUrl: './reset-senha.component.html',
  styleUrl: './reset-senha.component.css'
})
export class ResetSenhaComponent {

  constructor(private api: ApiService) { }

  reenviarEmail() {
    let email = ((<HTMLInputElement>document.getElementById("email-usuario")).value);    

    this.api.reenvioSenha(email).subscribe({
      next: (resposta) => {},
      error: erro => {
        console.error(erro)
        alert("Erro ao enviar e-mail com nova senha!");
      }
    })  
  }

}
