date=`date "+%Y%m%d%H%M%S"`
echo "${date}: $3 $4 $5 $6" >&2
for i in `seq $1 $2`
do
    x="000${i}"
    filename="input${x: -4}".txt
    # echo ${filename}
    ./asprocon7_a_0811 $3 $4 $5 $6 < "./tools/in/${filename}" > "./tools/out/${filename}"
    ./tools/output_checker "./tools/in/${filename}"  "./tools/out/${filename}" >> "./tools/scores/${date}.txt" 
done

outfile=./tools/scores/${date}.txt
sed -i -e 's/IMOJUDGE<<<//' $outfile
sed -i -e 's/>>>//' $outfile
python3 ./tools/ave.py $outfile

rm ./tools/scores/${date}.txt-e