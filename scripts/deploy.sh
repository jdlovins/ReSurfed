#!/bin/bash
if [ "$TRAVIS_BRANCH" == "development" ]
then
        echo "We are in the dev branch settings"
        HOST=$dev_host
        USER_NAME=$dev_user
        HOME_DIR=$dev_home

        export SSHPASS=$dev_pass
fi

if [ $TRAVIS_BRANCH == "master" ]
then
        echo "We are in the master branch settings"
        HOST=$PROD_HOST
        USER=$PROD_USER
        PASSWORD=$PROD_PASSWORD
        HOME_DIR=$PROD_DIR
fi



sshpass -e ssh -o stricthostkeychecking=no $USER_NAME@$HOST "echo 'abc' > test.file"