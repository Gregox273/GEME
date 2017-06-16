for filename in *.csv; do
    head -n -3 $filename > tmp;
    cat tmp > $filename
done
rm tmp;
