# for i in `seq 0 $1`
# do
#     x="000${i}"
#     filename="${x: -4}".txt
#     echo ${filename}
#     ../ahc001_a < "in/${filename}" > "out/${filename}"
#     cargo run --release --bin vis "in/${filename}" "out/${filename}"
#     cp out.svg svgs/"${x: -4}.svg"
# done

rm ./devided_outs/*.txt
rm ./devided_svgs/*.svg
python devide.py out_d.txt
# cargo run --release --bin vis "in/$0.txt" "devided_outs/${filename}"
echo "done"
i=0
for file in `\find ./devided_outs -maxdepth 1 -type f`; do
    echo $file
    filename=${file##*/}
    filename=${filename%.*}
    echo $filename
    cargo run --release --bin vis "in/$1.txt" "$file"
    # cp out.svg "devided_svgs/$1_${i}.svg"
    cp out.svg "devided_svgs/${filename}.svg"
    i=`expr $i + 1`
done
