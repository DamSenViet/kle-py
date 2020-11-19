#!/bin/bash
set -e


BASEDIR=$(dirname "$0")
cd "$BASEDIR"

cd ./../docs/_build/html
python3 -m http.server 8000 --bind 127.0.0.1