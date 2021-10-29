#!/bin/bash -eu
set -eu

input_file="${HOME}/Desktop/pro_con/code_runner_input.txt"
RUST_RUNNER_DIR="${HOME}/Desktop/pro_con/rust_runner"
RUNNER_MAIN="src/main.rs"
RUNNER_EXE="./target/debug/rust_runner"

dir=$1
filename=$2
filename_without_ext=$3

cd $dir # dir
rm "${RUST_RUNNER_DIR}/${RUNNER_MAIN}" || true
cp $filename "${RUST_RUNNER_DIR}/${RUNNER_MAIN}"
cd $RUST_RUNNER_DIR
cargo build

if [ -s $input_file ]; then
    # cat $input_file
    # echo "input from file"
    # $dir$filename_without_ext < $input_file > "$HOME/Desktop/tmp.txt"
    $RUNNER_EXE < $input_file
else
    echo "Please input..."
    $RUNNER_EXE
fi