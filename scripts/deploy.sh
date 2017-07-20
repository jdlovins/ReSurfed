#!/bin/bash
set -x

export SSHPASS=$dev_pass
echo $SSHPASS

sshpass -f pass.txt ssh $USER@$HOST "echo 'please' > /tmp/file"
