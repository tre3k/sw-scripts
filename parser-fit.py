#!/usr/bin/env python3

import os
import sys
import glob

from fitparser import Fitparser

if len(sys.argv) < 2:
    print(sys.argv[0]+" <directory with *.fit files>")
    exit(0)

fit_files = glob.glob(sys.argv[1]+"/*.fit")

fd = open(sys.argv[1]+"/theta_c.dat", 'w')
fd.write("# field,mT theta_c theta_c_err\n")

for fit_file in fit_files:
    filename = os.path.split(fit_file)[-1]
    field = float(filename.split("mT")[0])

    fp = Fitparser(fit_file)
    print(field,fp.getValues()['xc'].val,fp.getValues()['xc'].err)
    fd.write(str(field)+" "+str(fp.getValues()['xc'].val)+" "+str(fp.getValues()['xc'].err)+"\n")

fd.close()
    
    
