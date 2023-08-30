from tkinter import*
try:
    import tkinter as tk
except:
    import tkinter as tk       # untuk import tampilan GUI
import os
import sys
import random
import sqlite3  #digunakan untuk memasukkan database Nemuu
import time
import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
LED1=16
LED2=20
LED3=21
GPIO.setup(LED1,GPIO.OUT)
GPIO.setup(LED2,GPIO.OUT)
GPIO.setup(LED2,GPIO.OUT)
print("*************START******************")


root = Tk()
root.title('Nemuu Page')
lbl=Label(root,text ="Nemuu",fg ='black' , font =("times new roman", 90),bg='white')
lbl.place(x=100,y=10) 

lbl3=Label(root,text ="Developed By",fg ='black' , font =("times new roman", 40),bg='white')
lbl3.place(x=30,y=700)

lbl3=Label(root,text ="Team 198",fg ='black' , font =("times new roman", 40),bg='white')
lbl3.place(x=30,y=760)


large_font=('Verdana',40)
ID = Entry(root,width=3,font=large_font) #membuat box scanner
ID .grid(row=4, column=2)
ID .place(x=760,y=400)
ID.focus()

txt  = "Scan ID"
lbl6=Label(root,fg ='red' , font =("times new roman", 50),bg='white')
lbl6.place(x=500,y=400)

def labelconfig():
     p=txt
     color = '#'+("%09x" % random.randint(0,0xFFFFFF))
     lbl6.config(text=p,fg=str(color))
     root.after(200,labelconfig)
labelconfig()

root.geometry('1920x1080')
root['bg'] = 'white'  #background color



def fg():
                                            try:
                                                        large_font=('Verdana',20)
                                                        gk=code
                                                        global ID
                                                        coll_id=gk
                                                        ID.delete(0, END)
                                                        ID.insert(0,gk)
                                                        
                                                        conn=sqlite3.connect('Nemuu.db')
                                                        c=conn.cursor()
                                                        c.execute( "SELECT *  FROM id_table WHERE ID='%s'  " %ID.get()) #check barcode database Nemuu
                                                        records1 = c.fetchall()
                                                        print_records= ' '
                       
                                                        global ff
                                                        global jj
                                                        ID.delete(0, END)
                                                        row=["Empty","Empty"]
                                                        for row in records1:
                                                                
                                                                ff=row[0]  ###### id
                                                                jj=row[1]  ##### name
                                                                                                                               
                                                        conn.commit()
                                                        conn.close()
                                                        ID.delete(0, END)                                                       
                                                        if (row[0]=='Empty'):                 
                                                                  large_font=('Verdana',20)                                                                 
                                                                  txt='           Error In Matching Unidentified User            '
                                                                  lbl6=Label(root,fg ='red' , font =("times new roman", 50),bg='white')
                                                                  lbl6.place(x=400,y=500)
                                                                  
                                                                  ID.delete(0, END)
                                                                  print("code tidak cocok")
                                                                  GPIO.output (LED1,GPIO.LOW) #ketika barcode salah dimasukkan maka akan terjadi error & loker tidak terbuka
                                                                   
                                                                  def labelconfig():
                                                                     p=txt
                                                                     color = '#'+("%06x" % random.randint(0,0xFFFFFF))
                                                                     lbl6.config(text=p,fg=str(color))
                                                                     root.after(300,labelconfig)
                                                                  labelconfig()
                                                        else:               #otherwise door is open
                                                                  large_font=('Verdana',20)                                                             
                                                                  txt='           Correct Matching, Identified User                          '
                                                                  lbl6=Label(root,fg ='red' , font =("times new roman", 50),bg='white')
                                                                  lbl6.place(x=400,y=500)
                                                                  ID.delete(0, END)
                                                                  
                                                                  GPIO.output (LED1,GPIO.HIGH)  # Loker 1 Terbuka
                                                                  time.sleep(2)
                                                                  print("open")
                                                                  GPIO.output (LED1,GPIO.LOW)
                                                                  print("close")
                                                                  
                                                                  GPIO.output (LED2,GPIO.HIGH)  # Loker 2 Terbuka
                                                                  time.sleep(2)
                                                                  print("open")
                                                                  GPIO.output (LED2,GPIO.LOW)
                                                                  print("close")
                                                                  
                                                                  GPIO.output (LED3,GPIO.HIGH)  # Loker 3 Terbuka
                                                                  time.sleep(2)
                                                                  print("open")
                                                                  GPIO.output (LED3,GPIO.LOW)
                                                                  print("close")
                                                                  
                                                                  def labelconfig():
                                                                     p=txt
                                                                     color = '#'+("%06x" % random.randint(0,0xFFFFFF))
                                                                     lbl6.config(text=p,fg=str(color))
                                                                     root.after(300,labelconfig)
                                                                  labelconfig()
                                                                  
                                                            
                                            except Exception as e:
                                             print('Operation failed!')
                                             print('Exception message: ' + str(e))      

def get_key(event):    # code id pada barcode akan masuk ke sebuah box, dan nanti akan di compare ke database Nemuu
    global code
    if event.char in '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM':
       code += event.char

    elif event.keysym == 'Return':
        #print('result:', code)
        fg()           # call the fg() function 
        code=""
code = ''                        
root.bind('<Key>', get_key)

root.mainloop()