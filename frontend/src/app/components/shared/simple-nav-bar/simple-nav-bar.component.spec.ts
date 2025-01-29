import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SimpleNavBarComponent } from './simple-nav-bar.component';

describe('SimpleNavBarComponent', () => {
  let component: SimpleNavBarComponent;
  let fixture: ComponentFixture<SimpleNavBarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SimpleNavBarComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SimpleNavBarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
