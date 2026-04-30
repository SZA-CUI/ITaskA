import csv
import datetime
import time
#  ............................................ONE DAY ACTIVITY MODELING...............................
description5 = []
programfile5 = []
days5 = []
slots5 = []
activityclass5 = []
specificclass5 = []

with open('PycharmProjects/Code/data/Data set/FinalTrain.csv','r') as csv3file:
    csv3Reader = csv.reader(csv3file)
    for row in csv3Reader:
        description5.append(row[0])
        programfile5.append(row[1])
        days5.append(row[2])
        slots5.append(row[3])
        activityclass5.append(row[4])
        specificclass5.append(row[5])
    weekdays = []
    weekdays.append('Saturday')
    weekdays.append('Sunday')
    weekdays.append('Monday')
    weekdays.append('Tuesday')
    weekdays.append('Wednesday')
    weekdays.append('Thursday')
    weekdays.append('Friday')
    fmt = '%Y-%m-%d %H:%M:%S'
    dt = '%Y-%m-%d'
#[description3[j], programfile3[j], days3[j], slots3[j], activityclass3[j], specificclass3[j]])
    for j in range(len(description5)):
        for k in range(7):
            if days5[j]==weekdays[k]:
                with open('PycharmProjects/Code/data/Data set/train/'+weekdays[k]+'.csv', 'ab') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(
                        [description5[j], programfile5[j], days5[j], slots5[j], activityclass5[j], specificclass5[j]])

