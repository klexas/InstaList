import { Component, OnInit } from '@angular/core';
import { CommonService } from '../../services/common.service';
import { ListingsService } from '../../services/listings.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  logoUrl: string;
  siteName: string;
  listings: any[];

  constructor(commonService: CommonService, listingServices: ListingsService) {
    this.logoUrl = commonService.getSettings().logo;
    this.siteName = commonService.getSettings().siteName;
    this.listings = commonService.getSettings().listings;
   }

  ngOnInit(): void {

  }

}
