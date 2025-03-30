from tkinter import filedialog
import os
from tokeniser import tokeniser
from compilationengine import CompileEngine
import sys
import logging

jack_dir = filedialog.askdirectory()

jack_files = os.listdir(jack_dir)

import time



for i in range (len(jack_files)):
    file_name = jack_files[i]
    #print(file_name)
    path = jack_dir + '/'+ file_name
    filename, ext_name = os.path.splitext(file_name)
    
    if ext_name == '.jack':
        start_time = time.time()
        jack_file = open(path, 'r')
        logpath= jack_dir+ '/' + filename + '.log'

        cmpl = CompileEngine(jack_file, logpath ) 
        jack_file.close()
        #print(cmpl.parsed)
        xmlpath= jack_dir+ '/' + filename + '.xml'

        xmlfile = open (xmlpath, 'w')
        xmlfile.write(cmpl.parsed)
        print(f"| Compilation Successful for file: {path} in {round(time.time()-start_time, 5)} seconds |\n| xml file: {xmlpath} | log file: {logpath} |\n")


sys.exit(0)

