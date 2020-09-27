# fastAPI w/ Alembic (and SQLAlchemy)

Trying to find a nice pattern.
See [alembic/](./alembic/) for more alembic details.
The [tests/test_alembic.py](./tests/test_alembic.py) looks somewhat hacky
but it is the best solution I found (see docstring).
In docker, the test will be done before starting the app.

```
sudo docker build -t test .
sudo docker run -t -i --rm -p 8000:8000 test
```
