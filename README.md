# django-studybud

This application, developed in Python using the Django framework, allows users to create study rooms centered around a variety of subjects. It is inspired and built upon an in-depth tutorial by Traversy Media. You can view the tutorial at: https://www.youtube.com/watch?v=PtQiiknWUcI&t=22474

## Prerequisites

- Python 3.x
- pip

## Installation

1. **Clone the Repository**

   ```
   git clone https://github.com/davidcastagnetoa/django-studybud.git
   cd django-studybud
   ```

2. **Set Up a Virtual Environment (optional, but recommended)**

   ```
   python -m venv venv
   source venv/bin/activate  # En Windows usa: venv\Scripts\activate
   ```

3. **Install Django and Dependencies**

   ```
   pip install django
   pip install -r requirements.txt
   ```

## Execution

1. Perform initial migrations:

   ```
   python manage.py migrate
   ```

2. Start the development server:

   ```
   python manage.py runserver
   ```
