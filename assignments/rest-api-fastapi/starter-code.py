from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# TODO: Define your Book model using Pydantic BaseModel
# Include fields like: id, title, author, genre, year

# TODO: Create an in-memory storage for books (e.g., a list or dictionary)

@app.get("/")
def read_root():
    """Welcome endpoint"""
    return {"message": "Welcome to the Book Library API"}

# TODO: Implement GET /books - Get all books

# TODO: Implement GET /books/{book_id} - Get a specific book

# TODO: Implement POST /books - Create a new book

# TODO: Implement PUT /books/{book_id} - Update a book

# TODO: Implement DELETE /books/{book_id} - Delete a book

# Run with: uvicorn starter-code:app --reload
