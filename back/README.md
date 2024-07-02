# Install it
1. Create a virtual env if needed
```bash
python3 -m venv venv
```

2. Install the dependencies
```bash
pip install ".[quality,deployment]"
```

# Run it
```bash
gunicorn \
  --workers 1 \
  --worker-class uvicorn.workers.UvicornWorker \
  --threads 2 \
  --timeout 0 \
  "chat_backend:create_app()"
```

# Test it
Run the tests
```bash
pytest
```

Or perform a load test with locust
```bash
locust
```
