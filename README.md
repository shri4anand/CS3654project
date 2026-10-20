# CS3654 Final Project
This code holds the dashboard for the final CS3654 project. The Dataset of interest is [Twitter-Bot Detection Dataset](https://www.kaggle.com/datasets/goyaladi/twitter-bot-detection-dataset/data).


Authors: Rudra Patel, and Shriram Anand

## Backend

Install the dependencies and start the FastAPI development server from the
repository root:

```bash
pip install -r requirements.txt
uvicorn src.backend.main:app --reload
```

The hello-world endpoint is available at <http://127.0.0.1:8000/>. Interactive
API documentation is available at <http://127.0.0.1:8000/docs>.

## Frontend

Start the Dash frontend from the repository root in a second terminal:

```bash
python -m src.frontend.app
```

The dashboard is available at <http://127.0.0.1:8050/>. It uses a separate port
from the backend, so both applications can run concurrently.
