a = [1395,1391,1387,1383,1379,1375,1371,1367,1363,1359,
     1355,1351,1347,1343,1339,1335,1331,1327,1323,1319,
     1315,1311,1307,1303]

fname = input("Please enter your file name : ")+'.txt'
f=open(fname,"w")
y = int(input("Please enter Start year : "))
m = int(input("Please enter Start month :  "))
om = str(m)
d = int(input("Please enter Start day :  "))
od = str(d)
ey = int(input("Please enter end year :  "))
dy = y-ey
maxi = int(input("Loftan Maximum ra Vared konid (1-5) : "))
dn = input("Do you want append name of person(s) in passwords ? ( yes or no ) : ")
if dn == "yes" or dn == "Yes":
    nm = input("Do you Have Name list ( type yes | or no ) : ")
    if nm == 'yes' or nm == 'Yes':
            Nl = input("Please enter Your names list (Exampel Names.txt) : ")
            fn = open(Nl,'r')
            names = fn.readlines()
            fm = 0
    elif nm == 'no' or nm == 'No' :
            name = input("Enter Name of person that you want append in passwords (Exampel : Mohammad ) : ")
            opn = open('names.txt','w')
            opn.write(name+'1')
            opn.close()
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
def passlist(fname, y, m, d, ey, maxi):
        n = 1
        counter = 0
        e1 = 30
        e2 = 31
        e3 = 29
        dfg = 1
        re = 1
        for c in a:
            while y>=ey:
                if y == c or y == c-1300 :
                    while m>=1 and m<=12:
                        if m>6:
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
                            if m-1>=1 and m-1<=6:
                                d = e2
                            elif m-1>6 and m-1<=12:
                                d = e1
                        elif m<=6:
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
                else:
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
                    "press"
                d = 30
                m = 12
                print(str(int(counter/(dy)*100)),"%")
                y = int(y)-1
                n = n+1
                counter = counter+1
        
        f.close()
        print("Passlist was Crated!")
passlist(fname, y, m, d, ey, maxi)
def comboS(username, fname):
    passlist = open(fname,'r')
    combolist = open(fname[0:-4]+'combo.txt','w')
    passwords = passlist.readlines()
    for password in passwords:
        combolist.write(username+':'+password[0:-1]+'\n')
    print("\ncombolist was Crated!")
def comboES(usernames):
    passlist = open(fname,'r')
    combolist = open(fname[0:-4]+'combo.txt','w')
    passwords = passlist.readlines()
    for username in usernames:
        for password in passwords:
            combolist.write(username[0:-1]+':'+password[0:-1]+'\n')
    print("\ncombolist was Crated!")
combostart = input("Are you want make a combolist With this passwords ? (yes-no)")
if combostart == 'Yes' or combostart == 'yes' :
    ussorus = input("Do You Have a Userlist ? ( yes or no ) : ")
    if ussorus == "no" or ussorus == "No":
        username = input("So enter Username that you want append to passwords for combolist (exampel@gmail.com) : ")
        comboS(username, fname)
    elif ussorus == "yes" or ussorus == "Yes" :
        col = input("Please enter your name of userlinst (exampel : Users.txt ) : ")
        usF = open(col,'r')
        usernames = usF.readlines()
        comboES(usernames) 
elif combostart == 'No' or combostart == 'no' :
    print("Ok")
Finished=input("\nAll of Work Was successfuly Finished :) \n\n Good luCk !")
#Created By Pat&Mat , [Your Name]
