import sys

reload(sys)
sys.setdefaultencoding("utf-8")


out_file = open("../OUTPUT/artistClean.txt", "w")
with open('../DATA/genre_20160403.csv') as fp:
    for line in fp:
        newStr = line.replace(", ", "; ")
        out_file.write(newStr)
out_file.close()