#!/bin/bash
TRAVIS_BRANCH="master"

if [ $TRAVIS_BRANCH == "development" ]; then
	HOST=$dev_host
	USER=$ev_user
	PASSWORD=$dev_pass
	HOME_DIR=$dev_home
fi

if [ $TRAVIS_BRANCH == "master" ]; then
	HOST=$PROD_HOST
	USER=$PROD_USER
	PASSWORD=$PROD_PASSWORD
	HOME_DIR=$PROD_DIR
fi

export SSHPASS=$DEPLOY_PASS

sshpass -e ssh $USER@$HOST 'echo "abc" > test.file'