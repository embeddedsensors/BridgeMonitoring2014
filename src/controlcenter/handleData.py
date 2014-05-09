import os 
import glob
import csv

datapath = 'Data/'
NWpath = datapath + 'NW/'
NEpath = datapath + 'NE/'
SEpath = datapath + 'SE/'
SWpath = datapath + 'SW/'
header_size = 5

def getNewData():
    # '''Gets the newest text file from each directory'''
    fileArr = []
    fileArr.append(max(glob.iglob(NWpath + '*.txt'), key=os.path.getctime))
    fileArr.append(max(glob.iglob(NEpath + '*.txt'), key=os.path.getctime))
    fileArr.append(max(glob.iglob(SWpath + '*.txt'), key=os.path.getctime))
    fileArr.append(max(glob.iglob(SEpath + '*.txt'), key=os.path.getctime))
    ind = 0
    x = []
    y = []
    z = []
    dataArr = []
    for fi in fileArr:
        print 'Converting ' + fi 
        with open(fi, 'rb') as f:
            reader = csv.reader(f, delimiter=',')
            # Skip the header lines
            line = 0
            for row in reader:
                if line < header_size:
                    line += 1
                    pass
                else:
                    x.append(row[0])
                    y.append(row[1])
                    z.append(row[2])
        dataArr.append(x)
        dataArr.append(y)
        dataArr.append(z)
        x = []
        y = []
        z = []
        ind += 1
    return dataArr