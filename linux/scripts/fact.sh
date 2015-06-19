#!/bin/bash 
 
if [ "$#" -eq 0 ]; then 
    echo "Saisir une valeur : " 
    read -r val 
else 
    val=$1 
fi 
 
# Dans le cas où c'est négatif, on rend la valeur positive 
if [ "$val" -lt 0 ]; then 
    let val=-1*$val 
fi 
 
result=1 
val2="$val"
 
while [ "$val" -ne 0 ]; do 
    echo -n "$val " 
    let result=$result*$val 
    let val=$val-1 
    if [ "$val" -ne 0 ]; then 
        echo -n "* " 
    fi 
done 
 
echo "= $result"

