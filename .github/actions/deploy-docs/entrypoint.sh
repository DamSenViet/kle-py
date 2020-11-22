#!/bin/bash

set -e

cd "${GITHUB_WORKSPACE}"

echo "install dependencies"

pip install .[test,docs]

echo "installed dependencies"

echo "testing"

./scripts/test.sh

echo "tested"


echo "building"
./scripts/build-docs.sh

echo "built"

cd ./docs/_build/html

echo "git configuring"

git init
git config user.name "${GITHUB_ACTOR}"
git config user.email "${GITHUB_ACTOR}@users.noreply.github.com"

echo "git configured"
echo "${GITHUB_ACTOR}"
echo "${GITHUB_REPOSITORY}"
echo "https://${ACCESS_TOKEN}@github.com/${GITHUB_REPOSITORY}.git"

git add .
git commit -m "Auto deploy from GitHub Actions"

echo "pushing"

git push -f "https://${ACCESS_TOKEN}@github.com/${GITHUB_REPOSITORY}.git" master:gh-pages

rm -rf .git

echo "pushed"