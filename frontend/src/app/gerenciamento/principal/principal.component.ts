import { Component } from '@angular/core';
import { ListaDadosComponent } from "../lista-dados/lista-dados.component";
import { NavbarComponent } from "../navbar/navbar.component";
import { ResponderComponent } from "../responder/responder.component";
import { CommonModule } from '@angular/common';
import { FiltrarComponent } from "../filtrar/filtrar.component";
import { ShareService } from '../../services/share.service';

@Component({
  selector: 'app-principal',
  standalone: true,
  imports: [ListaDadosComponent, NavbarComponent, ResponderComponent, CommonModule, FiltrarComponent],
  templateUrl: './principal.component.html',
  styleUrl: './principal.component.css'
})
export class PrincipalComponent {

  divResponder:boolean = false;
  divFiltrar:boolean = false;

  constructor(private shareService: ShareService) {}

  ngOnInit(): void {
    this.shareService.filtrar$.subscribe(filtrar => {
      this.divFiltrar = filtrar;
    })
    this.shareService.responder$.subscribe(responder => {
      this.divResponder = responder;
    })
  }

}
