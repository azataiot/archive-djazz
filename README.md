<p align="center">
  <a href="https://github.com/azataiot/djazz/">
    <img src="assets/img/icon-teal-200.png" alt="django-template logo" width="200" height="200">
  </a>
</p>
<h1 align="center">djazz</h1>
<p align="center">
  Batteries included Django project designed for practical, real-world applications
  <br>
  <a href="#"><strong>Explore docs »</strong></a>
  <br>
  <br>
</p>

![PyPI - Versions from Framework Classifiers](https://img.shields.io/pypi/frameworkversions/django/djazz-cc?link=https%3A%2F%2Fdjazz.cc)
![GitHub Issues or Pull Requests](https://img.shields.io/github/issues/azataiot/djazz)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/azataiot/djazz)
![GitHub commit activity](https://img.shields.io/github/commit-activity/t/azataiot/djazz?logo=github)

A ready-to-use Django project tailored for practical, real-world applications, djazz comes with pre-configured essential
settings and industry best practices built-in, ensuring a streamlined development process right out of the box. Ideal
for developers looking to jumpstart their projects without the hassle of initial setup.

**NOTE:** THIS PROJECT IS STILL IN DEVELOPMENT AND NOT YET READY FOR PRODUCTION USE.

---

**Documentation**: [Coming soon! 🚧](#)  
**Live Demo**: [Coming soon! 🚧](#)  
**Source Code**: https://github.com/azataiot/djazz

---

## What is coming ?
- Official website of **Djazz**, for sharing best practices, resources, tutorials etc. will be available soon at https://djazz.cc
- A robust and well tested django project template, Enterprise projects ready deployment and development.
- Apps will be coming to this template: 
  - 'Pages' : An app for handling either static or dynamic pages. Analog to WordPress pages model.
  - 'Blog' : A blog app seems necessary for all django projects nowadays, so we are going to embed an blog application.
  - 'Snippets' : A snippets app that gives you quick reference to code examples !
  - 'Accounts' : An application for user authentication and authorization.
- Tools will be coming to this template:
  - 'Lorem Ipsum' : A Djazz tool to help you quickly mock your data. 
  - 'String case converter' : To help you with all that string conversion headache. 
- What else you want ? Request future on [GitHub Issue](https://github.com/azataiot/djazz/issues) or on [Discord](docs/discord.md)!

## Features

- **Free and Open Source**: This project is completely free and open source !! Check [LICENSE](LICENSE) for details.
- **Django ^5.0.**: The latest version of Django, the web framework for perfectionists with deadlines.
- **PostgreSQL**: The world's most advanced open-source relational database.
- **Powered by Docker**: Dockerized development environment for easy setup and deployment.
- **Built-in User Authentication and Authorization**: Fully functional user authentication and authorization system
  included.
- **Custom User Model**: A custom user model is provided out of the box.
- **Built-in API**: A RESTful API (both django rest framework and django ninja) is included for easy integration with
  frontend frameworks.
- **Django Debug Toolbar**: For easy debugging and performance optimization.
- **And much more!**

## Requirements

- **Django**: 5.0 or higher
- **Python**: 3.11 or higher

## Quick Start

To run djazz, you need to have Python and Docker installed on your machine. You also need to create an `.env` file in
the root directory (where the `manage.py` file is located) with the following contents at minimum:

```.dotenv
# Profiles
COMPOSE_PROFILES=development
# Django
DEBUG=1
ALLOWED_HOSTS=localhost,127.0.0.1,[::1],djazz.cc
POSTGRES_DB=djazz
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db

# Email settings (mailpit)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
DEFAULT_FROM_EMAIL="Djazz! <info@djazz.cc>"
EMAIL_HOST=mail
EMAIL_PORT=1025
EMAIL_USE_TLS=False
EMAIL_HOST_USER=""
EMAIL_HOST_PASSWORD=""
```

The easiest way to run djazz is using Docker. Make sure you have **Docker installed on your machine**.

```bash
docker compose --profile debug up
```

or you can use the `djazz CLI` tool [Coming soon! 🚧](#) :

This will start the development server and PostgreSQL database as well as the Redis cache server. You can access the
development server at `http://localhost:8000/`.

