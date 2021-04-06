#!/usr/bin/env gnuplot -pare

FILENAME = ARG1

set terminal eps size 12cm,9cm
set termoption font 'Times New Roman,14'
set output sprintf("%s.eps",FILENAME)

_logfile=sprintf("%s.fit",FILENAME)
print _logfile
set fit logfile _logfile

set samples 10000
set xlabel "θ, mrad"
set ylabel "count"

a = 6
xc = 22
d = 1
y0 = 0.0001

fit_from = 5

fit_function(_a,_xc,_d,_y0,x) = -_a*atan((x-_xc)/_d)/pi + _a*0.5 + _y0

fit [fit_from:] fit_function(a,xc,d,y0,x) FILENAME using 1:8 via a,xc,d,y0

plot FILENAME using 1:8:9 with yerrorbars pt 7 ps 0.25 lw 2 title FILENAME, \
     [fit_from:] fit_function(a,xc,d,y0,x) with lines dt 2 lc rgb 'red' lw 3 t 'fit atan'

pause -1
