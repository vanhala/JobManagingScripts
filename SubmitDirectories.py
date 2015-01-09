from glob import glob
import subprocess
from FindLargestFileIndex import *
import sys

def SubmitBatchscriptInFolder(folder,batchscript,DependencyID):
    
    if DependencyID!=None:
        output=subprocess.check_output(['sbatch','--workdir='+folder,'--dependency=afterany:'+DependencyID,batchscript])
    else:
        output=subprocess.check_output(['sbatch','--workdir='+folder,batchscript])

    #print 'sbatch output:'
    #print output

    words=output.split(' ');
    JobID=words[-1][:-1]
    
    return JobID


def SubmitDirectories(basedir,dirlist,NRuns,batchscript,slurmidfile=''):

    if slurmidfile=='':
        index=FindLargestFileIndex(basedir+'slurmidfile*.txt')
        index=index+1
        slurmidfile=basedir+'slurmidfile'+str(index)+'.txt'
    
    print 'Writing slurm id file at '+slurmidfile
    f=open(slurmidfile,'w')

    JobIDs=[None]*len(dirlist)

    for l in range(0,NRuns):

        for k in range(0,len(dirlist)):

            SimulationDirectory=dirlist[k]
            DependID=JobIDs[k]
            JobIDs[k]=SubmitBatchscriptInFolder(SimulationDirectory,batchscript,DependID)
            if DependID!=None:
                #print 'Submitted '+JobIDs[k]+' dependent on '+DependID
                f.write(JobIDs[k]+' '+DependID+' '+SimulationDirectory+'\n')
            else:
                #print 'Submitted '+JobIDs[k]+' with no dependency'
                f.write(JobIDs[k]+' '+'-1'+' '+SimulationDirectory+'\n')

if len(sys.argv)<4:
    sys.exit('Usage: python SubmitDirectories.py [NRuns] [batchscript] [directory1] {directory2} ...')

try:
    NRuns=int(sys.argv[1])
except ValueError:
    sys.exit('The first argument must be the number of runs.')

batchscript=sys.argv[2]
dirs=sys.argv[3:]

print('Submitting '+str(len(dirs))+' directories for '+str(NRuns)+' runs with batchscript '+batchscript+'.')

SubmitDirectories('./',dirs,NRuns,batchscript)
