#!/usr/bin/python3.5
a = [1395,1391,1387,1383,1379,1375,1371,1367,1363,1359,1355,1351,1347,1343,1339,1335,1331,1327,1323,1319,
     1315,1311,1307,1303]#Leap years
numcounts = ["First","Secend","Third"]
numcount = 0
fname = input("Please enter your file name : ")+'.txt' #To create file
f=open(fname,"w")
y = int(input("Please enter Start year : "))#Strating the program in this year
m = int(input("Please enter Start month :  "))#Strating the program in this month
om = str(m)#in program object "m" Changes , so We need an initial value of "m" , we called 'om -> old month'
d = int(input("Please enter Start day :  "))#Strating the program in this day
od = str(d)#in program object "d" Changes , so We need an initial value of "d" , we called 'od -> old d'
ey = int(input("Please enter end year :  "))#The program will end this year '-> ey/01/01 '
dy = y-ey#The intervals of years
maxi = int(input("Please enter the number of repetitions : "))#the number of repetitions that you want reapat password
dn = input("Do you want append name of person(s) in passwords ? ( yes or no ) : ")#(Exampel : mat9512 )
if dn == "yes" or dn == "Yes":
    nm = input("Do you Have Name list ( type yes | or no ) : ")
    if nm == 'yes' or nm == 'Yes':
            Nl = input("Please enter Your names list (Exampel Names.txt) : ")
            fn = open(Nl,'r')
            names = fn.readlines()
            fm = 0
    elif nm == 'no' or nm == 'No' :
            name = input("Enter "+numcounts[numcount]+"  Name of person that you want append in passwords and type End (Exampel : Mohammad ) : ")
            while name !='end' and name !='End' and name != '':
                numcount = numcount +1
                if numcount <= 2:
                    whnum = numcounts[numcount]
                else :
                    whnum = str(numcount+1)+'th'
                opn = open('names.txt','a')
                opn.write(name+'\n')
                name = input("Enter "+whnum+" Name of person that you want append in passwords and type End (Exampel : Mohammad ) : ")
            opn.close()
            numcount = 0
            opnes = open('names.txt','r')
            names = opnes.readlines() 
            fm = 0
elif dn == 'no' or dn == 'No':
        print("Ok")
        names = {"\n"}
        fm = 1
else:
    fm = 2
    print("Oh sary I don't can know What you say , if you have name list please restart this program and type yes or no , Don't type else things ")
def passlist(fname, y, m, d, ey, maxi):#begging Password list
        n = 1
        counter = 0
        e1 = 30
        e2 = 31
        e3 = 29
        dfg = 1
        re = 1
        for c in a:
            while y>=ey:
                if y == c or y == c-1300 :#Check leap years
                    while m>=1 and m<=12:
                        if m>6:#six month secend
                            while d>=1 and d<=e1:
                                y = str(y)
                                m = str(m)
                                d = str(d)
                                if(dfg==1):
                                    if(n == 1 or (m != om or d != od)):
                                        while re<=maxi:
                                            for name in names:
                                                f.write(name[0:-1]+re*(m + d) + '\n')
                                            if fm == 0 : f.write(re*(m + d) + '\n')
                                            re = re+1
                                    else:dfg = 2
                                re = 1
                                while re<=maxi:
                                    for name in names:
                                        f.write(name[0:-1]+re*(str(y) + m + d) + '\n')
                                        y = int(y)
                                        if(y>=1300): f.write(name[0:-1]+re*(str(y-1300) + m + d) + '\n')
                                    if fm == 0:
                                        f.write(re*(str(y) + m + d) + '\n')
                                        f.write(re * (str(y - 1300) + m + d) + '\n')
                                    re = re+1
                                re = 1
                                m = int(m)
                                d = int(d)
                                d = d-1
                            if m-1>=0 and m-1<=6:
                                d = e2
                            elif m-1>6 and m-1<=12:
                                d = e1
                        elif m<=6:#six month first
                            while d>=1 and d<=e2:
                                y = str(y)
                                m = str(m)
                                d = str(d)
                                if(dfg==1):
                                    if (n == 1 or (d != od or m !=om)):
                                        while(re<=maxi):
                                            for name in names:
                                                f.write(name[0:-1]+re*(m + d) + '\n')
                                            if fm == 0: f.write(re * (m + d) + '\n')
                                            re = re+1
                                    else : dfg = 2
                                re = 1
                                while(re<=maxi):
                                    for name in names:
                                        f.write(name[0:-1]+re*(str(y) + m + d) + '\n')
                                        y = int(y)
                                        if (y >= 1300): f.write(name[0:-1]+re*(str(y-1300) + m + d) + '\n')
                                    if fm == 0:
                                        f.write(re*(str(y) + m + d) + '\n')
                                        f.write(re * (str(y - 1300) + m + d) + '\n')
                                    re = re+1
                                re = 1
                                m = int(m)
                                d = int(d)
                                d = d-1
                            if m-1>=1 and m-1<=6:
                                d = e2
                            elif m-1>6 and m-1<=12:
                                d = e1
                        m = m-1
                else:#check not leap year
                    while m>=1 and m<=12:
                        if m>6 and m<=11:
                            while d>=1 and d<=e1:
                                y = str(y)
                                m = str(m)
                                d = str(d)
                                if(dfg==1):
                                    if (n == 1 or (om != m or od != d)):
                                        while(re<=maxi):
                                            for name in names:
                                                f.write(name[0:-1]+re*(m + d)+ '\n')
                                            if fm == 0: f.write(re * (m + d) + '\n')
                                            re = re+1
                                    else : dfg = 2
                                re = 1
                                while(re<=maxi):
                                    for name in names:
                                        f.write(name[0:-1]+re*(str(y) + m + d) + '\n')
                                        y = int(y)
                                        if (y >= 1300): f.write(name[0:-1]+re*(str(y-1300) + m + d) + '\n')
                                    if fm == 0:
                                        f.write(re*(str(y) + m + d) + '\n')
                                        f.write(re * (str(y - 1300) + m + d) + '\n')
                                    re = re+1
                                re = 1
                                m = int(m)
                                d = int(d)
                                d = d-1
                            if m-1>=1 and m-1<=6:
                                d = e2
                            elif m-1>6 and m-1<=11:
                                d = e1
                            else:
                                d = e3
                        elif m<=6 and m>=1:
                            while d>=1 and d<=e2:
                                y = str(y)
                                m = str(m)
                                d = str(d)
                                if(dfg==1):
                                    if (n == 1 or (om != m or od != d)):
                                        while(re<=maxi):
                                            for name in names:
                                                f.write(name[0:-1]+re*(m + d) + '\n')
                                            if fm == 0: f.write(re * (m + d) + '\n')
                                            re = re+1
                                    else : dfg = 2
                                re = 1
                                while(re<=maxi):
                                    for name in names:
                                        f.write(name[0:-1]+re*(str(y) + m + d) + '\n')
                                        y = int(y)
                                        if (y >= 1300): f.write(name[0:-1]+re*(str(y-1300) + m + d) + '\n')
                                    if fm == 0:
                                        f.write(re*(str(y) + m + d) + '\n')
                                        f.write(re * (str(y - 1300) + m + d) + '\n')
                                    re = re+1
                                re = 1
                                m = int(m)
                                d = int(d)
                                d = d-1
                            if m-1>=1 and m-1<=6:
                                d = e2
                            elif m-1>6 and m-1<=11:
                                d = e1
                            else:
                                d = e3
                        elif m==12:
                            d = e3
                            while d>=1 and d<=e3:
                                y = str(y)
                                m = str(m)
                                d = str(d)
                                if(dfg==1):
                                    if (n == 1 or (om != m or od != d)):
                                        while(re<=maxi):
                                            for name in names:
                                                f.write(name[0:-1]+re*(m + d) + '\n')
                                            if fm == 0: f.write(re * (m + d) + '\n')
                                            re = re+1
                                    else : dfg = 2
                                re = 1
                                while(re<=maxi):
                                    for name in names:
                                        f.write(name[0:-1]+re*(str(y) + m + d) + '\n')
                                        y = int(y)
                                        if (y >= 1300): f.write(name[0:-1]+re*(str(y-1300) + m + d) + '\n')
                                    if fm == 0:
                                        f.write(re*(str(y) + m + d) + '\n')
                                        f.write(re * (str(y - 1300) + m + d) + '\n')
                                    re =re+1
                                re = 1
                                m = int(m)
                                d = int(d)
                                d = d-1
                            if m-1>=1 and m-1<=6:
                                d = e2
                            elif m-1>6 and m-1<=11:
                                d = e1
                            else:
                                d = e3
                        m = m-1
                    pass#For more code :]
                d = 30
                m = 12
                print(str(int(counter/(dy)*100)),"%")#print dasad of work !
                y = int(y)-1
                n = n+1
                counter = counter+1
        
        f.close()
        print("Passlist was Crated!")
passlist(fname, y, m, d, ey, maxi)
def comboS(username, fname):#Creat a combolist with Passlist and Username(s) that user enter in program
    passlist = open(fname,'r')
    combolist = open(fname[0:-4]+'combo.txt','a')
    passwords = passlist.readlines()
    for password in passwords:
        combolist.write(username+':'+password[0:-1]+'\n')
    print("\ncombolist was Crated!")
def comboES(usernames):#Creat a combolist with passlist and userlist
    passlist = open(fname,'r')
    combolist = open(fname[0:-4]+'combo.txt','w')
    passwords = passlist.readlines()
    for username in usernames:
        for password in passwords:
            combolist.write(username[0:-1]+':'+password[0:-1]+'\n')
    print("\ncombolist was Crated!")
combostart = input("Are you want make a combolist With this passwords ? (yes-no)")
if combostart == 'Yes' or combostart == 'yes' :#Check creat a combolist
    ussorus = input("Do You Have a Userlist ? ( yes or no ) : ")#Check have a user list
    if ussorus == "no" or ussorus == "No":
        username = input("So enter "+numcounts[numcount]+"  Username that you want append to passwords for combolist and type end(exampel@gmail.com) : ")
        while username !='end' and username !='End' and username != '':
            numcount = numcount +1
            if numcount <= 2:
                whnum = numcounts[numcount]
            else :
                whnum = str(numcount+1)+'th'
            comboS(username, fname)
            username = input("So enter "+whnum+"  Username that you want append to passwords for combolist and type end(exampel@gmail.com) : ")
    elif ussorus == "yes" or ussorus == "Yes" :#Import a userlist in program
        col = input("Please enter your name of userlinst (exampel : Users.txt ) : ")
        usF = open(col,'r')
        usernames = usF.readlines()
        comboES(usernames) 
elif combostart == 'No' or combostart == 'no' :
    print("Ok")
Finished=input("\nAll of Works had been successfuly Finished! :) \n\n Good luCk !")
#https://github.com/ali-shokoohi/copass/
#Created By ali-shokoohi ,  , [Your Name]
