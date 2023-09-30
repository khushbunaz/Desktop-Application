from tkinter import *
import mysql.connector
import tkinter.messagebox as msg

def create_conn():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="tkinter"
    )

def insert_data():
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="":
        msg.showinfo("Insert Status","All fields are mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        
        query="insert into class(fname,lname,email,mobile) values(%s,%s,%s,%s)"
        args=(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()

        #clear textboxes
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')

        #display message
        msg.showinfo('Insert Status','Data inserted successfully')


def search_data():
    #clear textboxes
    e_fname.delete(0,'end')
    e_lname.delete(0,'end')
    e_email.delete(0,'end')
    e_mobile.delete(0,'end')
    
    if e_id.get=="":
        msg.showinfo("Search Status","Id is mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        
        query="select * from class where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        row=cursor.fetchall()
        
        if row:
            for i in row:
                e_fname.insert(0,i[1])
                e_lname.insert(0,i[2])
                e_email.insert(0,i[3])
                e_mobile.insert(0,i[4])
            #if data is changing then only commit is used
        else:
            msg.showinfo("Search Status","Id not found")
            

def update_data():
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="" or e_id.get()=="":
        msg.showinfo("Update Status","All fields are mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()

        query="update class set fname=%s, lname=%s, email=%s, mobile=%s where id=%s"
        args=(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get(),e_id.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()

        #clear textboxes
        e_id.delete(0,'end')
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')

        msg.showinfo('Update Status','Data updated successfully')
    
def delete_data():
    if e_id.get()=="":
        msf.showinfo("Delete Status","Id is mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()

        query="delete from class where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        conn.commit()
        conn.close()

        #clear textboxes
        e_id.delete(0,'end')
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')

        msg.showinfo("Delete Status","Data deleted successfully")


root=Tk()
root.geometry("440x420")
root.title("Desktop Applicatiion")
root.resizable(width=False,height=False)

title=Label(root,text="Welcome to Desktop Application",font=("Arial",20))
title.place(x=15,y=30)

l_id=Label(root,text='ID',font=("Arial",15))
l_id.place(x=50,y=90)

l_fname=Label(root,text='First Name',font=("Arial",15))
l_fname.place(x=50,y=140)

l_lname=Label(root,text='Last Name',font=("Arial",15))
l_lname.place(x=50,y=190)

l_email=Label(root,text='Email',font=("Arial",15))
l_email.place(x=50,y=240)

l_mobile=Label(root,text='Mobile',font=("Arial",15))
l_mobile.place(x=50,y=290)

e_id=Entry(root)
e_id.place(x=200,y=90)

e_fname=Entry(root)
e_fname.place(x=200,y=140)

e_lname=Entry(root)
e_lname.place(x=200,y=190)

e_email=Entry(root)
e_email.place(x=200,y=240)

e_mobile=Entry(root)
e_mobile.place(x=200,y=290)

insert=Button(root,text="INSERT",font=("Arial",15),bg="pink",fg="black",command=insert_data)
insert.place(x=10,y=370)

search=Button(root,text="SEARCH",font=("Arial",15),bg="pink",fg="black",command=search_data)
search.place(x=110,y=370)

update=Button(root,text="UPDATE",font=("Arial",15),bg="pink",fg="black",command=update_data)
update.place(x=215,y=370)

delete=Button(root,text="DELETE",font=("Arial",15),bg="pink",fg="black",command=delete_data)
delete.place(x=320,y=370)
