fna__big = 'py__bills01.txt'
fna__small = 'OneCBills01.txt'


LI = {}
LI[0] = []
LI[1] = []

fi = open(fna__big, 'r')
rl = fi.readlines()
fi.close()

for line in rl:
    line = line.strip()
    LI[0].append(line)

fi = open(fna__small, 'r')
rl = fi.readlines()
fi.close()

    
for line in rl:
    line = line.strip()
    LI[1].append(line)

counter = 0
for line in LI[0]:
    if line in LI[1]:
        print line
    else:
        print '=======', line
        counter += 1

print 'total:', counter
            
