# Tree menu

Django app, реализующий древовидное меню.

# Install, Prepare, Run

1. Install

```shell
rye install
```

Alternative:

```shell
pip install -r requirements.lock
```

1. Prepare. Create `.env`, migrate, load data. Uses `envsubst`, works only for Linux.

```shell
make prepare
```

3. Run

```shell
make run
```

# Launched

Server should launch on `http://127.0.0.1:8000/`

Admin panel: `http://127.0.0.1:8000/admin`

Admin credentials:

login: admin
password: admin

# Screenshots

Located in `/static/screenshots`

Can be viewed in `SCREENSHOTS.md`

# Technology stack

1. Python3.12
2. Django
3. HTMX
4. django-split-settings
5. Pydantic
6. Dishka
7. Ruff, mypy, pre-commit
