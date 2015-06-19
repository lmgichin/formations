#!/bin/bash

if [ $# -eq 0 ] 
then
   echo "User is required"
   exit -1
fi

GREP="/bin/egrep"
PF="/etc/passwd"
ID="/usr/bin/id"
CUT="/bin/cut"

user=`$GREP "^$1:" $PF`

if [ "$user" == "" ]
then
    echo "User $1 not found in the system"
else
    echo "Id of user $1 is : " `$ID $1`
    HM=`echo $user | $CUT -d ':' -f 6`
    BS=`echo $user | $CUT -d ':' -f 7`
    echo -e "Home of user is : $HM\nBash is : $BS"
fi

