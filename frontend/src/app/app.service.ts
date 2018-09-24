import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Observable} from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import {API_URL} from './env';
import {Question} from './qmodel';


@Injectable()
export class QuestionAPI {
  constructor(private http: HttpClient) {
  }

  private static _handleError(err: HttpErrorResponse | any) {
    return Observable.throw(err.message || 'Error: Unable to complete request.');
  }

  getQuestion(): Observable<any> {
    return this.http.get<Question[]>(`${API_URL}/api/question`).catch(QuestionAPI._handleError);
  }
}
