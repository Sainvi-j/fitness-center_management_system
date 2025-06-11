        

import mysql.connector as sql
fit=sql.connect(host='localhost',user='root',passwd='osito',database='employee')
if fit.is_connected():
                print('connected')
                c1=fit.cursor()
                c1.execute('create table user_fitness_saiwi(user_id varchar(10) primary key,password varchar(11),name varchar(10))')
                fit.commit()
                print('table created')







import mysql.connector as sql
fit=sql.connect(host='localhost',user='root',passwd='osito',database='employee')
if fit.is_connected():
    print('connected')
    c1=fit.cursor()
    c1.execute('create table gym_items(object_id varchar(22) primary key,object_name varchar(65),date_of_parchase varchar(65),repairing_data date,total_people_using varchar(65))')
    fit.commit()
    print('table created')

