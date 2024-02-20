﻿# User Accounts Mini Project

This is a Django-based mini project for managing user accounts with custom user models, authentication, and profile management features.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Setup](#setup)
4. [Usage](#usage)
5. [API Endpoints](#api-endpoints)
6. [Unit Tests](#unit-tests)
7. [Documentation](#documentation)
8. [License](#license)

## Introduction

This project aims to provide a simple yet comprehensive solution for managing user accounts in Django applications. It includes custom user models, authentication views, serializers, and permissions for building robust user management systems.

## Features

- Custom user model with extended fields like user type, profile picture, and biography.
- User authentication using JWT tokens.
- CRUD operations for user profiles.
- Custom permission classes for controlling access to user resources.
- Integration with Django admin for user management.

## Setup

To set up the project locally, follow these steps:

1. Clone the repository:

```
git clone https://github.com/mohammad-faalfard/user_accounts
cd accounts
```

2. Create a virtual environment and activate it:

```
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Run migrations:

```
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser:

```
python manage.py createsuperuser
```

6. Run the development server:

```
python manage.py runserver
```

## Usage

Once the project is set up, you can use Django admin to manage users, including creating, updating, and deleting user accounts. Additionally, the project provides API endpoints for user authentication and profile management.

## API Endpoints

The API endpoints provided by this project include:

- `/api/login/`: Endpoint for user authentication and obtaining JWT tokens.
- `/api/user/profile/`: Endpoint for retrieving user profile information.
- `/api/user/profile/update/`: Endpoint for updating user profile information.

## Unit Tests

Unit tests are implemented to ensure the correctness and reliability of the codebase. To run the unit tests, use the following command:

```
python manage.py test accounts.tests
```

Make sure to review and extend the unit tests as needed when making changes to the codebase.

## Documentation

For detailed documentation on each component and usage instructions, refer to the code comments and docstrings provided throughout the project. Additionally, the Swagger documentation is available at `/swagger/` for exploring the API endpoints interactively.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
