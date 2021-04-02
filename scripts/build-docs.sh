#!/bin/bash
set -e


BASEDIR=$(dirname "$0")
cd "$BASEDIR"

cd ./../docs
rm -rf _build
make html