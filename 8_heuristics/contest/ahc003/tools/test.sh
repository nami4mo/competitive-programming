date=`date "+%Y%m%d%H%M%S"`
for i in `seq $1 $2`
do
    x="000${i}"
    filename="${x: -4}".txt
    echo ${filename}
    # ../ahc001_a < "in/${filename}" > "out/${filename}" 2>> "out_records/${date}.txt"
    # ../ahc001_a < "in/${filename}" > "out/${filename}"
    # ../ahc001_a < "in/${filename}" > "out/${filename}"
    cargo run --release --bin tester in/${filename} ../ahc003_a > out/${filename}  2>> out_score/${date}.txt
    # cargo run --release --bin vis "in/${filename}" "out/${filename}"
done

outfile=out_score/${date}.txt
sed -i -e '/Finished/d' $outfile
sed -i -e '/Running/d' $outfile
sed -i -e 's/Score = //g' $outfile
python ave.py $outfile

rm out_score/${date}.txt-e
head -n 12 $outfile