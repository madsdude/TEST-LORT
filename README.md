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

The web service will be available on `http://localhost:8000`.

### Endpoints

- `GET /diagnostic` - Check socket connectivity. Optional query parameters
  `host` and `port` allow testing a specific endpoint.
- `GET /http_check` - Perform a simple HTTP HEAD request using the `url`
  query parameter.

Example diagnostic request:

```bash
curl "http://localhost:8000/diagnostic?host=1.1.1.1&port=53"
```
