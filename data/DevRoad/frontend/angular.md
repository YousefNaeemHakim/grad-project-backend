# Angular

Angular is a JavaScript framework used for building dynamic web applications. In this learning summary, we will cover some of the key concepts and code snippets for getting started with Angular.

## Prerequisites

Before getting started with Angular, you should have a basic understanding of HTML, CSS, and JavaScript.

## Setting Up Your Development Environment

To start developing Angular applications, you will need to have Node.js and npm (Node Package Manager) installed on your computer. You can download Node.js from the official website: [https://nodejs.org/](https://nodejs.org/). Once Node.js is installed, you can use npm to install the Angular CLI (Command Line Interface) by running the following command in your terminal or command prompt:

```
npm install -g @angular/cli
```

## Creating Your First Angular Application

Once the Angular CLI is installed, you can use it to create a new Angular application. Open your terminal or command prompt and run the following command:

```
ng new my-app
```

This will create a new Angular application in a directory called `my-app`. You can navigate into this directory by running the following command:

```bash
cd my-app
```

You can then start the development server by running the following command:

```
ng serve --open
```

This will compile your application and open it in your default web browser.

## Setup

To get started with Angular, you need to set up a development environment. Here are the steps:

1. Install Node.js and npm.
2. Install the Angular CLI using npm: `npm install -g @angular/cli`.
3. Create a new Angular project using the CLI: `ng new my-app`.
4. Navigate to the project directory: `cd my-app`.
5. Serve the application using the CLI: `ng serve`.

Once the application is served, you can view it in your browser at `http://localhost:4200/`.

## Components

Components are the building blocks of Angular applications. They are responsible for rendering the user interface and handling user interactions. Here is an example of a simple component in Angular:

```ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-hello-world',
  template: '<h1>Hello World!</h1>',
})
export class HelloWorldComponent {}
```

In this example, we have defined a component called `HelloComponent`. The `@Component` decorator is used to provide metadata about the component, including its selector and template. The `name` property is used to interpolate a value into the template.

To use this component in your application, you would add the following HTML tag to one of your templates:

```html
<app-hello-world></app-hello-world>
```

## Modules

Modules are used to organize code in Angular applications. They group related components, services, and other features together. Here is an example of a simple module in Angular:

```ts
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HelloWorldComponent } from './hello-world.component';

@NgModule({
  declarations: [HelloWorldComponent],
  imports: [BrowserModule],
  bootstrap: [HelloWorldComponent],
})
export class AppModule {}
```

In this example, we have defined a module called `AppModule`. The `@NgModule` decorator is used to provide metadata about the module, including its declarations (components, directives, and pipes), imports (other modules that this module depends on), and bootstrap component (the component that is the starting point of the application).

## Data Binding

Data binding is used to connect data from the component to the template. There are several types of data binding in Angular:

### Interpolation

Interpolation is used to display data in the template. Here is an example:

```html
<p>My name is {{name}}</p>
```

In this example, the `name` property from the component is interpolated into the template.

### Property Binding

Property binding is used to set the value of an HTML element property. Here is an example:

```html
<img [src]="imageUrl" alt="An image">
```

In this example, the `src` property of the `img` element is bound to the `imageUrl` property of the component.

### Event Binding

Event binding is used to handle user events, such as clicks. Here is an example:

```html
<button (click)="onButtonClick()">Click me!</button>
```

In this example, the `click` event of the `button` element is bound to the `onButtonClick()` method of the component.

## Services

Services are used in Angular to provide functionality that can be shared across multiple components. They are often used for data access, logging, and other common tasks. Here is an example of a simple service in Angular:

```ts
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export

class UserService {
 private users: string[] = ['Alice', 'Bob', 'Charlie'];
 getUsers() 
    { 
      return this.users; 
    } 
    addUser(user: string) {
     this.users.push(user); 
 } 
}
```

In this example, we have defined a service called `UserService`. The `@Injectable` decorator is used to indicate that this service can be injected into other components or services. The service has two methods:

- `getUsers()`: returns an array of users.
- `addUser()`: adds a new user to the array.

## Dependency Injection

Dependency injection is a key feature of Angular that allows you to easily inject services and other dependencies into your components. Here is an example of a component that uses dependency injection to access a service:

```ts
import { Component } from '@angular/core';
import { UserService } from './user.service';

@Component({
  selector: 'app-user-list',
  template: `
    <h2>User List</h2>
    <ul>
      <li *ngFor="let user of users">{{user}}</li>
    </ul>
    <input type="text" [(ngModel)]="newUser">
    <button (click)="addUser()">Add User</button>
  `,
})
export class UserListComponent {
  users: string[] = [];
  newUser: string;

  constructor(private userService: UserService) {}

  ngOnInit() {
    this.users = this.userService.getUsers();
  }

  addUser() {
    this.userService.addUser(this.newUser);
    this.newUser = '';
    this.users = this.userService.getUsers();
  }
}
```

In this example, we have defined a component called `UserListComponent`. The component has a dependency on the `UserService`, which is injected into the component using the constructor. The `ngOnInit()` method is called when the component is initialized, and it uses the `UserService` to get the list of users. The `addUser()` method is called when the user clicks the "Add User" button, and it uses the `UserService` to add a new user to the list.

## Conclusion

In this learning summary, we covered some of the key concepts and code snippets for getting started with Angular. We discussed components, modules, data binding, services, and dependency injection. With these foundational concepts, you should be well on your way to building your own Angular applications.