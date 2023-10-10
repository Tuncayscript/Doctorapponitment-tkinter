from tkinter import *
from tkinter import messagebox
import center_tk_window as ctw
from tkinter import ttk
from tkcalendar import *

window = Tk()
window.title('Doctors appointment')
window.geometry('300x300')
window.configure(bg = 'bisque')
ctw.center_on_screen(window)

lst_of_users = []
user_num = 0

def login():
    login = Toplevel()
    login.title("Login")
    login.geometry('300x300')
    login.configure(bg = 'bisque')
    ctw.center_on_screen(login)

    def login2():
        if len(entry.get()) == 0 or len(str(entry2.get())) == 0:
             messagebox.showerror('Invalid credintials', 'Your username or passcode is not valid!')
        else:
            username = entry.get()
            password = entry2.get()

            window.withdraw()
            login.destroy()
            appointment = Tk()
            appointment.title('Appointment')
            appointment.geometry('600x600')
            appointment.configure(bg = 'bisque')
            ctw.center_on_screen(appointment)
            data_lbl = Label(appointment,text = 'Məlumatlar',bg = 'bisque', bd = 0, fg = 'Black', width= 9)
            data_lbl.grid(row = 1, column = 0, pady = 5, ipady = 5)
            us_lbl = Label(appointment, text = f'İstifadəçi adi: {username}', bg = 'bisque', bd = 0, fg = 'Black', width= 25 )
            us_lbl.grid(row = 2, column = 0, pady = 5, ipady = 5,padx = 10)
            lbl_klinik = Label(appointment, text = 'Klinika seçin: ',bg = 'bisque', bd = 0, fg = 'Black', width= 15)
            lbl_klinik.grid( row = 1,column =2,pady = 5, ipady = 5,padx = 50)
            cbox = ttk.Combobox(appointment, justify = CENTER, state = 'readonly',width=26)
            cbox['values'] = ['---Select hospital---','Mediland','Mediarkt','Mərkəzi klinika']
            cbox.current(0)
            cbox.grid(row = 2, column =2, pady = 5, ipady = 5,padx = 50)
            def first_cbox_ok():
                if cbox.get() != '---Select hospital---':
                    if cbox.get() == 'Mediland':
                        lbl_hekim = Label(appointment, text = 'Həkim seçin:',bg = 'bisque', bd = 0, fg = 'Black', width= 15)
                        lbl_hekim.grid( row = 3,column =2,pady = 5, ipady = 5,padx = 50)
                        hekimler = ttk.Combobox(appointment, justify = CENTER, state = 'readonly', width = 26)
                        hekimler['values'] = ['Həkimlər','Vahid Süleymanov', 'Tural Əliyev']
                        hekimler.current(0)
                        hekimler.grid(row = 4, column =2, pady = 5, ipady = 5,padx = 50)
                    elif cbox.get() == 'Mediarkt':
                        lbl_hekim = Label(appointment, text = 'Həkim seçin:',bg = 'bisque', bd = 0, fg = 'Black', width= 15)
                        lbl_hekim.grid( row = 3,column =2,pady = 5, ipady = 5,padx = 50)
                        hekimler_2 = ttk.Combobox(appointment, justify = CENTER, state = 'readonly', width = 26)
                        hekimler_2['values'] = ['Həkimlər','Vahid Süleymanov', 'Əli Rüstəmov']
                        hekimler_2.current(0)
                        hekimler_2.grid(row = 4, column =2, pady = 5, ipady = 5,padx = 50)
                    elif cbox.get() == 'Mərkəzi klinika':
                        lbl_hekim = Label(appointment, text = 'Həkim seçin:',bg = 'bisque', bd = 0, fg = 'Black', width= 15)
                        lbl_hekim.grid( row = 3,column =2,pady = 5, ipady = 5,padx = 50)
                        hekimler_3 = ttk.Combobox(appointment, justify = CENTER, state = 'readonly', width = 26)
                        hekimler_3['values'] = ['Həkimlər','Ceyhun Bayramov', 'Xalidə Əhmədova']
                        hekimler_3.current(0)
                        hekimler_3.grid(row = 4, column =2, pady = 5, ipady = 5,padx = 50)
                                    
                        cal = Calendar(appointment, selectmode = 'day', year = 2023, month = 5, day = 7)
                        cal.grid(row = 5,column = 2, pady = 5,padx = 50)
                        
                        hr_min_sec = Label(appointment, text = 'HOUR MINUTE SECOND', font = ('Times', 12), bg = 'bisque')
                        hr_min_sec.grid(row = 6, column = 2,padx = 50)

                        hr_sb = Spinbox(appointment, from_=0, to=23, wrap=True, 
                                         width=2, state='readonly', font = ('Times',20), justify=CENTER)
                        hr_sb.grid(row = 7,column = 2, pady = 5, ipady = 5,padx = 50)

                        min_sb = Spinbox(appointment, from_=0, to=59, wrap=True, 
                                            width=2, state='readonly', font = ('Times',20), justify=CENTER)
                        min_sb.grid(row = 8,column = 2, pady = 5, ipady = 5,padx = 50)

                        sec_sb = Spinbox(appointment, from_=0, to=59, wrap=True,width=2, font = ('Times',20), justify=CENTER)
                        sec_sb.grid(row = 9,column = 2, pady = 5, ipady = 5,padx = 30)
                                
                        tesdiqle = Button(appointment, text = 'Təsdiqlə', cursor = 'hand2',fg = 'white', bg = 'black', bd = 0, width = 20)
                        tesdiqle.grid(row = 10, column = 2, pady = 5, ipady = 5,padx = 10) 


                        ok_bttn = Button(appointment, text = 'Ok', cursor = 'hand2',fg = 'white', bg = 'black', bd = 0, width = 5, command = first_cbox_ok)
                        ok_bttn.grid(row = 2, column = 3,pady = 5, ipady = 5,padx = 10)

            def show_main_window():
                appointment.withdraw()
                window.deiconify()

                lbl3=Label(appointment,text = f' Welcome back {username} ',bg = 'bisque', fg = 'black', width = 25)
                lbl3.grid(row=0,column = 3,pady = 5, ipady = 5,padx = 30)
                sign_out= Button(appointment, text = 'Sign Out', cursor = 'hand2', 
                                                    fg = 'white', bg = 'black', bd = 0, width = 18, command = show_main_window)
                sign_out.grid(row = 0,column = 0, pady = 5, ipady = 5,padx = 10)
                appointment.mainloop()
                # break once find the user from the user_register table
                #break

      
 
        lbl = Label(login, text = 'Username', bd = 0, bg = 'green', fg = 'white', width = 13)
        lbl.grid(row = 0,column = 0, pady = 5, ipady = 5,padx = 10)
        entry = Entry(login,bd = 0, justify = CENTER, width = 20, font = ('bold',11))
        entry.grid(row = 0,column = 1, pady = 5, ipady = 5,padx = 10)
        lbl2 = Label(login, text = 'Password', bd = 0, bg = 'green', fg = 'white', width = 13)
        lbl2.grid(row = 1,column = 0, pady = 5, ipady = 5,padx = 10)
        entry2 = Entry(login,bd = 0, justify = CENTER, width = 20, font = ('bold',11))
        entry2.grid(row = 1,column = 1, pady = 5, ipady = 5,padx = 10)
        btn_3= Button(login, text = 'Login', cursor = 'hand2', fg = 'white', bg = 'black', bd = 0, width = 6,command = login2)
        btn_3.grid(row = 2, column = 1, pady = 5, ipady  = 5, padx = 3)

def sign_up():
    sign_up = Tk()
    sign_up.title('Sign Up')
    sign_up.geometry('300x300')
    sign_up.configure(bg = 'bisque')
    ctw.center_on_screen(sign_up)

    
    lbl = Label(sign_up, text = 'Username', bd = 0, bg = 'green', fg = 'white', width = 13)
    lbl.grid(row = 0,column = 0, pady = 5, ipady = 5,padx = 10)
    entry = Entry(sign_up,bd = 0, justify = CENTER, width = 20, font = ('bold',11))
    entry.grid(row = 0,column = 1, pady = 5, ipady = 5,padx = 10)
    lbl2 = Label(sign_up, text = 'Password', bd = 0, bg = 'green', fg = 'white', width = 13)
    lbl2.grid(row = 1,column = 0, pady = 5, ipady = 5,padx = 10)
    entry2 = Entry(sign_up,bd = 0,show = '*', justify = CENTER, width = 20, font = ('bold',11))
    entry2.grid(row = 1,column = 1, pady = 5, ipady = 5,padx = 10)
    lbl3 = Label(sign_up, text = 'Number', bd = 0, bg = 'green', fg = 'white', width = 13)
    lbl3.grid(row = 2,column = 0, pady = 5, ipady = 5,padx = 10)
    entry3 = Entry(sign_up,bd = 0, justify = CENTER, width = 20, font = ('bold',11))
    entry3.grid(row = 2,column = 1, pady = 5, ipady = 5,padx = 10)
    lbl4 = Label(sign_up, text = 'Email', bd = 0, bg = 'green', fg = 'white', width = 13)
    lbl4.grid(row = 3,column = 0, pady = 5, ipady = 5,padx = 10)
    entry4 = Entry(sign_up,bd = 0, justify = CENTER, width = 20, font = ('bold',11))
    entry4.grid(row = 3,column = 1, pady = 5, ipady = 5,padx = 10)

    gender = StringVar()

    def male():
        gender.set('Male')
    
    def female():
        gender.set('Female')
    

    R1 = Radiobutton(sign_up, text="Female", variable = gender, value=1,bg = 'bisque',
                  command= female)
    R1.grid(row = 4, column = 0)
    R2 = Radiobutton(sign_up, text="Male", variable= gender, value=2,bg = 'bisque',
                  command= male)
    R2.grid(row = 4, column= 1)


    def insert_user_info():
        if len(lst_of_users) != 0:
            for user in lst_of_users:
                if entry.get() == user[1] or entry4.get() == user[4]:
                    messagebox.showerror('Invalid credintials', 'This username or email has already been registrated!')
                    return

        global user_num
        user_num += 1
        user_row = [user_num]
        for value in [entry, entry2, entry3, entry4]:
            user_row.append(value.get())

        user_row.append(gender.get())
        lst_of_users.append(user_row)
        print(lst_of_users)
        messagebox.showinfo('Sign Up Success', 'You did sign Up well.Now Login Please')
        sign_up.destroy()
    
    btn_signUp = Button(sign_up,text = 'Sign Up', fg = 'white', bg = 'black', cursor='hand2', width = 40, command=insert_user_info)
    btn_signUp.grid(row = 5, columnspan = 2)
    
    btn_signUp = Button(sign_up,text = 'Sign Up', fg = 'white', bg = 'black', cursor='hand2', width = 40, command=insert_user_info)
    btn_signUp.grid(row = 5, columnspan = 2)




label = Label(window, text = 'DOCTORS APPOINTMENT', bd = 0, bg = 'black', fg = 'white', width = 40)
label.grid(row = 0,column = 1, pady = 5, ipady = 5,padx = 10)

btn_1=Button(window, text = 'Sign up', cursor = 'hand2', fg = 'white', bg = 'blue', bd = 0, width = 9,command = sign_up)
btn_1.grid(row = 1, column = 1, pady = 5, ipady  = 5, padx = 3)

btn_2=Button(window, text = 'Login', cursor = 'hand2', fg = 'white', bg = 'blue', bd = 0, width = 10,command = login)
btn_2.grid(row = 2, column = 1, pady = 5, ipady  = 5, padx = 3)






window.mainloop()
