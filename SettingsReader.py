import collections

def LoadSettings(filename):

    f=open(filename,'r')

    settings=collections.OrderedDict()
    #settings=dict()

    for line in f:
        if line[-1]=='\n':
            line=line[0:-1]
        if len(line)!=0 and line[0]!='%':
            var=ReadLine(line)
            settings[var[0]]=var[1]

    return settings


def ReadLine(line):

    parts=line.split(' ',2)

    VarType=parts[0]
    VarName=parts[1]
    VarValueStr=parts[2]

    NameAndValue=InterpretVariable(VarType,VarName,VarValueStr)

    return NameAndValue

def InterpretVariable(VarType,VarName,VarValueStr):

    if VarType==None:
        VarType=GuessVariableType(VarValueStr)

    if VarType=='int':
        VarValue=int(VarValueStr)
    elif VarType=='double':
        VarValue=float(VarValueStr)
    elif VarType=='string':
        VarValue=VarValueStr[1:-1]
    else:
        raise(Exception('unknown variable type'))

    return [VarName,VarValue]

def GuessVariableType(VarValueStr):

    if len(VarValueStr)>=2 and VarValueStr.startswith('"') and VarValueStr.endswith('"'):
        return 'string'

    try:
        VarValue=int(VarValueStr)
        return 'int'
    except ValueError:
        pass
    
    try:
        VarValue=float(VarValueStr)
        return 'double'
    except ValueError:
        pass
    
    return None
    

def PrintSettings(settings,f):

    if type(f)==str:
        #cosider this as a file name
        f=open(f,'w')
    
    for VarName in settings:
        VarValue=settings[VarName]

        if type(VarValue)==int:
            f.write('int '+VarName+' %d'%(VarValue))
        elif type(VarValue)==float:
            f.write('double '+VarName+' %f'%(VarValue))
        elif type(VarValue)==str:
            f.write('string '+VarName+' "%s"'%(VarValue))
        else:
            raise(Exception('unknown variable type'))

        f.write('\n')
        

#import sys
#settings=LoadSettings('/triton/tfy/work/vanhalt1/BilayerModelFixedSymmetrization/1398442889.0/settings.txt')
#print settings
#PrintSettings(settings,sys.stdout)
