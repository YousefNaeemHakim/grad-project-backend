# grad-project-backend
## Technologies ( PERN Stack )
- Node.js
- Express.js
- PostgreSQL
- No React :)

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
| package.json             | Contains npm dependencies as well as [build scripts](#what-if-a-library-isnt-on-definitelytyped)   | tsconfig.json            | Config settings for compiling source code only written in TypeScript                                             |
