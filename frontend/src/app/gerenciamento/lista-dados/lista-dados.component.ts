import { Component, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Usuario } from '../../entidades/Usuarios';
import { CommonModule } from '@angular/common';
import { Mensagem } from '../../entidades/Usuarios';
import { FormsModule } from '@angular/forms';
import { ShareService } from '../../services/share.service';
import { ApiService } from '../../services/api.service';
import { MatDialog } from '@angular/material/dialog';
import { DialogImagemComponent } from '../dialog-imagem/dialog-imagem.component';
import { MatIconModule } from '@angular/material/icon';
import { ReprocessarComponent } from '../reprocessar/reprocessar.component';

@Component({
  selector: 'app-lista-dados',
  standalone: true,
  imports: [CommonModule, FormsModule, MatIconModule],
  templateUrl: './lista-dados.component.html',
  styleUrl: './lista-dados.component.css'
})
export class ListaDadosComponent {

  usuarios: Usuario[] = [];
  mensagens: Mensagem[] = [];

  isResponderSelecionado: boolean = false;
  btnResponder: boolean = false;
  usuarioSelecionado: number = -1;

  isDadosFiltrados: boolean = false;

  constructor(
    private share: ShareService,
    private api: ApiService
  ) { }

  ngOnInit() {
    this.carregarUsuarios();
    this.atualizarUsuariosFiltrados()
  }

  limparFiltros() {
    this.isDadosFiltrados = false;
    this.carregarUsuarios();
    this.mensagens = [];
  }

  atualizarUsuariosFiltrados() {
    this.share.obterUsuariosFiltrados().subscribe(
      (usuarios: Usuario[]) => {
        this.usuarios = usuarios;
        this.isDadosFiltrados = true;
        this.mensagens = [];
      },
      (error) => {
        console.error('Erro ao receber os dados no Componente A:', error);
      }
    );
  }

  carregarUsuarios() {
    this.api.obterDadosTabela().subscribe({
      next: res => {
        console.log(res)
        this.usuarios = res
      },
      error: erro => console.error(erro)
    });
  }

  informarStatus(codigo: number): String {
    if (codigo === 0) {
      return "Em aberto";
    } else {
      return "Respondido"
    }
  }

  informarTipo(tipo: string): String {
    if (tipo === "text") {
      return "Texto";
    } else if (tipo === "voice") {
      return "Audio"
    } else {
      return "Imagem"
    }
  }

  checkSelecionado(mensagem: Mensagem) {
    mensagem.checkbox = !mensagem.checkbox;
  }

  isUsuarioSelecionado: boolean = false;
  verMensagens(mensagens: Mensagem[], id: number) {
    if (!this.isUsuarioSelecionado) {
      this.mensagens = mensagens;
      this.btnResponder = true;
      this.usuarioSelecionado = id
    } else {
      this.mensagens = [];
    }
    this.isUsuarioSelecionado = !this.isUsuarioSelecionado;
  }

  responderMensagem(usuarios: Usuario[]) {
    let isOneSelected = false;
    for (const usuario of usuarios) {
      for (const msg of usuario.mensagens) {
        if (msg.checkbox) {
          isOneSelected = true;
        }
      }
    }
    if (isOneSelected) {
      this.share.shareMensagem(usuarios, this.usuarioSelecionado);
      this.isResponderSelecionado = !this.isResponderSelecionado;
      this.share.mostrarFiltrarResponder(false, this.isResponderSelecionado)
    } else {
      alert('Nenhuma opção foi selecionada para resposta. Favor escolher pelo menos uma opção!')
    }
  }

  verUmaMensagem(mensagem: Mensagem) {
    alert(mensagem.texto_msg)
  }

  converterTimestampData(timestamp: number): string {
    const data = new Date(timestamp * 1000);
    const dia = data.getDate().toString().padStart(2, '0');
    const mes = (data.getMonth() + 1).toString().padStart(2, '0'); // Mês começa do 0
    const ano = data.getFullYear();
    return `${dia}/${mes}/${ano}`;
  }

  converterTimestampHora(timestamp: number): string {
    const data = new Date(timestamp * 1000);
    const horas = data.getHours().toString().padStart(2, '0');
    const minutos = data.getMinutes().toString().padStart(2, '0');
    return `${horas}:${minutos}`;
  }

  readonly dialog = inject(MatDialog);

  abrirDialogImagem(nome_arquivo: string, tipo_mensagem: string, texto_msg: string) {
    const dialogRef = this.dialog.open(DialogImagemComponent, {
      data: {
        url: nome_arquivo,
        tipo: tipo_mensagem,
        texto: texto_msg,
      }
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log(`Dialog result: ${result}`);
    });
  }

  abrirReprocessar() {
    const dialogRef = this.dialog.open(ReprocessarComponent);
  }

}
