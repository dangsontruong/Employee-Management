import os
import sqlite3
import tempfile
from configparser import ConfigParser
from tkinter import *
from tkinter import colorchooser
from tkinter import messagebox
from tkinter import ttk


# =========================================== Description ==============================================
# Employee Management System
# Develop by Thành Nam
# Đây là chương trình  giúp các công ty hoặc manager quản lí danh sách nhân viên
# Dev Language: Python
# =======================================================================================================


class Tologin:
    conn = sqlite3.connect("EmployeeList.db")
    conn.execute("CREATE TABLE if not exists ADMIN(ADMIN_ID INTEGER, USERNAME TEXT, PASSWORD TEXT )")
    conn.commit()

    conn.close()
    # account
    user1 = 'nam'


    def __init__(self,root):

        self.root = root
        self.root.title('Login')

        Label(text=' Username ', font='Arial 12 bold').grid(row=1, column=1, pady=20, padx=50)
        self.username = Entry()
        self.username.grid(row=1, column=2)

        Label(text=' Password ', font='Arial 12 bold ').grid(row=2, column=1, pady=10, padx=50)
        self.password = Entry(show='*')
        self.password.grid(row=2,column=2)

        ttk.Button(text='Login', command=self.login_user, width="20", ).grid(row=3, column=2, pady=20)


    def login_user(self):
        conn = sqlite3.connect('EmployeeList.db')
        cur = conn.cursor()
        # Thực hiện lênh sql
        cur.execute("SELECT PASSWORD  FROM  ADMIN WHERE USERNAME = ?", (self.username.get(),))
        result = cur.fetchall()

        for attribute in result:
            print(attribute[0])


        conn.commit()

        conn.close()

        '''Check username and password entered are correct'''
        '''self.username.get() == self.user and self.password.get() == self.passw or'''
        if  self.username.get() == self.user1 and self.password.get() == attribute[0]:

            # Destroy the current window
            self.root.destroy()



            # Open new window


            # Display Screen
            root = Tk()
            root.title('Employee Management System - Group 4')
            root.geometry("1000x550")

            # Read config file ColorSources and get colors
            parser = ConfigParser()
            parser.read("ColorSources.ini")
            choose_firstColor = parser.get('color_list', 'firstColor')
            choose_secondColor = parser.get('color_list', 'secondColor')
            choose_highlightColor = parser.get('color_list', 'highlight_color')

            def managedata():

                # Clear report box view
                for attribute in my_reportbox.get_children():
                    my_reportbox.delete(attribute)

                # Create database and connect to
                conn = sqlite3.connect('EmployeeList.db')

                # Create a cursor instance
                cur = conn.cursor()

                # print all data from employee table
                cur.execute("SELECT rowid, * FROM employee")
                result = cur.fetchall()

                # Add data to the screen
                global count
                count = 0

                # print attribute trong khoảng result
                # show data to the table report
                # trong lệnh này còn tag cột chẵn và cột lẻ để fill color
                for attribute in result:
                    if count % 2 == 0:
                        my_reportbox.insert(parent='', index='end', iid=count, text='',
                                            values=(
                                            attribute[1], attribute[2], attribute[0], attribute[4], attribute[5],
                                            attribute[6], attribute[7], attribute[8]),
                                            tags=('evenrow',))
                    else:
                        my_reportbox.insert(parent='', index='end', iid=count, text='',
                                            values=(
                                            attribute[1], attribute[2], attribute[0], attribute[4], attribute[5],
                                            attribute[6], attribute[7], attribute[8]),
                                            tags=('oddrow',))

                    count += 1

                # Commit changes
                conn.commit()

                # Close connection
                conn.close()
            # ====================================== Profile Functions =================================================
            def viewProfile_box():
                global view

                view = Toplevel(root)
                view.title("Admin Profile")
                view.geometry('1000x532')
                bg_color = '#99FFFF'

                # =====================variable=======================
                id_var = IntVar()
                name_var = StringVar()
                gender_var = StringVar()
                email_var = StringVar()
                address_var = StringVar()
                phone_var = StringVar()
                newpass_var = StringVar()
                passenter_var = StringVar()


                # ==================fuction===============

                def update():

                    conn = sqlite3.connect('EmployeeList.db')
                    cur = conn.cursor()

                    cur.execute(
                        "UPDATE adminProfile SET ID = :id, FullName = :name, Gender = :gender, Email = :email, Address = :address, PhoneNumber = :phone ",
                        {
                            'id': id_var.get(),
                            'name': name_var.get().capitalize(),
                            'gender': gender_var.get().capitalize(),
                            'email': email_var.get().capitalize(),
                            'address': address_var.get().capitalize(),
                            'phone': phone_var.get().capitalize(),
                        })

                    if id_var.get() == 0 or name_var.get() == '' or gender_var.get() == ''  or email_var.get() == '' or phone_var.get() == '' or address_var.get() == '':
                        messagebox.showerror('Error', 'All fields are required ?')
                    else:
                        textarea.delete(1.0, END)
                        textarea.insert(END, '\n-------------------------------------------------------------------------------------')
                        textarea.insert(END, f'\nAdmin ID\t\t\t{id_var.get()}')
                        textarea.insert(END, '\n-------------------------------------------------------------------------------------')
                        textarea.insert(END, f'\n\nFull Name\t\t\t{name_var.get()}')
                        textarea.insert(END, f'\n\nGender \t\t\t{gender_var.get()}')
                        textarea.insert(END, f'\n\nEmail\t\t\t{email_var.get()}')
                        textarea.insert(END, f'\n\nContact Number\t\t\t{phone_var.get()}')
                        textarea.insert(END, f'\n\nAddress\t\t\t{address_var.get()}')
                        textarea.insert(END, '\n\n------------------------------------------------------------------------------------')
                        textarea.insert(END, f'\n\nDevelop by ThanhNam\t\t\t')
                    conn.commit()
                    conn.close()

                def show():
                    conn = sqlite3.connect('EmployeeList.db')
                    cur = conn.cursor()


                    # Thực hiện lênh sql
                    cur.execute("SELECT * FROM adminProfile ")
                    showinform = cur.fetchall()
                    for a in showinform:
                        print(a[0])
                        print(a[1])
                        print(a[2])
                        print(a[3])
                        print(a[4])
                        print(a[5])


                    textarea.delete(1.0, END)
                    textarea.insert(END, '\n-----------------------------------------------------------------------------------------')
                    textarea.insert(END, f'\nAdmin ID\t\t\t{a[0]}')
                    textarea.insert(END, '\n-----------------------------------------------------------------------------------------')
                    textarea.insert(END, f'\n\nFull Name\t\t\t{a[1]}')
                    textarea.insert(END, f'\n\nGender \t\t\t{a[2]}')
                    textarea.insert(END, f'\n\nEmail\t\t\t{a[3]}')
                    textarea.insert(END, f'\n\nContact Number\t\t\t{a[5]}')
                    textarea.insert(END, f'\n\nAddress\t\t\t{a[4]}')
                    textarea.insert(END, '\n\n---------------------------------------------------------------------------------------')
                    textarea.insert(END, f'\n\nDevelop by ThanhNam\t\t\t')
                    conn.commit()
                    conn.close()



                def changePass_box():

                    global changeP,Khung

                    changeP = Toplevel(root)
                    changeP.title("Change Password")
                    changeP.geometry('500x318')
                    bg_color = '#FFFF66'

                    title = Label(changeP, text='Change Password', bg=bg_color, fg='black',
                                  font=('Helvetica', 12, 'bold'), relief=GROOVE, bd=12)
                    title.pack(fill=X)

                    Khung = Frame(changeP, bg=bg_color, relief=RIDGE, bd=15)
                    Khung.place(y=48, width=500, height=270)

                    lab_pass = Label(Khung, text='Enter Password', font=('Helvetica', 11, 'bold'), fg='black', bg=bg_color)
                    lab_pass.grid(row=0, column=0, padx=30, pady=10)

                    pass_ent = Entry(Khung, font=('Helvetica', 11, 'bold'), relief=RIDGE, bd=7, textvariable= passenter_var)
                    pass_ent.grid(row=0, column=1, pady=10, sticky='w')

                    new_pass = Label(Khung, text='Enter New Password', font=('Helvetica', 11, 'bold'), fg='black', bg=bg_color)
                    new_pass.grid(row=1, column=0, padx=30, pady=10)
                    newpass_ent = Entry(Khung, font=('Helvetica', 11, 'bold'), relief=RIDGE, bd=7,textvariable= newpass_var)
                    newpass_ent.grid(row=1, column=1, pady=10, sticky='w')
                    # Add button
                    search_button = Button(Khung, text="   Change   ", command=change_password)
                    search_button.grid(row=2, column=1, pady=10, sticky='w')





                def change_password():
                    b_color = '#FFFF66'
                    global messages
                    if passenter_var.get() == '' or newpass_var.get() == '':
                        messages = Label(Khung, text='                                                  ', fg='Red', bg=b_color)
                        messages.grid(row=3, column=1, pady=10, sticky='w')
                        messages = Label(Khung, text='                       ', fg='Red', bg=b_color)
                        messages.grid(row=4, column=1,  sticky='w')
                        # show warning when username or password are not filled
                        messages = Label(Khung,text='Password or New Password are not filled ', fg='Red',bg=b_color)
                        messages.grid(row=3, column=1, pady=10, sticky='w')
                        messages = Label(Khung,text='Please fill it!!', fg='Red',bg=b_color)
                        messages.grid(row=4, column=1, sticky='w')

                    elif passenter_var.get() != attribute[0]:
                        messages = Label(Khung, text='                                                                      ', fg='Red', bg=b_color)
                        messages.grid(row=3, column=1, pady=10, sticky='w')
                        messages = Label(Khung, text='                       ', fg='Red', bg=b_color)
                        messages.grid(row=4, column=1, sticky='w')

                        messages = Label(Khung,text='Wrong Password. Enter Again!!', fg='Red',bg=b_color)
                        messages.grid(row=3, column=1, pady=10, sticky='w')



                    else:
                        conn = sqlite3.connect('EmployeeList.db')
                        cur = conn.cursor()
                        # Thực hiện lênh sql
                        cur.execute(
                            "UPDATE ADMIN SET PASSWORD = :PASSWORD",
                            {
                                'PASSWORD': newpass_var.get(),
                            })
                        messages = Label(Khung, text='                                                                      ', fg='Red', bg=bg_color)
                        messages.grid(row=3, column=1, pady=10, sticky='w')
                        messages = Label(Khung, text='                       ', fg='Red', bg=bg_color)
                        messages.grid(row=4, column=1, sticky='w')
                        messages = Label(Khung,text='Change password successfully', fg='Red',bg=bg_color)
                        messages.grid(row=3, column=1, pady=10, sticky='w')
                        conn.commit()

                        conn.close()

                # =====================Heading=======================
                title = Label(view, text='Admin Profile', bg=bg_color, fg='black',
                              font=('Helvetica', 20, 'bold'), relief=GROOVE, bd=12)
                title.pack(fill=X)

                # ====================left frame details===================
                F1 = Frame(view, bg=bg_color, relief=RIDGE, bd=15)
                F1.place( y=58, width=500, height=400)

                lbl_id = Label(F1, text='Admin ID', font=('Helvetica', 14, 'bold'), fg='black', bg=bg_color)
                lbl_id.grid(row=0, column=0, padx=30, pady=10)
                txt_id = Entry(F1, font=('Helvetica', 12, 'bold'), relief=RIDGE, bd=7, textvariable=id_var)
                txt_id.grid(row=0, column=1, pady=10, sticky='w')

                lbl_name = Label(F1, text='Full Name', font=('Helvetica', 14, 'bold'), fg='black', bg=bg_color)
                lbl_name.grid(row=1, column=0, padx=30, pady=10)
                txt_name = Entry(F1, font=('Helvetica', 12, 'bold'), relief=RIDGE, bd=7, textvariable=name_var)
                txt_name.grid(row=1, column=1, pady=10, sticky='w')

                lbl_email = Label(F1, text='Email', font=('Helvetica', 14, 'bold'), fg='black', bg=bg_color)
                lbl_email.grid(row=2, column=0, padx=30, pady=10)
                txt_email = Entry(F1, font=('Helvetica', 12, 'bold'), relief=RIDGE, bd=7, textvariable=email_var)
                txt_email.grid(row=2, column=1, pady=10, sticky='w')

                lbl_Gender = Label(F1, text='Gender', font=('Helvetica', 14, 'bold'), fg='black', bg=bg_color)
                lbl_Gender.grid(row=3, column=0, padx=30, pady=10)

                combo_gender = ttk.Combobox(F1, font=('Helvetica', 12), state='readonly',
                                            textvariable=gender_var)
                combo_gender['value'] = ('Male', 'Female')
                combo_gender.grid(row=3, column=1, pady=10)

                lbl_phone = Label(F1, text='Phone No.', font=('Helvetica', 14, 'bold'), fg='black', bg=bg_color)
                lbl_phone.grid(row=5, column=0, padx=30, pady=10)
                txt_phone = Entry(F1, font=('Helvetica', 12, 'bold'), relief=RIDGE, bd=7, textvariable=phone_var)
                txt_phone.grid(row=5, column=1, pady=10, sticky='w')

                lbl_add = Label(F1, text='Address', font=('Helvetica', 14, 'bold'), fg='black', bg=bg_color)
                lbl_add.grid(row=6, column=0, padx=30, pady=10)
                txt_add = Entry(F1, font=('Helvetica', 12, 'bold'), relief=RIDGE, bd=7, textvariable=address_var)
                txt_add.grid(row=6, column=1, pady=10, sticky='w')


                # ==========================Right frame================
                F2 = Frame(view, bg=bg_color, relief=RIDGE, bd=15)
                F2.place(x=500, y=58, width=500, height=400)

                lbl_t = Label(F2, text='Admin Details', font=('Helvetica 12 bold'), fg='black', bd=7, relief=GROOVE)
                lbl_t.pack(fill=X)

                scrol = Scrollbar(F2, orient=VERTICAL)
                scrol.pack(side=RIGHT, fill=Y)
                textarea = Text(F2, font='Helvetica 12', yscrollcommand=scrol.set)
                textarea.pack(fill=BOTH)
                scrol.config(command=textarea.yview)

                # ===================Buttons=================
                F3 = Frame(view, bg=bg_color, relief=RIDGE, bd=15)
                F3.place( y=448, width=1000, height=90)

                btn1 = Button(F3, text=' Update ', font='Helvetica 13 bold', bg='yellow', fg='crimson', width=10,
                              command=update)
                btn1.grid(row=0, column=4, padx=30, pady=7)

                btn2 = Button(F3, text=' Show ', font='Helvetica 13 bold', bg='yellow', fg='crimson', width=10, command=show)
                btn2.grid(row=0, column=3, padx=30, pady=7)

                btn3 = Button(F3, text='Change Password', font='arial 13 bold', bg='yellow', fg='crimson', width=15,
                              command=changePass_box)
                btn3.grid(row=0, column=2, padx=30, pady=7)

                '''btn4 = Button(F3, text='Reset', font='arial 20 bold', bg='yellow', fg='crimson', width=10,
                              command=reset)
                btn4.grid(row=0, column=3, padx=25, pady=7)

                btn5 = Button(F3, text='Exit', font='arial 20 bold', bg='yellow', fg='crimson', width=10, command=Exit)
                btn5.grid(row=0, column=4, padx=25, pady=7)'''




            # ====================================== Search Functions ==================================================

            # Search First Name
            def search_date():
                find_date = search_enter.get()

                # close search box
                search.destroy()

                # Clear report box view
                for attribute in my_reportbox.get_children():
                    my_reportbox.delete(attribute)

                # Connect to database
                conn = sqlite3.connect('EmployeeList.db')
                cur = conn.cursor()

                # Thực hiện lênh sql
                cur.execute("SELECT rowid, * FROM employee WHERE date like ?", ('%'+find_date+'%',))

                # print out
                result = cur.fetchall()

                global count
                count = 0

                # print out attribute in range result
                for attribute in result:
                    if count % 2 == 0:
                        my_reportbox.insert(parent='', index='end', iid=count, text='',
                                            values=(
                                            attribute[1], attribute[2], attribute[0], attribute[4], attribute[5],
                                            attribute[6], attribute[7], attribute[8]),
                                            tags=('evenrow',))
                    else:
                        my_reportbox.insert(parent='', index='end', iid=count, text='',
                                            values=(
                                            attribute[1], attribute[2], attribute[0], attribute[4], attribute[5],
                                            attribute[6], attribute[7], attribute[8]),
                                            tags=('oddrow',))

                    count += 1
                conn.commit()
                conn.close()

            # Search Last Name
            def search_name():
                find_name = search_enter.get()

                # close search box
                search.destroy()

                # Clear report box view
                for attribute in my_reportbox.get_children():
                    my_reportbox.delete(attribute)

                # Connect to database
                conn = sqlite3.connect('EmployeeList.db')
                cur = conn.cursor()

                # Thực hiện lênh sql
                cur.execute("SELECT rowid, * FROM employee WHERE name like ?", ('%' + find_name + '%',))

                # print out
                result = cur.fetchall()

                global count
                count = 0

                # print out (attribute) in range result
                for attribute in result:
                    if count % 2 == 0:
                        my_reportbox.insert(parent='', index='end', iid=count, text='',
                                            values=(
                                            attribute[1], attribute[2], attribute[0], attribute[4], attribute[5],
                                            attribute[6], attribute[7], attribute[8]),
                                            tags=('evenrow',))
                    else:
                        my_reportbox.insert(parent='', index='end', iid=count, text='',
                                            values=(
                                            attribute[1], attribute[2], attribute[0], attribute[4], attribute[5],
                                            attribute[6], attribute[7], attribute[8]),
                                            tags=('oddrow',))

                    count += 1
                conn.commit()
                conn.close()

            # Search Position
            def search_position():
                find_position = search_enter.get()

                # close search box
                search_box.destroy()

                # Clear report box view
                for attribute in my_reportbox.get_children():
                    my_reportbox.delete(attribute)

                # Connect to database
                conn = sqlite3.connect('EmployeeList.db')
                cur = conn.cursor()

                # Thực hiện lênh sql
                cur.execute("SELECT rowid, * FROM employee WHERE position like ?", ('%'+find_position + '%',))

                # print out
                result = cur.fetchall()

                global count
                count = 0

                # print out (attribute) in range result
                for attribute in result:
                    if count % 2 == 0:
                        my_reportbox.insert(parent='', index='end', iid=count, text='',
                                            values=(
                                            attribute[1], attribute[2], attribute[0], attribute[4], attribute[5],
                                            attribute[6], attribute[7], attribute[8]),
                                            tags=('evenrow',))
                    else:
                        my_reportbox.insert(parent='', index='end', iid=count, text='',
                                            values=(
                                            attribute[1], attribute[2], attribute[0], attribute[4], attribute[5],
                                            attribute[6], attribute[7], attribute[8]),
                                            tags=('oddrow',))

                    count += 1
                conn.commit()
                conn.close()

            def search_address():
                find_address = search_enter.get()

                # close search box
                search_box.destroy()

                # Clear report box view
                for attribute in my_reportbox.get_children():
                    my_reportbox.delete(attribute)

                # Connect to database
                conn = sqlite3.connect('EmployeeList.db')
                cur = conn.cursor()

                # Thực hiện lênh sql
                cur.execute("SELECT rowid, * FROM employee WHERE address LIKE ?", ('%' + find_address + '%',))

                # print out
                result = cur.fetchall()

                global count
                count = 0

                # print out (attribute) in range result
                for attribute in result:
                    if count % 2 == 0:
                        my_reportbox.insert(parent='', index='end', iid=count, text='',
                                            values=(
                                            attribute[1], attribute[2], attribute[0], attribute[4], attribute[5],
                                            attribute[6], attribute[7], attribute[8]),
                                            tags=('evenrow',))
                    else:
                        my_reportbox.insert(parent='', index='end', iid=count, text='',
                                            values=(
                                            attribute[1], attribute[2], attribute[0], attribute[4], attribute[5],
                                            attribute[6], attribute[7], attribute[8]),
                                            tags=('oddrow',))

                    count += 1
                conn.commit()
                conn.close()
                # Search Empcode

            def search_empcode():
                find_empcode = search_enter.get()

                # close search box
                search_box.destroy()

                # Clear report box view
                for attribute in my_reportbox.get_children():
                        my_reportbox.delete(attribute)

                # Connect to database
                conn = sqlite3.connect('EmployeeList.db')
                cur = conn.cursor()

                # Thực hiện lênh sql
                cur.execute("SELECT rowid, * FROM employee WHERE phone_no LIKE ?", (find_empcode,))

                # print out
                result = cur.fetchall()

                global count
                count = 0

                # print out (attribute) in range result
                for attribute in result:
                    if count % 2 == 0:
                            my_reportbox.insert(parent='', index='end', iid=count, text='',
                                                values=(
                                                    attribute[1], attribute[2], attribute[0], attribute[4],
                                                    attribute[5],
                                                    attribute[6], attribute[7], attribute[8]),
                                                tags=('evenrow',))
                    else:
                            my_reportbox.insert(parent='', index='end', iid=count, text='',
                                                values=(
                                                    attribute[1], attribute[2], attribute[0], attribute[4],
                                                    attribute[5],
                                                    attribute[6], attribute[7], attribute[8]),
                                                tags=('oddrow',))

                    count += 1
                conn.commit()
                conn.close()

            # Search First Name Box
            def searchDate_box():
                global search_enter, search

                search = Toplevel(root)
                search.title("Search Date")
                search.geometry("380x180")

                # Create label frame cho cửa số search
                search_frame = LabelFrame(search, text="Enter Date")
                search_frame.pack(padx=10, pady=10)

                # Add enter box
                search_enter = Entry(search_frame, font=("Arial", 19))
                search_enter.pack(pady=20, padx=20)

                # Add button
                search_button = Button(search, text="   Search   ", command=search_date)
                search_button.pack(padx=10, pady=10)

            # Search Last Name Box
            def searchName_box():
                global search_enter, search

                search = Toplevel(root)
                search.title("Search Name")
                search.geometry("380x180")

                # Create label frame cho cửa số search
                search_frame = LabelFrame(search, text="Enter Name")
                search_frame.pack(padx=10, pady=10)

                # Add enter box
                search_enter = Entry(search_frame, font=("Arial", 18))
                search_enter.pack(pady=20, padx=20)

                # Add button
                search_button = Button(search, text="   Search   ", command=search_name)
                search_button.pack(padx=10, pady=10)

            # Search Position Box
            def searchPosition_box():
                global search_enter, search_box

                search_box = Toplevel(root)
                search_box.title("Search Position")
                search_box.geometry("380x180")

                # Create label frame cho cửa số search
                search_frame = LabelFrame(search_box, text="Enter Position")
                search_frame.pack(padx=10, pady=10)

                # Add enter box
                search_enter = Entry(search_frame, font=("Arial", 18))
                search_enter.pack(pady=20, padx=20)

                # Add button
                search_button = Button(search_box, text="   Search   ", command=search_position)
                search_button.pack(padx=10, pady=10)

            def searchAddress_box():
                global search_enter, search_box

                search_box = Toplevel(root)
                search_box.title("Search Address")
                search_box.geometry("380x180")

                # Create label frame cho cửa số search
                search_frame = LabelFrame(search_box, text="Enter Address")
                search_frame.pack(padx=10, pady=10)

                # Add enter box
                search_enter = Entry(search_frame, font=("Arial", 18))
                search_enter.pack(pady=20, padx=20)

                # Add button
                search_button = Button(search_box, text="   Search   ", command=search_address)
                search_button.pack(padx=10, pady=10)

            def searchEmpcode_box():
                global search_enter, search_box

                search_box = Toplevel(root)
                search_box.title("Search Employee Code")
                search_box.geometry("380x180")

                # Create label frame cho cửa số search
                search_frame = LabelFrame(search_box, text="Enter EmpCode")
                search_frame.pack(padx=10, pady=10)

                # Add enter box
                search_enter = Entry(search_frame, font=("Arial", 18))
                search_enter.pack(pady=20, padx=20)

                # Add button
                search_button = Button(search_box, text="   Search   ", command=search_empcode)
                search_button.pack(padx=10, pady=10)

            # =================================== Color Function =============================================
            # set up firstColor( color in odd row)
            def firstColor():
                # Pick Color
                firstColor = colorchooser.askcolor()[1]

                # Update report box view Color
                if firstColor:
                    # Create Striped Row Tags
                    my_reportbox.tag_configure('evenrow', background=firstColor)

                    # Config file
                    parser = ConfigParser()
                    parser.read("ColorSources.ini")
                    # Set the color change
                    parser.set('color_list', 'firstColor', firstColor)
                    # Save the config file
                    with open('ColorSources.ini', 'w') as configfile:
                        parser.write(configfile)

            # set up second color (color in even row)
            def secondColor():
                # Pick Color
                secondColor = colorchooser.askcolor()[1]

                # Update color Treeview
                if secondColor:
                    # Create Striped Row Tags
                    my_reportbox.tag_configure('oddrow', background=secondColor)

                    # Config file
                    parser = ConfigParser()
                    parser.read("ColorSources.ini")
                    # Set the color change
                    parser.set('color_list', 'secondary_color', secondColor)
                    # Save the config file
                    with open('ColorSources.ini', 'w') as configfile:
                        parser.write(configfile)

            # set up highlight color (color you tick in row)
            def highlight_color():
                # Choose Color
                highlight_color = colorchooser.askcolor()[1]

                # Change Selected Color
                if highlight_color:
                    style.map('Treeview', background=[('selected', highlight_color)])

                    # Config file
                    parser = ConfigParser()
                    parser.read("ColorSources.ini")
                    # Set the color change
                    parser.set('color_list', 'highlight_color', highlight_color)
                    # Save the config file
                    with open('ColorSources.ini', 'w') as configfile:
                        parser.write(configfile)

            # làm màu trở về màu mặc định
            def reset_color():
                # Save original colors to config file
                parser = ConfigParser()
                parser.read('ColorSources.ini')
                parser.set('color_list', 'firstColor', '#F1F1F2')  # Overcast Color
                parser.set('color_list', 'secondColor', '#B2DBD5')  # Arctic Color
                parser.set('color_list', 'highlight_color', '#2B616D')  # Dark teal Color
                with open('ColorSources.ini', 'w') as configfile:
                    parser.write(configfile)
                # Reset the colors
                my_reportbox.tag_configure('oddrow', background='#B2DBD5')
                my_reportbox.tag_configure('evenrow', background='#F1F1F2')
                style.map('Treeview',
                          background=[('selected', '#347083')])


            # =================================== Rank Function ======================================

            def rank_salary():
                # Clear report box view
                for attribute in my_reportbox.get_children():
                    my_reportbox.delete(attribute)

                # Connect to database
                conn = sqlite3.connect('EmployeeList.db')
                cur = conn.cursor()
                # Thực hiện lênh sql
                cur.execute("SELECT rowid, *  FROM  employee ORDER BY salary DESC LIMIT 5 ", ())
                # Thực hiện lênh sql

                # print out
                result = cur.fetchall()

                global count
                count = 0

                # print out attribute in range result
                for attribute in result:
                    if count % 2 == 0:
                        my_reportbox.insert(parent='', index='end', iid=count, text='',
                                            values=(
                                                attribute[1], attribute[2], attribute[0], attribute[4], attribute[5],
                                                attribute[6],
                                                attribute[7], attribute[8]),
                                            tags=('evenrow',))
                    else:
                        my_reportbox.insert(parent='', index='end', iid=count, text='',
                                            values=(
                                                attribute[1], attribute[2], attribute[0], attribute[4], attribute[5],
                                                attribute[6],
                                                attribute[7], attribute[8]),
                                            tags=('oddrow',))

                    count += 1
                conn.commit()
                conn.close()


            def salary_management():
                global sala_manage
                sala_manage = Toplevel(root)
                sala_manage.title('Salary Management')
                sala_manage.geometry('1060x605')
                bg_color = '#2D9290'

                # =====================variables===================

                Overtime = IntVar()
                Bonus = StringVar()
                salaryEmp = StringVar()
                Total = IntVar()

                sala_ot = StringVar()
                sala_bonus = StringVar()
                sala_emp = StringVar()
                year_sala = StringVar()
                allowance = StringVar()



                total_salary = StringVar()

                # ===========Function===============

                def cal_Wages():

                    if Overtime.get() == 0 and salaryEmp.get() == '':
                        messagebox.showerror('Error', 'Fill out all the information, please!')
                    else:
                        conn = sqlite3.connect('EmployeeList.db')
                        cur = conn.cursor()

                        # Thực hiện lênh sql
                        cur.execute("SELECT position FROM employee WHERE phone_no = ?", (salaryEmp.get(),))

                        # print out
                        result = cur.fetchall()
                        for a in result:
                            print(a[0])

                        if a[0] == "Project manager":
                            sal_bonus = 1.5
                        elif a[0] == "Business analyst":
                            sal_bonus = 1.2
                        elif a[0] == "Tester":
                            sal_bonus = 1.0
                        elif a[0] == "Developer":
                            sal_bonus = 0.9
                        elif a[0] == "Designer":
                            sal_bonus = 1.1

                        conn.commit()
                        conn.close()

                        conn = sqlite3.connect('EmployeeList.db')
                        cur = conn.cursor()
                        # Thực hiện lênh sql
                        cur.execute("SELECT salary  FROM  employee WHERE phone_no = ?  ", (salaryEmp.get(),))
                        result = cur.fetchall()

                        for attribute in result:
                            print(attribute[0])


                        o = Overtime.get()
                        b = float(sal_bonus)
                        allow = float(950)
                        luong = int(attribute[0])


                        t = float(o * 10 + luong * b + allow)
                        est = float(t * 12)

                        Total.set(o)
                        total_salary.set('$ ' + str(t))
                        sala_ot.set('$ ' + str(o * 10))
                        sala_bonus.set(str(b))
                        sala_emp.set('$ ' + str(luong))
                        year_sala.set('$ ' + str(est))
                        allowance.set('$ ' + str(allow))

                        conn.commit()
                        conn.close()

                def export_bill():
                    conn = sqlite3.connect('EmployeeList.db')
                    cur = conn.cursor()
                    # Thực hiện lênh sql
                    cur.execute("SELECT name  FROM  employee WHERE phone_no = ?", (salaryEmp.get(),))
                    result = cur.fetchall()

                    for attribute in result:
                        print(attribute[0])

                    textarea.delete(1.0, END)
                    textarea.insert(END, f'\nEmployee Name:\t {attribute[0]}')
                    textarea.insert(END, f'\n\nEmployee Code:\t {salaryEmp.get()}')
                    textarea.insert(END, ' \n\nItems\t\t      \t    Salary\n')
                    textarea.insert(END, '===================================')
                    textarea.insert(END, f'\nEmployee Salary\t\t\t   {sala_emp.get()}')
                    textarea.insert(END, f'\n\nCoefficients\t\t\t   {sala_bonus.get()}')
                    textarea.insert(END, f'\n\nAllowance\t\t\t   {allowance.get()}')
                    textarea.insert(END, f'\n\nOvertime({Overtime.get()} hours)\t\t\t   {sala_ot.get()}')
                    textarea.insert(END, f"\n\n===================================")
                    textarea.insert(END, f'\nTotal Salary\t\t                \t  {total_salary.get()}')
                    textarea.insert(END, f'\n\nSalary Estimate (1 year)\t\t         \t  {year_sala.get()}')
                    textarea.insert(END, f"\n===================================")

                    conn.commit()
                    conn.close()

                def export_txt():
                    q = textarea.get('1.0', 'end-1c')
                    filename = tempfile.mktemp('.txt')
                    open(filename, 'w').write(q)
                    os.startfile(filename, 'Print')

                def clear_entry():
                    textarea.delete(1.0, END)
                    Overtime.set('')
                    Bonus.set('')
                    salaryEmp.set('')
                    Total.set(0)
                    sala_ot.set('')
                    sala_bonus.set('')
                    sala_emp.set('')

                    total_salary.set('')

                def out():
                    if messagebox.askyesno('Exit', 'Do you really want to exit'):
                        sala_manage.destroy()

                title = Label(sala_manage, pady=5, text="Salary Management", bd=12, bg=bg_color, fg='white',
                              font=('Helvetica', 20, 'bold'), relief=GROOVE, justify=CENTER)
                title.pack(fill=X)



                # ===============Product Details=================
                F1 = LabelFrame(sala_manage, text='Salary Details', font=('Helvetica', 15, 'bold'), fg='gold', bg=bg_color,
                                bd=15, relief=RIDGE)
                F1.place(y=70, width=698, height=450)

                # =====================Heading==========================


                # row 0

                note = Label(F1, text='Note: 1h OT = $10', font=('Helvetica', 10, 'bold', 'underline'), fg='#F3CA11',
                          bg=bg_color)
                note.grid(row=2, column=1, padx=30, pady=15)

                # row1

                ec = Label(F1, text='Employee Code (*)', font=('Helvetica', 10, 'bold'), fg='black', bg=bg_color)
                ec.grid(row=0, column=0, padx=10, pady=10)
                ec_enter = Entry(F1, font='Helvetica 10 bold', relief=SUNKEN, bd=7, textvariable=salaryEmp,
                                 justify=CENTER)
                ec_enter.grid(row=0, column=1, padx=10, pady=10)

                Emp_S= Label(F1, text='Basic Salary', font=('Helvetica', 10, 'bold'), fg='black', bg=bg_color)
                Emp_S.grid(row=0, column=2, padx=10, pady=10)

                Es_txt = Entry(F1, font='Helvetica 10 bold', relief=SUNKEN, bd=7, textvariable=sala_emp,
                               justify=CENTER)
                Es_txt.grid(row=0, column=3, padx=10, pady=10)

                # row 2
                '''bn = Label(F1, text='Bonus (*)', font=('Helvetica', 10, 'bold'), fg='black', bg=bg_color)
                bn.grid(row=2, column=0, padx=10, pady=10)

                bn_txt = Entry(F1, font='Helvetica 10 bold', relief=SUNKEN, bd=7, textvariable=Bonus,
                               justify=CENTER)
                bn_txt.grid(row=2, column=1, padx=10, pady=10)'''




                Bon_S = Label(F1, text='Coefficients Salary', font=('Helvetica', 10, 'bold'), fg='black', bg=bg_color)
                Bon_S.grid(row=1, column=2, padx=10, pady=10)

                Es_txt = Entry(F1, font='Helvetica 10 bold', relief=SUNKEN, bd=7, textvariable=sala_bonus,
                               justify=CENTER)
                Es_txt.grid(row=1, column=3, padx=10, pady=10)

                Allow_S = Label(F1, text='Allowance', font=('Helvetica', 10, 'bold'), fg='black', bg=bg_color)
                Allow_S.grid(row=2, column=2, padx=10, pady=10)

                allow_txt = Entry(F1, font='Helvetica 10 bold', relief=SUNKEN, bd=7, textvariable=allowance,
                               justify=CENTER)
                allow_txt.grid(row=2, column=3, padx=10, pady=10)

                # row 3
                oth = Label(F1, text='OverTime Hours (*)', font=('Helvetica', 10, 'bold'), fg='black', bg=bg_color)
                oth.grid(row=3, column=0, padx=10, pady=10)

                oth_txt = Entry(F1, font='Helvetica 10 bold', relief=SUNKEN, bd=7, textvariable=Overtime,
                               justify=CENTER)
                oth_txt.grid(row=3, column=1, padx=10, pady=10)

                ot_S = Label(F1, text='OverTime Salary', font=('Helvetica', 10, 'bold'), fg='black', bg=bg_color)
                ot_S.grid(row=3, column=2, padx=10, pady=10)

                ot_txt = Entry(F1, font='Helvetica 10 bold', relief=SUNKEN, bd=7, textvariable=sala_ot,
                               justify=CENTER)
                ot_txt.grid(row=3, column=3, padx=10, pady=10)

                chia = Label(F1,  text='================', fg='black', bg=bg_color)
                chia.grid(row=4, column=0, padx=5, pady=10)
                chia1 = Label(F1, text='================', fg='black', bg=bg_color)
                chia1.grid(row=4, column=1, padx=5, pady=10)
                chia2 = Label(F1, text='================', fg='black', bg=bg_color)
                chia2.grid(row=4, column=2, padx=5, pady=10)
                chia3 = Label(F1, text='================', fg='black', bg=bg_color)
                chia3.grid(row=4, column=3, padx=5, pady=10)

                al = Label(F1, text='Total', font=('Helvetica', 10, 'bold'), fg='Black', bg=bg_color)
                al.grid(row=5, column=2, padx=10, pady=10)
                total_salary_txt = Entry(F1, font='Helvetica 10 bold', relief=SUNKEN, bd=7, textvariable=total_salary,
                                      justify=CENTER)
                total_salary_txt.grid(row=5, column=3, padx=10, pady=10)

                esti = Label(F1, text='Salary Estimate (1 year)', font=('Helvetica', 10, 'bold'), fg='Black', bg=bg_color)
                esti.grid(row=6, column=2, padx=10, pady=10)
                es_salary_txt = Entry(F1, font='Helvetica 10 bold', relief=SUNKEN, bd=7, textvariable=year_sala,
                                         justify=CENTER)
                es_salary_txt.grid(row=6, column=3, padx=10, pady=10)



                # =====================Bill area====================
                F2 = Frame(sala_manage, relief=GROOVE, bd=10)
                F2.place(x=699, y=70, width=360, height=450)
                titleF2 = Label(F2, text='Receipt', font='Helvetica 14 bold', bd=7, relief=GROOVE).pack(fill=X)
                scrol_y = Scrollbar(F2, orient=VERTICAL)
                scrol_y.pack(side=RIGHT, fill=Y)
                textarea = Text(F2, font='arial 12', yscrollcommand=scrol_y.set)
                textarea.pack(fill=BOTH)
                scrol_y.config(command=textarea.yview)

                # =====================Buttons========================
                F3 = Frame(sala_manage, bg=bg_color, bd=15, relief=RIDGE)
                F3.place(y=520, width=1060, height=90)


                btn1 = Button(F3, text='Calculation', font='Helvetica 12 bold', padx=5, pady=5, bg='yellow', fg='red',
                              width=10, command=cal_Wages)
                btn1.grid(row=0, column=0, padx=30, pady=10)

                btn2 = Button(F3, text='Receipt', font='Helvetica 12 bold', padx=5, pady=5, bg='yellow', fg='red',
                              width=10, command=export_bill)
                btn2.grid(row=0, column=1, padx=30, pady=10)

                btn3 = Button(F3, text='Print', font='Helvetica 12 bold', padx=5, pady=5, bg='yellow', fg='red',
                              width=10, command=export_txt)
                btn3.grid(row=0, column=2, padx=30, pady=10)

                btn4 = Button(F3, text='Reset', font='Helvetica 12 bold', padx=5, pady=5, bg='yellow', fg='red',
                              width=10, command=clear_entry)
                btn4.grid(row=0, column=3, padx=30, pady=10)

                btn5 = Button(F3, text='Exit', font='Helvetica 12 bold', padx=5, pady=5, bg='yellow', fg='red',
                              width=10, command=out)
                btn5.grid(row=0, column=4, padx=30, pady=10)




            # =================================== Filter Function ======================================

            def filter_male():
                # Clear report box view
                for attribute in my_reportbox.get_children():
                    my_reportbox.delete(attribute)

                # Connect to database
                conn = sqlite3.connect('EmployeeList.db')
                cur = conn.cursor()
                # Execute sql query
                cur.execute("SELECT rowid, *  FROM  employee WHERE gender= 'Male' OR gender =  'male'  ", ())
                # Thực hiện lênh sql

                # print out
                result = cur.fetchall()

                global count
                count = 0

                # print out attribute in range result
                for attribute in result:
                    if count % 2 == 0:
                        my_reportbox.insert(parent='', index='end', iid=count, text='',
                                            values=(
                                                attribute[1], attribute[2], attribute[0], attribute[4], attribute[5],
                                                attribute[6],
                                                attribute[7], attribute[8]),
                                            tags=('evenrow',))
                    else:
                        my_reportbox.insert(parent='', index='end', iid=count, text='',
                                            values=(
                                                attribute[1], attribute[2], attribute[0], attribute[4], attribute[5],
                                                attribute[6],
                                                attribute[7], attribute[8]),
                                            tags=('oddrow',))

                    count += 1
                conn.commit()
                conn.close()

            def filter_female():
                # Clear report box view
                for attribute in my_reportbox.get_children():
                    my_reportbox.delete(attribute)

                # Connect to database
                conn = sqlite3.connect('EmployeeList.db')
                cur = conn.cursor()
                # Execute sql query
                cur.execute("SELECT rowid, *  FROM  employee WHERE gender= 'Female' OR gender = 'female' ", ())
                # Thực hiện lênh sql

                # print out
                result = cur.fetchall()

                global count
                count = 0

                # print out attribute in range result
                for attribute in result:
                    if count % 2 == 0:
                        my_reportbox.insert(parent='', index='end', iid=count, text='',
                                            values=(
                                                attribute[1], attribute[2], attribute[0], attribute[4], attribute[5],
                                                attribute[6],
                                                attribute[7], attribute[8]),
                                            tags=('evenrow',))
                    else:
                        my_reportbox.insert(parent='', index='end', iid=count, text='',
                                            values=(
                                                attribute[1], attribute[2], attribute[0], attribute[4], attribute[5],
                                                attribute[6],
                                                attribute[7], attribute[8]),
                                            tags=('oddrow',))

                    count += 1
                conn.commit()
                conn.close()

            # ================================== Menu ================================================
            # Add Menu
            my_menu = Menu(root)
            root.config(menu=my_menu)

            # Profile menu
            pro_menu = Menu(my_menu, tearoff=0)
            my_menu.add_cascade(label=" Profile Admin ", menu=pro_menu)

            # Commands in Profile Menu
            pro_menu.add_command(label=" View & Edit", command=viewProfile_box)

            # Configure menu
            optColor_menu = Menu(my_menu, tearoff=0)
            my_menu.add_cascade(label=" Color Options ", menu=optColor_menu)

            # Commands in Option Color Menu
            optColor_menu.add_command(label="First Color", command=firstColor)
            optColor_menu.add_command(label="Second Color", command=secondColor)
            optColor_menu.add_command(label="Highlight Color", command=highlight_color)
            optColor_menu.add_separator()  # help chia ô cho từng phần
            optColor_menu.add_command(label="Reset Colors", command=reset_color)

            # Search Menu
            search_menu = Menu(my_menu, tearoff=0)
            my_menu.add_cascade(label=" Search ", menu=search_menu)
            # Commands in Search Menu
            search_menu.add_command(label="Search by Date", command=searchDate_box)
            search_menu.add_command(label="Search by Name", command=searchName_box)
            search_menu.add_command(label="Search by Position", command=searchPosition_box)
            search_menu.add_command(label="Search by  Address", command=searchAddress_box)
            search_menu.add_command(label="Search by  Empcode", command=searchEmpcode_box)
            search_menu.add_separator()  # help chia ô cho từng phần
            search_menu.add_command(label="Reset", command=managedata)


            # Salary Management Menu
            sm_menu = Menu(my_menu, tearoff=0)
            my_menu.add_cascade(label=" Salary Management ", menu=sm_menu)
            # Commands in Rank Menu
            sm_menu.add_command(label="Top 5 highest salary", command=rank_salary)
            sm_menu.add_command(label="Calculation of wages", command=salary_management)

            sm_menu.add_separator()
            sm_menu.add_command(label="Reset", command=managedata)

            # Filter Menu
            filter_menu = Menu(my_menu, tearoff=0)
            my_menu.add_cascade(label=" Filter ", menu=filter_menu)
            # Commands in Filter Menu
            filter_menu.add_command(label="Male", command=filter_male)
            filter_menu.add_command(label="Female", command=filter_female)
            filter_menu.add_separator()
            filter_menu.add_command(label="Reset", command=managedata)

            # Exit Menu
            exit_menu = Menu(my_menu, tearoff=0)
            my_menu.add_cascade(label=" Exit ", menu=exit_menu)
            # Command in Exit menu
            exit_menu.add_command(label="Exit", command=root.quit)

            # =================================== Report Box =========================================

            # Do some database stuff
            # Connect to database
            conn = sqlite3.connect('EmployeeList.db')

            # Create a cursor instance
            cur = conn.cursor()

            # Create Table
            cur.execute(
                "CREATE TABLE if not exists employee (date text, name text, id integer, gender text, address text, position text, salary real, phone_no integer) ")

            # Commit changes
            conn.commit()

            # Close connection
            conn.close()

            # Add Some Style
            style = ttk.Style()

            # Choose A Theme
            style.theme_use('default')

            # Configure the Treeview Colors
            style.configure("Treeview", rowheight=30, fieldbackground="#99AAB5")

            # Change Selected Color
            style.map('Treeview', background=[('selected', choose_highlightColor)])

            # Create Report Box Frame
            tree_frame = Frame(root)
            tree_frame.pack(pady=10)

            # Create scrollbar for ReportBox
            scroll = Scrollbar(tree_frame)
            scroll.pack(side=RIGHT, fill=Y)

            # Create ReportBox
            my_reportbox = ttk.Treeview(tree_frame, yscrollcommand=scroll.set, selectmode="extended")
            my_reportbox.pack()

            # Configure Scrollbar
            scroll.config(command=my_reportbox.yview)

            # Define Columns
            my_reportbox['columns'] = ("Start Date", "Full Name", "ID", "Gender", "Address", "Position", "Salary", "Phone No")

            # Format Our Columns
            my_reportbox.column("#0", width=0, stretch=NO)
            my_reportbox.column("Start Date", anchor=CENTER, width=100)
            my_reportbox.column("Full Name", anchor=CENTER, width=150)
            my_reportbox.column("ID", anchor=CENTER, width=60)
            my_reportbox.column("Gender", anchor=CENTER, width=90)
            my_reportbox.column("Address", anchor=CENTER, width=140)
            my_reportbox.column("Position", anchor=CENTER, width=140)
            my_reportbox.column("Salary", anchor=CENTER, width=140)
            my_reportbox.column("Phone No", anchor=CENTER, width=100)

            # Create Headings
            my_reportbox.heading("#0", text="", anchor=W)
            my_reportbox.heading("Start Date", text="Start Date", anchor=CENTER)
            my_reportbox.heading("Full Name", text="Full Name", anchor=CENTER)
            my_reportbox.heading("ID", text="No", anchor=CENTER)
            my_reportbox.heading("Gender", text="Gender", anchor=CENTER)
            my_reportbox.heading("Address", text="Address", anchor=CENTER)
            my_reportbox.heading("Position", text="Position", anchor=CENTER)
            my_reportbox.heading("Salary", text="Salary/Month ($)", anchor=CENTER)
            my_reportbox.heading("Phone No", text="EmpCode", anchor=CENTER)

            # Create Striped Row Tags
            my_reportbox.tag_configure('oddrow', background=choose_secondColor)
            my_reportbox.tag_configure('evenrow', background=choose_firstColor)

            # ===================================== ENTER BOXES ========================================
            # Add Attribute Entry Boxes
            att_frame = LabelFrame(root, text="Attribute")
            att_frame.pack(fill="x", expand="yes", padx=20)

            date_label = Label(att_frame, text="Start Date")
            date_label.grid(row=0, column=0, padx=10, pady=10)
            date_enter = Entry(att_frame)
            date_enter.grid(row=0, column=1, padx=10, pady=10)

            name_label = Label(att_frame, text="Full Name")
            name_label.grid(row=0, column=2, padx=10, pady=10)
            name_enter = Entry(att_frame)
            name_enter.grid(row=0, column=3, padx=10, pady=10)

            # Id auto fill nên không cần có box enter
            id_entry = Entry()

            gender_label = Label(att_frame, text="Gender")
            gender_label.grid(row=0, column=4, padx=10, pady=10)
            gender_enter = Entry(att_frame)
            gender_enter.grid(row=0, column=5, padx=10, pady=10)


            address_label = Label(att_frame, text="Address")
            address_label.grid(row=1, column=0, padx=10, pady=10)
            address_enter = Entry(att_frame)
            address_enter.grid(row=1, column=1, padx=10, pady=10)

            position_label = Label(att_frame, text="Position")
            position_label.grid(row=1, column=2, padx=10, pady=10)
            position_enter = Entry(att_frame)
            position_enter.grid(row=1, column=3, padx=10, pady=10)

            salary_label = Label(att_frame, text="Salary ($)")
            salary_label.grid(row=1, column=4, padx=10, pady=10)
            salary_enter = Entry(att_frame)
            salary_enter.grid(row=1, column=5, padx=10, pady=10)

            pn_label = Label(att_frame, text="Employee Code")
            pn_label.grid(row=1, column=6, padx=10, pady=10)
            pn_enter = Entry(att_frame)
            pn_enter.grid(row=1, column=7, padx=10, pady=10)

            # ================================== Commands Functions ====================================

            # Move Up the Row
            def up():
                r = my_reportbox.selection()
                for row in r:
                    my_reportbox.move(row, my_reportbox.parent(row), my_reportbox.index(row) - 1)

            # Move Down the Row
            def down():
                r = my_reportbox.selection()
                for row in reversed(r):
                    my_reportbox.move(row, my_reportbox.parent(row), my_reportbox.index(row) + 1)

            # Remove one employee
            def removeOne_selected():
                x = my_reportbox.selection()[0]
                my_reportbox.delete(x)

                # Connect database
                conn = sqlite3.connect('EmployeeList.db')
                cur = conn.cursor()

                # Delete From Database
                cur.execute("DELETE from employee WHERE oid=" + id_entry.get())

                # Commit changes
                conn.commit()

                # Close connection database
                conn.close()
                clear_enterBox()

                # message box show Notification
                messagebox.showinfo("Deleted", "Successfully deleted")

            # Remove Many Employee
            def removeMany_emp():
                # Add message box question yes no
                notification = messagebox.askyesno("DELETE MANY EMPLOYEE","Are you sure to DELETE employee who you selected ?!")

                # Add logic for message box
                if notification == 1:
                    # Designate selections
                    x = my_reportbox.selection()

                    # Create List of ID
                    ids_to_delete = []

                    # Add selections to ids_to_delete list
                    for attribute in x:
                        ids_to_delete.append(my_reportbox.item(attribute, 'values')[2])

                    # Delete From Report Box
                    for attribute in x:
                        my_reportbox.delete(attribute)

                    conn = sqlite3.connect('EmployeeList.db')
                    cur = conn.cursor()

                    # Delete Employee who you selected
                    cur.executemany("DELETE FROM employee WHERE id = ?", [(a,) for a in ids_to_delete])

                    # Reset List
                    ids_to_delete = []

                    conn.commit()
                    conn.close()

                    # Clear enter boxes if filled
                    clear_enterBox()

            # Remove All employee
            def removeAll_emp():

                # Create message box
                response = messagebox.askyesno("Delete All Employee", "Are you sure to DELETE ALL EMPLOYEE ?!")

                if response == 1:
                    for attribute in my_reportbox.get_children():
                        my_reportbox.delete(attribute)

                    # Connect to database
                    conn = sqlite3.connect('EmployeeList.db')

                    # Create a cursor instance
                    cur = conn.cursor()

                    # Delete Table (xóa bảng là xóa tất cả data trong bảng)
                    cur.execute("DROP TABLE employee")

                    # Commit changes
                    conn.commit()

                    # Close our connection
                    conn.close()

                    # Clear entry boxes if filled
                    clear_enterBox()

                    # Bởi vì khi xóa bảng rồi sẽ bị mất bảng nên phải tạo 1 bảng mới
                    # Recreate The Table
                    create_table_again()

            # Clear enter boxes
            def clear_enterBox():
                # Clear enter boxes
                date_enter.delete(0, END)
                name_enter.delete(0, END)
                id_entry.delete(0, END)
                gender_enter.delete(0, END)
                address_enter.delete(0, END)
                position_enter.delete(0, END)
                salary_enter.delete(0, END)
                pn_enter.delete(0, END)

            # Select Employee
            def select_employee(e):
                # Clear entry boxes
                date_enter.delete(0, END)
                name_enter.delete(0, END)
                id_entry.delete(0, END)
                gender_enter.delete(0, END)
                address_enter.delete(0, END)
                position_enter.delete(0, END)
                salary_enter.delete(0, END)
                pn_enter.delete(0, END)

                # Grab attribute Number
                selected = my_reportbox.focus()
                # Grab attribute values
                values = my_reportbox.item(selected, 'values')

                # output enter boxes

                date_enter.insert(0, values[0])
                name_enter.insert(0, values[1])
                id_entry.insert(0, values[2])
                gender_enter.insert(0, values[3])
                address_enter.insert(0, values[4])
                position_enter.insert(0, values[5])
                salary_enter.insert(0, values[6])
                pn_enter.insert(0, values[7])

            # Update employee
            def update_employee():
                # Grab the employee number
                selected = my_reportbox.focus()
                # Update data
                my_reportbox.item(selected, text="", values=(
                date_enter.get(), name_enter.get(), id_entry.get(), gender_enter.get(), address_enter.get(),
                position_enter.get(), salary_enter.get(), pn_enter.get(),))

                # Connect to database
                conn = sqlite3.connect('EmployeeList.db')
                cur = conn.cursor()
                # SQL query
                cur.execute(
                    "UPDATE employee SET date = :date, name = :name, gender = :gender, address = :address, position = :position, salary = :salary, phone_no = :phone_no WHERE oid = :oid",
                    {
                        'date': date_enter.get(),
                        'name': name_enter.get(),
                        'oid': id_entry.get(),
                        'gender': gender_enter.get().capitalize(),
                        'address': address_enter.get().capitalize(),
                        'position': position_enter.get().capitalize(),
                        'salary': salary_enter.get(),
                        'phone_no': pn_enter.get(),
                    })

                conn.commit()
                conn.close()

                # Clear enter boxes
                date_enter.delete(0, END)
                name_enter.delete(0, END)
                id_entry.delete(0, END)
                gender_enter.delete(0, END)
                address_enter.delete(0, END)
                position_enter.delete(0, END)
                salary_enter.delete(0, END)
                pn_enter.delete(0, END)

            # Add employee
            def add_employee():
                if date_enter.get() == "" or name_enter.get() == "" or gender_enter.get() == "" or address_enter.get() == "" or position_enter.get() == "" or salary_enter.get() == "" or pn_enter.get() == "":
                    result = messagebox.showwarning('', 'Please Complete The Required Field', icon="warning")

                else:
                    conn = sqlite3.connect('EmployeeList.db')
                    cur = conn.cursor()
                    cur.execute(
                        "INSERT  INTO employee VALUES ( :date, :name, :id, :gender, :address, :position, :salary, :phone_no )",
                        {
                            'date': date_enter.get(),
                            'name': name_enter.get(),
                            'id': id_entry.get(),
                            'gender': gender_enter.get().capitalize(),
                            'address': address_enter.get().capitalize(),
                            'position': position_enter.get().capitalize(),
                            'salary': salary_enter.get(),
                            'phone_no': pn_enter.get(),
                        })
                    conn.commit()
                    conn.close()

                    # Clear entry boxes
                    date_enter.delete(0, END)
                    name_enter.delete(0, END)
                    id_entry.delete(0, END)
                    gender_enter.delete(0, END)
                    address_enter.delete(0, END)
                    position_enter.delete(0, END)
                    salary_enter.delete(0, END)
                    pn_enter.delete(0, END)

                    # Clear The Report Box
                    my_reportbox.delete(*my_reportbox.get_children())

                    # đưa dữ liệu từ database lên
                    managedata()

            def create_table_again():
                # Connect to database
                conn = sqlite3.connect('EmployeeList.db')

                # Create a cursor
                cur = conn.cursor()

                # Create Table with sql query
                cur.execute(
                    "CREATE TABLE if not exists employee (date text, name text, id integer, gender text, address text, position text, salary REAL, phone_no integer ) ")

                # Commit changes
                conn.commit()

                # Close our connection
                conn.close()

            # Create Buttons Commands
            button = LabelFrame(root, text="Commands")
            button.pack(fill="x", expand="yes", padx=20)

            add_button = Button(button, text="Add New", command=add_employee)
            add_button.grid(row=0, column=0, padx=19, pady=10)

            update_button = Button(button, text="Update Attribute", command=update_employee)
            update_button.grid(row=0, column=1, padx=19, pady=10)

            removeOne_button = Button(button, text="Remove One", command=removeOne_selected)
            removeOne_button.grid(row=0, column=2, padx=19, pady=10)

            removeMany_button = Button(button, text="Remove Many", command=removeMany_emp)
            removeMany_button.grid(row=0, column=3, padx=19, pady=10)

            removeAll_button = Button(button, text="Remove All", command=removeAll_emp)
            removeAll_button.grid(row=0, column=4, padx=19, pady=10)

            up_button = Button(button, text="Move Up", command=up)
            up_button.grid(row=0, column=5, padx=19, pady=10)

            down_button = Button(button, text="Move Down", command=down)
            down_button.grid(row=0, column=6, padx=19, pady=10)

            selectAttribute_button = Button(button, text="Clear Enter Boxes", command=clear_enterBox)
            selectAttribute_button.grid(row=0, column=7, padx=19, pady=10)

            # Bind the Report Box
            my_reportbox.bind("<ButtonRelease-1>", select_employee)

            managedata()
            root.mainloop()

        elif self.username.get() == '' and self.password.get() == '':
            self.message = Label(text='                                                                ', fg='Red')
            self.message.grid(row=6, column=2)
            self.message = Label(text='                                                        ', fg='Red')
            self.message.grid(row=7, column=2)
            # show warning when username or password are not filled
            self.message = Label(text='  Username or Password are not filled ', fg='Red')
            self.message.grid(row=6, column=2)
            self.message = Label(text='Please fill it!!', fg='Red')
            self.message.grid(row=7, column=2)

        else:
            # show warning when username or password are wrong
            self.message = Label(text='                                                                ', fg='Red')
            self.message.grid(row=6, column=2)
            self.message = Label(text='                                                        ', fg='Red')
            self.message.grid(row=7, column=2)
            self.message = Label(text = '     Wrong username or password',fg = 'Red')
            self.message.grid(row=6,column=2)
            self.message = Label(text='Try Again!!', fg='Red')
            self.message.grid(row=7, column=2)

if __name__ == '__main__':

    root = Tk()
    root.geometry('500x220')
    application = Tologin(root)

    root.mainloop()
