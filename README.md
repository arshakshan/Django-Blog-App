# Blog Platform with Commenting System

## Overview

This project is a Django-based blog platform that allows users to create blog posts, comment on them, and engage with the content by liking or disliking posts and comments. The platform includes a well-structured PostgreSQL database to manage relationships between blog posts, comments, authors, and likes/dislikes. It also features a RESTful API for interacting with the data programmatically and a user-friendly frontend interface rendered with Django templates.

## Features

- **User Authentication & Authorization**: Secure user registration, login, and management features to control access to post creation and commenting.
- **CRUD Operations**: Create, read, update, and delete operations for blog posts, comments, and likes/dislikes.
- **Interactive UI**: User interface components for creating posts, commenting, and liking/disliking, all dynamically rendered with Django templates.
- **RESTful API**: Endpoints for programmatic access to blog posts, comments, and user interactions, built using Django REST Framework.
- **Advanced Sorting & Filtering**: Sort and filter blog posts based on date, number of likes, and categories.
- **Database Management**: PostgreSQL as the backend for robust and scalable data storage.

## Technologies Used

- **Django**: Web framework used to build the application.
- **PostgreSQL**: Relational database management system for storing blog data.
- **Django REST Framework**: For building the RESTful API endpoints.
- **PGAdmin**: Database management tool used for designing the database schema.
- **HTML/CSS & Django Templates**: Frontend rendering of the blog content and user interactions.
- **Postman**: Tool used for testing and validating API endpoints.

## Project Setup

### Prerequisites

- Python 3.11.4
- PostgreSQL
- Django 5.0.6
- Django REST Framework
- PGAdmin (optional for database management)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/arshakshan/Django-Blog-App.git
   cd blogapp
   ```

2. **Create a Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup PostgreSQL Database**
   - Create a PostgreSQL database and configure your `settings.py` to include the database connection details.

5. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

### ER Diagram

The project includes an ER diagram that illustrates the relationships between the main entities: blog posts, comments, authors, and likes/dislikes. This diagram can be found in the `docs/` directory.

## API Endpoints

- **/api/posts/**: Access to blog posts (GET, POST, PUT, DELETE)
- **/api/comments/**: Access to comments on posts (GET, POST, PUT, DELETE)
- **/api/likes/**: Access to likes/dislikes on posts and comments (GET, POST)

### Testing API Endpoints

You can use Postman or any other API testing tool to interact with the API endpoints.

## Usage

1. **Creating Posts**: Authenticated users can create blog posts via the provided form or through the API.
2. **Commenting**: Users can comment on posts and like/dislike comments and posts.
3. **Sorting & Filtering**: Users can sort and filter posts based on various criteria directly from the UI.

## Advanced Features

- **Sorting & Filtering**: Users can sort posts by date or number of likes and filter by categories.
- **User Authentication**: Integrated user authentication allows secure access to post creation and commenting features.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to suggest improvements.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---