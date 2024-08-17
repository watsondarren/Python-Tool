import { ComponentFixture, TestBed } from '@angular/core/testing';

import { [CAP_NAME]Component } from './[LOWER_NAME].component';

describe('[CAP_NAME]Component', () => {
  let component: [CAP_NAME]Component;
  let fixture: ComponentFixture<[CAP_NAME]Component>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [[CAP_NAME]Component]
    })
    .compileComponents();

    fixture = TestBed.createComponent([CAP_NAME]Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
