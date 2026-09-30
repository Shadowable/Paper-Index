# API Overview

This project is a small Flask REST API for retrieving a sample list of items. It returns JSON and currently exposes read-only endpoints.

## Features

- List all sample items.
- Retrieve one item by its integer ID.
- Return a JSON 404 error when the requested item does not exist.
- Browse a designed catalog at `/`, search the items, and open an individual detail page at `/items/<id>`.
- Reject write requests such as POST, PUT, PATCH, and DELETE. Flask also handles HEAD and OPTIONS automatically.

The sample catalog contains a Notebook (ID 1) and a Pen (ID 2). Data is stored in memory, so it resets when the app restarts. There is no database or item-editing functionality.

## Start the API

Open PowerShell in the project directory. The workspace's virtual environment can be activated with:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks the activation script, allow it for the current terminal process, then activate:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
.\.venv\Scripts\Activate.ps1
```

Install dependencies and start the local development server:

```powershell
python -m pip install -r requirements.txt
python app.py
```

The visual catalog is available at `http://127.0.0.1:5000/`; the JSON list remains at `http://127.0.0.1:5000/api/items`. Keep the terminal running while browsing or making requests.

## Endpoints

### List items

`GET /api/items`

```powershell
curl.exe http://127.0.0.1:5000/api/items
```

Returns an array of items:

```json
[
  {"id": 1, "name": "Notebook"},
  {"id": 2, "name": "Pen"}
]
```

### Get an item

`GET /api/items/<id>`

```powershell
curl.exe http://127.0.0.1:5000/api/items/1
```

Returns the matching item as JSON:

```json
{"id": 1, "name": "Notebook"}
```

For an unknown ID, such as `999`, the API returns HTTP 404:

```json
{"error": "Item not found"}
```

This Flask development server is for local development, not production deployment.
