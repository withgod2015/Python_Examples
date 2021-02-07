# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 19:44:27 2020

@author: Administrator


  10−12	1 picosecond	One trillionth of one second    (1/1000000000000)
  10−9	1 nanosecond	One billionth of one second     (1/1000000000)
* 10−6	1 microsecond	One millionth of one second     (1/1000000)
  10−3	1 millisecond	One thousandth of one second    (1/1000)

url : https://www.youtube.com/watch?v=ekOeCnCSyUc&ab_channel=Codegnan

"""

import tkinter as tk
import tkinter.font as TkFont
from datetime import datetime

def run():
    current_time = datetime.now()
    diff = current_time - start_time
    txt_var.set('%d.%06d' %(diff.seconds,diff.microseconds))
    if running: #for timelapse
        root.after(20,run) #to reschedule after 20ms,refresh display
 
def start():
    global running
    global start_time   

    if not running:
        running = True
        start_time = datetime.now()
        
        root.after(10,run)
        
def stop():
    global running
    
    running = False
    
def reset():
    
    global start_time
    start_time = datetime.now()    
    
    if not running:
        txt_var.set('0:000000')
        
running = False
start_time = None

root = tk.Tk()
root.geometry("500x200") #width x height
root.title("StopWatch")

txt_var = tk.StringVar()
txt_var.set('0.000000')

fontstyle = TkFont.Font(family ="Lucida Grande",size = 50)
tk.Label(root,textvariable=txt_var,font=fontstyle).pack()

tk.Button(root,text = "Start",command=start).pack(fill = 'x')
tk.Button(root,text='Stop',command = stop).pack(fill='x')
tk.Button(root,text = 'Reset',command = reset).pack(fill='x')
tk.Button(root,text = 'Timelapse',command = run).pack(fill='x')
root.mainloop()
