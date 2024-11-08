#!/bin/sh

set -e

alembic revision --autogenerate -m "init"
alembic upgrade head




