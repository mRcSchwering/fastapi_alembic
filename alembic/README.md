# Migrations with Alembic

Created generic environment according to the [docs](https://alembic.sqlalchemy.org/en/latest/tutorial.html#the-migration-environment).
Note that in [alembic.ini](../alembic.ini) I need to enter the database URI and define the path of this directory.

In [env.py](./env.py) I import the declarative base and use it for autogenerating the migrations scripts.
Note that I also need to import the `models` module so that the declarative base gets actually _filled_ with
all the table meta data.
In order for alembic to see my package I need to add its directory to _PYTHONPATH_.

With an empty [sql_app.db](../sql_app.db) SQLite database the process could be like this:

1. `alembic revision --autogenerate -m "init"` which should create a migration file under [versions/](./versions/).
2. Check the migration file. Alembic doesnt always detect: column type change, table name change, column name change, special types like _Enum_, sequence additions/removals (see [the docs](https://alembic.sqlalchemy.org/en/latest/autogenerate.html#what-does-autogenerate-detect-and-what-does-it-not-detect))
3. `alembic upgrade head` which should create the tables.
4. Another update: added table `Test` to `models`
5. `alembic revision --autogenerate -m "test table added"`
6. Check migration file.
7. `alembic upgrade head` which should create the new table

In a fresh database with the above migrations in [versions/](./versions/) I can do
`alembic upgrade head` to create the latest database version.
So this is basically the equivalent of SQLAlchemy's `create_all()`.
Nice to know: `alembic current`, `alembic history --verbose`

Checking if code and database are in sync doesn't seem trivial: https://groups.google.com/g/sqlalchemy-alembic/c/uVU5Bxsqy44
