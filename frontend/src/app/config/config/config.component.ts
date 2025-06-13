import { Component } from '@angular/core';
import { NabvarConfigComponent } from '../nabvar-config/nabvar-config.component';
import { TabelaUsuariosComponent } from "../tabela-usuarios/tabela-usuarios.component";
import { ApiService } from '../../services/api.service';
import { LLM } from '../../entidades/LLM';

@Component({
  selector: 'app-config',
  standalone: true,
  imports: [NabvarConfigComponent, TabelaUsuariosComponent],
  templateUrl: './config.component.html',
  styleUrl: './config.component.css'
})
export class ConfigComponent {

  constructor(private api: ApiService) { }

  llms: LLM[] = [];

  // Variáveis para armazenar os valores dos inputs e do select
  modelIA: string = '';
  chaveAPI: string = '';
  linkPowerBI: string = '';

  ngOnInit() {
    this.api.obterTodosLLMs().subscribe({
      next: res => {
        this.llms = res;
        console.log(this.llms);
      },
      error: erro => {
        console.error(erro)
      }
    })
  }

  // Método para obter os dados dos inputs e do select
  obterDadosInput() {
    // Capturando os valores
    this.modelIA = (document.getElementById('model-ia') as HTMLSelectElement).value;
    this.chaveAPI = (document.getElementById('chave-api') as HTMLInputElement).value;
    this.linkPowerBI = (document.getElementById('link-powerbi') as HTMLInputElement).value;

    this.api.salvarInputsConfig(this.modelIA, this.chaveAPI, this.linkPowerBI).subscribe({
      next: (resposta) => {},
      error: erro => {
        console.error(erro)
        alert("Erro ao carregar os jogos");
      }
    })
  }

}
