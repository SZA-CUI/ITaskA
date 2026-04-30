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
