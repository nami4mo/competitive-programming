date=`date "+%Y%m%d%H%M%S"`
for i in `seq $1 $2`
do
    x="000${i}"
    filename="input_${x: -1}".txt
    # echo ${filename}
    ./main_b < "./tools/in_b/${filename}" > "./tools/out_b/${filename}"
    python3 ./tools/judge_b.py "./tools/in_b/${filename}"  "./tools/out_b/${filename}" >> "./tools/scores_b/${date}.txt"  
done

# outfile=./tools/scores_b/${date}.txt
# sed -i -e 's/IMOJUDGE<<<//' $outfile
# sed -i -e 's/>>>//' $outfile
# python3 ./tools/ave.py $outfile

# rm ./tools/scores_b/${date}.txt-e