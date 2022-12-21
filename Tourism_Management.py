import mysql.connector

import time

mydb=mysql.connector.connect(host="localhost",user="root",passwd="123456",database='tourism')
mycursor=mydb.cursor()
mydb.autocommit=True

table1='''create table if not exists Hotel(
          H_ID VARCHAR(10) ,
          Place VARCHAR(20),
          Hotel_Name VARCHAR(30),
          Facilities VARCHAR(100),
          Rating float,
          Package VARCHAR(30),
          H_Cost float)'''

mycursor.execute(table1)
table2='''create table if not exists transport(
          T_ID VARCHAR(10) ,
          Destination VARCHAR(30),
          Place_of_origin VARCHAR(30),
          Mode_of_transport VARCHAR(30),
          Dep_time time,
          Arr_time time,
          T_Cost float)'''

mycursor.execute(table2)

table3='''create table if not exists Customer(
          Cust_ID integer  PRIMARY KEY AUTO_INCREMENT ,
          Name VARCHAR(20),
          H_ID VARCHAR(10),
          T_ID VARCHAR(10),
          Date_of_Travel DATE,
          Destination VARCHAR(20),
          Hotel_Name VARCHAR(30),
          Transport VARCHAR(20),
          Place_o_Origin VARCHAR(20)
          )'''
mycursor.execute(table3)

table4='''create table if not exists Bill(
          cust_id INT references customer(Cust_ID),
          H_cost float,
          T_cost float
          )'''
mycursor.execute(table4)
sql='ALTER TABLE Customer AUTO_INCREMENT=1000;'
mycursor.execute(sql)
mydb.commit()
l=''
def travel_book():
    global j
    des=input("Enter your destination : ")
    h,j=0,des
    time.sleep(1)
    print('...')
    if des.lower()=='bangalore':
        org=input('Enter the starting point : ')
        if org.lower() =='mumbai':
            show('Bangalore','Mumbai')
        elif org.lower()=='delhi':
            show('Bangalore','Delhi')
        elif org.lower()=='kolkata':
            show('Bangalore','Kolkata')
        else:
            print('Invalid Input.\n Try Again')
            

    if des.lower()=='mumbai':
        org=input('Enter the starting point : ')
        if org.lower() =='bangalore':
            show('Mumbai','Bangalore')
        elif org.lower()=='delhi':
            show('Mumbai','Delhi')
        elif org.lower()=='kolkata':
            show('Mumbai','Kolkata')
        else:
            print('Invalid Input.\n Try Again')
            
                
    if des.lower()=='delhi':
        org=input('Enter the starting point : ')
        if org.lower() =='bangalore':
            show('Delhi','Bangalore')
        elif org.lower()=='mumbai':
            show('Delhi','Mumbai')
        elif org.lower()=='kolkata':
            show('Delhi','Kolkata')
        else:
            print('Invalid Input.\n Try Again')
            
            
    if des.lower()=='kolkata':
        org=input('Enter the starting point : ')
        if org.lower() =='bangalore':
            show('Kolkata','Bangalore')
        elif org.lower()=='delhi':
            show('Kolkata','Delhi')
        elif org.lower()=='mumbai':
            show('Kolkata','Mumbai')
        else:
            print('Invalid Input.\n Try Again')
                     

def book(b,c):
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="123456",database='tourism')
    mycursor=mydb.cursor()
    l=[]
    while True:
        name=input("\nEnter Your name : ")
        Date_Of_Travel=input("\nEnter the date when ou want to book the room (YYYY-MM-DD) : ")
        H_Name,transports,origin='','',''        
        if b==1:
            H_Id = input("\nEnter the hotel Id for which hotel you want to book a room : ")
            for i in V:
                for ir in i:
                    if i[0]==H_Id:
                        H_Name=i[2]
            T_Id=input("Enter the ID of which transport method you would like to book : ")
            for j in Val:
                for jr in j:
                    if j[0]==T_Id:
                        transports,origin=j[3],j[2]

            sql="insert into customer (Name,H_ID,T_ID,Date_of_Travel,Destination,Hotel_Name,Transport,Place_o_Origin) values( %s, %s, %s, %s, %s,%s,%s,%s)"
            mycursor.execute(sql,(name,H_Id,T_Id,Date_Of_Travel,c,H_Name,transports,origin,))
            mydb.commit()
            sql='select Cust_ID from customer where Name=%s'
            mycursor.execute(sql,(name,))
            result=mycursor.fetchall()
            print('Your CUSTOMER ID is : ',result)
            u=input("\nIs there another customer (Y/N) : ")
            if u.upper()=='Y':
                continue
            if u.upper()=='N':
                break
        if b==2:
            H_Id = input("\nEnter the hotel Id for which hotel you want to book a room : ")
            for i in V:
                for ir in i:
                    if i[0]==H_Id:
                        H_Name=i[2]
                        
                        
            sql="insert into customer (name,H_ID,Date_of_Travel,Destination,Hotel_Name) values(%s,%s,%s,%s,%s)"
            mycursor.execute(sql,(name,H_Id,Date_Of_Travel,c,H_Name,))
            mydb.commit()
            sql='select Cust_ID from customer where Name= %s'
            mycursor.execute(sql,(name,))
            result=mycursor.fetchall()
            print('Your CUSTOMER ID is : ',result[0])
            u=input("\nIs there another customer (Y/N) : ")
            if u.upper()=='Y':
                continue
            if u.upper()=='N':
                break
        if b==3:
            T_Id=input("Enter the ID of which transport method you would like to book : ")
            for j in Val:
                for jr in j:
                    if j[0]==T_Id:
                        transports,origin=j[3],j[2]
                        
            sql="insert into customer (name,T_ID,Date_of_Travel,Destination,Transport,Place_o_Origin) values (%s,%s,%s,%s,%s,%s)"
            mycursor.execute(sql,(name,T_Id,Date_Of_Travel,c,transports,origin,))
            mydb.commit()
            sql='select Cust_ID from customer where Name=%s'
            mycursor.execute(sql,(name,))
            result=mycursor.fetchall()
            print('Your CUSTOMER ID is : ',result[0])
            u=input("\nIs there another customer (Y/N) : ")
            if u.upper()=='Y':
                continue
            if u.upper()=='N':
                break
            
def printbox():
    print("\t\t_______________________________________________________________________________________________")
    print("\t\t|                            Voyager Tours and Travels                                        |")
    print("\t\t|      C-57,G-Block,Bandra Kurla Complex,Bandra East,Mumbai,Maharashtra 400051                |")
    print("\t\t|                         phone no.:022-5798465,022-6248957                                   |")
    print("\t\t|                            website: www.Voyager.com                                         |")
    print("\t\t|                                                                                             |")
    print("\t\t|                    Places:Delhi | Mumbai | Bangalore | Kolkata                              |")
    print("\t\t|                                                                                             |")
    print("\t\t|             Winner of BEST TOURS AND TRAVELS AGENCY IN INDIA IN 2019 award                  |")
    print("\t\t|_____________________________________________________________________________________________|")


V=[('B01','Bangalore','The Oberoi',' Free Wi-Fi | Luxury Suites','4.5','5N|4D','30000'),
   ('B02','Bangalore','The Velvett','Free Wi-Fi|Power Backup' ,'4','5N|4D','50000'),
   ('B03','Bangalore','The Ritz Carlton','Free Parking|Premium rooms','4','7N|6D','80000'),
   ('M01','Mumbai','Taj Palace','Premium rooms|Spa' ,'5','7D|6N','90000'),
   ('M02','Mumbai','Trident','Luxurious Buisness stays|Free Wi-Fi','5','4N|3D','50000'),
   ('M03','Mumbai','Sofitel','Premium Rooms|Hair and Beauty Salon','4.5','5N|4D','90000'),
   ('D01','Delhi','Maidens Hotel','Premium Rooms|Restaurant','5','5N|4D','54000'),
   ('D02','Delhi','The Imperial','Luxury Suites|Pool and Yoga Studio','5','4N|3D','25000'),
   ('D03','Delhi','The Claridges','Free Wi-Fi and parking|Outdoor sports','4','5N|4D','80000'),
   ('K01','Kolkata','Hyatt Regency','Free WiFi|Spa','5','6N|7D','85000'),
   ('K02','Kolkata','ITC Sonar','Free WiFi|Free Parking','5','5N|6D','65000'),
   ('K03','Kolkata','The Oberoi Grand','Airport Shuttle|Swimming Pool','5','8N|9D','100000')]
d1,d2={},{}

Val=[('BDT01','Bangalore','Delhi','Train','09:00:00','16:00:00','5000'),
    ('BDF01','Bangalore','Delhi','Flight','12:00:00','14:00:00','10000'),
    ('BDB01','Bangalore','Delhi','Bus','18:45:00','09:30:00','2000'),
    ('BMF01','Bangalore','Mumbai','Flight','15:30:00','17:00:00','12000'),
    ('BMT01','Bangalore','Mumbai','Train','17:30:00','07:00:00','4000'),
    ('BMB01','Bangalore','Mumbai','Bus','10:30:00','20:30:00','13000'),
    ('BKF01','Bangalore','Kolkata','Flight','12:30:00','15:00:00','13000'),
    ('BKT01','Bangalore','Kolkata','Train','17:45:00','13:00:00','2400'),
    ('BKB01','Bangalore','Kolkata','Bus','12:30:00','07:00:00','1500'),
    ('MDF02','Mumbai','Delhi','Flight','11:00:00','12:30:00','8000'),
    ('MDT02','Mumbai','Delhi','Train','15:00:00','21:30:00','1800'),
    ('MDB02','Mumbai','Delhi','Bus','11:00:00','22:30:00','1200'),
    ('MKF02','Mumbai','Kolkata','Flight','09:00:00','11:30:00','18000'),
    ('MKT02','Mumbai','Kolkata','Train','06:00:00','11:30:00','2800'),
    ('MKB02','Mumbai','Kolkata','Bus','19:00:00','18:30:00','1500'),
    ('MBF02','Mumbai','Bangalore','Flight','17:30:00','19:00:00','14000'),
    ('MBT02','Mumbai','Bangalore','Train','11:30:00','09:00:00','2200'),
    ('MBB02','Mumbai','Bangalore','Bus','17:30:00','19:00:00','1400'),
    ('DMF03','Delhi','Mumbai','Flight','07:30:00','09:00:00','12000'),
    ('DMT03','Delhi','Mumbai','Train','07:30:00','09:00:00','3900'),
    ('DMB03','Delhi','Mumbai','Bus','07:30:00','09:00:00','12000'),
    ('DKF03','Delhi','Kolkata','Flight','11:00:00','12:45:00','15000'),
    ('DKT03','Delhi','Kolkata','Train','15:30:00','10:00:00','3200'),
    ('DKB03','Delhi','Kolkata','Bus','05:30:00','22:30:00','1900'),
    ('DBF03','Delhi','Bangalore','Flight','19:30:00','21:30:30','16000'),
    ('DBT03','Delhi','Bangalore','Train','06:45:00','09:00:00','4200'),
    ('DBB03','Delhi','Bangalore','Bus','13:00:00','10:45:00','1400'),
    ('KMF04','Kolkata','Mumbai','Flight','09:30:00','11:30:00','15000'),
    ('KMT04','Kolkata','Mumbai','Train','14:00:00','13:30:00','3800'),
    ('KMB04','Kolkata','Mumbai','Bus','19:30:00','11:45:00','2100'),
    ('KDF04','Kolkata','Delhi','Flight','16:00:00','18:00:00','17000'),
    ('KDT04','Kolkata','Delhi','Train','07:00:00','20:30:00','4100'),
    ('KDB04','Kolkata','Delhi','Bus','11:00:00','22:30:00','1200'),
    ('KBF04','Kolkata','Bangalore','Flight','09:00:00','11:30:00','18000'),
    ('KBT04','Kolkata','Bangalore','Train','07:30:00','09:00:00','3900'),
    ('KBB04','Kolkata','Bangalore','Bus','17:30:00','19:00:00','1400')]
def pricing(a,b):
    for i in a :
        for ir in i:
            d1[i[0]]=i[2],i[4]
    for j in b:
        for jr in j:
            d2[j[0]]=j[6]

pricing(V,Val)    
def insert():
    sql="insert into Hotel (H_ID,Place ,Hotel_Name ,Facilities ,Rating,Package,H_cost  ) values (%s,%s,%s,%s,%s,%s,%s)"
    global V
    for i in V:
        mycursor.execute(sql,i)
    mydb.commit()



def insert_T():
    sql1="insert into transport (T_ID,Destination,Place_of_origin,Mode_of_transport,Dep_time,Arr_time,T_cost ) values (%s,%s,%s,%s,%s,%s,%s)"
    global Val
    for i in Val:
        mycursor.execute(sql1,i)
    mydb.commit()

insert()
insert_T()
printbox()

def show(des,org):
    h=0
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="123456",database='tourism')
    mycursor=mydb.cursor()
    dis="select * from transport where Place_of_origin = %s and Destination= %s"
    mycursor.execute(dis,(org,des,))
    rec=mycursor.fetchall()
    for i in rec:
        print(f'''
\t\t++  T_ID            : {i[0]}
\t\t++  Destination     : {i[1]}
\t\t++  Place of origin : {i[2]}
\t\t++  Mode of Travel  : {i[3]}
\t\t++  Depature Time   : {i[4]}
\t\t++  Arrival Time    : {i[5]}
\t\t++  Travel Cost     : {i[6]}

''')
        h+=1
        if h==3:
            break

    

while True:
    print('''\n\n\n
                      +===========================================================================+
                      +                                                                           +
                      +       1)BOOKING                       2) REVIEW BOOKING INFORMATION       +
                      +                                                                           +
                      +                                                                           +
                      +                                                                           +
                      +                                                                           +
                      +       3) BILLING                      4) UPDATE OR DELETE                 +
                      +                                                                           +
                      +                           5)EXIT                                          +
                      +                                                                           +
                      +===========================================================================+\n\n''')
    print("\n\n")
    ch=int(input("Enter Your option : "))
    print("Processing")
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')


    if ch==1:
        print('''\n\n
\t\t\t\t\t+=============================+
\t\t\t\t\t+                             +
\t\t\t\t\t+                             +
\t\t\t\t\t+  1)Hotel and Transport      +
\t\t\t\t\t+  2)Hotel                    +
\t\t\t\t\t+  3)Transport                +
\t\t\t\t\t+                             +
\t\t\t\t\t+                             +
\t\t\t\t\t+=============================+\n\n''')
        hnt=int(input("Enter your booking option  : "))     
        if hnt==1:
            time.sleep(1)
            print('...')
            print("\n\n\t\t\t\t\t FOR HOTEL BOOKING\n\n ")
            destination=input("\nEnter your desitination : ")
            dis="select * from hotel where place = %s "
            mycursor.execute(dis,(destination,))
            c=0
            records=mycursor.fetchall()
            for row in records:
                print(f'''\n\n
\t\t\t\t\t+  H_ID           :   {row[0]}
\t\t\t\t\t+  Place          :   {row[1]}                               
\t\t\t\t\t+  Hotel Name     :   {row[2]}                                              
\t\t\t\t\t+  Facilities     :   {row[3]}
\t\t\t\t\t+  Rating         :   {row[4]}
\t\t\t\t\t+  Package        :   {row[5]}
\t\t\t\t\t+  Price          :   {row[6]}\n\n''')
                c+=1
                if c==3:
                    break
            print('\n\n\t\t\t\t\t FOR TRAVEL BOOKING\n\n')
            travel_book()
            print('\n\n')
            Book=input("Would you like to proceed to booking (Y/N) : ")
            print('\n\n')            
            if Book.upper()=='Y':
                book(hnt,j)
        
        if hnt==2:
            print("\n\n\t\t\t\t\t FOR HOTEL BOOKING\n\n ")
            destination=input("Enter your desitination : ")
            dis="select * from hotel where place = %s "
            mycursor.execute(dis,(destination,))
            c=0
            records=mycursor.fetchall()
            for row in records:
                print(f'''
\t\t\t\t\t+  H_ID           :   {row[0]}
\t\t\t\t\t+  Place          :   {row[1]}                               
\t\t\t\t\t+  Hotel Name     :   {row[2]}                                              
\t\t\t\t\t+  Facilities     :   {row[3]}
\t\t\t\t\t+  Rating         :   {row[4]}
\t\t\t\t\t+  Package        :   {row[5]}
\t\t\t\t\t+  Price          :   {row[6]}\n\n''')
                c+=1
                if c==3:
                    break
            print('\n\n')
            Book=input("Would you like to prceed to booking (Y/N) : ")
            if Book.upper()=='Y':
                book(hnt,destination)
        if hnt==3:
            print('\n\n\t\t\t\t\t FOR TRAVEL BOOKING\n\n')
            travel_book()
            print('\n\n')
            Book=input("Would you like to proceed to booking (Y/N) : ")
            if Book.upper()=='Y':
                book(hnt,j)
            print('\n\n')


    if ch==2:
        ID=int(input("Enter your user ID : "))
        time.sleep(1)
        print('...')
        sql="SELECT * FROM CUSTOMER WHERE Cust_ID =%s"
        mycursor.execute(sql,(ID,))
        rec=mycursor.fetchall()
        if rec==[]:
            print('There is no such record')
            continue
        if rec!=[]:
            for row in rec:
                print(f'''\n\n
\t\t\t\t\t+  Cust_ID         :   {row[0]}
\t\t\t\t\t+  Name            :   {row[1]}
\t\t\t\t\t+  H_ID            :   {row[2]}
\t\t\t\t\t+  T_ID            :   {row[3]}
\t\t\t\t\t+  Date_of_Travel  :   {row[4]}
\t\t\t\t\t+  Destination     :   {row[5]}
\t\t\t\t\t+  Hotel_Name      :   {row[6]}
\t\t\t\t\t+  Transport       :   {row[7]}
\t\t\t\t\t+  Place_o_Origin  :   {row[8]}\n\n
''')


    if ch==3:
        cost,h,t=[],0,0
        c_ID=int(input("Enter your customer ID : "))
        sql="SELECT * FROM CUSTOMER WHERE Cust_ID = %s"
        mycursor.execute(sql,(c_ID,))
        rec=mycursor.fetchall()
        H,T='',''
        h_name,Destination,Place_o_Origin,transport='','','',''
        for row in rec:
            H=row[2]
            T=row[3]
        sql1="select H_Cost from Hotel where H_ID= %s"
        mycursor.execute(sql1,(H,))
        rec=mycursor.fetchall()
        for row in rec:
            cost.append(row[0])
            if row[0]!='':
                h+=1
                break
        sql2="select T_Cost from Transport where T_ID= %s"
        mycursor.execute(sql2,(T,))
        rec=mycursor.fetchall()
        for row in rec:
            cost.append(row[0])
            if row[0]!='':
                t+=1
                break
        
        if h==1 and t==0:
            
            sql="insert into Bill(cust_id,H_cost) values(%s,%s)"
            mycursor.execute(sql,(c_ID,cost[0],))
            mydb.commit()
            sql0='select cust_id,H_cost,T_cost,(H_cost)as Total from Bill where cust_id= %s'
            mycursor.execute(sql0,(c_ID,))
            rec=mycursor.fetchall()
            for row in rec:
                print(f'''
\t\t\t\t\t+  C_ID      :  {row[0]}
\t\t\t\t\t+  H_Cost    :  {row[1]}
\t\t\t\t\t+  T_Cost    :    -
\t\t\t\t\t+  Total     :  {row[3]}\n\n''')
                break

        if t==1 and h==0:
            sql="insert into Bill(cust_id,T_cost) values(%s,%s)"
            mycursor.execute(sql,(c_ID,cost[0],))
            mydb.commit()
            sql0='select cust_id,H_cost,T_cost,(T_cost)as Total from Bill where cust_id= %s'
            mycursor.execute(sql0,(c_ID,))
            rec=mycursor.fetchall()
            for row in rec:
                print(f'''
\t\t\t\t\t+  C_ID      :  {row[0]}
\t\t\t\t\t+  H_Cost    :    -
\t\t\t\t\t+  T_Cost    :  {row[2]}
\t\t\t\t\t+  Total     :  {row[3]}\n\n''')
                break            
        if h==1 and t==1:
            sql="insert into Bill(cust_id,H_cost,T_cost) values(%s,%s,%s)"
            mycursor.execute(sql,(c_ID,cost[0],cost[1],))
            mydb.commit()
            sql0='select cust_id,H_cost,T_cost,(H_cost+T_cost)as Total from Bill where cust_id= %s'
            mycursor.execute(sql0,(c_ID,))
            rec=mycursor.fetchall()
            for row in rec:
                print(f'''
\t\t\t\t\t+  C_ID      :  {row[0]}
\t\t\t\t\t+  H_Cost    :  {row[1]}
\t\t\t\t\t+  T_Cost    :  {row[2]}
\t\t\t\t\t+  Total     :  {row[3]}\n\n''')
                break

    if ch==5:
        print("Thank You  ")
        break


    if ch==4:
        print('''\n\n
\t\t\t\t\t+====================================================+
\t\t\t\t\t+                                                    +
\t\t\t\t\t+         1) To change the Name                      +
\t\t\t\t\t+         2) To change Date of Travel                +
\t\t\t\t\t+         3) To change hotel booking                 +
\t\t\t\t\t+         4) To change travel booking                +
\t\t\t\t\t+         5) To change both travel and hotel booking +
\t\t\t\t\t+                                                    +
\t\t\t\t\t+                                                    +
\t\t\t\t\t+====================================================+\n\n''')
        ch3=int(input('Enter your choice : '))

        if ch3==1:
            U_ID=int(input("Enter your user ID : "))
            name=input('Enter the new name : ')
            sql='''UPDATE customer SET Name = %s WHERE Cust_ID = %s;'''
            mycursor.execute(sql,(name,U_ID,))
            print("Changes have been made")

        if ch3==2:
            U_ID=int(input("Enter your user ID : "))
            DOT=input("Enter the new date of travel (YYYY/MM/DD) : ")
            sql='''UPDATE customer SET Date_of_Travel = %s WHERE Cust_ID = %s;'''
            mycursor.execute(sql,(DOT,U_ID,))
            print("Changes have been made")            


        if ch3==3:
            U_ID=int(input("Enter your user ID : "))
            H_ID=input("Enter the hotel ID of the Hotel You want to book : ")
            sql='select Hotel_Name,Place from Hotel where H_ID=%s'
            mycursor.execute(sql,(H_ID,))
            H_name,place='',''
            rec=mycursor.fetchall()
            for row in rec:
                H_name=row[0]
                place=row[1]
            sql='update customer set H_ID=%s,Hotel_Name=%s,Destination=%s where Cust_ID=%s'
            mycursor.execute(sql,(H_ID,H_name,place,U_ID,))
            print("Changes have been made")
        
        if ch3==4:
            U_ID=int(input("Enter your user ID : "))
            travel_book()
            dest,plac,trans='','',''
            T_ID=input("Enter the transport ID of the transport you would like to book : ")
            sql='select Destination,Place_of_origin,Mode_of_transport from Transport where T_ID=%s'
            mycursor.execute(sql,(T_ID,))
            rec=mycursor.fetchall()
            for row in rec:
                dest,plac,trans=row[0],row[1],row[2]
            sql='update customer set Destination=%s,Place_o_Origin=%s,Transport=%s,T_ID=%s where Cust_ID=%s'
            mycursor.execute(sql,(dest,plac,trans,T_ID,U_ID,))
            print("Changes have been made")

        if ch3==5:
            U_ID=int(input("Enter your user ID : "))
            H_ID=input("Enter the hotel ID of the Hotel You want to book : ")
            sql='select Hotel_Name,Place from Hotel where H_ID=%s'
            mycursor.execute(sql,(H_ID,))
            H_name,place='',''
            rec=mycursor.fetchall()
            for row in rec:
                H_name=row[0]
                place=row[1]
            travel_book()
            dest,plac,trans='','',''
            T_ID=input("Enter the transport ID of the transport you would like to book : ")
            sql='select Destination,Place_of_origin,Mode_of_transport from Transport where T_ID=%s'
            mycursor.execute(sql,(T_ID,))
            rec=mycursor.fetchall()
            for row in rec:
                dest,plac,trans=row[0],row[1],row[2]
            sql='update customer set H_ID=%s,Hotel_Name=%s,Destination=%s,Place_o_Origin=%s,Transport=%s,T_ID=%s where Cust_ID=%s'
            mycursor.execute(sql,(H_ID,H_name,place,plac,trans,T_ID,U_ID,))
            print("Changes Made")
            
