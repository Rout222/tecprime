import { TestBed } from '@angular/core/testing';

import { CadastrosService } from './cadastros.service';

describe('CadastrosService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: CadastrosService = TestBed.get(CadastrosService);
    expect(service).toBeTruthy();
  });
});
