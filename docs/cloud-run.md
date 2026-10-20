# Dummy Docker and Cloud Run Deployment Guide

This document is an illustrative deployment plan for the CS3654 project. It
does not create Docker images or deploy anything by itself.

The backend and frontend should be deployed as separate Cloud Run services:

- `cs3654-backend`: FastAPI API
- `cs3654-frontend`: Dash dashboard

## Prerequisites

Install Docker and the Google Cloud CLI, then authenticate and select a
Google Cloud project:

```bash
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
gcloud services enable run.googleapis.com artifactregistry.googleapis.com
```

Set a deployment region and Artifact Registry repository:

```bash
gcloud config set run/region us-east1
gcloud artifacts repositories create cs3654 \
  --repository-format=docker \
  --location=us-east1
```

Replace `YOUR_PROJECT_ID` and `us-east1` with the values for the deployment.

## Backend container

Create a file named `Dockerfile.backend` in the repository root:

```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src ./src

CMD exec uvicorn src.backend.main:app \
  --host 0.0.0.0 \
  --port ${PORT:-8080}
```

Build, push, and deploy the backend:

```bash
export REGION=us-east1
export PROJECT_ID=YOUR_PROJECT_ID
export REPOSITORY=cs3654
export BACKEND_IMAGE=$REGION-docker.pkg.dev/$PROJECT_ID/$REPOSITORY/backend:latest

gcloud auth configure-docker $REGION-docker.pkg.dev
docker build -f Dockerfile.backend -t $BACKEND_IMAGE .
docker push $BACKEND_IMAGE
gcloud run deploy cs3654-backend \
  --image $BACKEND_IMAGE \
  --platform managed \
  --allow-unauthenticated
```

Record the backend URL printed by Cloud Run. It can be used by the frontend
once the dashboard makes API requests.

## Frontend container

The current Dash app is intended for local development and hardcodes port
`8050`. Before deploying it to Cloud Run, update it to bind to
`0.0.0.0` and read the Cloud Run `PORT` environment variable. For example:

```python
import os

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", "8050")),
        debug=False,
    )
```

Create a file named `Dockerfile.frontend` in the repository root after making
that change:

```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src ./src

CMD exec python -m src.frontend.app
```

Build and deploy the frontend:

```bash
export FRONTEND_IMAGE=$REGION-docker.pkg.dev/$PROJECT_ID/$REPOSITORY/frontend:latest

docker build -f Dockerfile.frontend -t $FRONTEND_IMAGE .
docker push $FRONTEND_IMAGE
gcloud run deploy cs3654-frontend \
  --image $FRONTEND_IMAGE \
  --platform managed \
  --allow-unauthenticated
```

## Notes for a real deployment

- Do not use `debug=True` in production.
- Pin dependency versions before building release images.
- Store secrets in Secret Manager rather than in Dockerfiles or source code.
- Restrict backend access if it should not be publicly reachable.
- Configure CORS and the frontend API base URL when the frontend starts calling
  the deployed backend.
- Add health checks, logging, monitoring, and a CI/CD workflow before relying
  on the deployment.
