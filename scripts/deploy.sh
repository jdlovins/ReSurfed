#!/bin/bash
set -x

export SSHPASS=$dev_pass
echo $SSHPASS

sshpass -e ssh $dev_user@$dev_host "echo 'please' > /tmp/file"
