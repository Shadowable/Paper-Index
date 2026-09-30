# Flask GET API

## Implementation Process

1. Declare Flask as the project dependency in `requirements.txt`.
2. Create `app.py` with a browser catalog at `/`, item detail pages at `/items/<id>`, and two read-only JSON GET routes backed by a small in-memory item list:
   - `GET /api/items` returns all items as JSON.
   - `GET /api/items/<id>` returns one item as JSON, or a JSON 404 response if it does not exist.
3. Install the dependency in the project's virtual environment and run the development server.
4. Verify both routes using a browser or `curl.exe`.

The Flask development server is intended for local development, not production deployment. The sample data resets when the server restarts.

## Setup

The workspace already has a `.venv` virtual environment. If setting up a fresh checkout, create it with:

```powershell
python -m venv .venv
```

Activate it in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks the activation script, allow scripts for the current terminal process only, then activate:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
.\.venv\Scripts\Activate.ps1
```

Install Flask and start the app from the project directory:

```powershell
python -m pip install -r requirements.txt
python app.py
```

## Try the API

With the server running, send GET requests from another terminal:

```powershell
curl.exe http://127.0.0.1:5000/api/items
curl.exe http://127.0.0.1:5000/api/items/1
curl.exe http://127.0.0.1:5000/api/items/999
```

The first request returns the item list, the second returns item 1, and the last returns a 404 JSON error. The routes support GET; Flask also provides automatic HEAD and OPTIONS handling. Write methods such as POST, PUT, PATCH, and DELETE are not supported.
