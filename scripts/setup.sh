#!/bin/bash

PROJECT_FOLDER=$1
PROJECT_BRANCH=$2
PROJECT_REPO=$3

source ./env_variables

if [ ! -d "$PROJECT_FOLDER" ]; then
    git clone $PROJECT_REPO --branch $PROJECT_BRANCH --single-branch $PROJECT_FOLDER
    virtualenv venv
else
    cd $PROJECT_FOLDER
    git checkout
    cd ..
fi

source venv/bin/activate
pip install -r $PROJECT_FOLDER/requirements.txt

cd $PROJECT_FOLDER

python manage.py migrate
python manage.py collectstatic