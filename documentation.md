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

## Publish the Docker image with GitHub Actions

The `Build and publish Docker image` workflow builds the image from the repository's `Dockerfile` and pushes it to Docker Hub whenever code is pushed to any branch. It also supports manual runs from the GitHub Actions tab. Each published image receives a branch tag and a tag containing the commit SHA; pushes to the repository's default branch also update the `latest` tag.

Before the first run, add these repository secrets under **Settings → Secrets and variables → Actions**:

- `DOCKERHUB_USERNAME` — your Docker Hub username
- `DOCKERHUB_TOKEN` — a Docker Hub access token with permission to push to the target repository

By default, the target Docker Hub repository is `paper-index`, so the resulting image is `DOCKERHUB_USERNAME/paper-index`. If your Docker Hub repository has a different name, add an Actions repository variable named `DOCKERHUB_REPOSITORY` with that name. Create the target repository on Docker Hub before running the workflow if it does not already exist.
