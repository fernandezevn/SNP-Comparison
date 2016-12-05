import re, sys

#TODO:                                                                                                                                                                                                              
#    -Find out why file order matters                                                                                                                                                                               

def contingency_map(str1, str2, contingency):
    arr1 = []
    arr2 = []
#0 = 0|0 1 = 1|0 or 0|1 2 = 1|1                                                                                                                                                                                     
    for curr in  str1.replace("0|0", "0").replace("1|0", "1").replace("0|1", "1").replace("1|1", "2").split("\t"):
        if(curr == "0" or curr == "1" or curr == "2"):
           arr1.append(curr)

    for curr in  str2.replace("0|0", "0").replace("1|0", "1").replace("0|1", "1").replace("1|1", "2").split("\t"):
        if(curr == "0" or curr == "1" or curr == "2"):
           arr2.append(curr)

    if(len(arr1) <= len(arr2)):
        shorter = len(arr1)
    else:
        shorter = len(arr2)

    i = 0
    while i < shorter:
        contingency[int(arr1[i])][int(arr2[i])] = contingency[int(arr1[i])][int(arr2[i])] + 1
        i = i + 1

    return contingency

f1 = open(sys.argv[1], "r")
f2 = open(sys.argv[2], "r")
file1 = f1.read()
file2 = f2.read()
f1.close()
f2.close()


positions_file1 = re.findall(r"20\s+(\d+)", file1)
positions_file2 = re.findall(r"20\s+(\d+)", file2)

print "Total SNPs in %s: %d" %(sys.argv[1], len(positions_file1))
print "Total SNPs in %s: %d" %(sys.argv[2], len(positions_file2))

gen_file1 = []
gen_file2 = []
for match in  re.finditer(r"\w{2}\s+((\d{1}\|\d{1})|(\.\|\.))\s+", file1):
    gen_file1.append(match.group(1))

for match in  re.finditer(r"\w{2}\s+((\d{1}\|\d{1})|(\.\|\.))\s+", file2):
    gen_file2.append(match.group(1))

table = [[0 for x in range(3)] for y in range(3)]

pos = []
other = []
same = 0
pos_str = ""
other_str = ""
if(len(positions_file1) > len(positions_file2)):
    pos = positions_file2
    positions_file2 = []
    other = positions_file1
    positions_file1 = []
    pos_gen = gen_file2
    other_gen = gen_file1

if(len(positions_file1) <= len(positions_file2)):
    pos = positions_file1
    positions_file1 = []
    other = positions_file2
    positions_file2 = []
    pos_gen = gen_file1
    other_gen = gen_file2

i = 0
while i < len(pos):
    if(pos[i] in other):
        ind = other.index(pos[i])
        same = same + 1
        table = contingency_map(pos_gen[i], other_gen[ind], table)
    i = i + 1

print "Number of SNPs in both files: %d" %same

if(pos == positions_file1):
    gen_file1_str = pos_gen
    gen_file2_str = other_gen
    print "x-axis = %s" %sys.argv[1]
    print "y-axis = %s" %sys.argv[2]
else:
    gen_file1_str = other_gen
    gen_file2_str = pos_gen
    print "x-axis = %s" %sys.argv[2]
    print "y-axis = %s" %sys.argv[1]

total = 0
for curr in table:
    total = total + curr[0] + curr[1] + curr[2]
if(total != 0):
    total = float(total)
else:
    total = 1.0


print"Actual: "
print "%d\t%d\t%d\n%d\t%d\t%d\n%d\t%d\t%d" %(table[0][0], table[1][0], table[2][0], table[0][1],table[1][1],table[2][1],table[0][2],table[1][2],table[2][2])
print "Percents:"
print "%.3f\t%.3f\t%.3f\n%.3f\t%.3f\t%.3f\n%.3f\t%.3f\t%.3f" %(float(table[0][0])/total, float(table[1][0])/total, float(table[2][0])/total, float(table[0][1])/total, float(table[1][1])/total, float(table[2][1])\
/total, float(table[0][2])/total, float(table[1][2])/total, float(table[2][2])/total)

print "Total Same: %d" %same
