hw = input().strip()
r = []
AreaTB = 0
AreaRW = 0
AreaCW = 0
AreaTB = 0

row = int(hw[0])
print("n(row) = ",row)
column = int(hw[2])
print("n(column) = ",column)

for rows in range(0,int(hw[0])):

    new = (input().strip()).split(' ')
    colcheck = 0
    temp = []
    
    for x in new:
        x = int(x)
        if(rows == 0 or rows == row-1):
            AreaRW += x                 #Row-wise area

        if(colcheck==0 or colcheck==column-1):
            AreaCW+=x

        colcheck += 1
        temp.append(x)
    
    r.append(temp)

AreaTB = (row*column)*2                 #Area at the top and bottom

print("AreaTB = {}".format(AreaTB))
print("AreaRW = {}".format(AreaRW))
print("AreaCW = {}".format(AreaCW))
