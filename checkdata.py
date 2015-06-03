#created to check all census files have the same format
import os

Directory = r'C:\\Users\\GIS_tech\\Desktop\\66county'
SampleDir = os.path.join(Directory,"sample")
CmpDir = os.path.join(Directory,'extracted')

#check have same attributes
for x in os.listdir(SampleDir):
    if "metadata" in x:
        #print x
        for folder in os.listdir(CmpDir):
            #print folder
            cur_dir = os.path.join(CmpDir,folder)
            #print cur_dir
            file = os.path.join(cur_dir,x)
            assert os.path.exists(file), file
            #f=open(file,'rb')
            #print f
print "GOOD"

#check no duplicated counties
first_list = []
for county in os.listdir(CmpDir):

    cur_dir = os.path.join(CmpDir,county+'\\DEC_10_SF1_H1_with_ann.csv')
    assert os.path.exists(cur_dir),cur_dir
    cur_f = open(cur_dir,'rb')
    cur_f.readline()
    cur_f.readline()
    line = cur_f.readline()
    if line in first_list:
        raise Exception(line)
    else:
        first_list.append(line)
    cur_f.close()
print first_list, len(first_list)
       
