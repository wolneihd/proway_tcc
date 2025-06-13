import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ReprocessarComponent } from './reprocessar.component';

describe('ReprocessarComponent', () => {
  let component: ReprocessarComponent;
  let fixture: ComponentFixture<ReprocessarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ReprocessarComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ReprocessarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
