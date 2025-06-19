# TEST-LORT

This project demonstrates a simple Flask application that performs a basic
network connectivity diagnostic.

## Running with Docker

Build the Docker image:

```bash
docker build -t test-lort .
```

Run the container:

```bash
docker run -p 8000:8000 test-lort
```

The web service will be available on `http://localhost:8000`. Visit
`/diagnostic` to run a basic connectivity check.
