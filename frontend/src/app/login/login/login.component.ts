import { Component, inject } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatDialog, MatDialogModule } from '@angular/material/dialog';
import { ContatoComponent } from '../contato/contato.component';
import { ResetSenhaComponent } from '../reset-senha/reset-senha.component';
import { enviroment } from '../../environment/environment';

const frontEndUrl = enviroment.frontEndUrl;

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [MatButtonModule, MatDialogModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {

  avisoLogin: boolean = false;

  readonly dialog = inject(MatDialog);

  abrirDialogContato() {
    const dialogRef = this.dialog.open(ContatoComponent);

    dialogRef.afterClosed().subscribe(result => {
      console.log(`Dialog result: ${result}`);
    });
  }

  abrirDialogResetSenha() {
    const dialogRef = this.dialog.open(ResetSenhaComponent);

    dialogRef.afterClosed().subscribe(result => {
      console.log(`Dialog result: ${result}`);
    });
  }

  abrirTelaPrincipal() {
    let email = ((<HTMLInputElement>document.getElementById("email")).value);
    let password = ((<HTMLInputElement>document.getElementById("password")).value);  
    if (email == "admin" && password == "admin") {
      window.location.href = `${frontEndUrl}/gerenciamento`;      
    } else {
      this.avisoLogin = true;
    }
  }
}
