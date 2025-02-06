# HNG-Stage1
# Number Classification API

## Overview
The **Number Classification API** is a FastAPI-based service that classifies numbers based on their mathematical properties and provides a fun fact retrieved from the Numbers API.

## Features
- Determines if a number is **prime** or **perfect**
- Checks if a number is an **Armstrong number**
- Identifies whether the number is **even** or **odd**
- Computes the **sum of its digits**
- Fetches a **fun fact** about the number from the Numbers API

## API Endpoint

### **GET** `/api/classify-number?number=<integer>`

### Request Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `number`  | int  | Yes      | The number to be classified |

### Success Response (200 OK)
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### Error Response (400 Bad Request)
```json
{
    "number": "alphabet",
    "error": true
}
```

## Installation & Setup

### Prerequisites
- Python 3.9+
- pip (Python package manager)

## Tech Stack
- **FastAPI** - Web framework
- **Uvicorn** - ASGI server
- **httpx** - HTTP client for external API calls

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/number-classification-api.git
   cd number-classification-api
   ```
2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the API Locally
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## Deployment
You can deploy this API on **Render, Vercel, or Heroku**.

### Deploying with Docker
1. Build the Docker image:
   ```bash
   docker build -t number-api .
   ```
2. Run the container:
   ```bash
   docker run -p 8000:8000 number-api
   ```

## Testing
Run tests using:
```bash
pytest tests/
```

## Tech Stack
- **FastAPI** - Web framework
- **Uvicorn** - ASGI server
- **httpx** - HTTP client for external API calls


## Author
[Caaleb Anoff](https://github.com/Anofff)

