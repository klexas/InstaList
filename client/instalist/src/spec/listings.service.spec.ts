import { TestBed } from '@angular/core/testing';
import { CommonService } from '../app/services/common.service';

import { ListingsService } from '../app/services/listings.service';

describe('ListingsService', () => {
  let service: ListingsService;
  let commonService: any;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    commonService = { getSettings: () => ([{ name: 'FAKE_NAME' }]) };
  });

    it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
