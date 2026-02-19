```markdown
# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Create a small RESTful API using the FastAPI framework to practice designing endpoints, request/response models, and basic testing. The finished project should demonstrate correct HTTP methods, JSON handling, and simple in-memory persistence.

## 📝 Tasks

### 🛠️ Implement a basic REST API

#### Description
Use the provided starter code at [assignments/fastapi-rest-apis/starter-code.py](assignments/fastapi-rest-apis/starter-code.py) as the starting point. Implement endpoints to create, read, update, and delete simple `item` resources and validate request payloads with Pydantic models.

#### Requirements
Completed program should:

- Expose at least these endpoints:
  - `GET /` — returns a welcome message.
  - `GET /items/` — returns a list of items.
  - `GET /items/{item_id}` — returns a single item or 404.
  - `POST /items/` — create a new item from JSON payload.
  - `PUT /items/{item_id}` — update an existing item.
  - `DELETE /items/{item_id}` — remove an item.
- Use Pydantic models for request validation and response serialization.
- Use appropriate HTTP status codes for success and error cases.
- Keep data in-memory (a Python list or dict) — persistence to disk is optional.
- Include example requests in the README and ensure the app runs with `uvicorn`.


### 🛠️ Optional enhancements

#### Description
Add features that demonstrate deeper understanding of FastAPI and web APIs.

#### Suggestions

- Add query parameters for filtering or pagination on `GET /items/`.
- Add basic dependency injection for a simple auth token.
- Add OpenAPI examples and response models to improve documentation.
- Add unit tests using `pytest` and `httpx` (or `requests`) to exercise endpoints.

## Files

- Starter code: [assignments/fastapi-rest-apis/starter-code.py](assignments/fastapi-rest-apis/starter-code.py)

## How to run

From the repository root, install dependencies and run the app:

```bash
pip install fastapi uvicorn
cd assignments/fastapi-rest-apis
uvicorn starter-code:app --reload
```

Open the interactive API docs at http://127.0.0.1:8000/docs

## Submission

Submit the updated `starter-code.py` (and any additional files) in the `assignments/fastapi-rest-apis/` folder following course instructions.

```
