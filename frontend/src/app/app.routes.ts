import { Routes } from '@angular/router';
import { ListaDadosComponent } from './gerenciamento/lista-dados/lista-dados.component';
import { ResponderComponent } from './gerenciamento/responder/responder.component';
import { LoginComponent } from './login/login/login.component';
import { PrincipalComponent } from './gerenciamento/principal/principal.component';
import { ConfigComponent } from './config/config/config.component';
import { DashboardComponent } from './totem/dashboard/dashboard.component';

export const routes: Routes = [
  {
    path: 'main',
    component: ListaDadosComponent
  },
  {
    path: 'main/responder',
    component: ResponderComponent
  },
  {
    path: 'login',
    component: LoginComponent
  },
  {
    path: 'gerenciamento',
    component: PrincipalComponent
  },
  {
    path: 'configurar',
    component: ConfigComponent
  },
  {
    path: 'totem',
    component: DashboardComponent
  },
  {
    path: '',
    component: LoginComponent
  },
  {
    path: '**',
    component: LoginComponent
  }
];
