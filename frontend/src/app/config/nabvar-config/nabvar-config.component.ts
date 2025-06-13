import { Component, inject } from '@angular/core';
import { enviroment } from '../../environment/environment';
import { ContatoComponent } from '../../login/contato/contato.component';
import { MatDialog, MatDialogModule } from '@angular/material/dialog';
import { Router } from '@angular/router';

const frontEndUrl = enviroment.frontEndUrl;

@Component({
  selector: 'app-nabvar-config',
  standalone: true,
  imports: [MatDialogModule],
  templateUrl: './nabvar-config.component.html',
  styleUrl: './nabvar-config.component.css'
})
export class NabvarConfigComponent {

  readonly dialog = inject(MatDialog);

  constructor(private router: Router) { }

  voltarGerenciamento() {
    // window.location.href = `${frontEndUrl}/gerenciamento`;
    this.router.navigate(['/gerenciamento'])
  }

  abrirDialogContato() {
    const dialogRef = this.dialog.open(ContatoComponent);

    dialogRef.afterClosed().subscribe(result => {
      console.log(`Dialog result: ${result}`);
    });
  }

  sair() {
    // window.location.href = `${frontEndUrl}/login`;
    this.router.navigate(['/login'])
  }

}
