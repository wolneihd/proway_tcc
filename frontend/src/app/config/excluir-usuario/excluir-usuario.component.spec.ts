import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ExcluirUsuarioComponent } from './excluir-usuario.component';

describe('ExcluirUsuarioComponent', () => {
  let component: ExcluirUsuarioComponent;
  let fixture: ComponentFixture<ExcluirUsuarioComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ExcluirUsuarioComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ExcluirUsuarioComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
