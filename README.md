# Sample pages for browser testing

How to develop locally:

1. Install [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/install/)
2. Run `docker-compose up --build`.
3. Go http://localhost:8080

You can override port: `PORT=5000 docker-compose up`

To run tests:

```sh
docker-compose down # down currenly running dev containers if any
./scripts/test.sh
```
