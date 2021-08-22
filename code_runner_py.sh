input_file="${HOME}/Desktop/pro_con/code_runner_input.txt"
# input_tmp="${HOME}Desktop/pro_con/input_tmp.txt"
# cp $input_file $input_tmp
# sed -i '/^$/d' $input_tmp

if [ -s $input_file ]; then
    cat $input_file
    python3 -u $1 < $input_file
else
    echo "Please input..."
    python3 -u $1
fi