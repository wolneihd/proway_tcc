import { Component } from '@angular/core';
import { Busca } from '../../entidades/Busca';
import { ApiService } from '../../services/api.service';
import { ShareService } from '../../services/share.service';

@Component({
  selector: 'app-filtrar',
  standalone: true,
  imports: [],
  templateUrl: './filtrar.component.html',
  styleUrl: './filtrar.component.css'
})
export class FiltrarComponent {

  constructor(private api: ApiService, private share: ShareService) {}

  fecharResponder() {
    this.share.mostrarFiltrarResponder(false, false);
  }

  captarDadosBusca() {

    let nome = ((<HTMLInputElement>document.getElementById("texto-busca")).value);
    let categoria = ((<HTMLInputElement>document.getElementById("categoria")).value);
    let status = ((<HTMLInputElement>document.getElementById("status")).value);
    let tipo = ((<HTMLInputElement>document.getElementById("tipo")).value);
    let ia = ((<HTMLInputElement>document.getElementById("ia")).value);
    let dataDe = ((<HTMLInputElement>document.getElementById("data-de")).value);
    let dataAte = ((<HTMLInputElement>document.getElementById("data-ate")).value);
    let analise_ia = ((<HTMLInputElement>document.getElementById("analise_ia")).value);
  
    let busca: Busca = {
      categoria: categoria,
      dataDe: dataDe,
      DataAte: dataAte,
      ia: ia,
      nome: nome.toLowerCase(),
      status: status,
      tipo: tipo,
      analise_ia: analise_ia
    };

    console.log("Realizar busca de:", busca);

    // enviar para a tabela os dados filtrados
    this.api.filtrarBusca(busca).subscribe({
      next: res => {
        this.share.emitirUsuariosFiltrados(res);
      },
      error: erro => {
        console.error(erro)
      }
    })
    this.fecharResponder();
  }

}
