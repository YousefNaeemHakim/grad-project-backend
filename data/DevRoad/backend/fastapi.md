# FastAPI

## Introduction

FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard Python type hints. It is built on top of Starlette for the web parts and Pydantic for the data parts.

In this learning summary, we will cover the basics of FastAPI and how to build a simple API using it. We will go from zero to hero with code snippets to help you learn FastAPI.

## Prerequisites

To follow this learning summary, you will need to have Python 3.6 or later installed on your machine. You will also need to have pip, the Python package installer, installed.

You can install FastAPI and its dependencies by running the following command in your terminal:

```bash
pip install fastapi uvicorn[standard] aiofiles
```

- `fastapi` - the FastAPI framework
- `uvicorn` - a high-performance ASGI server
- `aiofiles` - for handling files asynchronously

## Getting Started

Let's start by creating a new file called `main.py`. This file will contain the code for our FastAPI application.

```py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

This code creates a new FastAPI application instance and defines a single route at the root URL ("/"). When the route is requested, the `root` function is called and returns a JSON object containing the message "Hello World".

We are using the HTTP method decorator `@app.get("/")` to define a route that will respond to HTTP GET requests on the root URL ("/"). The `async def` keyword indicates that this function is asynchronous, meaning it can handle multiple requests at the same time without blocking.

## Running the Application

To run the application, we will use Uvicorn, a fast HTTP server. You can start the server by running the following command in your terminal:

```bash
uvicorn main:app --reload
```

- `main:app` refers to the `app` object in our `main.py` file.
- `--reload` enables auto-reloading, which means that the server will automatically restart whenever you make changes to your code.

This will start the server on port 8000. You can now access your application by visiting `http://localhost:8000/` in your web browser.

## Testing the API

To test the API, you can use a tool like `curl` or a web browser. Open a new terminal window and run the following command to send a GET request to the root URL:

```bash
curl http://localhost:8000/
```

You should see the following JSON response:

```json
{"message": "Hello World"}
```

Congratulations, you have successfully built and tested your first FastAPI application!

## Adding Request Parameters

Let's modify our application to accept a request parameter. We will define a new route at `/items/{item_id}` that will return a JSON object containing the item ID that was passed in.

```py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

The new route `/items/{item_id}` has a path parameter `item_id` that is defined in the function signature. The `int` type hint specifies that this parameter should be an integer.

## Handling Request Bodies

FastAPI makes it easy to handle request bodies. Let's create a new route that accepts a JSON request body and returns it as a response

```py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.post("/items/")
async def create_item(item: Item):
    return item
```

We have created a new class `Item` that inherits from `BaseModel`. This class defines the structure of our request body. We have also defined a new route `/items/` that accepts HTTP POST requests and expects an `Item` object as the request body.

When a request is made to this route, the `create_item` function is called with the request body as its parameter. The function simply returns the same object back as a response.

## Adding Documentation

FastAPI generates interactive documentation for your API automatically based on the type hints you provide. Let's add some documentation to our API by adding descriptions to our routes and parameters:

```py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

@app.get("/", summary="Root Route", description="This is the root route of the API")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}", summary="Read Item", description="Read an item by ID")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.post("/items/", summary="Create Item", description="Create a new item")
async def create_item(item: Item):
    return item
```

We have added `summary` and `description` attributes to our routes and parameters to provide more information about them. This information will be displayed in the documentation.

To view the documentation, go to `http://localhost:8000/docs` in your web browser. You will see an interactive API documentation page that allows you to test your API and view the documentation for each route and parameter.

## Handling Errors

When developing APIs, it's important to handle errors gracefully. FastAPI makes it easy to handle errors by defining custom exception handlers.

```py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

inventory = {}

@app.get("/items/{item_id}", summary="Read Item", description="Read an item by ID")
async def read_item(item_id: int):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "name": inventory[item_id]["name"], "price": inventory[item_id]["price"], "is_offer": inventory[item_id]["is_offer"]}

@app.post("/items/", summary="Create Item", description="Create a new item")
async def create_item(item: Item):
    item_id = len(inventory) + 1
    inventory[item_id] = {"name": item.name, "price": item.price, "is_offer": item.is_offer}
    return {"item_id": item_id, "name": item.name, "price": item.price, "is_offer": item.is_offer}

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(status_code=exc.status_code, content={"error": exc.detail})
```

In this example, we have defined a new exception handler using the `@app.exception_handler` decorator. This handler will be called whenever an `HTTPException` is raised in one of our routes.

The handler takes two arguments: the request and the exception that was raised. It returns a `JSONResponse` object with the appropriate status code and error message.

Now, when a request is made to a route that raises an `HTTPException`, our custom handler will be called and the error will be returned as a JSON response.

## Conclusion

In this part of our learning summary, we have learned how to handle errors in our API using FastAPI's built-in exception handling system. By defining custom exception handlers, we can provide informative error messages to our clients and handle errors gracefully.