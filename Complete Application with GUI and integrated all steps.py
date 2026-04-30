import sys    
import Tkinter as tk
import ttk
py3 = False
import test
#import DataMiningApp_support
import os.path

def vp_start_gui():
    
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    print ('prog_call = {}'.format(prog_call))
    prog_location = os.path.split(prog_call)[0]
    print ('prog_location = {}'.format(prog_location))
    sys.stdout.flush()
    root = tk.Tk()
    top = Toplevel1 (root)
    DataMiningApp_supportinit(root, top)
    root.mainloop()   
    w = None

def DataMiningApp_supportinit(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def create_Toplevel1(root, *args, **kwargs):
      
    global w, w_win, rt
    global prog_location
    prog_call = sys.argv[0]
    print ('prog_call = {}'.format(prog_call))
    prog_location = os.path.split(prog_call)[0]
    print ('prog_location = {}'.format(prog_location))
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    DataMiningApp_supportinit(w, top, *args, **kwargs)
    return (w, top)

def one(event):
    import pandas as pd
    import datetime
    import time


    df = pd.read_table('PycharmProjects/Code/data/Data set/t_log.txt', delimiter='	', names=('Action', 'Time', 'Processid','Exe','Description'))

    #df = pd.read_table('PycharmProjects/Code/data/Data set/t_log1.txt', delimiter='	', names=('Action', 'Time', 'Processid','Exe','Description'))
    df = df[pd.notnull(df['Time'])]
    #df

    Action = []
    Time = []
    Processid = []
    Exe = []
    Description = []
    for index, row in df.iterrows():
        Action.append(row['Action'])
        Time.append(row['Time'])
        Processid.append(row['Processid'])
        Exe.append(row['Exe'])
        Description.append(row['Description'])
    print (len(Action));
    df2 = pd.DataFrame(columns=['Action', 'StartTime', 'EndTime', 'Processid','Exe','Description']) 
    Action2 = []
    StartTime = []
    EndTime = []
    Processid2 = []
    Exe2 = []
    Description2 = []
    fmt = '%Y-%m-%d %H:%M:%S'
    dt = '%Y-%m-%d'
    rows=len(Action)
    #rows=2000

    import csv
    with open('PycharmProjects/Code/data/Data set/step1.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['program_desc', 'start_time', 'end_time', 'program_file', 'activity_class', 'specific Class',                 
                         'days', 'activity_time', 'slots', 'each slot time', 'processid','action'])        
        i=0
        for i in range(rows):

            #print (row["name"], row["age"])
            #if Action[i] == 'CREATED ' or Action[j] == 'ACTIVATED':
            if str(Action[i]) in ("CREATED "):
            #if Action[i]=="ACTIVATED":

                s1 = datetime.datetime.strptime(Time[i], '%Y-%m-%dT%H:%M:%S+05').strftime(dt)
                s1 = datetime.datetime.strptime(s1, dt)
                Action2.append(Action[i])
                StartTime.append(Time[i])
                #EndTime.append('TBD')
                Processid2.append(Processid[i])
                pid=Processid[i]
                exe=Exe[i]
                Exe2.append(Exe[i])

                j=i
                for j in range(rows):
                #for index, row in df.iterrows():   
                    if (Action[j] == 'DESTROYED'):
                        if (pid==Processid[j]):
                            if (exe==Exe[j]):
                                e1 = datetime.datetime.strptime(Time[j], '%Y-%m-%dT%H:%M:%S+05').strftime(dt)
                                e1 = datetime.datetime.strptime(e1, dt)
                                if (e1==s1):
                                    EndTime.append(Time[j])
                                    Description2.append(Description[j])
                                    writer.writerow([Description[j], Time[i], Time[j], Exe[i],'','','','','','',Processid[i],Action[i]])
                                else:
                                    Description2.append(Description[i])
                                    EndTime.append('TBD')
                                    writer.writerow([Description[i], Time[i], 'TBD', Exe[i],'','','','','','',Processid[i],Action[i]])



                length=len(Action2)-1
                if (length>len(Description2)-1):
                    Description2.append(Description[i])
                    EndTime.append('TBD')
                    writer.writerow([Description[i], Time[i], 'TBD', Exe[i],'','','','','','', Processid[i],Action[i]])
        j=0
        for j in range(rows):

        #print (row["name"], row["age"])
        #if Action[i] == 'CREATED ' or Action[j] == 'ACTIVATED':
            if str(Action[j]) in ("ACTIVATED"):
            #if Action[i]=="ACTIVATED":            
                s2 = datetime.datetime.strptime(Time[j], '%Y-%m-%dT%H:%M:%S+05').strftime(dt)
                s2 = datetime.datetime.strptime(s2, dt)
                Action2.append(Action[j])
                StartTime.append(Time[j])
            #EndTime.append('TBD')
                Processid2.append(Processid[j])
                pid2=Processid[j]
                exe2=Exe[j]
                Exe2.append(Exe[j])

                k=j
                for k in range(rows):
                    if (Action[k] == 'DESTROYED'): 
                        if (pid2==Processid[k]):     
                            if (exe2==Exe[k]):
                                e2 = datetime.datetime.strptime(Time[k], '%Y-%m-%dT%H:%M:%S+05').strftime(dt)
                                e2 = datetime.datetime.strptime(e2, dt)
                                if (e2==s2):
                                    EndTime.append(Time[k])
                                    Description2.append(Description[k])
                                    writer.writerow([Description[k], Time[j], Time[k], Exe[j],'','','','','','',Processid[j],Action[j]])

    print (len(Action2));
    print (len(Description2));        
    print("Step Preprocessing Raw Data Completed Successfuly")

def two(event):
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

        i=1
        index='start_time'
        for row in starttime[1:]:

                d= time.strptime(row,'%Y-%m-%dT%H:%M:%S+05')
                days[i]=time.strftime('%A',d)
                i = i + 1
    # ........................................Activity time calculation...................................
        activity = []
        activity.append('Minutes in each slot')
        activitytiming[0]='activity_time'
        i=1
        fmt = '%Y-%m-%d %H:%M:%S'
        dt = '%Y-%m-%d'
        index='start_time'
        for st in starttime[1:]:
            et = endtime[i]
            if et != 'TBD':
                s1 = datetime.datetime.strptime(st, '%Y-%m-%dT%H:%M:%S+05').strftime(dt)
                e1 = datetime.datetime.strptime(et, '%Y-%m-%dT%H:%M:%S+05').strftime(dt)
                s1 = datetime.datetime.strptime(s1, dt)
                e1 = datetime.datetime.strptime(e1, dt)

            if et!='TBD' and e1==s1:
                s = datetime.datetime.strptime(st,'%Y-%m-%dT%H:%M:%S+05').strftime(fmt)
                e = datetime.datetime.strptime(et,'%Y-%m-%dT%H:%M:%S+05').strftime(fmt)
                s = datetime.datetime.strptime(s,fmt)
                e = datetime.datetime.strptime(e,fmt)
                s=time.mktime(s.timetuple())
                e=time.mktime(e.timetuple())
                r = e-s
                r=r/60
                activitytiming[i]=r
                activity.append(r)

            else:
                activity.append('0')
            i = i + 1

        print(activity)
        print(activitytiming)
        # print (len(activity))
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




                else:
                    aslot.append('slots')
                    writer.writerow(['program_desc', 'start_time', 'end_time', 'program_file', 'activity_class', 'specific Class',
                                    'days', 'activity_time', 'slots', 'each slot time','', 'action', 'processid'])


    print (slots)    
    print("Step Avtivity Time Sloting/Days Classification Completed Successfuly")
def three(event):
    
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


    print("Step Each Activity Time Calculation Completed Successfuly")
def four(event):
    import csv
    description3 = []
    starttime3 = []
    endtime3 = []
    programfile3 = []
    activityclass3 = []
    specificclass3 = []
    days3 = []
    activitytiming3 = []
    slots3 = []
    eachslottime3 = []
    action3 = []
    processid3 = []
    with open('PycharmProjects/Code/data/Data set/step3.csv','r') as csv3file:
        csv3Reader = csv.reader(csv3file)
        for row in csv3Reader:
            description3.append(row[0])
            starttime3.append(row[1])
            endtime3.append(row[2])
            programfile3.append(row[3])
            activityclass3.append(row[4])
            specificclass3.append(row[5])
            days3.append(row[6])
            activitytiming3.append(row[7])
            slots3.append(row[8])
            eachslottime3.append(row[9])
            action3.append(row[10])
            processid3.append(row[11])

    with open('PycharmProjects/Code/data/teststep.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile)
        for j in range(len(description3)):
            writer.writerow(
                [description3[j], programfile3[j], days3[j], slots3[j], activityclass3[j], specificclass3[j]])
    
    print("Step Test Data Generated Completed Successfuly")    
def five(event):
    # Load libraries
    import pandas
    from pandas.plotting import scatter_matrix
    import matplotlib.pyplot as plt
    from sklearn import model_selection
    from sklearn.metrics import classification_report
    from sklearn.metrics import confusion_matrix
    from sklearn.metrics import accuracy_score
    from sklearn.linear_model import LogisticRegression
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    from sklearn.naive_bayes import GaussianNB
    from sklearn.svm import SVC
    # Load Train dataset
    url = "PycharmProjects/Code/data/trainnew1.csv"
    names = ['program_desc', 'program_file', 'days', 'slots', 'activity_class', 'specific Class']
    dataset = pandas.read_csv(url, names=names)
    # Load Test dataset
    urlT = "PycharmProjects/Code/data/teststep.csv"
    namesT = ['program_desc', 'program_file', 'days', 'slots', 'activity_class', 'specific Class']
    datasetT = pandas.read_csv(urlT, names=namesT)
    from sklearn.preprocessing import LabelEncoder
    #if dataset[column].dtype == type(object):        
    pd = LabelEncoder()
    dataset['program_desc'] = pd.fit_transform(dataset['program_desc'])
    pf = LabelEncoder()
    dataset['program_file'] = pf.fit_transform(dataset['program_file'])
    d = LabelEncoder()
    dataset['days'] = d.fit_transform(dataset['days'])
    s = LabelEncoder()
    dataset['slots'] = s.fit_transform(dataset['slots'])
    ac = LabelEncoder()
    dataset['activity_class'] = ac.fit_transform(dataset['activity_class'])
    sc = LabelEncoder()
    dataset['specific Class'] = sc.fit_transform(dataset['specific Class'])
    pdT = LabelEncoder()
    datasetT['program_desc'] = pdT.fit_transform(datasetT['program_desc'])
    pfT = LabelEncoder()
    datasetT['program_file'] = pfT.fit_transform(datasetT['program_file'])
    dT = LabelEncoder()
    datasetT['days'] = dT.fit_transform(datasetT['days'])
    sT = LabelEncoder()
    datasetT['slots'] = sT.fit_transform(datasetT['slots'])
    acT = LabelEncoder()
    datasetT['activity_class'] = acT.fit_transform(datasetT['activity_class'])
    scT = LabelEncoder()
    datasetT['specific Class'] = scT.fit_transform(datasetT['specific Class'])
    # Split-out validation dataset
    array = dataset.values
    X = array[:,1:2]
    #print (X)
    Y = array[:,4]
    #print (Y)
    validation_size = 0.10
    seed = 7
    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
    arrayT = datasetT.values
    XT = arrayT[:,1:2]
    #XT = arrayT[:,1]
    print (XT)
    YT = arrayT[:,4]
    XT_validation=XT

    YT_validation=YT
    print YT_validation
    # Test options and evaluation metric
    seed = 7
    scoring = 'accuracy'
    # Spot Check Algorithms
    models = []
    models.append(('LR', LogisticRegression()))
    #models.append(('LDA', LinearDiscriminantAnalysis()))
    models.append(('KNN', KNeighborsClassifier()))
    models.append(('DecisionTree', DecisionTreeClassifier()))
    models.append(('NB', GaussianNB()))
    models.append(('SVM', SVC()))
    # evaluate each model in turn
    results = []
    names = []

    for name, model in models:


            kfold = model_selection.KFold(n_splits=10, random_state=seed)
            cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
            results.append(cv_results)
            names.append(name)

            msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
            print(msg)
    # Compare Algorithms
    fig = plt.figure()
    fig.suptitle('Algorithm Comparison')
    ax = fig.add_subplot(111)
    plt.boxplot(results)
    ax.set_xticklabels(names)
    plt.show()
    # Make predictions on validation dataset
    knn = KNeighborsClassifier()
    knn.fit(X, Y)

    nb=GaussianNB()
    nb.fit(X, Y)
    predictions3 = nb.predict(XT_validation)
    datasetT['Naive Bays class']=predictions3

    svm=SVC()
    svm.fit(X, Y)
    predictions4 = svm.predict(XT_validation)
    datasetT['svm class']=predictions4


    from sklearn import tree
    tree = tree.DecisionTreeClassifier()
    tree.fit(X, Y)
    #print X_train
    print tree
    #print Y_train
    #print X_validation
    predictions = tree.predict(XT_validation)
    predictions2 = knn.predict(XT_validation)
    print predictions
    datasetT['activity_class']=predictions
    datasetT['Decision Tree class']=predictions
    datasetT['KNN class']=predictions2
    #predictions=sc.inverse_transform(predictions)
    #print predictions
    datasetT['program_desc'] = pdT.inverse_transform(datasetT['program_desc'])
    datasetT['program_file'] = pfT.inverse_transform(datasetT['program_file'])
    datasetT['days'] = dT.inverse_transform(datasetT['days'])
    datasetT['slots'] = sT.inverse_transform(datasetT['slots'])
    datasetT['activity_class'] = ac.inverse_transform(datasetT['activity_class'])
    datasetT['specific Class'] = scT.inverse_transform(datasetT['specific Class'])

    datasetT['Decision Tree class'] = ac.inverse_transform(datasetT['Decision Tree class'])
    datasetT['KNN class'] = ac.inverse_transform(datasetT['KNN class'])
    datasetT['Naive Bays class']=ac.inverse_transform(datasetT['Naive Bays class'])
    datasetT['svm class'] = ac.inverse_transform(datasetT['svm class'])
    print datasetT
    datasetT.to_csv('PycharmProjects/Code/data/result.csv')
    print ('PycharmProjects/Code/data/result.csv'+ 'hase been created.')
    print("Step Data minig and Classification of Activities Completed Successfuly")
def six(event):
    # Load libraries
    import pandas
    from pandas.plotting import scatter_matrix
    import matplotlib.pyplot as plt
    from sklearn import model_selection
    from sklearn.metrics import classification_report
    from sklearn.metrics import confusion_matrix
    from sklearn.metrics import accuracy_score
    from sklearn.linear_model import LogisticRegression
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    from sklearn.naive_bayes import GaussianNB
    from sklearn.svm import SVC
    import csv
    description3 = []
    programfile3 = []
    days3 = []
    slots3 = []
    activityclass3 = []
    specificclass3 = []


    with open('PycharmProjects/Code/data/trainnew1.csv','r') as csv3file:
        csv3Reader = csv.reader(csv3file)
        for row in csv3Reader:
            description3.append(row[0])
            programfile3.append(row[1])
            days3.append(row[2])
            slots3.append(row[3])
            activityclass3.append(row[4])
            specificclass3.append(row[5])
    with open('PycharmProjects/Code/data/result.csv','r') as csv4file:
        csv4Reader = csv.reader(csv4file)
        for row in csv4Reader:
            description3.append(row[1])
            programfile3.append(row[2])
            days3.append(row[3])
            slots3.append(row[4])
            activityclass3.append(row[5])
            specificclass3.append(row[7])
    with open('PycharmProjects/Code/data/FinalTrain.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile)
        for j in range(len(description3)):
            writer.writerow(
                [description3[j], programfile3[j], days3[j], slots3[j], activityclass3[j], specificclass3[j]])

    
    print("Step Fianal Train Data Generated Completed Successfuly")
def seven(event):
    import csv
    import datetime
    import time


    #  ............................................One day modeling...............................
    description3 = []
    starttime3 = []
    endtime3 = []
    programfile3 = []
    activityclass3 = []
    specificclass3 = []
    days3 = []
    activitytiming3 = []
    slots3 = []
    eachslottime3 = []
    action3 = []
    processid3 = []
    with open('PycharmProjects/Code/data/Data set/step3.csv','r') as csv3file:
        csv3Reader = csv.reader(csv3file)
        for row in csv3Reader:
            description3.append(row[0])
            starttime3.append(row[1])
            endtime3.append(row[2])
            programfile3.append(row[3])
            activityclass3.append(row[4])
            specificclass3.append(row[5])
            days3.append(row[6])
            activitytiming3.append(row[7])
            slots3.append(row[8])
            eachslottime3.append(row[9])
            action3.append(row[10])
            processid3.append(row[11])
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

        for j in range(len(description3)):
            for k in range(7):
                if days3[j]==weekdays[k]:
                    with open('PycharmProjects/Code/data/Data set/Days/'+weekdays[k]+'.csv', 'ab') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow(
                            [description3[j], starttime3[j], endtime3[j], programfile3[j],
                            activityclass3[j],
                            specificclass3[j], days3[j], activitytiming3[j], slots3[j], eachslottime3[j],
                            action3[j],processid3[j]])

    
    print("Step One Day Modeling Completed Successfuly")

def eight(event):
    # Load libraries
    import pandas
    from pandas.plotting import scatter_matrix
    import matplotlib.pyplot as plt
    from sklearn import model_selection
    from sklearn.metrics import classification_report
    from sklearn.metrics import confusion_matrix
    from sklearn.metrics import accuracy_score
    from sklearn.linear_model import LogisticRegression
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    from sklearn.naive_bayes import GaussianNB
    from sklearn.svm import SVC
    # Load Train dataset
    url1 = "PycharmProjects/Code/data/FinalTrain.csv"
    names1 = ['program_desc', 'program_file', 'days', 'slots', 'activity_class', 'specific Class']
    dataset = pandas.read_csv(url1, names=names1)
    # Load Test dataset
    urlT = "PycharmProjects/Code/data/Predictions.csv"
    namesT = ['program_desc', 'program_file', 'days', 'slots', 'activity_class', 'specific Class']
    datasetT = pandas.read_csv(urlT, names=namesT)
    from sklearn.preprocessing import LabelEncoder
    #if dataset[column].dtype == type(object):        
    pd = LabelEncoder()
    dataset['program_desc'] = pd.fit_transform(dataset['program_desc'])
    pf = LabelEncoder()
    dataset['program_file'] = pf.fit_transform(dataset['program_file'])
    d = LabelEncoder()
    dataset['days'] = d.fit_transform(dataset['days'])
    s = LabelEncoder()
    dataset['slots'] = s.fit_transform(dataset['slots'])
    ac = LabelEncoder()
    dataset['activity_class'] = ac.fit_transform(dataset['activity_class'])
    sc = LabelEncoder()
    dataset['specific Class'] = sc.fit_transform(dataset['specific Class'])
    pdT = LabelEncoder()
    datasetT['program_desc'] = pdT.fit_transform(datasetT['program_desc'])
    pfT = LabelEncoder()
    datasetT['program_file'] = pfT.fit_transform(datasetT['program_file'])
    dT = LabelEncoder()
    datasetT['days'] = dT.fit_transform(datasetT['days'])
    sT = LabelEncoder()
    datasetT['slots'] = sT.fit_transform(datasetT['slots'])
    acT = LabelEncoder()
    datasetT['activity_class'] = acT.fit_transform(datasetT['activity_class'])
    scT = LabelEncoder()
    datasetT['specific Class'] = scT.fit_transform(datasetT['specific Class'])
    # Split-out validation dataset
    array = dataset.values
    X = array[:,2:4]
    print (X)
    Y = array[:,4]
    print (Y)
    validation_size = 0.10
    seed = 7
    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
    arrayT = datasetT.values
    XT = arrayT[:,0:2]
    #XT = arrayT[:,1]
    print (XT)
    YT = arrayT[:,2]
    XT_validation=XT

    YT_validation=YT
    print YT
    # Test options and evaluation metric
    seed = 7
    scoring = 'accuracy'
    # Spot Check Algorithms
    models = []
    models.append(('LR', LogisticRegression()))
    #models.append(('LDA', LinearDiscriminantAnalysis()))
    models.append(('KNN', KNeighborsClassifier()))
    models.append(('DecisionTree', DecisionTreeClassifier()))
    models.append(('NB', GaussianNB()))
    models.append(('SVM', SVC()))
    # evaluate each model in turn
    results = []
    names = []

    for name, model in models:


            kfold = model_selection.KFold(n_splits=10, random_state=seed)
            cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
            results.append(cv_results)
            names.append(name)

            msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
            print(msg)
    # Make predictions on validation dataset
    knn = KNeighborsClassifier()
    knn.fit(X, Y)

    nb=GaussianNB()
    nb.fit(X, Y)
    predictions3 = nb.predict(XT_validation)
    datasetT['Naive Bays class']=predictions3

    svm=SVC()
    svm.fit(X, Y)
    predictions4 = svm.predict(XT_validation)
    datasetT['svm class']=predictions4


    from sklearn import tree
    tree = tree.DecisionTreeClassifier()
    tree.fit(X, Y)
    #print X_train
    print tree
    #print Y_train
    #print X_validation
    predictions = tree.predict(XT_validation)
    predictions2 = knn.predict(XT_validation)
    print predictions
    datasetT['activity_class']=predictions
    datasetT['Decision Tree class']=predictions
    datasetT['KNN class']=predictions2
    #predictions=sc.inverse_transform(predictions)
    #print predictions
    datasetT['program_desc'] = pdT.inverse_transform(datasetT['program_desc'])
    datasetT['program_file'] = pfT.inverse_transform(datasetT['program_file'])
    datasetT['days'] = dT.inverse_transform(datasetT['days'])
    datasetT['slots'] = sT.inverse_transform(datasetT['slots'])
    datasetT['activity_class'] = ac.inverse_transform(datasetT['activity_class'])
    datasetT['specific Class'] = scT.inverse_transform(datasetT['specific Class'])

    datasetT['Decision Tree class'] = ac.inverse_transform(datasetT['Decision Tree class'])
    datasetT['KNN class'] = ac.inverse_transform(datasetT['KNN class'])
    datasetT['Naive Bays class']=ac.inverse_transform(datasetT['Naive Bays class'])
    datasetT['svm class'] = ac.inverse_transform(datasetT['svm class'])
    datasetT.to_csv('PycharmProjects/Code/data/Predicted.csv')
    print ('PycharmProjects/Code/data/Predicted.csv'+ 'hase been created.')
    
    print("Step Final Prediction based on Classification Completed Successfuly")
def nine(event):
    
    print("Step nine Completed Successfuly")
def ten(event):
    print("Step ten Completed Successfuly")
def eleven(event):
    print("Step eleven Completed Successfuly")
def twelve(event):
    print("Step twwlve Completed Successfuly")
def thirteen(event):
    print("Step thirteen Completed Successfuly")
    
def destroy_Toplevel1():
    
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        
  
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":   
            self.style.theme_use('winnative')
            self.style.configure('.',background=_bgcolor)
            self.style.configure('.',foreground=_fgcolor)
            self.style.map('.',background= [('selected', _compcolor), ('active',_ana2color)])
   
            top.geometry("1366x705+-9+-1")
            top.title("Mining User Activity")
            top.configure(background="#2b2e8e")
            top.configure(highlightbackground="#d9d9d9")
            top.configure(highlightcolor="#17ff3e")
   
            self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
            top.configure(menu = self.menubar)
    
            self.Label1 = tk.Label(top)
            self.Label1.place(relx=0.0, rely=0.0, height=81, width=1364)
            self.Label1.configure(activebackground="#d9d9d9")
            self.Label1.configure(activeforeground="#000000")
            self.Label1.configure(background="#d9d9d9")
            self.Label1.configure(disabledforeground="#a3a3a3")
            self.Label1.configure(font="-family {Times New Roman} -size 13 -slant italic -underline 1")
            self.Label1.configure(foreground="#303468")
            self.Label1.configure(highlightbackground="#d9d9d9")
            self.Label1.configure(highlightcolor="black")
            self.Label1.configure(text='''Periodic Mining of Users Routine Desktop Behavior for Task Assistance''')
   
            self.Button1_4 = tk.Button(top)
            self.Button1_4.place(relx=0.864, rely=0.645, height=64, width=167)
            self.Button1_4.configure(activebackground="#ececec")
            self.Button1_4.configure(activeforeground="#000000")
            self.Button1_4.configure(background="#d9d9d9")
            self.Button1_4.configure(disabledforeground="#a3a3a3")
            self.Button1_4.configure(foreground="#000000")
            self.Button1_4.configure(highlightbackground="#d9d9d9")
            self.Button1_4.configure(highlightcolor="black")
            self.Button1_4.configure(pady="0")
            self.Button1_4.configure(text='''Read Details''')
   
            self.Labelframe1 = tk.LabelFrame(top)
            self.Labelframe1.place(relx=0.864, rely=0.128, relheight=0.489 , relwidth=0.124)
            self.Labelframe1.configure(relief='groove')
            self.Labelframe1.configure(foreground="black")
            self.Labelframe1.configure(text='''Description''')
            self.Labelframe1.configure(background="#d9d9d9")
            self.Labelframe1.configure(highlightbackground="#d9d9d9")
            self.Labelframe1.configure(highlightcolor="black")
            self.Labelframe1.configure(width=170)
  
            self.Message1 = tk.Message(self.Labelframe1)
            self.Message1.place(relx=0.059, rely=0.058, relheight=0.907 , relwidth=0.882, bordermode='ignore')
            self.Message1.configure(background="#d9d9d9")
            self.Message1.configure(font="-family {Segoe UI} -size 12")
            self.Message1.configure(foreground="#6a6b68")
            self.Message1.configure(highlightbackground="#d9d9d9")
            self.Message1.configure(highlightcolor="black")
            self.Message1.configure(justify='center')
            self.Message1.configure(text='''Our work detect and classify meaningful activities form large data and then model these activities into users one day and routine behaviors. It mines the best models of routine activities which may be useful for the prediction of next possible activity of the user.''')
            self.Message1.configure(width=150)
   
            self.Label2 = tk.Label(top)
            self.Label2.place(relx=0.432, rely=0.128, height=351, width=574)
            self.Label2.configure(activebackground="#f9f9f9")
            self.Label2.configure(activeforeground="black")
            self.Label2.configure(background="#d9d9d9")
            self.Label2.configure(disabledforeground="#a3a3a3")
            self.Label2.configure(foreground="#000000")
            self.Label2.configure(highlightbackground="#d9d9d9")
            self.Label2.configure(highlightcolor="black")
            from PIL import Image, ImageTk
            photo_location = "C:\\Users\\zishanali\\Desktop\\Capture_png.gif"
            self._img0 = tk.PhotoImage(photo_location)
            self.Label2.configure(image=self._img0)
            self.Label2.configure(width=574)
  
            self.Labelframe1_1 = tk.LabelFrame(top)
            self.Labelframe1_1.place(relx=0.007, rely=0.128, relheight=0.858 , relwidth=0.417)
            self.Labelframe1_1.configure(relief='groove')
            self.Labelframe1_1.configure(foreground="black")
            self.Labelframe1_1.configure(text='''Steps to Mine Data''')
            self.Labelframe1_1.configure(background="#d9d9d9")
            self.Labelframe1_1.configure(highlightbackground="#d9d9d9")
            self.Labelframe1_1.configure(highlightcolor="black")
            self.Labelframe1_1.configure(width=570)
    
            self.Button1_3 = tk.Button(self.Labelframe1_1)
            self.Button1_3.place(relx=0.079, rely=0.083, height=64, width=227, bordermode='ignore')
            self.Button1_3.configure(activebackground="#ececec")
            self.Button1_3.configure(activeforeground="#000000")
            self.Button1_3.configure(background="#d9d9d9")
            self.Button1_3.configure(disabledforeground="#a3a3a3")
            self.Button1_3.configure(foreground="#000000")
            self.Button1_3.configure(highlightbackground="#d9d9d9")
            self.Button1_3.configure(highlightcolor="black")
            self.Button1_3.configure(pady="0")
            self.Button1_3.configure(text='''Preprocessing Raw Log Data''')
            self.Button1_3.bind('<Button-1>', one)
            #msg.pack()
  
            self.Button1_1 = tk.Button(self.Labelframe1_1)
            self.Button1_1.place(relx=0.07, rely=0.231, height=64, width=227, bordermode='ignore')
            self.Button1_1.configure(activebackground="#ececec")
            self.Button1_1.configure(activeforeground="#000000")
            self.Button1_1.configure(background="#d9d9d9")
            self.Button1_1.configure(disabledforeground="#a3a3a3")
            self.Button1_1.configure(foreground="#000000")
            self.Button1_1.configure(highlightbackground="#d9d9d9")
            self.Button1_1.configure(highlightcolor="black")
            self.Button1_1.configure(pady="0")
            self.Button1_1.configure(text='''Avtivity Time Sloting/Days Classification''')
            self.Button1_1.bind('<Button-1>', two)
 
            self.Button1_2 = tk.Button(self.Labelframe1_1)
            self.Button1_2.place(relx=0.07, rely=0.364, height=64, width=227, bordermode='ignore')
            self.Button1_2.configure(activebackground="#ececec")
            self.Button1_2.configure(activeforeground="#000000")
            self.Button1_2.configure(background="#d9d9d9")
            self.Button1_2.configure(disabledforeground="#a3a3a3")
            self.Button1_2.configure(foreground="#000000")
            self.Button1_2.configure(highlightbackground="#d9d9d9")
            self.Button1_2.configure(highlightcolor="black")
            self.Button1_2.configure(pady="0")
            self.Button1_2.configure(text='''Each Activity Time Calculation''')
            self.Button1_2.bind('<Button-1>', three)
  
            self.Button1_1 = tk.Button(self.Labelframe1_1)
            self.Button1_1.place(relx=0.07, rely=0.496, height=64, width=227, bordermode='ignore')
            self.Button1_1.configure(activebackground="#ececec")
            self.Button1_1.configure(activeforeground="#000000")
            self.Button1_1.configure(background="#d9d9d9")
            self.Button1_1.configure(disabledforeground="#a3a3a3")
            self.Button1_1.configure(foreground="#000000")
            self.Button1_1.configure(highlightbackground="#d9d9d9")
            self.Button1_1.configure(highlightcolor="black")
            self.Button1_1.configure(pady="0")
            self.Button1_1.configure(text='''Generate Test Data''')
            self.Button1_1.bind('<Button-1>', four)
  
            self.Button1_5 = tk.Button(self.Labelframe1_1)
            self.Button1_5.place(relx=0.07, rely=0.628, height=64, width=227, bordermode='ignore')
            self.Button1_5.configure(activebackground="#ececec")
            self.Button1_5.configure(activeforeground="#000000")
            self.Button1_5.configure(background="#d9d9d9")
            self.Button1_5.configure(disabledforeground="#a3a3a3")
            self.Button1_5.configure(foreground="#000000")
            self.Button1_5.configure(highlightbackground="#d9d9d9")
            self.Button1_5.configure(highlightcolor="black")
            self.Button1_5.configure(pady="0")
            self.Button1_5.configure(text='''Apply Data Minining/Classification Algos''')
            self.Button1_5.bind('<Button-1>', five)
  
            self.Button1_2 = tk.Button(self.Labelframe1_1)
            self.Button1_2.place(relx=0.07, rely=0.76, height=64, width=227, bordermode='ignore')
            self.Button1_2.configure(activebackground="#ececec")
            self.Button1_2.configure(activeforeground="#000000")
            self.Button1_2.configure(background="#d9d9d9")
            self.Button1_2.configure(disabledforeground="#a3a3a3")
            self.Button1_2.configure(foreground="#000000")
            self.Button1_2.configure(highlightbackground="#d9d9d9")
            self.Button1_2.configure(highlightcolor="black")
            self.Button1_2.configure(pady="0")
            self.Button1_2.configure(text='''Generate Train Data''')
            self.Button1_2.bind('<Button-1>', six)
  
            self.Button1_3 = tk.Button(self.Labelframe1_1)
            self.Button1_3.place(relx=0.561, rely=0.083, height=64, width=227, bordermode='ignore')
            self.Button1_3.configure(activebackground="#ececec")
            self.Button1_3.configure(activeforeground="#000000")
            self.Button1_3.configure(background="#d9d9d9")
            self.Button1_3.configure(disabledforeground="#a3a3a3")
            self.Button1_3.configure(foreground="#000000")
            self.Button1_3.configure(highlightbackground="#d9d9d9")
            self.Button1_3.configure(highlightcolor="black")
            self.Button1_3.configure(pady="0")
            self.Button1_3.configure(text='''One day modeling''')
            self.Button1_3.bind('<Button-1>', seven)
  
            self.Button1_4 = tk.Button(self.Labelframe1_1)
            self.Button1_4.place(relx=0.561, rely=0.231, height=64, width=227, bordermode='ignore')
            self.Button1_4.configure(activebackground="#ececec")
            self.Button1_4.configure(activeforeground="#000000")
            self.Button1_4.configure(background="#d9d9d9")
            self.Button1_4.configure(disabledforeground="#a3a3a3")
            self.Button1_4.configure(foreground="#000000")
            self.Button1_4.configure(highlightbackground="#d9d9d9")
            self.Button1_4.configure(highlightcolor="black")
            self.Button1_4.configure(pady="0")
            self.Button1_4.configure(text='''Make Final Prediction/Routine Modeling''')
            self.Button1_4.bind('<Button-1>', eight)
    
            self.Button1_6 = tk.Button(self.Labelframe1_1)
            self.Button1_6.place(relx=0.561, rely=0.364, height=64, width=227, bordermode='ignore')
            self.Button1_6.configure(activebackground="#ececec")
            self.Button1_6.configure(activeforeground="#000000")
            self.Button1_6.configure(background="#d9d9d9")
            self.Button1_6.configure(disabledforeground="#a3a3a3")
            self.Button1_6.configure(foreground="#000000")
            self.Button1_6.configure(highlightbackground="#d9d9d9")
            self.Button1_6.configure(highlightcolor="black")
            self.Button1_6.configure(pady="0")
            self.Button1_6.configure(text='''After One day Modeling Final Prdictions ''')
            self.Button1_6.bind('<Button-1>', nine)
    
            self.Button1_6 = tk.Button(self.Labelframe1_1)
            self.Button1_6.place(relx=0.561, rely=0.496, height=64, width=227 , bordermode='ignore')
            self.Button1_6.configure(activebackground="#ececec")
            self.Button1_6.configure(activeforeground="#000000")
            self.Button1_6.configure(background="#d9d9d9")
            self.Button1_6.configure(disabledforeground="#a3a3a3")
            self.Button1_6.configure(foreground="#000000")
            self.Button1_6.configure(highlightbackground="#d9d9d9")
            self.Button1_6.configure(highlightcolor="black")
            self.Button1_6.configure(pady="0")
            self.Button1_6.configure(text='''Done''')
  
            self.Button1_6 = tk.Button(self.Labelframe1_1)
            self.Button1_6.place(relx=0.561, rely=0.628, height=64, width=227 , bordermode='ignore')
            self.Button1_6.configure(activebackground="#ececec")
            self.Button1_6.configure(activeforeground="#000000")
            self.Button1_6.configure(background="#d9d9d9")
            self.Button1_6.configure(disabledforeground="#a3a3a3")
            self.Button1_6.configure(foreground="#000000")
            self.Button1_6.configure(highlightbackground="#d9d9d9")
            self.Button1_6.configure(highlightcolor="black")
            self.Button1_6.configure(pady="0")
            self.Button1_6.configure(text='''Make Prediction and classify Acativity''')
  
            self.Button1_6 = tk.Button(self.Labelframe1_1)
            self.Button1_6.place(relx=0.561, rely=0.752, height=64, width=227 , bordermode='ignore')
            self.Button1_6.configure(activebackground="#ececec")
            self.Button1_6.configure(activeforeground="#000000")
            self.Button1_6.configure(background="#d9d9d9")
            self.Button1_6.configure(disabledforeground="#a3a3a3")
            self.Button1_6.configure(foreground="#000000")
            self.Button1_6.configure(highlightbackground="#d9d9d9")
            self.Button1_6.configure(highlightcolor="black")
            self.Button1_6.configure(pady="0")
            self.Button1_6.configure(text='''Routine activity Modeling''')
  
            self.Label3 = tk.Label(self.Labelframe1_1)
            self.Label3.place(relx=0.0, rely=0.116, height=21, width=38 , bordermode='ignore')
            self.Label3.configure(activebackground="#f9f9f9")
            self.Label3.configure(activeforeground="black")
            self.Label3.configure(background="#d9d9d9")
            self.Label3.configure(disabledforeground="#a3a3a3")
            self.Label3.configure(foreground="#000000")
            self.Label3.configure(highlightbackground="#d9d9d9")
            self.Label3.configure(highlightcolor="black")
            self.Label3.configure(text='''Step 1''')
  
            self.Label3_5 = tk.Label(self.Labelframe1_1)
            self.Label3_5.place(relx=0.0, rely=0.264, height=21, width=38 , bordermode='ignore')
            self.Label3_5.configure(activebackground="#f9f9f9")
            self.Label3_5.configure(activeforeground="black")
            self.Label3_5.configure(background="#d9d9d9")
            self.Label3_5.configure(disabledforeground="#a3a3a3")
            self.Label3_5.configure(foreground="#000000")
            self.Label3_5.configure(highlightbackground="#d9d9d9")
            self.Label3_5.configure(highlightcolor="black")
            self.Label3_5.configure(text='''Step 2''')
 
            self.Label3_6 = tk.Label(self.Labelframe1_1)
            self.Label3_6.place(relx=0.0, rely=0.397, height=21, width=38 , bordermode='ignore')
            self.Label3_6.configure(activebackground="#f9f9f9")
            self.Label3_6.configure(activeforeground="black")
            self.Label3_6.configure(background="#d9d9d9")
            self.Label3_6.configure(disabledforeground="#a3a3a3")
            self.Label3_6.configure(foreground="#000000")
            self.Label3_6.configure(highlightbackground="#d9d9d9")
            self.Label3_6.configure(highlightcolor="black")
            self.Label3_6.configure(text='''Step 3''')
  
            self.Label3_7 = tk.Label(self.Labelframe1_1)
            self.Label3_7.place(relx=0.0, rely=0.529, height=21, width=38 , bordermode='ignore')
            self.Label3_7.configure(activebackground="#f9f9f9")
            self.Label3_7.configure(activeforeground="black")
            self.Label3_7.configure(background="#d9d9d9")
            self.Label3_7.configure(disabledforeground="#a3a3a3")
            self.Label3_7.configure(foreground="#000000")
            self.Label3_7.configure(highlightbackground="#d9d9d9")
            self.Label3_7.configure(highlightcolor="black")
            self.Label3_7.configure(text='''Step 4''')
  
            self.Label3_8 = tk.Label(self.Labelframe1_1)
            self.Label3_8.place(relx=0.0, rely=0.661, height=21, width=38 , bordermode='ignore')
            self.Label3_8.configure(activebackground="#f9f9f9")
            self.Label3_8.configure(activeforeground="black")
            self.Label3_8.configure(background="#d9d9d9")
            self.Label3_8.configure(disabledforeground="#a3a3a3")
            self.Label3_8.configure(foreground="#000000")
            self.Label3_8.configure(highlightbackground="#d9d9d9")
            self.Label3_8.configure(highlightcolor="black")
            self.Label3_8.configure(text='''Step 5''')
  
            self.Label3_9 = tk.Label(self.Labelframe1_1)
            self.Label3_9.place(relx=0.0, rely=0.777, height=31, width=38 , bordermode='ignore')
            self.Label3_9.configure(activebackground="#f9f9f9")
            self.Label3_9.configure(activeforeground="black")
            self.Label3_9.configure(background="#d9d9d9")
            self.Label3_9.configure(disabledforeground="#a3a3a3")
            self.Label3_9.configure(foreground="#000000")
            self.Label3_9.configure(highlightbackground="#d9d9d9")
            self.Label3_9.configure(highlightcolor="black")
            self.Label3_9.configure(text='''Step 6''')
  
            self.Label3_10 = tk.Label(self.Labelframe1_1)
            self.Label3_10.place(relx=0.482, rely=0.116, height=21, width=38 , bordermode='ignore')
            self.Label3_10.configure(activebackground="#f9f9f9")
            self.Label3_10.configure(activeforeground="black")
            self.Label3_10.configure(background="#d9d9d9")
            self.Label3_10.configure(disabledforeground="#a3a3a3")
            self.Label3_10.configure(foreground="#000000")
            self.Label3_10.configure(highlightbackground="#d9d9d9")
            self.Label3_10.configure(highlightcolor="black")
            self.Label3_10.configure(text='''Step 7''')
  
            self.Label3_11 = tk.Label(self.Labelframe1_1)
            self.Label3_11.place(relx=0.482, rely=0.264, height=21, width=38 , bordermode='ignore')
            self.Label3_11.configure(activebackground="#f9f9f9")
            self.Label3_11.configure(activeforeground="black")
            self.Label3_11.configure(background="#d9d9d9")
            self.Label3_11.configure(disabledforeground="#a3a3a3")
            self.Label3_11.configure(foreground="#000000")
            self.Label3_11.configure(highlightbackground="#d9d9d9")
            self.Label3_11.configure(highlightcolor="black")
            self.Label3_11.configure(text='''Step 8''')
  
            self.Label3_12 = tk.Label(self.Labelframe1_1)
            self.Label3_12.place(relx=0.482, rely=0.397, height=21, width=38 , bordermode='ignore')
            self.Label3_12.configure(activebackground="#f9f9f9")
            self.Label3_12.configure(activeforeground="black")
            self.Label3_12.configure(background="#d9d9d9")
            self.Label3_12.configure(disabledforeground="#a3a3a3")
            self.Label3_12.configure(foreground="#000000")
            self.Label3_12.configure(highlightbackground="#d9d9d9")
            self.Label3_12.configure(highlightcolor="black")
            self.Label3_12.configure(text='''Step 9''')
  
            self.Label3_13 = tk.Label(self.Labelframe1_1)
            self.Label3_13.place(relx=0.482, rely=0.529, height=21, width=38 , bordermode='ignore')
            self.Label3_13.configure(activebackground="#f9f9f9")
            self.Label3_13.configure(activeforeground="black")
            self.Label3_13.configure(background="#d9d9d9")
            self.Label3_13.configure(disabledforeground="#a3a3a3")
            self.Label3_13.configure(foreground="#000000")
            self.Label3_13.configure(highlightbackground="#d9d9d9")
            self.Label3_13.configure(highlightcolor="black")
            self.Label3_13.configure(text='''Step 10''')
    
            self.Label3_14 = tk.Label(self.Labelframe1_1)
            self.Label3_14.place(relx=0.482, rely=0.661, height=21, width=38 , bordermode='ignore')
            self.Label3_14.configure(activebackground="#f9f9f9")
            self.Label3_14.configure(activeforeground="black")
            self.Label3_14.configure(background="#d9d9d9")
            self.Label3_14.configure(disabledforeground="#a3a3a3")
            self.Label3_14.configure(foreground="#000000")
            self.Label3_14.configure(highlightbackground="#d9d9d9")
            self.Label3_14.configure(highlightcolor="black")
            self.Label3_14.configure(text='''Step 11''')
   
            self.Label3_15 = tk.Label(self.Labelframe1_1)
            self.Label3_15.place(relx=0.482, rely=0.793, height=21, width=38 , bordermode='ignore')
            self.Label3_15.configure(activebackground="#f9f9f9")
            self.Label3_15.configure(activeforeground="black")
            self.Label3_15.configure(background="#d9d9d9")
            self.Label3_15.configure(disabledforeground="#a3a3a3")
            self.Label3_15.configure(foreground="#000000")
            self.Label3_15.configure(highlightbackground="#d9d9d9")
            self.Label3_15.configure(highlightcolor="black")
            self.Label3_15.configure(text='''Step 12''')
  
            self.Label3_16 = tk.Label(self.Labelframe1_1)
            self.Label3_16.place(relx=0.158, rely=0.917, height=21, width=68 , bordermode='ignore')
            self.Label3_16.configure(activebackground="#f9f9f9")
            self.Label3_16.configure(activeforeground="black")
            self.Label3_16.configure(background="#d9d9d9")
            self.Label3_16.configure(disabledforeground="#a3a3a3")
            self.Label3_16.configure(foreground="#000000")
            self.Label3_16.configure(highlightbackground="#d9d9d9")
            self.Label3_16.configure(highlightcolor="black")
            self.Label3_16.configure(text='''Final Step''')
   
            self.Button1_6 = tk.Button(top)
            self.Button1_6.place(relx=0.139, rely=0.894, height=64, width=227)
            self.Button1_6.configure(activebackground="#ececec")
            self.Button1_6.configure(activeforeground="#000000")
            self.Button1_6.configure(background="#d9d9d9")
            self.Button1_6.configure(disabledforeground="#a3a3a3")
            self.Button1_6.configure(foreground="#000000")
            self.Button1_6.configure(highlightbackground="#d9d9d9")
            self.Button1_6.configure(highlightcolor="black")
            self.Button1_6.configure(pady="0")
            self.Button1_6.configure(text='''Print Results''')
            from ScrolledText import * 
            self.Scrolledtext1 = ScrolledText(top)
            self.Scrolledtext1.place(relx=0.436, rely=0.631, relheight=0.356 , relwidth=0.411)
            self.Scrolledtext1.configure(background="#191919")
            self.Scrolledtext1.configure(font="TkTextFont")
            self.Scrolledtext1.configure(foreground="#ffffff")
            self.Scrolledtext1.configure(highlightbackground="#d9d9d9")
            self.Scrolledtext1.configure(highlightcolor="black")
            self.Scrolledtext1.configure(insertbackground="black")
            self.Scrolledtext1.configure(insertborderwidth="3")
            self.Scrolledtext1.configure(selectbackground="#c4c4c4")
            self.Scrolledtext1.configure(selectforeground="black")
            self.Scrolledtext1.configure(width=10)
            self.Scrolledtext1.configure(wrap='none')

@staticmethod
def popup1(event, *args, **kwargs):
    
    Popupmenu1 = tk.Menu(root, tearoff=0)
    Popupmenu1.configure(activebackground="#f9f9f9")
    Popupmenu1.configure(activeborderwidth="1")
    Popupmenu1.configure(activeforeground="black")
    Popupmenu1.configure(background="#d9d9d9")
    Popupmenu1.configure(borderwidth="1")
    Popupmenu1.configure(disabledforeground="#a3a3a3")
    Popupmenu1.configure(font="-family {Segoe UI} -size 9")
    Popupmenu1.configure(foreground="black")
    Popupmenu1.post(event.x_root, event.y_root)
    
class AutoScroll(object):
    

    def __init__(self, master):
        
        #  Rozen. Added the tryxcept clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            
            pass
            hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
  
            #self.configure(yscrollcommand=_autoscroll(vsb),
            #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
            self.configure(xscrollcommand=self._autoscroll(hsb))
  
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
            hsb.grid(column=0, row=1, sticky='ew')
  
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
  
            # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() + tk.Place.__dict__.keys()
  
        for meth in methods:        
            if meth[0] != '_' and meth not in ('config', 'configure'):            
                setattr(self, meth, getattr(master, meth)) 
@staticmethod
def _autoscroll(sbar):
    
        
    def wrapped(first, last):
        first, last = float(first), float(last)
        if first <= 0 and last >= 1:            
            sbar.grid_remove()
        else:
            sbar.grid()
            sbar.set(first, last)
        return wrapped
  
    def __str__(self):
        
        return str(self.master)
    
    def _create_container(func):
        
 #569     '''Creates a ttk Frame with a given master, and use this new frame to
 #570     place the scrollbars and the widget.'''
        def wrapped(cls, master, **kw):
            container = ttk.Frame(master)
            container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
            container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
            return func(cls, container, **kw)
        return wrapped
            
class ScrolledText(AutoScroll, tk.Text):
    #@_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)
        
    import platform
    def _bound_to_mousewheel(event, widget):
        child = widget.winfo_children()[0]
        if platform.system() == 'Windows' or platform.system() == 'Darwin':
            child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
            child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
        else:
            child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
            child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
            child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
            child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))
    
    def _unbound_to_mousewheel(event, widget):
        if platform.system() == 'Windows' or platform.system() == 'Darwin':
            widget.unbind_all('<MouseWheel>')
            widget.unbind_all('<Shift-MouseWheel>')
        else:
            widget.unbind_all('<Button-4>')
            widget.unbind_all('<Button-5>')
            widget.unbind_all('<Shift-Button-4>')
            widget.unbind_all('<Shift-Button-5>')
    
    def _on_mousewheel(event, widget):
        if platform.system() == 'Windows':
            widget.yview_scroll(-1*int(event.delta/120),'units')
        elif platform.system() == 'Darwin':
            widget.yview_scroll(-1*int(event.delta),'units')
        else:
            if event.num == 4:
                widget.yview_scroll(-1, 'units')
            elif event.num == 5:
                widget.yview_scroll(1, 'units')
  
    def _on_shiftmouse(event, widget):
        if platform.system() == 'Windows':
            widget.xview_scroll(-1*int(event.delta/120), 'units')
        elif platform.system() == 'Darwin':
            widget.xview_scroll(-1*int(event.delta), 'units')
        else:
            if event.num == 4:
                widget.xview_scroll(-1, 'units')
            elif event.num == 5:
                widget.xview_scroll(1, 'units')
                
if __name__ == '__main__':
     vp_start_gui()
  
  

