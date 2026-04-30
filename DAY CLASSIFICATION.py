import csv
import datetime
import time
#import timestring
description = []
starttime = []
endtime = []
programfile = []
activityclass = []
specificclass = []
days = []
slots = []
activitytiming = []
eachslottime = []
action = []
processid = []
#  ...........................................Reding file data in arrays...............................
with open('PycharmProjects/Code/data/Data set/step1.csv','r') as csvfile:
    csvReader = csv.reader(csvfile)
    for row in csvReader:
        description.append(row[0])
        starttime.append(row[1])
        endtime.append(row[2])
        programfile.append(row[3])
        activityclass.append(row[4])
        specificclass.append(row[5])
        days.append(row[6])
        activitytiming.append(row[7])
        slots.append(row[8])
        eachslottime.append(row[9])
        processid.append(row[10])
        action.append(row[11])
#  ........................................ displaying file data from arrays...............................
# print (description)
# print (starttime)
# print (endtime)
# print (programfile)
# print (activityclass)
# print (specificclass)
# print (days)
# print (slots)
# print (activitytiming)
# print (cluster)
#  ..............................................Days classification...............................
    i=1
    index='start_time'
    for row in starttime[1:]:

            d= time.strptime(row,'%Y-%m-%dT%H:%M:%S+05')
            days[i]=time.strftime('%A',d)
            i = i + 1
    # print (starttime)
    # print (days)
