import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FiltrarComponent } from './filtrar.component';

describe('FiltrarComponent', () => {
  let component: FiltrarComponent;
  let fixture: ComponentFixture<FiltrarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FiltrarComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FiltrarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
