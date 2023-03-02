## Table of Content
- [Project Technologies](#project-technologies)
  - [Mobile App](#mobile-app)
  - [Client-Side](#client-side)
  - [Server-Side](#server-side)
  - [Development Tools](#development-tools)
- [Architecture](#architecture)
  - [Django Project Structure](#django-project-structure)
  - [Routes Structure](#routes-structure)
  - [Team Structure](#team-structure)


# Project Technologies 

## Mobile App
<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=dart,flutter" />
  </a>
</p>

## Client-Side
<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=html,css,javascript,bootstrap,jquery" />
  </a>
</p>

## Server-Side
<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=python,django,postgres,sqlite,nginx" />
  </a>
</p>

## Development Tools
<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=postman,vscode,androidstudio,git,github" />
  </a>
</p>


---

# <u>Architecture 

## <u>Django Project Structure
The folder structure of this app is explained below:

| Name | Description |
| ------------------------ | --------------------------------------------------------------------------------------------- |
| ``settings.py``         | contains the Django project configuration.                                                            |
| ``urls.py``                  | it contains all the endpoints that we should have for our app                            |
| ``admin.py``      | for registering the Django models into the Django administration. 
| ``apps.py``              | is a file that is used to help the user include the application configuration for their app.  
| ``models.py``      | represents the models of web applications in the form of classes                     
| ``views.py``           | It contains all the views in the form of classes.  |
| ``manage.py``         | This file is used as a command-line utility                                                  |
| ``wsgi.py``        | Web Server Gateway Interface 
| ``requirements.txt``             | Contains all installed python libraries

---

## <u>Routes Structure 

| Method | Route | Description |
| :----:   | :---------------: | ---------------------- |
| `GET`  | `api/v1/users`      | Route Description |
| `GET`  | `api/v1/user/:id`      | Route Description |
| `POST` | `api/v1/user/:id`      | Route Description                               |
|  `PUT`      | `api/v1/user/:id`      | Route Description 
| `DELETE`  | `api/v1/user/:id`      | Route Description 
|   `GET`     | `api/v1/books`      | Route Description  
|   `GET `     | `api/v1/book/:id`      | Route Description  
|   `POST`     | `api/v1/book/:id`      | Route Description  
|   `PUT`     | `api/v1/book/:id`      | Route Description  
|   `DELETE`     | `api/v1/book/:id`      | Route Description  
|   `GET`     | `api/v1/posts`      | Route Description  
|   `GET `     | `api/v1/post/:id`      | Route Description  
|   `POST`     | `api/v1/post/:id`      | Route Description  
|   `PUT`     | `api/v1/post/:id`      | Route Description  
|   `DELETE`     | `api/v1/post/:id`      | Route Description  
|   `GET`     | `api/v1/groups`      | Route Description  
|   `GET `     | `api/v1/group/:id`      | Route Description  
|   `POST`     | `api/v1/group/:id`      | Route Description  
|   `PUT`     | `api/v1/group/:id`      | Route Description  
|   `DELETE`     | `api/v1/group/:id`      | Route Description  

---

## Team Structure

| Name | Role
| :----: | :-----------------------------------------------:
| **Yousef Naeem** | Team Lead • Back-End Developer   | Server-Side                                                     
| **Omar Khaled** | Back-End Developer   
| **Assmaa Akram** | Mobile Team Lead
| **Ahmed Khalifa** | Mobile Developer
| **Mohamed Magdy** | Mobile Developer
| **Sara Gamal** | Mobile Developer                                           
| **Mohamed Samir** | Mobile Developer • SW Tester