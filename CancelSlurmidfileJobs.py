import sys
import subprocess

if len(sys.argv)!=2:
    sys.exit('Please give (only) the slurmid filename as a parameter')

filename=sys.argv[1]

f=open(filename)
text=f.read()
f.close()
lines=text.split('\n')

for line in lines:
    
    if len(line)==0:
        continue

    fields=line.split(' ')
    job=fields[0]
    print('Canceling job '+job)
    try:
        output=subprocess.check_output(['scancel',job])
    except subprocess.CalledProcessError:
        print('Warning: scancel returned an error')
        

