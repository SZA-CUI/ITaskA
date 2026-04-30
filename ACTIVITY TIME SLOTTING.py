#  ............................................Time Slotting...............................
    j = 0
    slotstart = []
    slotend = []
    sttime = '00:00:00'
    etime = '02:00:00'
    add = '02:00:00'
    ss1 = datetime.datetime.strptime(sttime, '%H:%M:%S').strftime('%H:%M:%S')
    se1 = datetime.datetime.strptime(etime, '%H:%M:%S').strftime('%H:%M:%S')
    sa1 = datetime.datetime.strptime(add, '%H:%M:%S').strftime('%H:%M:%S')
    ss1 = time.strptime(ss1, '%H:%M:%S')
    se1 = time.strptime(se1, '%H:%M:%S')
    sa1 = time.strptime(sa1, '%H:%M:%S')
    # print (ss1.hour)
    # ss1= datetime.timedelta(days=ss1.)
    for j in range(12):
        if j == 0:
            slotstart.append(str(ss1.tm_hour) + '0:00:00')
            slotend.append(str(se1.tm_hour) + ':00:00')

            print(ss1.tm_hour, se1.tm_hour)
        elif j == 11:
            ss1 = datetime.datetime.strptime('22:00:00', '%H:%M:%S').strftime('%H:%M:%S')
            se1 = datetime.datetime.strptime('00:00:00', '%H:%M:%S').strftime('%H:%M:%S')
            ss1 = time.strptime(ss1, '%H:%M:%S')
            se1 = time.strptime(se1, '%H:%M:%S')
            slotstart.append(str(ss1.tm_hour) + ':00:00')
            slotend.append(str(se1.tm_hour) + '0:00:00')
            print(ss1.tm_hour, se1.tm_hour)
        else:
            val1 = ss1.tm_hour + sa1.tm_hour
            val2 = se1.tm_hour + sa1.tm_hour
            val3 = str(val1) + ':00:00'
            val4 = str(val2) + ':00:00'
            val3 = datetime.datetime.strptime(val3, '%H:%M:%S').strftime('%H:%M:%S')
            val4 = datetime.datetime.strptime(val4, '%H:%M:%S').strftime('%H:%M:%S')
            val3 = time.strptime(val3, '%H:%M:%S')
            val4 = time.strptime(val4, '%H:%M:%S')
            ss1 = val3
            se1 = val4
            
            print(ss1.tm_hour, se1.tm_hour)
            slotstart.append(str(ss1.tm_hour) + ':00:00')
            slotend.append(str(se1.tm_hour) + ':00:00')
            # slotstart.append(ss1)
            # slotend.append(se1)
    print(slotstart, slotend)
#  .............................................Slotting..................................
#  ............................................Writing to a new file...............................
    aslot = []
    j=1
    k=0
    fmt = '%Y-%m-%d %H:%M:%S'
    dt = '%Y-%m-%d'
    aslot.append(slots)
    with open('PycharmProjects/Code/data/Data set/step2.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile)
        for j in range(len(description)):
            if j!=0:

                if endtime[j] != 'TBD':
                    s1 = datetime.datetime.strptime(starttime[j], '%Y-%m-%dT%H:%M:%S+05').strftime(dt)
                    e1 = datetime.datetime.strptime(endtime[j], '%Y-%m-%dT%H:%M:%S+05').strftime(dt)
                    s1 = datetime.datetime.strptime(s1, dt)
                    e1 = datetime.datetime.strptime(e1, dt)

                if endtime[j]!='TBD' and e1==s1:

                    s = datetime.datetime.strptime(starttime[j],'%Y-%m-%dT%H:%M:%S+05').strftime('%H:%M:%S')
                    e = datetime.datetime.strptime(endtime[j],'%Y-%m-%dT%H:%M:%S+05').strftime('%H:%M:%S')
                    s = time.strptime(s, '%H:%M:%S')
                    e = time.strptime(e, '%H:%M:%S')

                    for k in range(12):
                        slots = datetime.datetime.strptime(slotstart[k], '%H:%M:%S').strftime('%H:%M:%S')
                        slote = datetime.datetime.strptime(slotend[k], '%H:%M:%S').strftime('%H:%M:%S')
                        s2 = time.strptime(slots, '%H:%M:%S')
                        e2 = time.strptime(slote, '%H:%M:%S')
                        if (s.tm_hour >= s2.tm_hour and s.tm_hour < e2.tm_hour) or (e.tm_hour < e2.tm_hour and s.tm_hour >= s2.tm_hour)or (e.tm_hour >= e2.tm_hour and s.tm_hour < e2.tm_hour) or (s.tm_hour>=s2.tm_hour and k==11) or (s.tm_hour>=s2.tm_hour and k==11 and e.tm_hour==e2.tm_hour):

                            aslot.append(k)
                            writer.writerow([description[j], starttime[j], endtime[j], programfile[j], activityclass[j], specificclass[j], days[j], activitytiming[j], k ,activity[j] , eachslottime[j], action[j], processid[j]])
                        # elif s.tm_hour==22 or s.tm_hour==23:
                        #     if s.tm_hour>=22 and s.tm_hour<=23:
                        #         aslot.append(k)
                        #         writer.writerow(
                        #             [description[j], starttime[j], endtime[j], programfile[j], activityclass[j],
                        #              specificclass[j], days[j], activitytiming[j], k, activity[j], cluster[j]])





                else:
                    aslot.append('')
                    writer.writerow([description[j], starttime[j], endtime[j], programfile[j], activityclass[j],
                                specificclass[j], days[j], activitytiming[j], '', activity[j], eachslottime[j], action[j], processid[j]])






                    #print (s.tm_hour, s2.tm_hour)

            # if s.tm_hour > s2.tm_hour:
            #     if e.tm_hour < e2.tm_hour:






            else:
                aslot.append('slots')
                writer.writerow(['program_desc', 'start_time', 'end_time', 'program_file', 'activity_class', 'specific Class',
                                'days', 'activity_time', 'slots', 'each slot time','', 'action', 'processid'])



# print (description)
# print (starttime)
# print (endtime)
# print (programfile)
# print (activityclass)
# print (specificclass)
# print (days)
print (slots)

import csv
import datetime
import time


description2 = []
starttime2 = []
endtime2 = []
programfile2 = []
activityclass2 = []
specificclass2 = []
days2 = []
activitytiming2 = []
slots2 = []
activity2 = []
eachslottime2 = []
action2 = []
processid2 = []

#  ............................................ACTIVITY TIME SLOTTING...............................
j = 0
slotstart = []
slotend = []

sttime = '00:00:00'
etime = '02:00:00'
add = '02:00:00'
ss1 = datetime.datetime.strptime(sttime, '%H:%M:%S').strftime('%H:%M:%S')
se1 = datetime.datetime.strptime(etime, '%H:%M:%S').strftime('%H:%M:%S')
sa1 = datetime.datetime.strptime(add, '%H:%M:%S').strftime('%H:%M:%S')
ss1 = time.strptime(ss1, '%H:%M:%S')
se1 = time.strptime(se1, '%H:%M:%S')
sa1 = time.strptime(sa1, '%H:%M:%S')
# print (ss1.hour)
# ss1= datetime.timedelta(days=ss1.)
for j in range(12):
    if j == 0:
        slotstart.append(str(ss1.tm_hour) + '0:00:00')
        slotend.append(str(se1.tm_hour) + ':00:00')

        print(ss1.tm_hour, se1.tm_hour)
    elif j == 11:
        ss1 = datetime.datetime.strptime('22:00:00', '%H:%M:%S').strftime('%H:%M:%S')
        se1 = datetime.datetime.strptime('00:00:00', '%H:%M:%S').strftime('%H:%M:%S')
        ss1 = time.strptime(ss1, '%H:%M:%S')
        se1 = time.strptime(se1, '%H:%M:%S')
        slotstart.append(str(ss1.tm_hour) + ':00:00')
        slotend.append(str(se1.tm_hour) + '0:00:00')
        print(ss1.tm_hour, se1.tm_hour)
    else:
        val1 = ss1.tm_hour + sa1.tm_hour
        val2 = se1.tm_hour + sa1.tm_hour
        val3 = str(val1) + ':00:00'
        val4 = str(val2) + ':00:00'
        val3 = datetime.datetime.strptime(val3, '%H:%M:%S').strftime('%H:%M:%S')
        val4 = datetime.datetime.strptime(val4, '%H:%M:%S').strftime('%H:%M:%S')
        val3 = time.strptime(val3, '%H:%M:%S')
        val4 = time.strptime(val4, '%H:%M:%S')
        ss1 = val3
        se1 = val4
        print(ss1.tm_hour, se1.tm_hour)
        slotstart.append(str(ss1.tm_hour) + ':00:00')
        slotend.append(str(se1.tm_hour) + ':00:00')
        # slotstart.append(ss1)
        # slotend.append(se1)
print(slotstart, slotend)
