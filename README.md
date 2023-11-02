# Barber Shop - Django Project

This repository contains a project developed in Django that presents a system for a barber shop. Provides functionality to manage a dashboard menu, clients, products and barber services.

## Characteristics

- **Dashboard:** Includes a control panel to manage the store, with essential statistics and functionalities.
- **Customers:** Allows the management of the customer database.
- **Products:** Offers the administration of the products available in the store.
- **Barbershop:** Manage information and services related to the barbershop.

## Technologies and Features

- **Django Framework:** Used as the main framework for the development of the project.
- **Components:** Components have been used to improve the modularity and reuse of the code.
- **Models and SQLite:** Use of Django models for database management, using SQLite as the default database.
- **Bootstrap 5:** The Bootstrap 5 framework has been used for the design and user interface.

## Project Structure

The project is organized into different Django applications, each with its own specific functionality and responsibility:

- `dashboard`: Management of the control panel and statistics.
- `customers`: Functionality for customer management.
- `products`: Administration of available products.
- 'Barbers': Module for managing barber services.

## Installation and Execution

1. Clone this repository.
2. Create a virtual environment and activate the virtual environment.
3. Install the dependencies using `pip install -r requirements.txt`.
4. Run the migrations with `python manage.py migrate`.
5. Start the server with `python manage.py runserver`.

## Contributions

Contributions are welcome. If you want to contribute to this project, please create a fork, implement the improvements and create a pull request.

## Author

This project has been developed by [JerickTwO](https://github.com/JerickTwO).