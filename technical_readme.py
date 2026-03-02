tech_details = """
<details>
<summary>Technical README: Simple To-Do List Flask API</summary>

# Simple To-Do List Flask API

This is a minimalist To-Do List API built with Flask, providing basic CRUD operations for managing to-do items. The data is stored in memory and will reset upon application restart.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure you have Python and `pip` installed.

### Installation

1.  **Install Flask:**
    ```bash
    pip install Flask
    ```

### Running the Application

1.  **Navigate to the project directory:**
    ```bash
    cd /Users/dhananjayan/Documents/GitHub/self/newapp
    ```
2.  **Run the Flask development server:**
    ```bash
    python app.py
    ```
    The application will be running at `http://127.0.0.1:5000`.

## API Endpoints

The API provides the following endpoints for managing to-do items:

### 1. Get all To-Do Items

-   **URL:** `/todos`
-   **Method:** `GET`
-   **Description:** Retrieves a list of all existing to-do items.
-   **Response (200 OK):**
    ```json
    [
        {
            "id": 1,
            "task": "Learn Flask",
            "done": true
        },
        {
            "id": 2,
            "task": "Build a cool app",
            "done": false
        }
    ]
    ```
-   **Example `curl` command:**
    ```bash
    curl http://127.0.0.1:5000/todos
    ```

### 2. Add a New To-Do Item

-   **URL:** `/todos`
-   **Method:** `POST`
-   **Description:** Adds a new to-do item to the list.
-   **Request Body (JSON):**
    ```json
    {
        "task": "Buy groceries"
    }
    ```
-   **Response (201 Created):**
    ```json
    {
        "id": 3,
        "task": "Buy groceries",
        "done": false
    }
    ```
-   **Example `curl` command:**
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"task": "Buy groceries"}' http://127.0.0.1:5000/todos
    ```

### 3. Get a Specific To-Do Item

-   **URL:** `/todos/<int:todo_id>`
-   **Method:** `GET`
-   **Description:** Retrieves a single to-do item by its ID.
-   **Response (200 OK):**
    ```json
    {
        "id": 1,
        "task": "Learn Flask",
        "done": true
    }
    ```
-   **Response (404 Not Found):**
    ```json
    {
        "error": "Todo not found"
    }
    ```
-   **Example `curl` command:**
    ```bash
    curl http://127.0.0.1:5000/todos/1
    ```

### 4. Update a Specific To-Do Item

-   **URL:** `/todos/<int:todo_id>`
-   **Method:** `PUT`
-   **Description:** Updates an existing to-do item. You can update either `task`, `done`, or both.
-   **Request Body (JSON):**
    ```json
    {
        "task": "Finish project report",
        "done": true
    }
    ```
-   **Response (200 OK):**
    ```json
    {
        "id": 2,
        "task": "Finish project report",
        "done": true
    }
    ```
-   **Response (404 Not Found):**
    ```json
    {
        "error": "Todo not found"
    }
    ```
-   **Example `curl` command:**
    ```bash
    curl -X PUT -H "Content-Type: application/json" -d '{"done": true}' http://127.0.0.1:5000/todos/2
    ```

### 5. Delete a Specific To-Do Item

-   **URL:** `/todos/<int:todo_id>`
-   **Method:** `DELETE`
-   **Description:** Deletes a to-do item by its ID.
-   **Response (204 No Content):**
    (No content is returned upon successful deletion)
-   **Response (404 Not Found):**
    (If the ID does not exist, it will return 204 as the item is effectively "not there")
-   **Example `curl` command:**
    ```bash
    curl -X DELETE http://127.0.0.1:5000/todos/1
    ```

</details>
"""

if __name__ == "__main__":
    print(tech_details)
