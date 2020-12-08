#!/bin/bash
set -e


BASEDIR=$(dirname "$0")
cd "$BASEDIR"

cd ./../tests
# run pytest in parallel
pytest -n auto