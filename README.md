# Sample pages for browser testing

![Deploy](https://github.com/persidskiy/ibro-samples/workflows/Deploy/badge.svg)

[https://ibro.best](https://ibro.best)

### Developing

With docker:

1. Install [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/install/)
2. Run `docker-compose up --build`.
3. Go http://localhost:8080

You can override port: `PORT=5000 docker-compose up`

Without docker:

```bash
pip install -U flask
FLASK_APP=web/src/main.py FLASK_DEBUG=1 FLASK_ENV=development flask run
```

### Running tests

Tests just check that pages are available and respond HTTP 200.

```sh
docker-compose down # down currenly running dev containers if any
./scripts/test.sh
```
