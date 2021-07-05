import { Component, OnInit, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-not-found',
  templateUrl: './not-found.component.html',
  styleUrls: ['./not-found.component.css']
})
export class NotFoundComponent implements OnInit {

  constructor() {
    let error = new EventEmitter();
    error.emit('warning');
  }

  ngOnInit(): void {
  }

}
