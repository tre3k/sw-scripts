#!/usr/bin/env gnuplot -pare

FILENAME = sprintf("%s/theta_c.dat",ARG1)

print FILENAME

set terminal eps size 20cm,14.4cm
set termoption font 'Times New Roman,16'
set output sprintf("%s.eps",FILENAME)

set yrange [0:]
set ylabel "θ_C^2, mrad^2"
set xlabel "H, mT"
plot FILENAME using 1:($2**2):(2*$3) with yerrorbars pt 7 ps 0.5 lw 3 title 'θ_C^2'

pause -1
