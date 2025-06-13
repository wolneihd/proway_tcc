import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListaDadosComponent } from './lista-dados.component';

describe('ListaDadosComponent', () => {
  let component: ListaDadosComponent;
  let fixture: ComponentFixture<ListaDadosComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ListaDadosComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ListaDadosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
