#!/bin/bash
if [ "$TRAVIS_BRANCH" == "development" ]
then
        echo "We are in the dev branch settings"
        DEPLOY_HOST=$dev_host
        DEPLOY_USER=$dev_user
        DEPLOY_PATH=$dev_path

        export SSHPASS=$dev_pass
fi

if [ $TRAVIS_BRANCH == "master" ]
then
        echo "We are in the master branch settings"
        HOST=$PROD_HOST
        USER=$PROD_USER
        PASSWORD=$PROD_PASSWORD
        HOME_DIR=$PROD_DIR

        export SSHPASS=$prod_pass
fi

sshpass -e scp -o stricthostkeychecking=no scripts/setup.sh $DEPLOY_USER@$DEPLOY_HOST:$DEPLOY_PATH

sshpass -e ssh -o stricthostkeychecking=no $DEPLOY_USER@$DEPLOY_HOST << EOF
    chmod +x setup.sh
    bash setup.sh "ReSurfed" "$TRAVIS_BRANCH" "https://github.com/jdlovins/ReSurfed.git"
EOF