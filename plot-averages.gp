#!/usr/bin/env gnuplot -pare

FILENAME = ARG1

set terminal eps size 20cm,14.4cm
set termoption font 'Times New Roman,16'
set output sprintf("%s.eps",FILENAME)

_logfile=sprintf("%s.fit",FILENAME)
print _logfile
set fit logfile _logfile
set fit errorvariables

set samples 10000
set xlabel "θ, mrad"
set ylabel "count"

a = 6
xc = 10
d = 1
y0 = 0.0001

fit_from = 0

fit_function(_a,_xc,_d,_y0,x) = -_a*atan((x-_xc)/_d)/pi + _a*0.5 + _y0

#fit [fit_from:] fit_function(a,xc,d,y0,x) FILENAME using 1:8:9 with yerror via a,xc,d,y0
fit [fit_from:] fit_function(a,xc,d,y0,x) FILENAME using 1:8 via a,xc,d,y0

set yrange[0:]
plot FILENAME using 1:8:9 with yerrorbars pt 7 ps 0.5 lw 3 title FILENAME, \
     [fit_from:] fit_function(a,xc,d,y0,x) with lines dt 2 lc rgb 'red' lw 3 t sprintf("x_c = %.2f +/- %.2f",xc,xc_err)

pause -1
