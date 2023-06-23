## Table of Content
- [Project Technologies](#project-technologies)
  - [Mobile App](#mobile-app)
  - [Client-Side](#client-side)
  - [Server-Side](#server-side)
  - [Development Tools](#development-tools)
- [Architecture](#architecture)
  - [Django Project Structure](#django-project-structure)
  - [ Django REST Framework API folder structure in the project](#-django-rest-framework-api-folder-structure-in-the-project)
  - [|``urls.py`` | URL configuration file specific to the app. Maps URLs to corresponding views within the app](#urlspy--url-configuration-file-specific-to-the-app-maps-urls-to-corresponding-views-within-the-app)
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
    <img src="https://skillicons.dev/icons?i=firebase,python,django,postgres,sqlite" />
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


| App | Description |
| ----- | --- |
| ``accounts`` | Handles user authentication and registration functionality. Manages user profiles, login, logout, password reset, and account settings. |
| ``community`` | Provides features for community interactions, such as creating and joining groups, posting and commenting on discussions, and user-to-user messaging. |
| ``devroad`` | Offers roadmaps for computer science and software engineering roles. Contains curated learning paths, resources, and milestones to guide users in their career development. |
| ``base`` | Focuses on a books summaries app. Includes views that allows to create, view, and manage summaries of books. Provides search and filtering functionality for easy navigation and discovery of summaries. |
| ``iread`` | The default app in the Django project |

---

## <u> Django REST Framework API folder structure in the project

| File Name | Description |
| --- | --- |
|``serializers.py`` | Contains serializers to convert models into JSON representations and vice versa. |
|``views.py`` | Defines API views (e.g., class-based views or function-based views) for handling HTTP requests and generating responses. |
|``urls.py`` | URL configuration file specific to the app. Maps URLs to corresponding views within the app
---

| Name | Description |
| ------- | ------------ |
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

## Team Structure

| Name | Role
| :----: | :-----------------------------------------------:
| **Yousef Naeem** | Team Lead • Back-End Developer   | Server-Side                                                     
| **Omar Khaled** | Back-End Developer   
| **Assmaa Akram** | Mobile Team Lead
| **Ahmed Khalifa** | Mobile Developer
| **Mohamed Magdy** | Mobile Developer
| **Sara Gamal** | Mobile Developer                                           
| **Mohamed Samir** | SW Tester
