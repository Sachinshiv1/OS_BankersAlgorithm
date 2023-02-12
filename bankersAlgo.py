# Pre Defined Values of Procees their allocation
# and the Max Resourse Avaiable
process = ['P0','P1','P2','P3','P4']
alloc = [[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]]
max = [[7,5,3],[3,2,2],[9,0,2],[2,2,2],[4,3,3]]
avail = [3,3,2]
prno = len(process)
print(process)

# Finding the Need Matix
need = []
for i in range(prno):
    ab = [ ]
    for j in range(3):
        diff = max[i][j] - alloc[i][j]
        ab.append(diff)
    need.append(ab)

print("Need Matrix is ",need)

'''
   # Safe Algorithm 
if(need <= avail)
    avail += alloc
else 
    hold and go forward
'''
wait = process
safeque = [ ]
while(prno>0):
    arr = wait[-1]
    ap = process.index(arr)
    #print(nmat = need[(wait[-1]).index])
    nmat = need[ap]     # array
    print(ap)
    count = 0
    for i in range(3):
        nmat[i] <= avail[i]
        count += 1
    
    if(count == 3):
        safeque.append(nmat)
        for i in range(3):
            rall = alloc.index(nmat)
            avail[i] += rall[i]
            wait.pop()
    else:
        wait.append(nmat)
    
    prno = len(wait)

print(safeque)