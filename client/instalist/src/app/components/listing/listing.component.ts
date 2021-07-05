import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Listing } from '../../models/listing';
import { ListingsService } from '../../services/listings.service';

@Component({
  selector: 'app-listing',
  templateUrl: './listing.component.html',
  styleUrls: ['./listing.component.css']
})
export class ListingComponent implements OnInit {

  listing: Listing = new Listing();
  id: number;

  constructor(private route: ActivatedRoute, private listingService: ListingsService) {
    this.id = Number(this.route.snapshot.paramMap.get('id'));
    this.listing = new Listing();
  }

  ngOnInit(): void {
    this.getListing();
  }

  // TODO: Get from the DB - Simples
  getListing() {
    this.listing = this.listingService.getListing(this.id);
    console.log(this.listing);
  }

}
