#!/bin/bash
if [ "$TRAVIS_BRANCH" == "development" ]
then
        echo "We are in the dev branch settings"
        HOST=$dev_host
        USER=$dev_user
        HOME_DIR=$dev_home
        PASS=$dev_pass
fi

if [ $TRAVIS_BRANCH == "master" ]
then
        echo "We are in the master branch settings"
        HOST=$PROD_HOST
        USER=$PROD_USER
        HOME_DIR=$PROD_DIR

        export SSHPASS=$prod_pass
fi

echo $PASS > pass.txt
cat pass.txt

sshpass -f pass.txt -e ssh $USER@$HOST 'bash write.sh'
