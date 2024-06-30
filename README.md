
# Comparing Synchronous and Asynchronous Python Web Frameworks

### Purpose
Gain a deeper understanding of asynchronous web frameworks and their inner workings by comparing them to their synchronous counterparts.

### Conditions
- **Frameworks Compared:** FastAPI (asynchronous) and Flask (synchronous)
  
```python
# flask_app.py
import time
from flask import Flask

app = Flask(__name__)

@app.get('/')
def some_long_route():
    time.sleep(3)
    return "hello world"
```
```python
# fastapi_app.py
import asyncio
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def some_long_route():
    await asyncio.sleep(3)
    return 'hello world'
```

- **Server Configuration:** Launch each server with a single thread and worker process:
  - Flask: `gunicorn -w 1 flask_app:app`
  - FastAPI: `uvicorn fastapi_app:app --workers 1`
- **Load Testing:** Send 10 concurrent requests to each server using curl:
  ```bash
  seq 1 10 | xargs -n1 -P10 curl -s http://localhost:8000/
  ```

### Results
- **Flask:** Handled 10 requests in approximately 30 seconds.
- **FastAPI:** Handled 10 requests in approximately 3 seconds.

### Conclusion
FastAPI's ability to handle multiple requests at the same time is much better than Flask's. This experiment shows that asynchronous web frameworks like FastAPI are more efficient for tasks that involve waiting, such as I/O operations. As a result, FastAPI performs much better in situations where many requests need to be handled quickly, making it a great choice for modern web applications that need to be fast and scalable.