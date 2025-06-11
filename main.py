import mysql.connector as sql

fit=sql.connect(host='localhost',user='root',passwd='scott',database='lkd')
if fit.is_connected():
       print('HELLO THERE!')
 
print('............................................................')
print('************************************************************')
print('               WELCOME TO FITNESS CENTRE                ')
print('************************************************************')
print('............................................................')
print('TO LOGIN PRESS                                    :1        ')
print('------------------------------------------------------------')
print('')
print('TO CREATE YOUR NEW ACCOUNT PRESS                  :2        ')
print('------------------------------------------------------------')
print('')
print('TO EXIT PRESS                                     :3      ')
print('------------------------------------------------------------')
c=int(input('ENTER YOUR CHOICE: '))


if (c==1):
    print('')
    print('To LOGIN please enter your user id and password ')
    print('')
    user_id=input('Enter your USER ID: ')
    print('')
    passwd=input('Enter your PASSWORD: ')
    print('')
    name=input('Enter your NAME: ')
    print('')
    c1=fit.cursor()
    c1.execute('Select * from user_fitness_saiwi')
    data=c1.fetchall()
    count=c1.rowcount
    t1=tuple([user_id,passwd])
    for row in data:
           r1=row[0].strip()
           r2=row[1].strip()
           t2=tuple([r1,r2])
           if t1 ==t2:
                    print('___________SUCCESSFULLY LOGIN!!!!!!!!_____________')
                    print('......Welcome to ',name,' LKD fitness centre......')
                    print('__________________________________________________ ')
                    print(' ')
                    print('To see customer details press             :1          ')
                    print(' ')
                    print(' To update customer details press         :2           ')
                    print(' ')
                    print('To see items in gym press                 :3       ')
                    print('')
                    print('To update new items press                 :4         ')
                    print('_____________________________________________________')
                    c2=int(input('ENTER YOUR CHOICE: '))
                    if (c2==1):
                           c1=fit.cursor()
                           c1.execute('Select * from user_fitness_saiwi')
                           data=c1.fetchall()
                           count=c1.rowcount
                           print('Total customer is',count)
                           for row in data:
                                         print(row)
                    elif (c2==2):
                           print('')
                           print('To update customer details please enter the following details')
                           print('')
                           v_cus_id=int(input('Enter customer id:'))
                           print('')
                           v_cus_name=input('Customer name is:')
                           print('')
                           v_cus_address=input('Enter address of customer ')
                           print('')
                           v_date_of_joined=input('Customer joined data ')
                           print('')
                           v_amt_paid=int(input('Paid amount '))
                           print('')
                           c1=fit.cursor()
                           cre="create table customer(custmer varchar(100) primary key,custmer_name varchar(100),custmer_address varchar(1000),joined_date date,amt_paid varchar(100)"
                           update_dtails="insert into customer values(' "+ str(v_cus_id) +" ',' "+ (v_cus_name) +" ',' "+ (v_cus_address) +" ',' "+ (v_date_of_joined) +" ',' "+ str(v_amt_paid) + " ')"
                           c1.execute(cre,update_dtails)
                           fit.commit()
                           print('Customer details succesully updated')
                    elif (c2==3):
                                 print('FOLLOWING ITEMS ARE IN',name ,'GYM')
                                 c1=fit.cursor()
                                 c1.execute('select * from gym_items')
                                 data=c1.fetchall()
                                 count=c1.rowcount
                                 print('Total gym item is',count)
                                 for row in data:
                                        print(row)
                    elif (c2==4):
                            print('To update new items enter the following detils')
                            v_object_id=input('Enter the object code: ')
                            v_object_name=input('Enter the name of gym items: ')
                            v_date_of_purchase=input('Enter the date original purchase(yyyy/mm/dd):  ')
                            v_repairing_date=input('Enter the date of repair: ')
                            v_total_people_using=int(input('Total person using the item: '))
                            c1=fit.cursor()
                            updates2=("insert into gym_items values('"+ str(v_object_id) +"','"+ (v_object_name) +"','"+ (v_date_of_purchase) +"','"+ (v_repairing_date) +"','"+ str(v_total_people_using) +"')")
                            c1.execute(updates2)
                            fit.commit()
                            print('Item updated')
                    else:
                        ('Something went wrong')
            
    
              
                   
                
elif (c==2):
    print('')
    print('To create your account please enter your user id and password: ')
    print('')
    c1=fit.cursor()
    #c1=fit.cursor("('create table user_fitness_saiwi(user_id varchar(100) primary key,password varchar(100),name varchar(100))') 
    v_user_id=input('Choose your user id ')
    print('')
    v_passwd=input('Create your password (in integer)')
    print('')
    v_name=input('Your full name ')
    print('')
    c1=fit.cursor()
    update=("insert into user_fitness_saiwi values(' "+ str(v_user_id) +" ' ,' "+ str(v_passwd) +" ',' "+ (v_name) +" ')")
    c1.execute(update)
    fit.commit()
    print('account created')

elif (c==3):
    print('visit again')
    print('')
    print('thank you')

else:
    ('something went wrong')   
