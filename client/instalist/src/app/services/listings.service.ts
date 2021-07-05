import { Injectable } from '@angular/core';
import { Listing } from '../models/listing';
import { CommonService } from './common.service';

@Injectable({
  providedIn: 'root'
})

export class ListingsService {
  // Services we need
  commonService: CommonService;

  listings: Listing[] = [];

 constructor(commonService: CommonService) {
    this.commonService = commonService;

   }


  populateListings(): boolean {
    this.listings = this.commonService.getSettings().listings as Listing[];
    return true;
  }

  getListing(id: number): Listing {

    const results = this.listings.filter(listing => {return listing.id ==  id})

    if(results.length > 0)
      return results[0];

    else throw Error("No listing with the ID exists");

    // // TODO: get from d b
    // let listing =  new Listing();
    // listing.id = id;
    // listing.tags = ['clothes', 'shoes'];
    // listing.title = "ASOS";
    // listing.url = "http://asos.com/refferal";

    // return listing;
  }

  addListing(listing: Listing) : void {
    if(listing)
      this.listings.push(listing);
    else{
      return;
    }
  }

  getListings(count: number): Array<Listing> {
    let returnList = new Array<Listing>();



    return returnList;

  }
}
