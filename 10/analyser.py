from tkinter import filedialog
import os
from tokeniser import tokeniser
from compilationengine import CompileEngine


jack_dir = filedialog.askdirectory()

jack_files = os.listdir(jack_dir)


for i in range (len(jack_files)):
    file_name = jack_files[i]
    #print(file_name)
    path = jack_dir + '/'+ file_name
    filename, ext_name = os.path.splitext(file_name)
    
    if ext_name == '.jack':
        print(path)
        jack_file = open(path, 'r')

        cmpl = CompileEngine(jack_file)
        jack_file.close()
        #print(cmpl.parsed)
        xmlpath= jack_dir+ '/' + filename + '.xml'
        xmlfile = open (xmlpath, 'w')
        xmlfile.write(cmpl.parsed)


