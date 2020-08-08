#!/bin/bash

if [ -e "./test_case/$1/$2" ]; then
    echo ""
else
    python test_scrape.py $1 $2
fi

cnt=`cat ./test_case/$1/$2/test_cnt.txt`

for ((i=1; i<=cnt; i++)); do 
    echo "\033[0;37m---- case $i ----\033[0;39m"
    python "$1_$2.py" < "./test_case/$1/$2/input_$i.txt" > "./test_case/$1/$2/tmp.txt"
    diff -s -q "./test_case/$1/$2/tmp.txt" "./test_case/$1/$2/output_$i.txt" > /dev/null
    if [ $? -eq 0 ]; then
        echo "\033[0;34mOK\033[0;39m"
    elif [ $? -eq 1 ]; then
        echo "\033[0;31mNG\033[0;39m"
        echo "[input]"
        cat "./test_case/$1/$2/input_$i.txt"
        echo ""
        echo "[output]"
        cat "./test_case/$1/$2/tmp.txt"
        echo ""
        echo "[answer]"
        cat "./test_case/$1/$2/output_$i.txt"
    else
        echo "error"
    fi
    echo ""
done
