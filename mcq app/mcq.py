import  tkinter as tk
import q
from  tkinter import *
import random , im,xc
import time, logging,os
from time import sleep
him=0
akm = 0
log_dir = ""
logging.basicConfig(filename=(log_dir + "hs.txt"), level=logging.DEBUG, format='%(message)s')
kmn = 0
gum=0
def p():
    time.sleep(1)
    kim()
def kim():
    global gum, jbl, view, him, jill
    jbl = random.randint(0,13)
    view.pack_forget()
    
    while gum<=10:
        gum=gum+1
        break
    
    if (jill==him and gum<11):
        look()
    him = 1
    joker()  
    print jbl
    

def look():
    global akm,entry1

    akm=akm+5
    entry1.delete(0,END)
    entry1.insert(0,akm)
    kool()
    
def kool():
    global akm,kmn
    
    if int(akm>kmn):
        
        logging.info(akm)
        
    return None
def hkm():
    global gum
    gum = 10
    
    joker()
def rep():
    global gum,akm,entry1,kmn,him,v5
    v5.pack_forget()
    
    akm=0
    gum=0
    kmn=0
    him=0
    entry1.delete(0,END)
    
    nm3()
def joker():
    
    global view, lable, va, v, jill,gum,jbl,v3,akm,v5
    
    
    jbl = random.randint(0,13)
    if (gum==10):
        v3.pack_forget()
        view.pack_forget()
        v5 = Frame(root,bg=kl)
        sdf=str(akm)
        la = Label(v5,font=("Ink Free", 20),bg=kl, text="Thank you " + sa )
        la.pack()
        label8 = Label(v5,font=("Ink Free", 20),bg=kl,text="Your score is " + sdf)
        label8.pack()
        lb2 = xc.ImageLabel(v5)
        lb2.pack()
        lb2.load('1.gif')
        la1 = Label(v5,font=("Ink Free", 20),bg=kl, text="Come again to charge your brain " )
        la1.pack()
        re = Button(v5,text="Replay",bg=kl, command=rep)
        re.pack()
        v5.pack()
    elif (gum<10):
            
        view = Frame(root,bg=kl)
        f = q.q[jbl]
        l3 = Label(view, wraplength=400,borderwidth=2,bg=kl, text = gum + 1, font=("Ink Free", 15)).pack()
        lable = Label(view, wraplength=400,borderwidth=2,bg=kl, text = f, font=("Ink Free", 15)).pack()
        q.o[jbl]
        i=0
        v = StringVar()
        va = StringVar()
        #tk.Radiobutton(view,text=q.o[jbl][0],indicatoron =0,width =20,padx =20,variable=v,value=1,command=mmm).pack()
        #tk.Radiobutton(view,text=q.o[jbl][1],indicatoron =0,width =20,padx =20,variable=v,value=2,command=mmm).pack()
        #tk.Radiobutton(view,text=q.o[jbl][2],indicatoron =0,width =20,padx =20,variable=v,value=3,command=mmm).pack()
        #tk.Radiobutton(view,text=q.o[jbl][3],indicatoron =0,width =20,padx =20,variable=v,value=4,command=mmm).pack()
       
        button  = Radiobutton(view, text=q.o[jbl][0], variable=v,wraplength=200,command=mmm,indicatoron =0,width =20,padx =20,bg=kl, value=0, borderwidth=4, font=("Ink Free", 13))
        button.pack()
        button1 = Radiobutton(view, text=q.o[jbl][1], variable=v,wraplength=200,command=mmm,indicatoron =0,width =20,padx =20,bg=kl, value=1, borderwidth=4, font=("Ink Free", 13))
        button1.pack()
        button2 = Radiobutton(view, text=q.o[jbl][2], variable=v,wraplength=200,command=mmm,indicatoron =0,width =20,padx =20,bg=kl, value=2, borderwidth=4, font=("Ink Free", 13))
        button2.pack()
        button3 = Radiobutton(view, text=q.o[jbl][3], variable=v,wraplength=200,command=mmm,indicatoron =0,width =20,padx =20,bg=kl, value=3, borderwidth=4, font=("Ink Free", 13))
        button3.pack()
        
        jill = q.a[jbl]
        print (jill)
        btn = Button(view ,text="NEXT/SKIP",bg=kl, command=kim)
        btn.pack()

        btn1 = Button(view, text="QUIT",bg=kl, command=hkm)
        btn1.pack()
        view.pack()
        return view

def mmm():
    global v, kol, jbl, him, lb, va
    
    kol = v.get()
    print kol
    qw = int(jbl)
    er = int(kol)
    him = q.o[qw][er]
        
    if him is not None:
        p()
        



def nm():
    global v4
    v4 = Frame(root,bg=kl)
    l1 = Label(v4,text="WELCOME TO THE GAME", font=("Ink Free", 20),bg=kl)
    l1.pack()
    
    lbl = xc.ImageLabel(v4)
    lbl.pack()
    lbl.load('2.gif')
    
    v4.pack()
    btn = Button(v4, text="NEXT",bg=kl, command=nm1)
    btn.pack()
        
    
    
def nm1():
    global v4,v1,vk,sa,e1
    
    v4.pack_forget()
    v1 = Frame(root,bg=kl)
    a1= Label(v1,text="Enter Your Name", font=("Ink Free",18),padx=0,pady=100,bg=kl)
    a1.pack()
    vk = StringVar()
    e1 = Entry(v1, textvariable=vk, font=("Ink Free",13),bg=kl)
    e1.pack()
    btn = Button(v1, text="NEXT",bg=kl, command=nm2)
    btn.pack()
    v1.pack()
def nm2():
    
    global v1,v2,vk,sa,e1
    sa = e1.get()
    
    if len(e1.get()) == 0:
        v1.pack_forget()
        nm1()
        l=Label(v1,text="Please Input Your Name ",fg="red",font=("Ink Free",20),bg=kl).pack()
    elif sa is not None:
        
        v1.pack_forget()
        v2 = Frame(root,bg=kl)


        l1 = Label(v2,text="THIS QUIZ GAME IS MADE BY USING PYTHON", font=("Ink Free", 15),bg=kl,justify=CENTER)
        l1.pack()
        l1 = Label(v2,text="YOU CAN SELECT ONE OPTION FOR EACH QUESTION", font=("Ink Free", 15),bg=kl,justify=CENTER)
        l1.pack()
        l1 = Label(v2,text="YOU CAN PRESS SKIP/NEXT BUTTON TO SKIP THE QUESTION", font=("Ink Free", 15),bg=kl,justify=CENTER)
        l1.pack()
        l1 = Label(v2,text="THERE WILL BE TOTAL 10 QUESTION IN FRONT OF YOU ", font=("Ink Free", 15),bg=kl,justify=CENTER)
        l1.pack()
        l1 = Label(v2,text="EACH QUESTIONS WILL CARRY FIVE MARKS", font=("Ink Free", 15),bg=kl,justify=CENTER)
        l1.pack()
        l1 = Label(v2,text="THERE WILL BE NO NEGATIVE MARKS", font=("Ink Free", 15),bg=kl,justify=CENTER)
        l1.pack()
        l1 = Label(v2,text="CLICK NEXT TO START THE GAME", font=("Ink Free", 15),bg=kl,justify=CENTER)
        l1.pack()

        btn = Button(v2, text="NEXT",bg=kl, command=nm3)
        btn.pack()
        v2.pack()
    

        
def nm3():
    global jbl,v2, entry1,v3,kmn
    v2.pack_forget()
    v3 = Frame(root,bg=kl)
    
    Label(v3,text="SCORE",bg=kl).pack()
    entry1 = Entry(v3,bg=kl)
    entry1.pack()
    Label(v3,text="Highest Score",bg=kl).pack()
    entry2 = Entry(v3,bg=kl)
    entry2.pack()


    with open('hs.txt') as ok:
        for key in ok:
            entry2.delete(0,END)
            entry2.insert(0,key)
            kmn = int(key)
        


    

    
    
    v3.pack()
    joker()


root=Tk()
root.title("QUIZ GAME")
root.geometry("700x510")
j = random.randint(0,378)
kl = im.COLORS[j]
root.configure(background=kl)

nm()
root.mainloop()
