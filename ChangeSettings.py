from glob import glob
import sys
sys.path.append('/home/vanhalt1/batchscripts/')
import SettingsReader as SR
import re
import os
import collections

from numpy import *

def MakeSettings(filename,NewSettings,ForceTypeChange):

    settings=SR.LoadSettings(filename)
    
    for key in NewSettings:
        if (not ForceTypeChange) and (key in settings) and type(NewSettings[key])!=type(settings[key]):
            print('Tried to change '+key+' from '+str(settings[key])+' to '+str(NewSettings[key])+', but they are of different types.')
            continue

        settings[key]=NewSettings[key]
    
    SR.PrintSettings(settings,filename)


if len(sys.argv)<2:
    sys.exit('Usage: python ChangeSettings.py {-flags} [varname=value] {varname=value} ... [directory1] {directory2} ...')

flags=''

if sys.argv[1][0]=='-':
    flags=sys.argv[1][1:]
    del sys.argv[1]

filenames=[]
NewValues=collections.OrderedDict()

for argument in sys.argv[1:]:
    if re.match('.*=.*',argument):
        parts=argument.split('=',1)
        NameAndValue=SR.InterpretVariable(None,parts[0],parts[1])
        NewValues[NameAndValue[0]]=NameAndValue[1]
    else:
        filenames.append(argument)

ChangeTypes=('f' in flags)

for filename in filenames:
    MakeSettings(filename,NewValues,ChangeTypes)
