import sys

reload(sys)
sys.setdefaultencoding("utf-8")
import datetime
import csv


def toDate(your_timestamp):
    date = datetime.datetime.fromtimestamp(your_timestamp)
    str = date.strftime("%Y-%m-%d %H:%M:%S")
    return str


out_file = open("listeningsClean.txt", "w")

with open('../DATA/listenings_20160403.csv') as fp:
    for line in fp:
        str1 = line
        newStr = str1.replace(", ", "; ")
        lineS = newStr.split(",")
        if lineS[0] == "user_id":
            out_file.write(newStr)
            continue

        line1split = lineS[1].split(";", 1)
        if len(line1split) > 1:
            line1split[0] = datetime.datetime.fromtimestamp(float(line1split[0]) / 1e3)
            line1split[0] = line1split[0].strftime("%Y-%m-%d %H:%M:%S")
            lineS[1] = line1split[0] + "," + line1split[1]
        else:

            lineS[1] = datetime.datetime.fromtimestamp(float(lineS[1]) / 1e3)
            lineS[1] = lineS[1].strftime("%Y-%m-%d %H:%M:%S")
        newStr = ",".join(lineS)
        """print lineS
        print newStr
        sys.exit()"""
        out_file.write(newStr)

out_file.close()