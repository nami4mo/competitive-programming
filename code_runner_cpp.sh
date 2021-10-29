#!/bin/bash -eu
set -eu

input_file="${HOME}/Desktop/pro_con/code_runner_input.txt"

dir=$1
filename=$2
filename_without_ext=$3

cd $dir # dir
g++ $filename -std=c++17 -I${HOME}/Desktop/pro_con/ -o $filename_without_ext

if [ -s $input_file ]; then
    # cat $input_file
    # echo "input from file"
    # $dir$filename_without_ext < $input_file > "$HOME/Desktop/tmp.txt"
    $dir$filename_without_ext < $input_file
else
    echo "Please input..."
    $dir$filename_without_ext
fi