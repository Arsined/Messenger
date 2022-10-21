from tkinter import *
import datetime
from tkinter import messagebox
import socket
import threading
bgg = 1
fgg = 2
color = ["black", "gray", "white"]
x = 100
file = open("чат.txt", 'r')
mas = []
for i in file:
    mas.append(i.split())
file.close()


def revxod(winpro, chat, ent, enter):
    global x, bgg, fgg, win3, ent12
    if 'win3' in globals():
        win3.destroy()
    x = 100
    bgg = 1
    fgg = 2
    winpro.destroy()
    chat.destroy()
    ent.destroy()
    enter.destroy()
    root.withdraw()
    men = Menu(root)
    root.config(bg=color[bgg], menu=men)
    me = Menu(men, tearoff=0)
    me.add_command(label="Вход", command=lambda: vxod())
    me.add_command(label="Регистрация", command=lambda: reg())
    me.add_command(label="Выход", command=lambda: root.destroy())
    men.add_cascade(label="Меню", menu=me)
    win1 = Toplevel(root, bg=color[bgg])
    win1.minsize(width=500, height=275)
    win1.title("Вход")
    xx = (win1.winfo_screenwidth()) / 2.63
    yy = (win1.winfo_screenheight()) / 400
    win1.wm_geometry("+%d+%d" % (xx, yy))
    lab12 = Label(win1, text="Имя:", font=("Arial", int(13 * x / 100)), bg=color[bgg], fg=color[fgg])
    ent12 = Entry(win1, width=20, bd=3, font=("Arial", int(13 * x / 100)), bg=color[bgg], fg=color[fgg])
    lab22 = Label(win1, text="Пароль:", font=("Arial", int(13 * x / 100)), bg=color[bgg], fg=color[fgg])
    ent22 = Entry(win1, show='*', width=20, bd=3, font=("Arial", int(13 * x / 100)), bg=color[bgg], fg=color[fgg])
    but32 = Button(win1, width=10, height=1, font=("Arial", int(13 * x / 100)), text="Войти",
                   command=lambda: vxodfin(ent12, ent22, win1), bg=color[bgg], fg=color[fgg])
    butsv = Button(win1, width=3, height=1, font=("Arial", int(11 * x / 100)), text=('<', u'\u2299', '>'),
                   bg=color[bgg], fg=color[fgg])
    butsv.bind("<Button-1>", lambda event: show1(event, ent22))
    butsv.bind("<ButtonRelease-1>", lambda event: show2(event, ent22))
    butsv.place(x=310, y=100)
    but32.place(x=125, y=150)
    ent22.place(x=120, y=100)
    lab22.place(x=25, y=100)
    ent12.place(x=120, y=50)
    lab12.place(x=25, y=50)


def vxod():
    global win1, ent12
    if 'win1' in globals():
        win1.destroy()
    win1 = Toplevel(root, bg=color[bgg])
    win1.minsize(width=500, height=275)
    win1.title("Вход")
    xx = (win1.winfo_screenwidth()) / 2.63
    yy = (win1.winfo_screenheight()) / 400
    win1.wm_geometry("+%d+%d" % (xx, yy))
    lab12 = Label(win1, text="Имя:", font=("Arial", int(13*x/100)), bg=color[bgg], fg=color[fgg])
    ent12 = Entry(win1, width=20, bd=3, font=("Arial", int(13*x/100)), bg=color[bgg], fg=color[fgg])
    lab22 = Label(win1, text="Пароль:", font=("Arial", int(13*x/100)), bg=color[bgg], fg=color[fgg])
    ent22 = Entry(win1, show='*', width=20, bd=3, font=("Arial", int(13*x/100)), bg=color[bgg], fg=color[fgg])
    but32 = Button(win1, width=10, height=1, font=("Arial", int(13*x/100)), text="Войти",
                   command=lambda: vxodfin(ent12, ent22, win1), bg=color[bgg], fg=color[fgg])
    butsv = Button(win1, width=3, height=1, font=("Arial", int(11*x/100)), text=('<', u'\u2299', '>'),
                   bg=color[bgg], fg=color[fgg])
    butsv.bind("<Button-1>", lambda event: show1(event, ent22))
    butsv.bind("<ButtonRelease-1>", lambda event: show2(event, ent22))
    butsv.place(x=310, y=100)
    but32.place(x=125, y=150)
    ent22.place(x=120, y=100)
    lab22.place(x=25, y=100)
    ent12.place(x=120, y=50)
    lab12.place(x=25, y=50)


def show1(event, parol):
    parol.config(show='')


def show2(event, parol):
    parol.config(show='*')


def reg():
    global win2
    if 'win2' in globals():
        win2.destroy()
    win2 = Toplevel(root, bg=color[bgg])
    win2.minsize(width=500, height=275)
    win2.title("Регистрация")
    xx = (win2.winfo_screenwidth()) / 500
    yy = (win2.winfo_screenheight()) / 3.4
    win2.wm_geometry("+%d+%d" % (xx, yy))
    lab1 = Label(win2, text="Имя:", font=("Arial", int(13*x/100)), bg=color[bgg], fg=color[fgg])
    ent1 = Entry(win2, width=20, bd=3, font=("Arial", int(13*x/100)), bg=color[bgg], fg=color[fgg])
    lab2 = Label(win2, text="Пароль:", font=("Arial", int(13*x/100)), bg=color[bgg], fg=color[fgg])
    ent2 = Entry(win2, show='*', width=20, bd=3, font=("Arial", int(13*x/100)), bg=color[bgg], fg=color[fgg])
    but3 = Button(win2, width=20, height=1, font=("Arial", int(13*x/100)), text="Зарегистрироваться",
                  command=lambda: regfin(win2, ent1, ent2), bg=color[bgg], fg=color[fgg])
    butsr = Button(win2, width=3, height=1, font=("Arial", int(11 * x / 100)), text=('<', u'\u2299', '>'),
                   bg=color[bgg], fg=color[fgg])
    butsr.bind("<Button-1>", lambda event: show1(event, ent2))
    butsr.bind("<ButtonRelease-1>", lambda event: show2(event, ent2))
    butsr.place(x=310, y=100)
    but3.place(x=75, y=150)
    ent2.place(x=120, y=100)
    lab2.place(x=25, y=100)
    ent1.place(x=120, y=50)
    lab1.place(x=25, y=50)


def regfin(a, login, parol):
    if len(login.get()) != 0 and len(parol.get()) != 0:
        q = 0
        for j in mas:
            if j[0] == login.get():
                q = 1
        if len(login.get()) <= 3 or len(parol.get()) <= 3:
            q = 2
        for char in login.get():
            if char == ' ':
                q = 3
        for char in parol.get():
            if char == ' ':
                q = 3
        if q == 0:
            mas.append([login.get(), parol.get(),
                        datetime.datetime.now().strftime("%d.%m.%Y-%H:%M"), '1', '100'])
            login.delete(0, last=END)
            parol.delete(0, last=END)
            file = open("чат.txt", 'w+')
            for j in mas:
                file.write(j[0])
                file.write(" ")
                file.write(j[1])
                file.write(" ")
                file.write(j[2])
                file.write(" ")
                file.write(j[3])
                file.write(" ")
                file.write(j[4])
                file.write("\n")
            file.close()
            a.destroy()
            vxod()
        elif q == 1:
            messagebox.showerror("Ошибка", "Такой пользователь уже зарегестрирован")
        elif q == 2:
            messagebox.showerror("Ошибка", "Слишком короткое имя или пароль")
        elif q == 3:
            messagebox.showerror("Ошибка", "Пробел в логине или пароле")
    else:
        messagebox.showerror("Ошибка", "Пустое поле")


def vxodfin(login, parol, vxod):
    global e, men, win2
    q = 0
    ee = 0
    for j in mas:
        ee += 1
        if login.get() == j[0] and parol.get() == j[1]:
            e = ee
            men.destroy()
            q = 1
    if q == 1:
        if 'win2' in globals():
            win2.destroy()
        profil(login.get())
        vxod.destroy()
    if q == 0:
        messagebox.showerror("Ошибка", "Неверное имя пользователя или пароль")


def updatevxodfin(a, b, c, d, win, chat, ent, enter):
    global x, bgg, fgg
    ee = 0
    for j in mas:
        ee += 1
        if ee == e:
            x = int(j[4])
            if j[3] == '2':
                bgg = 2
                fgg = 0
            else:
                bgg = int(j[3])
                fgg = 2
            men = Menu(win)
            win.config(bg=color[bgg], menu=men)
            me = Menu(men, tearoff=0)
            me.add_command(label="Сменить пользователя", command=lambda: revxod(win, chat, ent, enter))
            me.add_command(label="Настройки", command=lambda: settings(a, b, c, d, win, chat, ent, enter))
            me.add_command(label="Разработчики", command=lambda:titr())
            me.add_command(label="Выход", command=lambda: exitprg())
            men.add_cascade(label="Меню", menu=me)
            a.config(bg=color[bgg], fg=color[fgg], font=("Arial", int(13*x/100)))
            b.config(bg=color[bgg], fg=color[fgg], font=("Arial", int(13*x/100)))
            c.config(bg=color[bgg], fg=color[fgg], font=("Arial", int(13*x/100)))
            d.config(bg=color[bgg], fg=color[fgg], font=("Arial", int(13*x/100)))
            chat.config(bg=color[bgg], fg=color[fgg], font=("Arial", int(13*x/100)))
            ent.config(bg=color[bgg], fg=color[fgg], font=("Arial", int(13*x/100)))
            enter.config(bg=color[bgg], fg=color[fgg], font=("Arial", int(13*x/100)))
            win.config(bg=color[bgg])
            root.config(bg=color[bgg])


def update1(event, sca1, lab3, lab4, rad0, rad1, rad2, labpro1, labpro2, labpro3, labpro4,
            chat, ent, enter):
    global x
    ee = 0
    file = open("чат.txt", 'w+')
    x = sca1.get()
    for j in mas:
        ee += 1
        if ee == e:
            j[4] = str(x)
            file.write(j[0])
            file.write(" ")
            file.write(j[1])
            file.write(" ")
            file.write(j[2])
            file.write(" ")
            file.write(j[3])
            file.write(" ")
            file.write(j[4])
            file.write("\n")
            sca1.config(font=("Arial", int(13 * x / 100)))
            lab4.config(font=("Arial", int(13 * x / 100)))
            lab3.config(font=("Arial", int(13 * x / 100)))
            rad0.config(font=("Arial", int(13 * x / 100)))
            rad1.config(font=("Arial", int(13 * x / 100)))
            rad2.config(font=("Arial", int(13 * x / 100)))
            labpro1.config(font=("Arial", int(13 * x / 100)))
            labpro2.config(font=("Arial", int(13 * x / 100)))
            labpro3.config(font=("Arial", int(13 * x / 100)))
            labpro4.config(font=("Arial", int(13 * x / 100)))
            chat.config(font=("Arial", int(13*x/100)))
            ent.config(font=("Arial", int(13*x/100)))
            enter.config(font=("Arial", int(13*x/100)))
        else:
            file.write(j[0])
            file.write(" ")
            file.write(j[1])
            file.write(" ")
            file.write(j[2])
            file.write(" ")
            file.write(j[3])
            file.write(" ")
            file.write(j[4])
            file.write("\n")
    file.close()


def update2(sca1, lab3, var, lab4, rad0, rad1, rad2, win3, labpro1, labpro2, labpro3, labpro4, winpro,
            chat, ent, enter):
    global bgg, fgg
    ee = 0
    file = open("чат.txt", 'w+')
    for j in mas:
        ee += 1
        if ee == e:
            if var.get() == 0 or var.get() == 1:
                bgg = var.get()
                fgg = 2
            else:
                bgg = var.get()
                fgg = 0
            j[3] = str(var.get())
            file.write(j[0])
            file.write(" ")
            file.write(j[1])
            file.write(" ")
            file.write(j[2])
            file.write(" ")
            file.write(j[3])
            file.write(" ")
            file.write(j[4])
            file.write("\n")
            sca1.config(bg=color[bgg], fg=color[fgg])
            lab4.config(bg=color[bgg], fg=color[fgg])
            lab3.config(bg=color[bgg], fg=color[fgg])
            rad0.config(bg=color[bgg], fg=color[fgg], activeforeground=color[fgg], activebackground=color[bgg])
            rad1.config(bg=color[bgg], fg=color[fgg], activeforeground=color[fgg], activebackground=color[bgg])
            rad2.config(bg=color[bgg], fg=color[fgg], activeforeground=color[fgg], activebackground=color[bgg])
            win3.config(bg=color[bgg])
            labpro1.config(bg=color[bgg], fg=color[fgg])
            labpro2.config(bg=color[bgg], fg=color[fgg])
            labpro3.config(bg=color[bgg], fg=color[fgg])
            labpro4.config(bg=color[bgg], fg=color[fgg])
            winpro.config(bg=color[bgg])
            chat.config(bg=color[bgg], fg=color[fgg])
            ent.config(bg=color[bgg], fg=color[fgg])
            enter.config(bg=color[bgg], fg=color[fgg])
            root.config(bg=color[bgg])
        else:
            file.write(j[0])
            file.write(" ")
            file.write(j[1])
            file.write(" ")
            file.write(j[2])
            file.write(" ")
            file.write(j[3])
            file.write(" ")
            file.write(j[4])
            file.write("\n")
    file.close()


def settings(a, b, c, d, win, chat, ent, enter):
    global x, win3
    if 'win3' in globals():
        win3.destroy()
    win3 = Toplevel(root, bg=color[bgg])
    win3.minsize(width=500, height=275)
    win3.title("Настройки")
    xx = (win3.winfo_screenwidth()) / 500
    yy = (win3.winfo_screenheight()) / 3.4
    win3.wm_geometry("+%d+%d" % (xx, yy))
    sca1 = Scale(win3, orient=HORIZONTAL, length=300, from_=75, to=135, resolution=5,
                 bg=color[bgg], fg=color[fgg], font=("Arial", int(13*x/100)))
    sca1.bind("<ButtonRelease-1>", lambda event: update1(event, sca1, lab3, lab4, rad0, rad1, rad2,
                                                         a, b, c, d, chat, ent, enter))
    sca1.set(x)
    x = sca1.get()
    lab3 = Label(win3, text="Размер текста", font=("Arial", int(13*x/100)), bg=color[bgg], fg=color[fgg])
    lab4 = Label(win3, text="Тема", font=("Arial", int(13*x/100)), bg=color[bgg], fg=color[fgg])
    if 'var' not in globals():
        var = IntVar()
    ee = 0
    for j in mas:
        ee += 1
        if ee == e:
            var.set(int(j[3]))
            print(j[0])
    rad0 = Radiobutton(win3, text="Ультратемная", variable=var, value=0, bg=color[bgg], activeforeground=color[fgg],
                       activebackground=color[bgg], fg=color[fgg], selectcolor=color[bgg],
                       font=("Arial", int(13*x/100)), 
                       command=lambda: update2(sca1, lab3, var, lab4, rad0, rad1, rad2, win3, a, b, c, d, win,
                                               chat, ent, enter))
    rad1 = Radiobutton(win3, text="Темная", variable=var, value=1, bg=color[bgg], activeforeground=color[fgg],
                       activebackground=color[bgg], fg=color[fgg], selectcolor=color[bgg],
                       font=("Arial", int(13*x/100)),
                       command=lambda: update2(sca1, lab3, var, lab4, rad0, rad1, rad2, win3, a, b, c, d, win,
                                               chat, ent, enter))
    rad2 = Radiobutton(win3, text="Светлая", variable=var, value=2, bg=color[bgg], activeforeground=color[fgg],
                       activebackground=color[bgg], fg=color[fgg], selectcolor=color[bgg],
                       font=("Arial", int(13*x/100)),
                       command=lambda: update2(sca1, lab3, var, lab4, rad0, rad1, rad2, win3, a, b, c, d, win,
                                               chat, ent, enter))
    sca1.place(x=75, y=40)
    lab3.place(x=175, y=5)
    lab4.place(x=200, y=100)
    rad0.place(x=10, y=140)
    rad1.place(x=200, y=140)
    rad2.place(x=350, y=140)


def profil(login1):
    ee = 0
    for j in mas:
        ee += 1
        if ee == e:
            winpro = Toplevel(root, bg=color[bgg])
            winpro.minsize(width=500, height=275)
            winpro.title("Профиль")
            xx = (winpro.winfo_screenwidth()) / 500
            yy = (winpro.winfo_screenheight()) / 400
            winpro.wm_geometry("+%d+%d" % (xx, yy))
            labpro1 = Label(winpro, text="Имя:", font=("Arial", int(13*x/100)), bg=color[bgg], fg=color[fgg])
            labpro2 = Label(winpro, text=j[0], font=("Arial", int(13 * x / 100)), bg=color[bgg], fg=color[fgg])
            labpro3 = Label(winpro, text="Дата Регистрации", font=("Arial", int(13 * x / 100)), bg=color[bgg],
                            fg=color[fgg])
            labpro4 = Label(winpro, text=j[2], font=("Arial", int(13 * x / 100)), bg=color[bgg], fg=color[fgg])
            labpro4.place(x=100, y=150)
            labpro3.place(x=100, y=100)
            labpro2.place(x=100, y=50)
            labpro1.place(x=50, y=50)
            chat1(login1, labpro1, labpro2, labpro3, labpro4, winpro)


def chat1(login1, labpro1, labpro2, labpro3, labpro4, winpro):
    global s, host, port, client, chat, ent, enter
    root.withdraw()
    root.deiconify()
    root.minsize(width=580, height=608)
    xx = (root.winfo_screenwidth()) / 2.63
    yy = (root.winfo_screenheight()) / 400
    root.wm_geometry("+%d+%d" % (xx, yy))
    chat = Text(root, width=45, height=20, bg=color[bgg], fg=color[fgg],  font=("Arial", int(13 * x / 100)),
                bd=2, wrap=WORD)
    ent = Text(root, width=35, height=2, bg=color[bgg], fg=color[fgg], font=("Arial", int(13 * x / 100)),
               bd=2, wrap=WORD)
    enter = Button(root, bg=color[bgg], fg=color[fgg],  font=("Arial", int(13 * x / 100)), text=">",
                   height=1, width=4, command=lambda: text(chat, ent, login1, client))
    updatevxodfin(labpro1, labpro2, labpro3, labpro4, winpro, chat, ent, enter)
    chat.configure(state='disabled')
    scr = Scrollbar(root, orient=VERTICAL, width=20, command=chat.yview)
    chat.configure(yscrollcommand=scr.set)
    ent.place(x=57, y=495)
    chat.place(x=37, y=20)
    scr.place(x=1000, y=1000)
    enter.place(x=460, y=500)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    client.connect(('127.0.0.1', 7976))
    client.send(login1.encode('utf-8'))
    receive_thread = threading.Thread(target=receive)  # Получение всех сообщений
    receive_thread.start()

    
def text(chat, ent, login1, client):
    tx = "<" + login1 + ">: " + str(ent.get(1.0, END))
    ent.delete(1.0, END)
    write_thread = threading.Thread(target=write(tx, client))
    write_thread.start()
    chat.yview_moveto(1)

  
def write(tx, client):
    message = tx
    client.send(message.encode('utf-8'))
    

def receive():
    global chat, client
    while True:  # Подтверждение соединения
            chat.configure(state='normal')
            chat.insert(END, client.recv(1024).decode('utf-8'))
            chat.configure(state='disabled')


def exitprg():
    global chat, client, ent12
    answer = messagebox.askyesno(title="Вопрос", message="Вы точно хотите выйти?")
    if answer:
        root.destroy()


def titr():
    win = Toplevel(root, bg=color[bgg])
    win.minsize(width=500, height=275)
    win.title("Разработчики")
    xx = (win.winfo_screenwidth()) / 500
    yy = (win.winfo_screenheight()) / 3.4
    win.wm_geometry("+%d+%d" % (xx, yy))
    lab = Label(win, text="\tArsined", font=("Arial", int(13*x/100)), bg=color[bgg], fg=color[fgg])
    lab.place(x=20, y=50)
    img = PhotoImage(file="R2.png")
    b=Label(win, image=img)
    b.image_ref=img
    b.place(x=50, y=100)
    lab1 = Label(win, text="\tSmoonFly", font=("Arial", int(13*x/100)), bg=color[bgg], fg=color[fgg])
    lab1.place(x=275, y=50)
    img = PhotoImage(file="NeR.png")
    b1=Label(win, image=img)
    b1.image_ref=img
    b1.place(x=300, y=100)


root = Tk()
root.title("Чат")
xx = (root.winfo_screenwidth()) / 500
yy = (root.winfo_screenheight()) / 400
root.wm_geometry("+%d+%d" % (xx, yy))
root.minsize(width=500, height=255)
men = Menu(root)
root.config(bg=color[bgg], menu=men)
me = Menu(men, tearoff=0)
me.add_command(label="Вход", command=lambda: vxod())
me.add_command(label="Регистрация", command=lambda: reg())
me.add_command(label="Разработчики", command=lambda:titr())
me.add_command(label="Выход", command=lambda: exitprg())
men.add_cascade(label="Меню", menu=me)
root.mainloop()
