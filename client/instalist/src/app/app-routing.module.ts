import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AboutComponent } from './components/about/about.component';
import { ContactComponent } from './components/contact/contact.component';
import { HomeComponent } from './components/home/home.component';
import { ListingComponent } from './components/listing/listing.component';
import { NotFoundComponent } from './components/not-found/not-found.component';
import { SubmitComponent } from './components/submit/submit.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'contact', component: ContactComponent },
  { path: 'submit', component: SubmitComponent },
  { path: 'about', component: AboutComponent },
  { path: 'listings', component: ListingComponent }, // all listings
  { path: 'p/:id', component: ListingComponent },
  { path: '**', component: NotFoundComponent }

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})

export class AppRoutingModule { }
