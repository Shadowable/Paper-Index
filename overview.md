# Paper Index Overview

Paper Index is a lightweight Flask web application that presents a small catalog of desk essentials and exposes the same data through JSON API endpoints. The product is intentionally simple: it shows a clean browser-based catalog, lets users click into individual items, and offers a readable API for the underlying data.

## What the product does

The app serves two main experiences:

- A catalog homepage that displays a curated list of items
- Individual detail pages for each item in the collection
- A machine-readable API that returns the same catalog data as JSON

In the current version, the catalog includes a few everyday items such as a notebook and a pen. The collection is intentionally minimal, making it easy to understand how the app works without extra database or infrastructure complexity.

## How it works

The application is built with Flask, a lightweight Python web framework.

### 1. App entry point

The main logic lives in `app.py`. This file:

- creates the Flask app
- defines the catalog data as a Python list
- registers routes for the web pages and API endpoints
- runs the development server when the script is launched directly

### 2. In-memory data source

The product stores its records in a Python list named `ITEMS`:

```python
ITEMS = [
    {"id": 1, "name": "Notebook"},
    {"id": 2, "name": "Pen"},
]
```

This design keeps the project easy to run and easy to understand. The data resets whenever the server restarts, because it is not persisted to a database.

### 3. Browser routes

The web app exposes these page routes:

- `/` — the main catalog page
- `/items/<int:item_id>` — the detail page for one item

The homepage renders a template called `templates/index.html`, which organizes the catalog into a visual product listing. The item page renders `templates/item.html`, which shows a larger view of one selected product and includes a JSON preview for that record.

### 4. API routes

The app also exposes read-only JSON endpoints:

- `GET /api/items` — returns the full list of items
- `GET /api/items/<int:item_id>` — returns one item by ID

These routes use Flask's `jsonify` helper to return structured JSON responses.

If the item ID does not exist, the API responds with a `404` status and an error payload such as:

```json
{"error": "Item not found"}
```

## Product flow

A typical user flow looks like this:

1. The user opens the landing page at `/`.
2. The homepage renders the collection of items using Jinja templates.
3. The user clicks an item card or navigates directly to `/items/1`.
4. The app searches the in-memory list for the matching item ID.
5. If the item exists, the detail page is shown; otherwise, a 404 page is displayed.
6. The same data can also be used programmatically through the API endpoints.

## Frontend behavior

The homepage includes a simple client-side search box. As the user types, the script filters item cards in the browser without reloading the page. This is a lightweight enhancement that makes the catalog feel more polished while keeping the backend simple.

## Why this product is useful

Paper Index is a good example of a minimal product that demonstrates:

- Flask route handling
- HTML template rendering
- JSON API design
- simple product catalog patterns
- separate frontend and API concerns in a small codebase

It is designed for learning, prototyping, and understanding how a basic web app can expose both user-friendly pages and machine-readable data.

## How to run it

From the project directory:

```powershell
python -m pip install -r requirements.txt
python app.py
```

Then open:

```text
http://127.0.0.1:5000/
```

You can also test the API directly with `curl`:

```powershell
curl.exe http://127.0.0.1:5000/api/items
curl.exe http://127.0.0.1:5000/api/items/1
```

## Summary

Paper Index is a small Flask-based catalog application that blends a polished, browser-friendly interface with straightforward API endpoints. Its architecture is intentionally simple: static data, clear route definitions, and easy-to-read templates. This makes it an ideal example for learning how a web product can serve both human users and API clients from the same underlying data source.
