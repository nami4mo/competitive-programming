date=`date "+%Y%m%d%H%M%S"`
for i in `seq $1 $2`
do
    x="000${i}"
    filename="${x: -4}".txt
    echo ${filename}
    # ../ahc001_a < "in/${filename}" > "out/${filename}" 2>> "out_records/${date}.txt"
    # ../ahc001_a < "in/${filename}" > "out/${filename}"
    # ../ahc001_a < "in/${filename}" > "out/${filename}"
    rm edges/${filename}
    cargo run --release --bin tester in/${filename} ../ahc003_a > out/${filename}  2>> edges/${filename}
    # cargo run --release --bin vis "in/${filename}" "out/${filename}"
    head -n 59 in/${filename} > tmp.txt
    cat edges/${filename} >> tmp.txt
    sed -i -e '/Finished/d' tmp.txt
    sed -i -e '/Running/d' tmp.txt
    sed -i -e '/Score/d' tmp.txt
    ./make_movie < tmp.txt
done

outfile=edges/${filename}
sed -i -e '/Finished/d' $outfile
sed -i -e '/Running/d' $outfile
sed -i -e '/Score/d' $outfile
# python ave.py $outfile

rm edges/${filename}-e
