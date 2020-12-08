#!/bin/bash
set -e


BASEDIR=$(dirname "$0")
cd "$BASEDIR"

cd ./../tests
pytest -vv