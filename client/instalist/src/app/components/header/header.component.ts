import { Component, OnInit } from '@angular/core';
import { EventEmitter} from 'events';
import { CommonService } from '../../services/common.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {

  siteName: string;

  warning: boolean = false;
  warningContent: string = '';

  subscriptions: EventEmitter[] = [];

  // Constructors will allow for service injection.. Here we want to use the common to get the site name.
  // Inject it and you're good to go. If you need a reference outside the constructor, then you can instanciate one outside the scope.
  constructor(commonService: CommonService) {
    this.siteName = commonService.getSettings().siteName;
  }

  ngOnInit(): void {
    this.subscribeEvents()
  }

  // Subscribe to events across the app
  private subscribeEvents(): void {
    var s = new EventEmitter();

    s.on('warning', (warningMessage: string)=>{
      this.warningContent = warningMessage;
      this.warning = true;
    })

    this.subscriptions.push(s);

  }
}
