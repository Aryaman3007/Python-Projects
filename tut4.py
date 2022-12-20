import tkinter
import mysql.connector

win = tkinter.Tk()
win.title("Tkinter GUI")                #change the name of the window
win.geometry("400x400+500+150")         #To change the dimension and change the position of window
#win.config(bg="cyan")

def create_table():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="123456",database='software_db')    
    mycursor=mydb.cursor()          
    mycursor.execute('''CREATE TABLE IF NOT EXISTS users (username VARCHAR(50),email VARCHAR(50) UNIQUE,gender INT,password VARCHAR(20));''')    
    mydb.commit()                   
    mydb.close()

def create_user(username,email,gender,password):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="123456",database='software_db')    
    mycursor=mydb.cursor()
    mycursor.execute('''INSERT into users VALUES(%s,%s,%s,%s)''', (username,email,gender,password))
    mydb.commit()
    mydb.close()
    

def onclick():
    username= username_entry.get()
    password= passwrd_entry.get()
    email= email_entry.get()
    condition= condition_variable.get()
    gender= gender_variable.get()

    correct_username= "Aryaman"
    correct_passwrd= "abcd1234"

    if(condition==1):
        create_user(username,email,gender,password)
        msg_label['text']="SignUp Successfull"        
        msg_label['fg']='green'
    else:
        msg_label['text']="Please agree with terms & conditions"        
        msg_label['fg']='red'       
    

    if(username==correct_username and password==correct_passwrd):
        msg_label['text']="Login is Successfull"        
        msg_label['fg']='green'

    else:
        msg_label['text']="Login Failed"        
        msg_label['fg']='red'

create_table()
        

condition_variable= tkinter.IntVar()
gender_variable= tkinter.IntVar()

username_label=tkinter.Label(win,text="USERNAME")
username_label.pack(pady=5)

username_entry=tkinter.Entry(width=30)
username_entry.pack(padx=10, pady=5)

email_label=tkinter.Label(win,text="EMAIL")
email_label.pack(pady=5)

email_entry=tkinter.Entry(width=30)
email_entry.pack(padx=10, pady=5)

male_button= tkinter.Radiobutton(win,text="Male", variable=gender_variable, value=0)
male_button.pack(pady=5)

female_button= tkinter.Radiobutton(win,text="Female", variable=gender_variable, value=1)
female_button.pack(pady=5)

other_button= tkinter.Radiobutton(win,text="other", variable=gender_variable, value=2)
other_button.pack(pady=5)

passwrd_label=tkinter.Label(win,text="PASSWORD")
passwrd_label.pack(pady=5)

passwrd_entry=tkinter.Entry(show="*",width=30)
passwrd_entry.pack(padx=10, pady=5)

condition_button=tkinter.Checkbutton(win,text="I agree with terms & conditions", onvalue=1, offvalue=0, variable=condition_variable)
condition_button.pack(pady=5)

signup_button=tkinter.Button(win,text="SignUp",bg="black",fg="white",command=onclick)    
signup_button.pack(padx=10, pady=5)

msg_label=tkinter.Label(win,text="Message will come here")
msg_label.pack(pady=5)


#submit_button2=tkinter.Button(win,text="Submit",bg="green")
#submit_button2.pack()


#Geometry manager helps us to put our component on the window
#1)Pack -> It is used to place the component in an order
#2)Place
#3)Grid

win.mainloop()                  #hold python window and not allowed to go

