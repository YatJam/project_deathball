# CodeClan First Project - DEATHBALL

* [Introduction](#introduction)
* [How to Run](#howtorun)


## Introduction

DEATHBALL is my first project as part of CodeClan's 16 week Professional Software Development course. This was a solo build, one week assignment which must have comprised of the following:
* HTML / CSS
* Python
* Flask
* PostgreSQL and the psycopg
* RESTful routes
* Test Driven Development

Out of a variety of briefs to chose from, I selected a sports scoring app and decided to set it in a fantasy world, taking heavy influence from the Lord of Rings and Games Workshop's Blood Bowl game (all rights reserved respectively).

The app allows you to see the latest news, a player roster, teams, game fixtures, and a league. Using RESTful routes, you are able to update players to what team they are assigned to as well as their abilities, team player lists, game fixtures and outcomes. The league takes all match outcomes and populates a ranking.

This is my very first full stack application after four full weeks of Python tuition.

Thank you for taking the time to view my project, I will include updates as an when they are shipped.

## How to Run
### Prerequisites
Please ensure you have Visual Studio Code installed on your machine.

### Executing the code
1. Clone the repo: from your terminal, run `git clone https://github.com/YatJam/project_deathball.git`
1. Go to the project directory: `cd project_deathball`
1. To view the code in Visual Studio, type: `code .`
1. Before lauching the web app, you will need to seed the database
    `PSQL -d deathball -f seeds.sql`
1. Followed by `Python3 console.py`
1. You will now need to run Flask `flask run`
1. In the terminal, you will be generated a localhost address. Copy and paste this into your browser to view the app.
    

### Terminate the applications
1. Use control + c in the terminal to close the app.

## Homepage
![alt text](image/homepage.png)


