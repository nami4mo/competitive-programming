date=`date "+%Y%m%d%H%M%S"`
for i in `seq $1 $2`
do
    x="000${i}"
    filename="${x: -4}".txt
    echo ${filename}
    ../ahc001_a < "in/${filename}" > "out/${filename}" 2>> "out_records/${date}.txt"
    # ../ahc001_a < "in/${filename}" > "out/${filename}"
    cargo run --release --bin vis "in/${filename}" "out/${filename}"
    cp out.svg svgs/"${x: -4}.svg"
done