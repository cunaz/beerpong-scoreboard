#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.4
#  in conjunction with Tcl version 8.7
#    Jul 23, 2020 11:29:20 PM CEST  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import scoreboard_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    scoreboard_support.set_Tk_var()
    top = Toplevel1 (root)
    scoreboard_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    scoreboard_support.set_Tk_var()
    top = Toplevel1 (w)
    scoreboard_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("670x479+1089+704")
        top.minsize(130, 10)
        top.maxsize(6414, 1431)
        top.resizable(0, 0)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.TCombobox1 = ttk.Combobox(top)
        self.TCombobox1.place(relx=0.209, rely=0.188, relheight=0.044
                , relwidth=0.212)
        self.TCombobox1.configure(takefocus="")
        self.TCombobox1.configure(cursor="fleur")

        self.TLabel1 = ttk.Label(top)
        self.TLabel1.place(relx=0.015, rely=0.188, height=19, width=65)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''Auflösung''')

        self.TButton1 = ttk.Button(top)
        self.TButton1.place(relx=0.821, rely=0.856, height=45, width=86)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''New Game''')
        self.TButton1.configure(cursor="fleur")

        self.TLabel2 = ttk.Label(top)
        self.TLabel2.place(relx=0.448, rely=0.251, height=19, width=116)
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font="TkDefaultFont")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(anchor='w')
        self.TLabel2.configure(justify='left')
        self.TLabel2.configure(text='''Spieler-Heim''')
        self.TLabel2.configure(cursor="fleur")

        self.TLabel3 = ttk.Label(top)
        self.TLabel3.place(relx=0.448, rely=0.313, height=19, width=120)
        self.TLabel3.configure(background="#d9d9d9")
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(font="TkDefaultFont")
        self.TLabel3.configure(relief="flat")
        self.TLabel3.configure(anchor='w')
        self.TLabel3.configure(justify='left')
        self.TLabel3.configure(text='''Spieler Auswärts''')
        self.TLabel3.configure(cursor="fleur")

        self.TCombobox2 = ttk.Combobox(top)
        self.TCombobox2.place(relx=0.209, rely=0.251, relheight=0.044
                , relwidth=0.213)
        self.TCombobox2.configure(textvariable=scoreboard_support.combobox)
        self.TCombobox2.configure(takefocus="")

        self.TCombobox3 = ttk.Combobox(top)
        self.TCombobox3.place(relx=0.209, rely=0.313, relheight=0.044
                , relwidth=0.213)
        self.TCombobox3.configure(textvariable=scoreboard_support.combobox)
        self.TCombobox3.configure(takefocus="")

        self.TLabel4 = ttk.Label(top)
        self.TLabel4.place(relx=0.015, rely=0.251, height=19, width=105)
        self.TLabel4.configure(background="#d9d9d9")
        self.TLabel4.configure(foreground="#000000")
        self.TLabel4.configure(font="TkDefaultFont")
        self.TLabel4.configure(relief="flat")
        self.TLabel4.configure(anchor='w')
        self.TLabel4.configure(justify='left')
        self.TLabel4.configure(text='''Heimteam''')
        self.TLabel4.configure(cursor="fleur")

        self.TLabel5 = ttk.Label(top)
        self.TLabel5.place(relx=0.015, rely=0.313, height=19, width=95)
        self.TLabel5.configure(background="#d9d9d9")
        self.TLabel5.configure(foreground="#000000")
        self.TLabel5.configure(font="TkDefaultFont")
        self.TLabel5.configure(relief="flat")
        self.TLabel5.configure(anchor='w')
        self.TLabel5.configure(justify='left')
        self.TLabel5.configure(text='''Auswärtsteam''')
        self.TLabel5.configure(cursor="fleur")

        self.TCombobox4 = ttk.Combobox(top)
        self.TCombobox4.place(relx=0.657, rely=0.251, relheight=0.044
                , relwidth=0.213)
        self.TCombobox4.configure(textvariable=scoreboard_support.combobox)
        self.TCombobox4.configure(takefocus="")

        self.TCombobox5 = ttk.Combobox(top)
        self.TCombobox5.place(relx=0.657, rely=0.313, relheight=0.044
                , relwidth=0.213)
        self.TCombobox5.configure(textvariable=scoreboard_support.combobox)
        self.TCombobox5.configure(takefocus="")

        self.TButton2 = ttk.Button(top)
        self.TButton2.place(relx=0.612, rely=0.167, height=35, width=206)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''Lade Teaminfos''')

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.373, rely=0.0, relheight=0.173, relwidth=0.2)
        self.Canvas1.configure(background="#d9d9d9")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="blue")
        self.Canvas1.configure(selectforeground="white")

if __name__ == '__main__':
    vp_start_gui()




