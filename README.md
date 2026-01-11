Django Discussion Board
=======================

Overview
--------
This project is a **web-based Discussion Board application** built using the Django framework.
It allows users to create discussion boards, post topics, and interact through messages/posts,
similar to a simple forum system.

The goal of this project is to demonstrate:
- Django project structuring
- User authentication and authorization
- Handling relational data (boards, topics, posts)
- Using templates and static files in Django
- Basic CRUD operations in a real-world web application

This project can be used for learning purposes, academic projects, or as a base
for a more advanced forum or community platform.

Main Features
-------------
- User registration and authentication
- Multiple discussion boards
- Topics inside each board
- Posts/messages inside each topic
- Django Admin panel for managing data
- Clean separation of apps and project settings

Project Structure
-----------------
Django_discussion_board/
│
├── accounts/
│   └── Handles user-related functionality (authentication, profiles, etc.)
│
├── boards/
│   └── Core discussion logic:
│       - Boards
│       - Topics
│       - Posts
│
├── discussion_board/
│   └── Main Django project folder:
│       - settings.py
│       - urls.py
│       - wsgi.py / asgi.py
│
├── templates/
│   └── HTML templates used by the application
│
├── static/
│   └── CSS, JavaScript, images, and other static files
│
├── manage.py
│   └── Django management utility
│
└── requirements.txt
    └── Python dependencies required for the project

Technologies Used
-----------------
- Python 3
- Django
- HTML5
- CSS3
- SQLite (default Django database, can be replaced)

Installation & Local Setup
--------------------------
1) Clone the repository:
   git clone https://github.com/Khalil-Abboud/Django_discussion_board.git
   cd Django_discussion_board

2) Create and activate a virtual environment:

   On Linux/macOS:
   python3 -m venv venv
   source venv/bin/activate

   On Windows:
   py -m venv venv
   venv\Scripts\activate

3) Install dependencies:
   pip install -r requirements.txt

4) Apply database migrations:
   python manage.py makemigrations
   python manage.py migrate

5) (Optional) Create a superuser:
   python manage.py createsuperuser

6) Run the development server:
   python manage.py runserver

7) Open your browser and visit:
   http://127.0.0.1:8000/

Admin Panel
-----------
You can access the Django admin panel at:
http://127.0.0.1:8000/admin/

Use the superuser credentials created earlier to log in.
From there you can manage users, boards, topics, and posts.

Static Files
------------
During development, Django serves static files automatically.
For production environments:
- Configure STATIC_ROOT and STATIC_URL in settings.py
- Run:
  python manage.py collectstatic

Environment & Security Notes
----------------------------
- Do NOT expose SECRET_KEY in production
- Set DEBUG = False in production
- Configure ALLOWED_HOSTS properly
- Use environment variables for sensitive settings

Common Commands
---------------
- Run tests (if available):
  python manage.py test

- Create migrations for a specific app:
  python manage.py makemigrations app_name

- Apply migrations:
  python manage.py migrate

Use Cases
---------
- Learning Django fundamentals
- University or training projects
- Prototype for a forum or community website
- Base project for expanding features like:
  - Likes
  - Comments
  - Notifications
  - User profiles

License
-------
No license file is currently provided.
By default, all rights are reserved.
You may add a LICENSE file (MIT, GPL, etc.) if desired.

Author
------
Developed by: Khalil Abboud
GitHub Repository: Django_discussion_board
