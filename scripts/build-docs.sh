#!/bin/bash
set -e


BASEDIR=$(dirname "$0")
cd "$BASEDIR"

cd ./../docs
rm -rf api _build
sphinx-apidoc -eM -o api -a ./../damsenviet
make html