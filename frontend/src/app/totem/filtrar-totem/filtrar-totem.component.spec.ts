import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FiltrarTotemComponent } from './filtrar-totem.component';

describe('FiltrarTotemComponent', () => {
  let component: FiltrarTotemComponent;
  let fixture: ComponentFixture<FiltrarTotemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FiltrarTotemComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FiltrarTotemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
