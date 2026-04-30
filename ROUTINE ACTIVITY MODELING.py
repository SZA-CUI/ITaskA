#  ............................................ROUTINE ACTIVITY MODELING...............................
description6 = []
programfile6 = []
days6 = []
slots6 = []
activityclass6 = []
specificclass6 = []

with open('PycharmProjects/Code/data/Data set/Predictions.csv','r') as csv3file:
    csv3Reader = csv.reader(csv3file)
    for row in csv3Reader:
        description6.append(row[2])
        programfile6.append(row[3])
        days6.append(row[0])
        slots6.append(row[1])
        activityclass6.append(row[4])
        specificclass6.append(row[5])
    weekdays2 = []
    weekdays2.append('Saturday')
    weekdays2.append('Sunday')
    weekdays2.append('Monday')
    weekdays2.append('Tuesday')
    weekdays2.append('Wednesday')
    weekdays2.append('Thursday')
    weekdays2.append('Friday')
    fmt = '%Y-%m-%d %H:%M:%S'
    dt = '%Y-%m-%d'
#[description3[j], programfile3[j], days3[j], slots3[j], activityclass3[j], specificclass3[j]])
    for j in range(len(days6)):
        for k in range(7):
            if days6[j]==weekdays2[k]:
                with open('PycharmProjects/Code/data/Data set/test/'+weekdays2[k]+'.csv', 'ab') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(
                        [description6[j], programfile6[j], days6[j], slots6[j], activityclass6[j], specificclass6[j]])
