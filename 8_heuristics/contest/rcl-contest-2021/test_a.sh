date=`date "+%Y%m%d%H%M%S"`
for i in `seq $1 $2`
do
    x="000${i}"
    filename="input_${x: -1}".txt
    # echo ${filename}
    ./main_a < "./tools/in_a/${filename}" > "./tools/out_a/${filename}"
    python3 ./tools/judge.py "./tools/in_a/${filename}"  "./tools/out_a/${filename}" >> "./tools/scores_a/${date}.txt"  
done

outfile=./tools/scores_a/${date}.txt
sed -i -e 's/IMOJUDGE<<<//' $outfile
sed -i -e 's/>>>//' $outfile
python3 ./tools/ave.py $outfile

rm ./tools/scores_a/${date}.txt-e