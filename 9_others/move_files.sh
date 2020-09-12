dirs=`find . -type d`
mkdir "all"
for d in $dirs;
do
    echo $d
    files=`find $d -type f -d 1 -name *.py`
    for f in $files;
    do
        filename_bottom=`basename $f`
        new_filename="${d#./}_${filename_bottom}"
        # echo $new_filename
        cp $f "./all/$new_filename"
    done
done