import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Mensagem, Usuario } from '../entidades/Usuarios';
import { Observable } from 'rxjs';
import { enviroment } from '../environment/environment';
import { Resposta } from '../entidades/Resposta';
import { Busca } from '../entidades/Busca';
import { User } from '../entidades/User';
import { Config, LLM } from '../entidades/Config';

const apiUrl = enviroment.apiUrl;

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  usuarios: Usuario[] = [];

  constructor(private httpClient: HttpClient) { }

  obterDadosTabela(): Observable<Usuario[]> {
    return this.httpClient.get<Usuario[]>(`${apiUrl}/mensagens`)
  }

  gerarRespostaIA(texto_adicional: string, mensagens: Mensagem[]): Observable<Resposta>{
    const dados = {
      "texto_adicional": texto_adicional,
      "mensagens": mensagens
    }
    return this.httpClient.post<Resposta>(`${apiUrl}/gerar_resposta`, dados)
  }

  enviarResposta(mensagens: Mensagem[], resposta: string): Observable<any>{
    const dados = {
      "mensagens": mensagens,
      "resposta": resposta
    }
    return this.httpClient.post<any>(`${apiUrl}/responder`, dados)
  }

  filtrarBusca(busca: Busca): Observable<Usuario[]>{
    return this.httpClient.post<Usuario[]>(`${apiUrl}/filtrar`, busca);
  }

  obterDadosTotem(): Observable<any[]> {
    return this.httpClient.get<any[]>(`${apiUrl}/totem`)
  }

  obterTodosUsuarios(): Observable<User[]> {
    return this.httpClient.get<User[]>(`${apiUrl}/usuarios`)
  }

  obterTodosLLMs(): Observable<Config> {
    return this.httpClient.get<Config>(`${apiUrl}/configs`)
  }

  salvarInputsConfig(ia: string, chave: string, powerbi: string): Observable<any>{
    const dados = {
      "ia": ia,
      "chave": chave,
      "powerbi": powerbi 
    }
    return this.httpClient.post<any>(`${apiUrl}/salvar-config`, dados);
  }

  salvarUsuario(nome: string, email: string): Observable<any>{
    const dados = {
      "nome": nome,
      "email": email
    }
    return this.httpClient.post<any>(`${apiUrl}/salvar_usuario`, dados);
  }

  reenvioSenha(email: string): Observable<any>{
    const dados = {
      "email": email
    }
    return this.httpClient.post<any>(`${apiUrl}/reenvio_senha`, dados);
  }
}
