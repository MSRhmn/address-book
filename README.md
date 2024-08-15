# Django Address Book Application

## Overview

This project is a basic Address Book application built with Django. It allows users to add, view, search, and delete contacts. The application uses Django's Model-View-Template (MVT) architecture and includes basic form handling, template rendering, and URL routing.

## Requirements

- Python 3.x
- Django 3.x or later

## Installation

1. **Clone the repository**

   `git clone https://github.com/yourusername/django-address-book.git`
   `cd django-address-book`

2. **Create and activate a virtual environment**

    `python3 -m venv venv`
    `source venv/bin/activate`  # On Windows use `venv\Scripts\activate`

3. **Install the required packages**

    `pip install -r requirements.txt`

4. **Apply migrations to set up the database**

    `python manage.py migrate`

5. **Run the development server**

    `python manage.py runserver`
