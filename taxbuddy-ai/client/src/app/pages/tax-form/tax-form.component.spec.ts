import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TaxForm } from './tax-form';

describe('TaxForm', () => {
  let component: TaxForm;
  let fixture: ComponentFixture<TaxForm>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TaxForm]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TaxForm);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
