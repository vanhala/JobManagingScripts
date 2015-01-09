from glob import glob
import sys
import os
import re

def FindLargestFileIndexInFileList(files):
    
    LargestIndex=-1
    for f in files:
        f=os.path.basename(f)
        index=int(re.findall(r'\d+',f)[0])
        #print(f)
        #print(index)
        if LargestIndex<index:
            LargestIndex=index

    return LargestIndex

def FindLargestFileIndex(NameFilter):
    files=glob(NameFilter)
    return FindLargestFileIndexInFileList(files)


if __name__=='__main__':

    NameFilter=sys.argv[1]
    index=FindLargestFileIndexInFileList(sys.argv[1:])
    print index
