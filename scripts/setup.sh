#!/bin/bash

PROJECT_FOLDER=$1
PROJECT_BRANCH=$2
PROJECT_REPO=$3


if [ ! -d "$PROJECT_FOLDER" ]; then
    git clone $PROJECT_REPO --branch $PROJECT_BRANCH --single-branch $PROJECT_FOLDER

else
    cd $PROJECT_FOLDER
    git checkout
fi