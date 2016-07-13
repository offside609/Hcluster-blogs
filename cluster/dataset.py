
def readfile(filename):
    a=open(filename,'r')
    lines=a.readlines()
    print(lines[1])


# First line is the column titles
    colnames=lines[0].strip( ).split('\t')[1:]
    rownames=[]
    data=[]
    for line in lines[1:]:
        p=line.strip( ).split('\t')
# First column in each row is the rowname
        rownames.append(p[0])
# The data for this row is the remainder of the row
        data.append([float(x) for x in p[1:]])
    return rownames,colnames,data

