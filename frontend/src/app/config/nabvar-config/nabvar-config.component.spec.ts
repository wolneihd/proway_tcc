import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NabvarConfigComponent } from './nabvar-config.component';

describe('NabvarConfigComponent', () => {
  let component: NabvarConfigComponent;
  let fixture: ComponentFixture<NabvarConfigComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [NabvarConfigComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NabvarConfigComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
