#!/bin/bash -eu
set -eu

input_file="${HOME}/Desktop/pro_con/code_runner_input.txt"
# input_tmp="${HOME}Desktop/pro_con/input_tmp.txt"
# cp $input_file $input_tmp
# sed -i '/^$/d' $input_tmp

dir=$1
filename=$2
filename_without_ext=$3

# echo $dir
# echo $filename
# echo $filename_without_ext

cd $dir # dir
g++ $filename -std=c++17 -I${HOME}/Desktop/pro_con/ -o $filename_without_ext

if [ -s $input_file ]; then
    # cat $input_file
    echo "input from file"
    $dir$filename_without_ext < $input_file
else
    echo "Please input..."
    $dir$filename_without_ext
fi