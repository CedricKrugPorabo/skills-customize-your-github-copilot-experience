# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern, high-performance REST APIs using the FastAPI framework. This assignment will teach you the fundamentals of API design, HTTP methods, request/response handling, and data validation in Python.

## 📝 Tasks

### 🛠️	Create a Book Library API

#### Description
Build a REST API for managing a book library. The API should allow users to create, read, update, and delete books from a collection. Implement proper HTTP methods and status codes for each operation.

#### Requirements
Completed program should:

- Implement GET endpoint to retrieve all books
- Implement GET endpoint to retrieve a single book by ID
- Implement POST endpoint to add a new book
- Implement PUT endpoint to update an existing book
- Implement DELETE endpoint to remove a book
- Use Pydantic models for request/response validation
- Include proper HTTP status codes (200, 201, 404, etc.)
- Store data in memory using a Python list or dictionary


### 🛠️	Add Query Parameters and Documentation

#### Description
Enhance your API with query parameters for filtering and searching. Take advantage of FastAPI's automatic API documentation to create a well-documented interface.

#### Requirements
Completed program should:

- Add query parameters to filter books by author or genre
- Implement pagination using limit and offset parameters
- Include proper type hints for all functions
- Add descriptive docstrings to all endpoints
- Test the API using the auto-generated Swagger UI at `/docs`
