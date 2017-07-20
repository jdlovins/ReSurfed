#!/bin/bash
if [ "$TRAVIS_BRANCH" == "development" ]
then
        echo "We are in the dev branch settings"
        HOST=$dev_host
        USER=$dev_user
        PASSWORD=$dev_pass
        HOME_DIR=$dev_home
fi

if [ $TRAVIS_BRANCH == "master" ]
then
        echo "We are in the master branch settings"
        HOST=$PROD_HOST
        USER=$PROD_USER
        PASSWORD=$PROD_PASSWORD
        HOME_DIR=$PROD_DIR
fi

export SSHPASS=$DEPLOY_PASS

sshpass -e ssh $USER@$HOST 'echo "abc" > test.file'