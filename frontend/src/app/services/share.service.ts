import { Injectable } from '@angular/core';
import { BehaviorSubject, Subject } from 'rxjs';
import { Usuario } from '../entidades/Usuarios';

@Injectable({
  providedIn: 'root'
})
export class ShareService {


  // Usando BehaviorSubject para armazenar e compartilhar dados
  private usuariosSource = new BehaviorSubject<Usuario[]>([]);
  private idSource = new BehaviorSubject<number>(0);
  private boxFiltrar = new BehaviorSubject<boolean>(false);
  private boxResponder = new BehaviorSubject<boolean>(false);

  // Observáveis para serem usados pelos componentes
  usuarios$ = this.usuariosSource.asObservable();
  id$ = this.idSource.asObservable();
  filtrar$ = this.boxFiltrar.asObservable();
  responder$ = this.boxResponder.asObservable();

  constructor() { }

  mostrarFiltrarResponder(filtrar: boolean, responder: boolean) {
    this.boxFiltrar.next(filtrar);
    this.boxResponder.next(responder);
  }

  // Métodos para atualizar os dados
  shareMensagem(usuarios: Usuario[], id: number): void {
    this.usuariosSource.next(usuarios);
    this.idSource.next(id);
  }

  // Criando um Subject para emitir os dados para o Componente A
  private usuariosFiltradosSubject = new Subject<Usuario[]>();
  usuariosFiltrados$ = this.usuariosFiltradosSubject.asObservable();

  // Função para emitir dados de usuários filtrados
  emitirUsuariosFiltrados(usuarios: Usuario[]) {
    this.usuariosFiltradosSubject.next(usuarios);
  }

  // Função para obter os dados atuais (se necessário)
  obterUsuariosFiltrados() {
    return this.usuariosFiltradosSubject.asObservable();
  }
}
