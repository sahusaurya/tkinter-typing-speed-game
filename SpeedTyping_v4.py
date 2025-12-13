    #All imports..........

import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
import time
##import mysql.connector
from datetime import datetime

#setting up sql connectivity
mycon = mysql.connector.connect(host = 'localhost',
                                user = 'root',
                                database = 'speedtyping',
                                password = 'project')
cursor = mycon.cursor()

#creating main window
root = tkinter.Tk()
root.title('SpeedTyping - Boost your typing speed!')
root.geometry("1200x700")

my_menu = Menu(root)
root.config(menu=my_menu)



#Defined functions..........

def begginer():
    hide_frames()
    begginer_frame.pack(fill="both", expand=1)
    
    
    def textbox_beg():
        
        try:
            del beg_t_init
            del beg_t_fin
        except:
            pass
        else:
            pass
        
        s='qwertyuiopasdfghjklzxcvbnm'
##        S='QWERTYUIOPASDFGHJKLZXCVBNM'
        l=list(s)
##        L=list(S)
        ques = ''
        i=1
        while i<=5:
            a = random.randrange(0,26)
            b = random.randrange(0,26)
            c = random.randrange(0,26)
            d = random.randrange(0,26)
            ques = ques + s[a] + s[b] + s[c] + s[d]
            if i<5:
                ques = ques + ' '
            i+=1

        label_ques_beg.config(text=ques, font=('Times',20))
               
        label_enter = tkinter.Label(begginer_frame, fg="black", bg="cyan", font=('Times',20))
        label_enter.config(text="Enter Your words here:")
        label_enter.grid(row=2,column=0)
        
        task_beg = ttk.Entry(begginer_frame, width=70, font=('Times',20))
        task_beg.grid(row=3,column=0)

        beg_t_init = time.time()

        def check_beg():
            beg_t_fin = time.time()
            
            acc_beg=0
            q = task_beg.get()

            list_beg_task = q.split()
            list_beg_ques = ques.split()
            
            if len(list_beg_task) > len(list_beg_ques):
                list_beg_task = list_beg_task[0:len(list_beg_ques)]
                list_beg_ques = list_beg_ques
            elif len(list_beg_task) < len(list_beg_ques):
                list_beg_task = list_beg_task
                list_beg_ques = list_beg_ques[0:len(list_beg_task)]
            else:
                list_beg_ques = list_beg_ques
                list_beg_task = list_beg_task
                    
            for run_beg in range(len(list_beg_task)):                 
                if list_beg_task[run_beg] == list_beg_ques[run_beg]:
                    acc_beg+=1
                    
            real_acc_beg = (acc_beg/len(list_beg_ques))*100
            result_beg.delete(0,END)
            beg_t_total= beg_t_fin - beg_t_init
            result_beg.insert(0,str(beg_t_total))
            result_beg.insert(0,"    Your total time taken is: ")
            result_beg.insert(0,str(real_acc_beg))
            result_beg.insert(0,"    Your accuracy in % is: ")
            result_beg.insert(0,str((acc_beg/beg_t_total)*acc_beg*100))
            result_beg.insert(0,"Your score is: ")
            score = (acc_beg/beg_t_total)*acc_beg*100

            cursor.execute('''insert into scores(UserName,DatePlay,Level,Score)values(%s,%s,%s,%s)''',(playernow,datetime.now(),'Beginner',score))
            mycon.commit()
##            cursor.execute('''select UserName, BegTop from userdata where UserName = '{}';'''.format(playernow))
##            beg_eval = cursor.fetchall()
##            if beg_eval[0][1] == None:
##                cursor.execute('''update userdata set BegTop = {} where UserName = '{}';'''.format(score,playernow))
##                mycon.commit()
##            else:
##                if beg_eval[0][1] >= score:
##                    pass
##                else:
##                    cursor.execute('''update userdata set BegTop = {} where UserName = '{}';'''.format(score,playernow))
##                    mycon.commit()
        b_check_beg = Button(begginer_frame, text="Click to show results", width=50, font=('Times',20), command=check_beg)
        b_check_beg.grid(row=4,column=0)
        result_beg = ttk.Entry(begginer_frame, width=100, font=('Times',20))
        result_beg.grid(row=5,column=0)
        
    b_beg = Button(begginer_frame, text="Click to start/restart", width=50, font=('Times',15), command=textbox_beg)
    b_beg.grid(row=0,column=0)


def intermediate():
    hide_frames()
    intermediate_frame.pack(fill="both", expand=1)
    
    
    def textbox_int():

        try:
            del int_t_init
            del int_t_fin
        except:
            pass
        else:
            pass
        
        L_int=('opera', 'bowl','helper','cheese','slime','barber','bite','hemp','yard','golf','best','thing','time','please''debate','arrived','first','continue','community','outpace',
               'analyse','evolution','human','adapt','theory','vulnerable','cyanide','topple','krypton','love','filth','please','colony','jumbo','lullaby','timeout','games','hurricane',
               'bench','fructose','dimple','jingle','emperor','emperial','moment','magic','blender','pride','envious','paradigm','humble','honest','grief','flatter','thick',)
        ques_int = ''
        i=1
        while i<=10:
            j = random.randrange(0,len(L_int))
            ques_int = ques_int + L_int[j]
            if i<10:
                ques_int = ques_int + ' '
            i+=1

        label_ques_int.config(text=ques_int)
        
        label_enter_int = tkinter.Label(intermediate_frame, fg="black", bg="yellow", font=('Times',20))
        label_enter_int.config(text="Enter Your words below:")
        label_enter_int.grid(row=2,column=0)
        
        task_int = ttk.Entry(intermediate_frame, width=70, font=('Times',20))
        task_int.grid(row=3,column=0)

        int_t_init = time.time()

        def check_int():
            int_t_fin = time.time()
            acc_int=0
            list_int_task = task_int.get().split()
            list_int_ques = ques_int.split()
            
            if len(list_int_task) > len(list_int_ques):
                list_int_task = list_int_task[0:len(list_int_ques)]
                list_int_ques = list_int_ques
            elif len(list_int_task) < len(list_int_ques):
                list_int_task = list_int_task
                list_int_ques = list_int_ques[0:len(list_int_task)]
            else:
                list_int_task = list_int_task
                list_int_ques = list_int_ques
                    
            for run_int in range(len(list_int_ques)):                 
                if list_int_ques[run_int] == list_int_task[run_int]:
                    acc_int+=1
                    
            real_acc_int = (acc_int/len(list_int_task))*100            
            result_int.delete(0,END)
            int_t_total= int_t_fin - int_t_init
            result_int.insert(0,str(int_t_total))
            result_int.insert(0,"    Your total time taken is: ")
            result_int.insert(0,str(real_acc_int))
            result_int.insert(0,"Your accuracy in % is: ")
            result_int.insert(0,str((acc_int/int_t_total)*acc_int*100))
            result_int.insert(0,"Your score is: ")
            score_int = (acc_int/int_t_total)*acc_int*100

            cursor.execute('''insert into scores(UserName,DatePlay,Level,Score)values(%s,%s,%s,%s)''',(playernow,datetime.now(),'Intermediate',score_int))
            mycon.commit()
##            cursor.execute('''select UserName, IntTop from userdata where UserName = '{}';'''.format(playernow))
##            int_eval = cursor.fetchall()
##            if int_eval[0][1] == None:
##                cursor.execute('''update userdata set IntTop = {} where UserName = '{}';'''.format(score_int,playernow))
##                mycon.commit()
##            else:
##                if beg_eval[0][1] >= score_int:
##                    pass
##                else:
##                    cursor.execute('''update userdata set IntTop = {} where UserName = '{}';'''.format(score_int,playernow))
##                    mycon.commit()

        b_check_int = Button(intermediate_frame, text="Click to show results", width=50, command=check_int, font=('Times',20))
        b_check_int.grid(row=4,column=0)
        result_int = ttk.Entry(intermediate_frame, width=100, font=('Times',20))
        result_int.grid(row=5,column=0)
   
    b_int = Button(intermediate_frame, text="Click to start/restart", width=50, command=textbox_int, font=('Times',20))
    b_int.grid(row=0,column=0)

def advanced():
    hide_frames()
    advanced_frame.pack(fill="both", expand=1)
    

    def textbox_adv():

        try:
            del adv_t_init
            del adv_t_fin
        except:
            pass
        else:
            pass
        
        P1="Twinkle-Twinkle little star, how I wonder what you are. Up'bove the world so high like a diamond in the sky. The night starry night sky, beautiful!"
        P2="Jack and Jill, went up the hill, to fetch a pail of water. Jack fell down n' broke his crown and Jill came tumbling after. Ouch! Jack hurt himself."
        P3='Itsy Bitsy Spider went up the water spout, down came the rain and washed the Spider out. The Sun comes out, dries it out and the Spider went up again.'
        P4="I'm little teapot, short and stout. Here's my handle here is my spout. When I get all steamed up, then I shout, just tip me over and pour me out."
        P5="Down in the jungle where nobody goes, there's an elephant, washing his clothes! Rubbing it here and rubbing it there. That's how he washes his clothes. "
        P6='Miss Polly had a dolly, who was sick, so she called for a Doctor to come quick. The doctor came with his bag, and his hat and knocked with a Rat-Tat.'
        
        L_adv=[]
        L_adv.extend([P1,P2,P3,P4,P5,P6])
        v=random.randrange(0,len(L_adv))
        ques_adv = L_adv[v]
    
        label_ques_adv.config(text=ques_adv)
        
        label_enter_adv = tkinter.Label(advanced_frame, fg="black", bg="red", font=('Times',20))
        label_enter_adv.config(text="Enter Your words below:")
        label_enter_adv.grid(row=2,column=0)
        
        task_adv = ttk.Entry(advanced_frame, width=70, font=('Times',20))
        task_adv.grid(row=3,column=0)

        adv_t_init = time.time()

        def check_adv():
            adv_t_fin = time.time()
            acc_adv=0
            list_int_task = task_adv.get().split()
            list_adv_ques = ques_adv.split()
            
            if len(list_int_task) > len(list_adv_ques):
                list_int_task = list_int_task[0:len(list_adv_ques)]
                list_adv_ques = list_adv_ques
            elif len(list_int_task) < len(list_adv_ques):
                list_int_task = list_int_task
                list_adv_ques = list_adv_ques[0:len(list_int_task)]
            else:
                list_int_task = list_int_task
                list_adv_ques = list_adv_ques
                    
            for run_beg in range(len(list_adv_ques)):                 
                if list_int_task[run_beg] == list_adv_ques[run_beg]:
                    acc_adv+=1
                    
            real_acc_adv = (acc_adv/len(list_adv_ques))*100
            result_adv.delete(0,END)
            adv_t_total= adv_t_fin - adv_t_init
            result_adv.insert(0,str(adv_t_total))
            result_adv.insert(0,"    Your total time taken is: ")
            result_adv.insert(0,str(real_acc_adv))
            result_adv.insert(0,"Your accuracy in % is: ")
            result_adv.insert(0,str((acc_adv/adv_t_total)*acc_adv*100))
            result_adv.insert(0,"Your score is: ")
            score_adv = (acc_adv/adv_t_total)*acc_adv*100


            cursor.execute('''insert into scores(UserName,DatePlay,Level,Score)values(%s,%s,%s,%s)''',(playernow,datetime.now(),'Advanced',score_adv))
            mycon.commit()
##            cursor.execute('''select UserName, AdvTop from userdata where UserName = '{}';'''.format(playernow))
##            adv_eval = cursor.fetchall()
##            if adv_eval[0][1] == None:
##                cursor.execute('''update userdata set AdvTop = {} where UserName = '{}';'''.format(score_adv,playernow))
##                mycon.commit()
##            else:
##                if adv_eval[0][1] >= score_adv:
##                    pass
##                else:
##                    cursor.execute('''update userdata set AdvTop = {} where UserName = '{}';'''.format(score_adv,playernow))
##                    mycon.commit()

        b_check_adv = Button(advanced_frame, text="Click to show results", font=('Times',20), width=50, command=check_adv)
        b_check_adv.grid(row=4,column=0)
        result_adv = ttk.Entry(advanced_frame, width=100, font=('Times',20))
        result_adv.grid(row=5,column=0)
        

    b_adv = Button(advanced_frame, text="Click to start/restart", width=50, font=('Times',20), command=textbox_adv)
    b_adv.grid(row=0,column=0)

def hide_frames():
    mainpage_frame.pack_forget()
    begginer_frame.pack_forget()
    intermediate_frame.pack_forget()
    advanced_frame.pack_forget()
    score_frame.pack_forget()
    devpage_frame.pack_forget()
    feed_frame.pack_forget()
    user_feed_frame.pack_forget()
    
def score_see():       
    hide_frames()
    score_frame.pack(fill="both", expand=1)

def beg_scoreshow():
    try:
        for widget in score_frame_mini.winfo_children():
            widget.destroy()
    except:
        pass
    else:
        pass
    head = Label(score_frame_mini, width =30, text= "Beginner Top Scores:", bg = 'White', fg = 'Black', font = ('Times',16))
    head.grid(row=0,column = 0)
    cursor.execute("SELECT UserName, DatePlay, Score FROM scores where Level = 'Beginner' order by Score desc limit 0,24;")
    data = cursor.fetchall()
    need = ('UserName', 'Date Played', 'Top scores')
    for j in range(len(need)):
        e = Label(score_frame_mini,width=30, text=need[j], bg = 'Black', fg = 'White', font = ('Times',16))
        e.grid(row=1, column=j)
    i=2
    for records in data:
        for j in range(len(records)):
            e = Label(score_frame_mini,width=30, text=records[j], font = ('Ariel',16)) 
            e.grid(row=i, column=j)
        i=i+1
        print()# line break at the end of one row

def int_scoreshow():
    try:
        for widget in score_frame_mini.winfo_children():
            widget.destroy()
    except:
        pass
    else:
        pass
    head = Label(score_frame_mini, width =30, text= "Intermediate Top Scores:", bg = 'White', fg = 'Black', font = ('Times',16))
    head.grid(row=0,column = 0)
    cursor.execute("SELECT UserName, DatePlay, Score FROM scores where Level = 'Intermediate' order by Score desc limit 0,24;")
    data = cursor.fetchall()
    need = ('UserName', 'Date Played', 'HighScore')
    for j in range(len(need)):
        e = Label(score_frame_mini,width=30, text=need[j], bg = 'Black', fg = 'White', font = ('Times',16))
        e.grid(row=1, column=j)
    i=2
    for records in data:
        for j in range(len(records)):
            e = Label(score_frame_mini,width=30, text=records[j], font = ('Ariel',16)) 
            e.grid(row=i, column=j)
        i=i+1
        print()# line break at the end of one row

def adv_scoreshow():
    try:
        for widget in score_frame_mini.winfo_children():
            widget.destroy()
    except:
        pass
    else:
        pass
    head = Label(score_frame_mini, width =30, text= "Advanced Top Scores:", bg = 'White', fg = 'Black', font = ('Times',16))
    head.grid(row=0,column = 0)
    cursor.execute("SELECT UserName, DatePlay, Score FROM scores where Level = 'Advanced' order by Score desc limit 0,24;")
    data = cursor.fetchall()
    need = ('UserName', 'Date Played', 'HighScore')
    for j in range(len(need)):
        e = Label(score_frame_mini,width=30, text=need[j], bg = 'Black', fg = 'White', font = ('Times',16))
        e.grid(row=1, column=j)
    i=2
    for records in data:
        for j in range(len(records)):
            e = Label(score_frame_mini,width=30, text=records[j], font = ('Ariel',16)) 
            e.grid(row=i, column=j)
        i=i+1
        print()# line break at the end of one row


def home():
    hide_frames()
    mainpage_frame.pack_forget()
    begginer_frame.pack_forget()
    devpage_frame.pack_forget()
    intermediate_frame.pack_forget()
    advanced_frame.pack_forget()
    score_frame.pack_forget()
    mainpage_frame.pack(fill="both", expand=1)

def dev():
    hide_frames()
    mainpage_frame.pack_forget()
    begginer_frame.pack_forget()
    intermediate_frame.pack_forget()
    advanced_frame.pack_forget()
    score_frame.pack_forget()
    devpage_frame.pack(fill="both",expand=1)
    feed_frame.pack_forget()
    
    
def duplicate_username():
    window = Tk()
    window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
    window.withdraw()

    messagebox.showerror('Oops try again!', 'A user with this username already exists. Try entering a new one.')

    window.deiconify()
    window.destroy()
    window.quit()

def register_succ():
    window = Tk()
    window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
    window.withdraw()

    messagebox.showinfo('Succesful Registration', 'Enjoy the full experience of the program.')

    window.deiconify()
    window.destroy()
    window.quit()

def login_succ():
    window = Tk()
    window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
    window.withdraw()

    if messagebox.showinfo("Succesful Login", "You're now logged into {}.".format(userenter.get())) == True:
        playernow = userenter.get()

    window.deiconify()
    window.destroy()
    window.quit()

def dev_succ():
    
    def confirm():
        global playerkill
        playerkill = user_del_enter.get()
    window = Tk()
    window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
    window.withdraw()

    if messagebox.showinfo("Succesful Login", "You're now logged into developer.") == True:
        playernow = userenter.get()

    window.deiconify()
    window.destroy()
    window.quit()

    try:
        for widget in devpage_frame.winfo_children():
            widget.destroy()
    except:
        pass
    else:
        pass
    user_del = tkinter.Label(devpage_frame, text="Enter the player to remove from database",fg="black", bg="white", font=('Times', 16))
    user_del_enter = tkinter.Entry(devpage_frame, width=70, font=('Times', 10))
    user_del_conf = tkinter.Button(devpage_frame, width=80, text="Click to confirm the name",bg = 'red', fg = 'white', font=('Times', 10), command = confirm)
    user_del_button = tkinter.Button(devpage_frame, width=80, text="Click to Remove the Player", font=('Times', 10), command = player_delete)
    show_feedback_but = tkinter.Button(devpage_frame, width=80, text="click to show player feedback", font=('Times', 10), command = feed_page)
    user_del.pack()
    user_del_enter.pack()
    user_del_conf.pack()
    user_del_button.pack()
    show_feedback_but.pack()

def player_delete():
    cursor.execute('''delete from userdata where UserName = '{}';'''.format(playerkill))
    mycon.commit()
    cursor.execute('''select * from scores where UserName = '{}';'''.format(playerkill))
    data=cursor.fetchall()
    for i in range(len(data)):
        cursor.execute('''delete from scores where UserName = '{}';'''.format(playerkill))
        mycon.commit()
    
def feed_page():
    hide_frames()
    feed_frame.pack(fill="both", expand=1)

def feed_show():
    feedofplayer = player_feed_search.get()
    cursor.execute('''select Feed from feedback where UserName = '{}';'''.format(feedofplayer))
    data = cursor.fetchall()
    player_feedshow.config(text=data[0])
    
def user_feedback_page():
    hide_frames()
    user_feed_frame.pack(fill="both", expand=1)

def feed_insert():
    value = feedback_true.get()
    cursor.execute('''insert into feedback(UserName,Feed)values(%s,%s)''',(playernow,value))
    mycon.commit()

def login_fail():
    window = Tk()
    window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
    window.withdraw()

    messagebox.showinfo("Failed Login attempt", "No player found. Retry Login.")

    window.deiconify()
    window.destroy()
    window.quit()

def dev_fail():
    window = Tk()
    window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
    window.withdraw()

    messagebox.showinfo("Failed Login attempt", "No developer account found. Retry Login.")

    window.deiconify()
    window.destroy()
    window.quit()

def player_reg():
    temp = userenter.get()
    cursor.execute('''select * from userdata where UserName = '{}';'''.format(temp) )
    values = cursor.fetchall()
    if values == []:
        global playernow
        playernow = userenter.get()
        cursor.execute('''insert into userdata(UserName, Password, Regdate) values(%s,%s,%s)''',(userenter.get(), passenter.get(), datetime.now()))
        mycon.commit()
        register_succ()
    else:
        duplicate_username()

def player_log():
    temp1 = userenter.get()
    temp2 = passenter.get()
    
    cursor.execute('''select * from userdata where UserName = '{}' and Password = '{}';'''.format(temp1,temp2) )
    values = cursor.fetchall()
    if values != []:
        global playernow
        playernow = userenter.get()
        login_succ()
    else:
        login_fail()

def dev_log():
    temp1 = deventer.get()
    temp2 = devpassent.get()
    if temp1 == 'developer' and temp2 == 'developer':
        global playernow
        playernow = deventer.get()
        dev_succ()
        
                
    else:
        dev_fail()

# Creating the Menus..........
options_menu = Menu(my_menu)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Home", command=home)
options_menu.add_separator()
options_menu.add_command(label="Exit", command=root.destroy)
options_menu.add_separator()
options_menu.add_command(label="DeveloperLogs", command=dev)

play_menu = Menu(my_menu)
my_menu.add_cascade(label="Play", menu=play_menu)
play_menu.add_command(label="Beginner Level", command=begginer)
play_menu.add_separator()
play_menu.add_command(label="Intermediate Level", command=intermediate)
play_menu.add_separator()
play_menu.add_command(label="Advanced Level", command=advanced)

scores_menu = Menu(my_menu)
my_menu.add_cascade(label="Feedback and scores", menu=scores_menu)
scores_menu.add_command(label="Show Top Scores", command=score_see)
scores_menu.add_command(label="Feedback", command=user_feedback_page)

icon = PhotoImage(file='icon.png')
root.iconphoto(False, icon)


#Creating Frames..........

mainpage_frame = LabelFrame(root, text="HomePage", width = 1200, height = 600, padx=50, pady=50)
username_label = tkinter.Label(mainpage_frame, text="Enter Username below:",fg="black", bg="white", font=('Times', 16))
userenter = tkinter.Entry(mainpage_frame, width=70, font=('Times', 10))
password_label = tkinter.Label(mainpage_frame, text="Enter Password below:",fg="black", bg="white", font=('Times', 16))
passenter = tkinter.Entry(mainpage_frame, width=70, font=('Times', 10))
player_add = tkinter.Button(mainpage_frame, width=50, text="CLick to register", font=('Times', 10), command = player_reg)
player_login = tkinter.Button(mainpage_frame, width=50, text="CLick to login", font=('Times', 10), command = player_log)

begginer_frame = LabelFrame(root, text="Level - Begginer", width = 1200, height = 600, bg="cyan", padx=100, pady=100)
label_ques_beg = tkinter.Label(begginer_frame, fg="black", font=('Times',20))
label_ques_beg.grid(row=1,column=0)

intermediate_frame = LabelFrame(root, text="Level - Intermediate", width = 1200, height = 600, bg="yellow", padx=100, pady=100)
label_ques_int = tkinter.Label(intermediate_frame, fg="black", font=('Times',20))
label_ques_int.grid(row=1,column=0)

advanced_frame = LabelFrame(root, text="Level - Advanced", width = 1200, height = 600, bg="red", padx=100, pady=100)
label_ques_adv= tkinter.Label(advanced_frame, fg="black", font=('Times',20))    
label_ques_adv.grid(row=1,column=0)

score_frame = LabelFrame(root, text="Keep track of your best performances! :)", width = 1200, height = 600, bg="white", padx=100, pady=50)
mainpage_frame.pack(fill="both", expand=1)

devpage_frame = LabelFrame(root, text="DEVELOPERLOGS", width = 1200, height = 600, padx=50, pady=50)
devname_label = tkinter.Label(devpage_frame, text="Enter Username below:",fg="black", bg="white", font=('Times', 16))
deventer = tkinter.Entry(devpage_frame, width=70, font=('Times', 10))
devpass_label = tkinter.Label(devpage_frame, text="Enter Password below:",fg="black", bg="white", font=('Times', 16))
devpassent = tkinter.Entry(devpage_frame, width=70, font=('Times', 10))
devlogin_confirm = tkinter.Button(devpage_frame, width=50, text="CLick to Login", font=('Times', 10), command = dev_log)
devname_label.pack()
deventer.pack()
devpass_label.pack()
devpassent.pack()
devlogin_confirm.pack()

feed_frame = LabelFrame(root, text="Feedback", width = 1200, height = 600, padx=100, pady=100)
player_name_feed= tkinter.Label(feed_frame, fg="black", text ="Enter the username of the player", font=('Times',20))
player_feed_search = ttk.Entry(feed_frame, width=70, font=('Times',20))
feed_reveal = tkinter.Button(feed_frame, width=50, text="click to load the feedback", font=('Times', 20), command = feed_show)
tellerlol = tkinter.Label(feed_frame, fg="black", font=('Times',10), text = "Player feedback")  
player_feedshow= tkinter.Label(feed_frame, fg="black", font=('Times',20))    
player_name_feed.pack()
player_feed_search.pack()
feed_reveal.pack()
tellerlol.pack()
player_feedshow.pack()

user_feed_frame = LabelFrame(root, text="User Feedback", width = 1200, height = 600, padx=100, pady=100)
instr= tkinter.Label(user_feed_frame, fg="black", text ="Enter the feedback here (50 characters only)", font=('Times',20))
feedback_true = ttk.Entry(user_feed_frame, width=70, font=('Times',20))
feed_send = tkinter.Button(user_feed_frame, width=50, text="click to load the feedback", font=('Times', 10), command = feed_insert)
instr.pack()
feedback_true.pack()
feed_send.pack()

#Adding other items to the Frames..........
peng= PhotoImage(file = 'home.png')
label_home = ttk.Label(mainpage_frame, image=peng)
PhotoImage(file = 'home.png')
label_home.pack()
username_label.pack()
userenter.pack()
password_label.pack()
passenter.pack()
player_add.pack()
player_login.pack()

b_begscore = Button(score_frame, text='''Click to Beginner LeaderBoard/n Refresh Beginner Leaderboard''', width=50, command=beg_scoreshow)
b_begscore.pack()

b_intscore = Button(score_frame, text='''Click to Intermediate LeaderBoard/n Refresh Beginner Leaderboard''', width=50, command=int_scoreshow)
b_intscore.pack()

b_advscore = Button(score_frame, text='''Click to Advanced LeaderBoard/n Refresh Beginner Leaderboard''', width=50, command=adv_scoreshow)
b_advscore.pack()

score_frame_mini = LabelFrame(score_frame, width = 1200, height = 600, bg="white")
score_frame_mini.pack(fill="both", expand=1)

root.mainloop()

