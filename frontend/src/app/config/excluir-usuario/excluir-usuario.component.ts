import { Component, Inject } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MAT_DIALOG_DATA, MatDialogModule } from '@angular/material/dialog';
import { MatIconModule } from '@angular/material/icon';

@Component({
  selector: 'app-excluir-usuario',
  standalone: true,
  imports: [MatButtonModule, MatDialogModule, MatIconModule],
  templateUrl: './excluir-usuario.component.html',
  styleUrl: './excluir-usuario.component.css'
})
export class ExcluirUsuarioComponent {

  nome: string = '';

  constructor(@Inject(MAT_DIALOG_DATA) public data: any) {
    this.ngOnInit()
  }

  ngOnInit(): void {
    this.nome = this.data.nome;
  }

  inativarUsuario() {
    alert('TODO: inativar usuário: ' + this.nome)
  }

}
