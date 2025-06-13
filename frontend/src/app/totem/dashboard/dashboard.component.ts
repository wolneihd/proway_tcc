import { Component } from '@angular/core';
import { NabvarConfigComponent } from '../../config/nabvar-config/nabvar-config.component';
import { ApiService } from '../../services/api.service';
import { NgxChartsModule } from '@swimlane/ngx-charts';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NoopAnimationsModule } from '@angular/platform-browser/animations'; 
import { CommonModule } from '@angular/common';
import { FiltrarTotemComponent } from "../filtrar-totem/filtrar-totem.component";

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [
    NabvarConfigComponent,
    NgxChartsModule,
    FiltrarTotemComponent
],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.css'
})
export class DashboardComponent {

  dadosTotem: any[] | null = null;

  constructor(private api: ApiService) { }

  ngOnInit(){
    this.api.obterDadosTotem().subscribe({
      next: res => {
        this.dadosTotem = res;
        console.log(this.dadosTotem);
      },
      error: erro => {
        console.error(erro)
      }
    })
  }

  // Definindo as opções do gráfico
  showXAxis = true;
  showYAxis = true;
  showLegend = false;
  showXAxisLabel = true;
  showYAxisLabel = true;
  xAxisLabel = 'Categorias';
  yAxisLabel = 'Quantidade de avaliações';
}
