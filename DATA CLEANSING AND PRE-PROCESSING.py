import pandas as pd
import datetime
import time
#..............DATA CLEANSING AND PRE-PROCESSING.........................   

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

#print (Action[0])
#c=0                    
#for index, row in df.iterrows():
 #   print(row['Action'], row['Time'], row['Processid'], row['Exe'], row['Description'])
  #  c=c+1

#print c

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
            
#print (len(Action2));
#print (len(Description2));
   
         #j = j + 1
    #i = i + 1         
#with open('PycharmProjects/Code/data/Data set/step1.csv', 'wb') as csvfile:
#    writer = csv.writer(csvfile)
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

