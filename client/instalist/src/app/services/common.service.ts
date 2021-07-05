import { Injectable } from '@angular/core';

// All of this will be from the Database
// For the moment we can use the json file as a flat document
// So add / edit/ remove as you like for playing around in dev
import * as data from '../settings.json';

@Injectable({
  providedIn: 'root'
})
export class CommonService {

  settings: any;

  constructor() {
    this.settings = data;
    console.log(data);
  }

  // All to be removed by DAL
  // Data access layer

  getSettings():any {
    return this.settings;
  }

}
