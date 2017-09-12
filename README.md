# ProjectApiFlask
Our API does just GET requests where the user can interact with the database, knows its structures and make query. The queries can be for a whole table, search a register by its id or a query relating different tables.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

* [Docker](https://docs.docker.com/engine/installation/)

### Installing & running
Clone the project on your local machine

`$ git clone https://github.com/albags/ProjectApiFlask.git`

`$ cd ProjectApiFlask/`

Create the database

`$ sudo docker build database`

Build the application, everytime you make a change you need to build the application again

`$ sudo docker-compose build`

Run the application

`$ sudo docker-compose up`

Go to your browser into [0.0.0.0:1080](http://0.0.0.0:1080)

Close the application

`$ sudo docker-compose down`

## Licence
ProjectApiFlask is released under the [MIT License](LICENSE).