import { Component, inject } from '@angular/core';
import { ShareService } from '../../services/share.service';
import { MatDialog, MatDialogModule } from '@angular/material/dialog';
import { ContatoComponent } from '../../login/contato/contato.component';
import { enviroment } from '../../environment/environment';
import { Router } from '@angular/router';

const frontEndUrl = enviroment.frontEndUrl;

@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [MatDialogModule],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.css'
})
export class NavbarComponent {

  readonly dialog = inject(MatDialog);
  mostrarFiltrar: boolean = false;

  constructor(private shareService: ShareService, private router: Router) { }

  filtrarMensagem() {
    this.mostrarFiltrar = !this.mostrarFiltrar;
    this.shareService.mostrarFiltrarResponder(this.mostrarFiltrar, false);
  }

  abrirDialogContato() {
    const dialogRef = this.dialog.open(ContatoComponent);

    dialogRef.afterClosed().subscribe(result => {
      console.log(`Dialog result: ${result}`);
    });
  }

  abrirConfigurar() {
    //window.location.href = `${frontEndUrl}/configurar`;
    this.router.navigate(['/configurar'])
  }

  abrirDashboardTotem() {
    //window.location.href = `${frontEndUrl}/totem`;
    this.router.navigate(['/totem'])
  }

  sair() {
    // window.location.href = `${frontEndUrl}/login`;
    this.router.navigate(['/login'])
  }
}
