#!/usr/bin/env bash

FILES=$@

for file in $FILES
do
    echo $file
    gnuplot -c plot-averages.gp $file


    directory=`dirname ${file}`
done

#cd $directory 
gs -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dSAFER -sOutputFile=$directory/averages.pdf $directory/*.eps

./parser-fit.py $directory
gnuplot -c plot-theta_c.gp $directory
