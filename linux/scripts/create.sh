#!/bin/bash

function is_user_exists()
{
   user=`egrep "^$username:" /etc/passwd`
   if [ "$user" == "" ] 
    then 
       return 0
    else
       return 1 
   fi
 
}


cat $1 | while read username
do
    is_user_exists
    bexists=$?

    if [ "$bexists" -eq 0 ] 
      then
         useradd $username
         echo "Created $username"
      else
         echo "Ignoring $username"
    fi

done
