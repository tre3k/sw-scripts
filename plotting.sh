#!/usr/bin/env bash

FILES=$@

for file in $FILES
do
    echo $file
    gnuplot -c plot-averages.gp $file
done

