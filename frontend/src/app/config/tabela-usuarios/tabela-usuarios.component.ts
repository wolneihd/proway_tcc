import { Component, inject } from '@angular/core';
import { ApiService } from '../../services/api.service';
import { User } from '../../entidades/User';
import { MatDialog, MatDialogModule } from '@angular/material/dialog';
import { UserConfigComponent } from '../user-config/user-config.component';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { ExcluirUsuarioComponent } from '../excluir-usuario/excluir-usuario.component';

@Component({
  selector: 'app-tabela-usuarios',
  standalone: true,
  imports: [MatButtonModule, MatDialogModule, MatIconModule],
  templateUrl: './tabela-usuarios.component.html',
  styleUrl: './tabela-usuarios.component.css'
})
export class TabelaUsuariosComponent {

  readonly dialog = inject(MatDialog);

  constructor(private api: ApiService) { }

  usuarios: User[] = [];

  ngOnInit() {
    this.api.obterTodosUsuarios().subscribe({
      next: res => {
        this.usuarios = res;
        // console.log(this.usuarios);
      },
      error: erro => {
        console.error(erro)
      }
    })
  }

  editarUsuario(nome: string, email: string) {
    const dialogRef = this.dialog.open(UserConfigComponent, {
      data: {
        titulo: "Editar usuário",
        nome: nome,
        email: email
      }
    });
  }

  excluirUsuario(nome: string) {
    const dialogRef = this.dialog.open(ExcluirUsuarioComponent, {
      data: {
        nome: nome,
      }
    });
  }

  novoUsuario() {
    const dialogRef = this.dialog.open(UserConfigComponent, {
      data: {
        titulo: "Digite os dados do novo usuário",
      }
    });
  }

}
