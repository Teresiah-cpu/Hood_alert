# Hood_alert

## Description
This is an application that lets you to be in the loop about everything happening in your neighborhood

## Author

[Teresiah Githua](https://github.com/Teresiah-cpu)


## Screenshots

```
Landing Page
```
<img src="./static/images/hood.png">



## Features


As a user of the application you will be able to:

1. See all posted projects
2. See each project's description, image, date submitted and title.
3. Submit projects
4. Create profile and edit profile
5. Search for a project by title

## BDD
| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- | 
|Signup to the application | Click on `Signup` | A sign up page appears with a sign up form |
|  Login to the site | Click on `Log in`  | Redirected to the login page with a login form |
|  Search in the search field | Input keywords to be searched then click SEARCH | Search page is loaded and displays with the searched results |
|Submit a post|click on `Upload Post`| An upload page appears with an upload form containing different fields|
|View profile|click `account` link in the navbar|Redirects to profile page with an option to edit profile|
|View businesses|click `businesses`|businesses page with the businesses in the neighbourhood|


## Getting started
### Prerequisites
* python3.6
* virtual environment
* pi
* django 3
### Technologies
* BackEnd:
      * Python
      * Django
* FontEnd:
      * HTML
      * CSS
      * JavaScript
      * Bootstrap
* Database
      * PostgreSQL
* Deployment
      * Heroku   



## Installation
### Requirements

* Either a computer,phone,tablet or an Ipad
* An access to the Internet


### Installation
To get the code..

1. Cloning the repository:
  ```bash
  git clone https://github.com/Teresiah-cpu/Hood_alert
  ```
2. Move to the folder and install requirements
  ```bash
  cd myapp
  pip install <package name>
  ```
3. Running the application

  ```bash
  make
  ```
4. Testing the application
  ```bash
  python3.8 manage.py test
  ```
Open the application on your browser `127.0.0.1:8000`.

## Contact Information
Email:terrywambo2018@gmail.com

### License

[MIT](license)

Copyright (c) 2021