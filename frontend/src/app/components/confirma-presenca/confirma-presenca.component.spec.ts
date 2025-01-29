import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ConfirmaPresencaComponent } from './confirma-presenca.component';

describe('ConfirmaPresencaComponent', () => {
  let component: ConfirmaPresencaComponent;
  let fixture: ComponentFixture<ConfirmaPresencaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ConfirmaPresencaComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ConfirmaPresencaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
