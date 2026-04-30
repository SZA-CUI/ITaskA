#  ..................................Each Slot time Calcultion..................................

with open('PycharmProjects/Code/data/Data set/step2.csv','r') as csv2file:
    csv2Reader = csv.reader(csv2file)
    for row in csv2Reader:
        description2.append(row[0])
        starttime2.append(row[1])
        endtime2.append(row[2])
        programfile2.append(row[3])
        activityclass2.append(row[4])
        specificclass2.append(row[5])
        days2.append(row[6])
        activitytiming2.append(row[7])
        slots2.append(row[8])
        # activity2.append(row[9])
        #eachslottime2.append(row[10])
        action2.append(row[11])
        processid2.append(row[12])
    aslot = []
    j2 = 1
    k = 0
    fmt = '%Y-%m-%d %H:%M:%S'
    dt = '%Y-%m-%d'
    activity2 = []
    activity2.append('Minutes in each slot')
    i = 1
    index = 'start_time'
    aslot.append(slots2)
    with open('PycharmProjects/Code/data/Data set/step3.csv', 'wb') as csvfile3:
        writer3 = csv.writer(csvfile3)
        for j2 in range(len(description2)):
            if j2!=0:
                
                if endtime2[j2] != 'TBD':
                    s1 = datetime.datetime.strptime(starttime2[j2], '%Y-%m-%dT%H:%M:%S+05').strftime(dt)
                    e1 = datetime.datetime.strptime(endtime2[j2], '%Y-%m-%dT%H:%M:%S+05').strftime(dt)
                    s0 = time.strptime(s1, dt)
                    e0 = time.strptime(e1, dt)
                    # s1 = datetime.datetime.strptime(s1, dt)
                
                # e1 = datetime.datetime.strptime(e1, dt)
                if endtime2[j2]!='TBD' and e1==s1:

                    s = datetime.datetime.strptime(starttime2[j2],'%Y-%m-%dT%H:%M:%S+05').strftime('%H:%M:%S')
                    e = datetime.datetime.strptime(endtime2[j2],'%Y-%m-%dT%H:%M:%S+05').strftime('%H:%M:%S')
                    s = time.strptime(s, '%H:%M:%S')
                    e = time.strptime(e, '%H:%M:%S')

                    for k in range(12):
                        if k==int(slots2[j2]):
                            print(slots2[j2])

                            slots = datetime.datetime.strptime(slotstart[k], '%H:%M:%S').strftime('%H:%M:%S')
                            slote = datetime.datetime.strptime(slotend[k], '%H:%M:%S').strftime('%H:%M:%S')
                            s2 = time.strptime(slots, '%H:%M:%S')
                            e2 = time.strptime(slote, '%H:%M:%S')
                            val1=str(s1)+' '+slotstart[k]
                            val2=str(s1)+' '+slotend[k]
                            # print(val1)
                            slots1 = datetime.datetime.strptime(val1, '%Y-%m-%d %H:%M:%S').strftime(fmt)
                            slote1 = datetime.datetime.strptime(val2, '%Y-%m-%d %H:%M:%S').strftime(fmt)
                            ss3 = datetime.datetime.strptime(slots1, fmt)
                            ee3 = datetime.datetime.strptime(slote1, fmt)

                            ss3 = time.mktime(ss3.timetuple())
                            ee3 = time.mktime(ee3.timetuple())

                            s3 = datetime.datetime.strptime(starttime2[j2], '%Y-%m-%dT%H:%M:%S+05').strftime(fmt)
                            e3 = datetime.datetime.strptime(endtime2[j2], '%Y-%m-%dT%H:%M:%S+05').strftime(fmt)
                            s3 = datetime.datetime.strptime(s3, fmt)
                            e3 = datetime.datetime.strptime(e3, fmt)
                            s3 = time.mktime(s3.timetuple())
                            e3 = time.mktime(e3.timetuple())
                            if (s.tm_hour >= s2.tm_hour) and (s.tm_hour < e2.tm_hour) and (e.tm_hour <= e2.tm_hour):
                                r = e3 - s3
                                r = r / 60
                                if r <= 120:
                                # activitytiming2[i] = r
                                # activity2.append(r)
                                    writer3.writerow(
                                        [description2[j2], starttime2[j2], endtime2[j2], programfile2[j2],
                                         activityclass2[j2],
                                         specificclass2[j2], days2[j2], activitytiming2[j2], slots2[j2], r,
                                         action2[j2],processid2[j2]])



                            if (s.tm_hour >= s2.tm_hour) and (s.tm_hour < e2.tm_hour) and (e.tm_hour > e2.tm_hour):
                                r = ee3 - s3
                                r = r / 60
                                if r<=120:
                                # activitytiming2[i] = r
                                #activity2.append(r)
                                    writer3.writerow(
                                        [description2[j2], starttime2[j2], endtime2[j2], programfile2[j2],
                                         activityclass2[j2],
                                         specificclass2[j2], days2[j2], activitytiming2[j2], slots2[j2],r,
                                         action2[j2],processid2[j2]])





                            if (s.tm_hour >= s2.tm_hour and int(slots2[j2]) == k == 11 and e.tm_hour <= 23):
                                r = e3 - s3
                                r = r / 60
                                if r <= 120:
                                    # activitytiming2[i] = r
                                    # activity2.append(r)
                                    writer3.writerow(
                                        [description2[j2], starttime2[j2], endtime2[j2], programfile2[j2],
                                         activityclass2[j2],
                                         specificclass2[j2], days2[j2], activitytiming2[j2], slots2[j2], r,
                                         action2[j2],processid2[j2]])
                            if (s.tm_hour < s2.tm_hour and int(slots2[j2]) == k == 11 and e.tm_hour <= 23 and e.tm_hour>=s2):
                                r = e3 - ss3
                                r = r / 60
                                if r <= 120:
                                    # activitytiming2[i] = r
                                    # activity2.append(r)
                                    writer3.writerow(
                                        [description2[j2], starttime2[j2], endtime2[j2], programfile2[j2],
                                         activityclass2[j2],
                                         specificclass2[j2], days2[j2], activitytiming2[j2], slots2[j2], r,
                                         action2[j2],processid2[j2]])
                            if (s.tm_hour>=s2.tm_hour and int(slots2[j2])==k==11 and e.tm_hour==e2.tm_hour):
                                val3=str(s1)+' '+'23:59:00'
                                e4 = datetime.datetime.strptime(val3, '%Y-%m-%d %H:%M:%S').strftime(fmt)
                                e4 = datetime.datetime.strptime(e4, fmt)
                                e4 = time.mktime(e4.timetuple())
                                r = e4 - s3
                                r = r / 60
                                if r <= 120:
                                # activitytiming2[i] = r
                                #activity2.append(r)
                                    writer3.writerow(
                                        [description2[j2], starttime2[j2], endtime2[j2], programfile2[j2],
                                         activityclass2[j2],
                                         specificclass2[j2], days2[j2], activitytiming2[j2], slots2[j2], r,
                                         action2[j2],processid2[j2]])
                                # else:
                                #     #activity2.append('0')
                                #     writer3.writerow(
                                #         [description2[j2], starttime2[j2], endtime2[j2], programfile2[j2],
                                #          activityclass2[j2],
                                #          specificclass2[j2], days2[j2], activitytiming2[j2], slots2[j2], ' ',
                                #          cluster2[j2]])
            else:
                aslot.append('slots')
                writer3.writerow(['program_desc', 'start_time', 'end_time', 'program_file', 'activity_class', 'specific Class',
                                  'days', 'activity_time', 'slots', 'each slot time', 'action','processid'])
