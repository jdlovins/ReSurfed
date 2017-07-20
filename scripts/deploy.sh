#!/bin/bash
if [ "$TRAVIS_BRANCH" == "development" ]
then
        echo "We are in the dev branch settings"
        HOST=$dev_host
        USER=$dev_user
        HOME_DIR=$dev_home

        export SSHPASS=$dev_pass
fi

if [ $TRAVIS_BRANCH == "master" ]
then
        echo "We are in the master branch settings"
        HOST=$PROD_HOST
        USER=$PROD_USER
        HOME_DIR=$PROD_DIR

        export SSHPASS=$prod_pass
fi



sshpass -e ssh $USER@$HOST 'echo "abc" > test.file'