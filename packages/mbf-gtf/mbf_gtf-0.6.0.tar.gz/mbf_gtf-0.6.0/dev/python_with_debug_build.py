#!/usr/bin/env -S python -i
import sys
import shutil
import os
import subprocess
try:
    import numpy
    import pandas
except:
    print("numpy and pandas are not installed, please use a venv that has them")
    os._exit(1)


print("copying debug build of mbf_gtf.so to target/debug")

subprocess.check_call(['cargo','build'])

shutil.copy("target/debug/libmbf_gtf.so", "target/debug/mbf_gtf.so")
sys.path.insert(0, 'target/debug')

import mbf_gtf
import code
print("entering interactive mode, mbf_gtf is loaded")
