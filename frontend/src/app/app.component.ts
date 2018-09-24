import {Component, OnInit, OnDestroy} from '@angular/core';
import {Subscription} from 'rxjs/Subscription';
import {QuestionAPI} from './app.service';
import {Question} from './qmodel';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent implements OnInit, OnDestroy {
  title = 'Online Trivia';
  qSubs: Subscription;
  currQuestion: Question[];

  constructor(private quest: QuestionAPI) {
  }

  ngOnInit() {
    this.qSubs = this.quest.getQuestion().subscribe(res => {
          this.qSubs = res;
        },
        console.error
      );
  }

  ngOnDestroy() {
  this.qSubs.unsubscribe();
  }
}
