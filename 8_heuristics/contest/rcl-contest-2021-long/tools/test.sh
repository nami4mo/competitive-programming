date=`date "+%Y%m%d%H%M%S"`
for i in `seq $1 $2`
do
    x="000${i}"
    filename="${x: -4}".txt
    filename="input_${x: -1}".txt
    echo ${filename}
    ../main < "../in/${filename}" > "../out/${filename}"
    python3 judge.py "../in/${filename}"  "../out/${filename}" >> "../out_score/${date}.txt"  
done

outfile="../out_score/${date}.txt"
# sed -i -e '/Finished/d' $outfile
# sed -i -e '/Running/d' $outfile
sed -i -e 's/score://g' $outfile
python3 ave.py $outfile

rm "${outfile}-e"
head -n 12 $outfile