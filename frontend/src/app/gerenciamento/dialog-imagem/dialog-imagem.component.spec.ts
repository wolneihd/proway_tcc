import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DialogImagemComponent } from './dialog-imagem.component';

describe('DialogImagemComponent', () => {
  let component: DialogImagemComponent;
  let fixture: ComponentFixture<DialogImagemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DialogImagemComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DialogImagemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
