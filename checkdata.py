#created to check all census files have the same format
import os

Directory = r'C:\\Users\\GIS_tech\\Desktop\\66county'
SampleDir = os.path.join(Directory,"sample")
CmpDir = os.path.join(Directory,'extracted')

for x in os.listdir(SampleDir):
    if "metadata" in x:
        print x
        for folder in os.listdir(CmpDir):
            #print folder
            cur_dir = os.path.join(CmpDir,folder)
            #print cur_dir
            file = os.path.join(cur_dir,x)
            assert os.path.exists(file), file
            f=open(file,'rb')
            print f
        
        
