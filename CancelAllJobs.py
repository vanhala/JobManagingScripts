import sys
import subprocess

def ParseOutput():
    
    output=subprocess.check_output(['squeue','-uvanhalt1','--format=%i'])

    lines=output.split('\n')
    ids=[]

    for line in lines:
        if line.isdigit():
            ids.append(line)

    return ids



jobs=ParseOutput()
print jobs


for job in jobs:
    output=subprocess.check_output(['scancel',job])
