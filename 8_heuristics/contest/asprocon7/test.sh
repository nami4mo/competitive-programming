date=`date "+%Y%m%d%H%M%S"`
for i in `seq $1 $2`
do
    x="000${i}"
    filename="input${x: -4}".txt
    # echo ${filename}
    ./asprocon7_a < "./tools/in/${filename}" > "./tools/out/${filename}"
    ./tools/output_checker "./tools/in/${filename}"  "./tools/out/${filename}" >> "./tools/scores/${date}.txt"  
done

outfile=./tools/scores/${date}.txt
sed -i -e 's/IMOJUDGE<<<//' $outfile
sed -i -e 's/>>>//' $outfile
python3 ./tools/ave.py $outfile

rm ./tools/scores/${date}.txt-e