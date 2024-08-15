# Theatre-API-Service

The "Theatre API Service" is an API for managing theatre operations, allowing users to book seats and make reservations online. Built with Django and Django REST Framework, it provides endpoints for managing plays, performances, theatre halls, and tickets, with user authentication for secure reservations.

# Installation
Python3 must be already installed

- git clone https://github.com/MaglorFeanorson/Theatre-API-Service.git
- python -m venv venv
- venv\Scripts\activate (on Windows)
- source venv/bin/activate (on macOS)
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver



# Environment Variables Setup
- Create a .env file in the root directory of your project.
- Add the following key-value pairs to the .env file. Example:
- DB_HOST=<your-db-host>
- DB_NAME=<your-db-name>
- DB_USER=<your-db-user>
- DB_PASSWORD=<your-db-password>
- DB_PORT=<your-db-port>

# Run with docker
Docker should be installed

   docker-compose build
   docker-compose up

# Features
- JWT-based authentication
- Admin dashboard available at /admin/
- API documentation available at /api/doc/swagger/
- Handling bookings and tickets
- Creating plays with different genres and actors
- Adding theatre halls
- Adding new performances
- Filtering plays and performances

![Website Interface](/project_shema.png)