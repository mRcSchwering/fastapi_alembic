#!/usr/bin/env bash
set -e
python tests/test_alembic.py
uvicorn --host 0.0.0.0 --reload myapp.app:app
set +e