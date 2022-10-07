## Table of Content
- [Project Technologies](#project-technologies)
  - [Tech Stack ( PERN || MERN )](#tech-stack--pern--mern-)
  - [Tools](#tools)
  - [Testing](#testing)
  - [Mobile App](#mobile-app)
- [Architecture](#architecture)
  - [Project Structure](#project-structure)
  - [Routes Structure](#routes-structure)


# Project Technologies 
## Tech Stack ( PERN || MERN )
<a href="https://nodejs.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/nodejs/nodejs-original-wordmark.svg" alt="nodejs" width="40" height="40"/></a>
<a href="https://expressjs.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/express/express-original-wordmark.svg" alt="express" width="40" height="40"/></a>
<a href="https://www.mongodb.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mongodb/mongodb-original-wordmark.svg" alt="mongodb" width="40" height="40"/> </a>
<a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="40" height="40"/></a>
<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a>
<a href="https://www.nginx.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/nginx/nginx-original.svg" alt="nginx" width="40" height="40"/> </a>

## Tools
<a href="https://postman.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/getpostman/getpostman-icon.svg" alt="postman" width="40" height="40"/> </a>
<a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a>

## Testing
<a href="https://jestjs.io" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/jestjsio/jestjsio-icon.svg" alt="jest" width="40" height="40"/> </a>

## Mobile App
<a href="https://dart.dev" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/dartlang/dartlang-icon.svg" alt="dart" width="40" height="40"/> </a>
<a href="https://flutter.dev" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/flutterio/flutterio-icon.svg" alt="flutter" width="40" height="40"/> </a>

---

# Architecture 

---

## Project Structure
The folder structure of this app is explained below:

| Name | Description |
| ------------------------ | --------------------------------------------------------------------------------------------- |
| **node_modules**         | Contains all  npm dependencies                                                            |
| **server/src**                  | Contains  source code that will be compiled to the dist dir                               |
| **configuration**        | Application configuration including environment-specific configs 
| **server/src/controllers**      | Controllers define functions to serve various express routes. 
| **server/src/lib**              | Common libraries to be used across your app.  
| **server/src/middlewares**      | Express middlewares which process the incoming requests before handling them down to the routes
| **server/src/routes**           | Contain all express routes, separated by module/area of application                       
| **server/src/models**           | Models define schemas that will be used in storing and retrieving data from Application database  |
| **server/src**/server.js         | Entry point to express app                                                               |
| package.json             | Contains npm dependencies as well as [build scripts](#what-if-a-library-isnt-on-definitelytyped)

---

## Routes Structure 

| Route | Description |
| ------------------------ | ---------------------- |
| ``api/v1/``      | Route Description |
| ``api/v1/``      | Route Description                               |
| ``api/v1/``      | Route Description 
| ``api/v1/``      | Route Description 
| ``api/v1/``      | Route Description  
