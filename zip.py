#unzip files in different folder into one folder
import os
import zipfile

directory = r'C:\\Users\\GIS_tech\\Desktop\\66county'
#print os.listdir(directory)
subdir = directory+'\\tem'
desdir = r'C:\\Users\\GIS_tech\\Desktop\\66county\\extracted'
#print os.listdir(subdir)
for x in os.listdir(subdir):
    xdir = os.path.join(subdir,x)
    #print xdir
    if "._" in x:
        print x
        continue
    fh = open(xdir,'rb')
    z = zipfile.ZipFile(fh)
    newdir = os.path.join(desdir,"biu_"+x)
    print newdir
    os.mkdir(newdir)
    for name in z.namelist():
        outpath = r'C:\\Users\\GIS_tech\\Desktop\\66county\\extracted'
        z.extract(name,newdir)
    fh.close()