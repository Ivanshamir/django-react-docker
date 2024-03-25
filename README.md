# docker-django-react-mysql-redis-nginx

## Description

This repository contains a sample project demonstrating the integration of Django, React, Docker and all served behind NGINX and reverse proxy.

## Main Frameworks/Libraries/Packages
- **Django Backend:** Provides the backend logic and APIs for the web application.
- **React Frontend:** The frontend code pulls from this [repo](https://github.com/umarfchy/poridhi-workshop/tree/11-docker-with-dynamic-nginx-upstreams).
- **Docker Configuration:** Use `Dockerfiles` and `docker-compose` configuration for containerizing the Django, React and NGINX applications.
- **Database Integration:** Used my-sql for data persistence.
- **Cache Integration:** Used redis for data caching.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Need to Docker installed on your local machine. 

## Usage
To set up and run the project locally, follow these steps:

### Clone the repository:

```bash
git clone https://github.com/Ivanshamir/django-react-docker.git
```
### Navigate to the project directory:
```bash
cd django-react-docker
```
Now copy `.env.example` and rename to `.env`:
```bash
cp .env.example .env
```
### Build and run the Docker containers using Docker Compose:
```bash
docker-compose up -d
```
Now you can access to the application using this url **http://localhost:8000** in your browser.

### To stop the containers, use Ctrl + C and then run:
```bash
docker-compose down
```
### View logs by service name.
```bash
docker compose logs <service-name>
```
### Enter shell for specified container (must be running)
```bash
docker exec -it <container-name> sh
```
### Containers, Services and Ports

| Container  | Service | Host Port | Docker Port |
| ---------- | ------- | --------- | ----------- |
| api        | api     | 5008      | 5000        |
| client     | client-service   | 3000      | 80 |
| db     | db      | 33061      | 3306  |
| redis     | redis      | 63792      | 6379   |
| nginx_server  | nginx   | 8080      | 80     |

### Can this be used for production?

This project is focused on making it easier to perform local full stack development.  However, it is possible to add new docker compose and docker files to also support production.  It's just out of scope for this project.  Please have a look in the archives folder for some old production docker files to give you an idea of what worked in the past.