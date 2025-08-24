E-commerce Product API
This project is a robust, RESTful API for managing e-commerce products. It provides a secure and efficient backend for a front-end application to handle product listings, user management, and advanced search and filtering.

🚀 Features
Product Management: Full CRUD (Create, Read, Update, Delete) functionality for products.

Product Attributes: Each product includes name, description, price, category, stock, and image_url.

User Management: Basic user registration and authentication for managing products.

Secure Endpoints: All product management endpoints are secured, requiring authentication.

Advanced Search & Filtering: Products can be searched by name or filtered by category, price range, and stock availability.

Pagination: Results are paginated to handle large datasets efficiently.

💻 Getting Started

Install the required packages:

pip install -r requirements.txt

Run database migrations:

python manage.py makemigrations
python manage.py migrate

Create a superuser to access the Django admin and get an authentication token:

python manage.py createsuperuser

Run the development server:

python manage.py runserver

The API will be available at http://127.0.0.1:8000/api/.

🗺️ API Endpoints
All endpoints are prefixed with /api/.

Authentication
POST /api/token-auth/

Description: Obtain a user's authentication token.

Permissions: Public access.

Request Body: {"username": "your_username", "password": "your_password"}

Response: {"token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"}

Users
POST /api/register/

Description: Register a new user.

Permissions: Public access.

Request Body: {"username": "new_user", "email": "user@example.com", "password": "a_strong_password"}

Products
All product endpoints are secured. You must include the header Authorization: Token <your_token> in all requests that modify data.

Route

Method

Description

Permissions

/api/products/

GET

List all products. Supports search, filtering, and pagination.

Read-only

/api/products/

POST

Create a new product.

Authenticated

/api/products/{id}/

GET

Retrieve a single product by ID.

Read-only

/api/products/{id}/

PUT / PATCH

Update a product by ID.

Authenticated

/api/products/{id}/

DELETE

Delete a product by ID.

Authenticated

Search & Filtering
The GET /api/products/ endpoint supports the following query parameters:

search: Searches for text in name, description, and category__name fields.

category: Filters by the exact category name.

price_gte: Filters for products with a price greater than or equal to the given value.

price_lte: Filters for products with a price less than or equal to the given value.

stock_quantity__gt: Filters for products with stock greater than the given value.

Example URL:
http://127.0.0.1:8000/api/products/?search=shirt&category=Clothing&price_lte=50

Categories
GET /api/categories/

Description: List all product categories.

Permissions: Read-only.

POST /api/categories/

Description: Create a new category.

Permissions: Authenticated.

🛠️ Technologies Used
Django: Web framework

Django REST Framework: Toolkit for building APIs

Django Filters: For advanced filtering capabilities

SQLite3: Default database for development