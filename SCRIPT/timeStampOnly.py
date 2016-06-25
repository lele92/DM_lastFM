import datetime
import time
import string

def toDate(your_timestamp):
    date = datetime.datetime.fromtimestamp(your_timestamp)
    str = date.strftime("%Y-%m-%d %H:%M:%S")
    return str

out_file=open("goodUsersN.txt","w")

with open("goodUsers.txt") as fp:
    count = 0
    for line in fp:
        if count == 0:
            count = count + 1
            out_file.write(line)
        else:
            lineS = line.split(",")
            timeStamp = lineS[10]
            try:
                if int(timeStamp) != 0:
                    newDate = toDate(int(timeStamp))
                    lineS[10] = newDate
                    newStr = ",".join(lineS)
                else:
                    lineS[1] = "undefined"
                    newStr = ",".join(lineS)
            except ValueError:
                newStr = line
            out_file.write(newStr)