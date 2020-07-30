
from tkinter import *
import tkinter.ttk as ttk
import requests
from bs4 import BeautifulSoup
import functools

class Display:

    def createButtons(self, frame, side, rows, arr):
        offset = 0
        bt_water = Button(frame)
        bt_water.place(x=side, y=90 ,height='45', width='45')
        bt_water.configure(image=self.img_cup_water)
        bt_water.configure(borderwidth="0")
        bt_water.configure(background=self.background_color)
        for hoehe in range(rows):
            for breite in range(rows-hoehe):
                tmp = Button(frame)
                tmp.place(x=  abs(190-(breite*45)-offset-side), y=135-(hoehe*45) ,height='45', width='45')
                tmp.configure(image=self.img_cup_beer)
                tmp.configure(borderwidth="0")
                tmp.configure(background=self.background_color)
                arr.append(tmp)
            offset += int(45/2)

    
    def __init__(self, master, aufloesung, playerhome, playeraway):
        #self.master = Toplevel(master)
        self.fontcolor = "white"
        self.background_color = "black"
        self.font = "Helvetica"
        self.fontsize_playername = 40
        self.fontsize_stats = 30
        self.var_spieler_heim = StringVar()
        self.var_spieler_heim.set(playerhome)
        self.var_spieler_auswaerts = StringVar()
        self.var_spieler_auswaerts.set(playeraway)
        self.var_stats_heim = StringVar()
        self.var_stats_auswaerts = StringVar()
        self.var_stats_auswaerts.set("0% 0/0")
        self.var_stats_heim.set("0/0 0%")
        self.img_cup_beer = PhotoImage(file="./cup.png")
        self.img_cup_water = PhotoImage(file="./cup_water.png")
        self.master = master
        if len(aufloesung)>0:
            self.master.geometry(aufloesung)
        else:
            self.master.geometry("1920x200")
        self.master.title("Bierpong Scoreboard - Display")
        self.master.configure(bg='black')
        self.master.resizable(width=0, height=0)

        
        self.lb_spieler_heim = Label(self.master,  textvariable=self.var_spieler_heim, fg=self.fontcolor, bg=self.background_color, font=(self.font,self.fontsize_playername))
        self.lb_spieler_heim.place(relx=0, rely=0.05, anchor=NW )
        self.lb_spieler_auswaerts = Label(self.master,  textvariable=self.var_spieler_auswaerts, fg=self.fontcolor, bg=self.background_color, font=(self.font,self.fontsize_playername))
        self.lb_spieler_auswaerts.place( relx=1, rely=0.05, anchor=NE)

        self.lb_stats_heim = Label(self.master, textvariable=self.var_stats_heim, fg=self.fontcolor, bg=self.background_color, font=(self.font, self.fontsize_stats) )
        self.lb_stats_heim.place(relx=0, rely=0.5, anchor=NW)
        self.lb_stats_auswaerts = Label(self.master, textvariable=self.var_stats_auswaerts, fg=self.fontcolor, bg=self.background_color, font=(self.font, self.fontsize_stats))
        self.lb_stats_auswaerts.place(relx=1, rely=0.5, anchor=NE)


        self.frame1 = Frame(self.master)
        self.frame1.place(relx=0.33, rely=0, relheight=1.0, relwidth=0.333)
        self.frame1.configure(background=self.background_color)

        self.frame_home = Frame(self.frame1)
        self.frame_home.place(x=10, y=10, height=180, width=235)
        self.frame_home.configure(background=self.background_color)

        self.frame_away = Frame(self.frame1)
        self.frame_away.place(x=(640-245), y=10, height=180, width=235) #640 ist ein 1/3 der akutellen Breite - 
        self.frame_away.configure(background=self.background_color)

        self.var_spielstand = StringVar()
        self.var_spielstand.set("0:0")
        self.lb_spielstand = Label(self.frame1, textvariable=self.var_spielstand, fg=self.fontcolor,bg=self.background_color, font=(self.font, self.fontsize_stats))
        self.lb_spielstand.place(relx=0.5, rely=0.5, anchor=CENTER)
        #TODO Skalierbarkeit der Breite
        
        self.bt_cups_home = []
        self.bt_cups_away = []
        self.createButtons(self.frame_home,0,4,self.bt_cups_home)
        self.createButtons(self.frame_away,190,4, self.bt_cups_away)
        self.master.update()

class Controller:
    

    def createButtons(self, frame, side, rows, arr):
            offset = 0
            bt_water = Button(frame, command= lambda idTeam=side : self.cuppressed_miss(side))
            bt_water.place(x=side, y=90 ,height='45', width='45')
            bt_water.configure(image=self.img_cup_water)
            bt_water.configure(borderwidth="0")
            bt_water.configure(background=self.background_color)
            for hoehe in range(rows):
                for breite in range(rows-hoehe):
                    tmp = Button(frame)
                    tmp.place(x=  abs(190-(breite*45)-offset-side), y=135-(hoehe*45) ,height='45', width='45')
                    tmp.configure(image=self.img_cup_beer)
                    tmp.configure(borderwidth="0")
                    tmp.configure(background=self.background_color)
                    tmp.configure(command=functools.partial(self.cuppressed_hit, id=len(arr), idTeam=side))#need lambda to suppress instant activation 
                    arr.append(tmp)
                    
                    
                offset += int(45/2)

    def __init__(self,master, obj):
        
        self.master = master
        self.obj = obj
        self.master.geometry("800x600")
        self.img_cup_beer = PhotoImage(file="./cup.png")
        self.img_cup_water = PhotoImage(file="./cup_water.png")
        self.fontcolor = "white"
        self.background_color = "black"
        self.font = "Helvetica"
        self.fontsize_playername = 40
        self.fontsize_stats = 30


        self.frame_cups = Frame(self.master)
        self.frame_cups.place(x=90, y=190, height=200,width=600)
        self.frame_cups.configure(bg=self.background_color)
        
        self.frame_cups_home = Frame(self.frame_cups)
        self.frame_cups_home.place(x=10, y=10, width=235, height=180)

        self.frame_cups_away = Frame(self.frame_cups)
        self.frame_cups_away.place(x=355, y=10, width=235, height=180)
        self.bt_cups_home = []
        self.bt_cups_away = []
        self.createButtons(self.frame_cups_home,0,4,self.bt_cups_home)
        self.createButtons(self.frame_cups_away,190,4, self.bt_cups_away)
        
        self.var_spielstand = StringVar()
        self.var_spielstand.set("0:0")
        self.lb_spielstand = Label(self.frame_cups, textvariable=self.var_spielstand, fg=self.fontcolor,bg=self.background_color, font=(self.font, self.fontsize_stats))
        self.lb_spielstand.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.bt_overtime = Button(self.frame_cups, text="OT", command=self.overtime)
        self.bt_newgame = Button(self.frame_cups, text="New Game", command=self.newgame)
        

        #akuteller spielstand
        self.var_game_home = 0
        self.var_game_away = 0
        #ewiger spielstand
        self.home_cups_hit = 0
        self.home_cups_miss = 0
        self.away_cups_hit = 0
        self.away_cups_miss = 0
        
        self.master.mainloop()


    def cuppressed_hit(self, id, idTeam):
        if idTeam==0: # home
            self.bt_cups_home[id].place_forget()
            #really change display
            self.obj.bt_cups_home[id].place_forget()
            
            self.home_cups_hit +=1
            self.var_game_home +=1

            #check if rerack
            if self.var_game_home==4 or self.var_game_home==7 or self.var_game_home==9:
                #do rerack
                for i in self.bt_cups_home:
                    i.place_forget()
                for i in self.obj.bt_cups_home:
                    i.place_forget()
                self.obj.bt_cups_home.clear()    
                self.bt_cups_home.clear()
                if self.var_game_home==4: 
                    self.createButtons(self.frame_cups_home,0,3,self.bt_cups_home)
                    self.obj.createButtons(self.obj.frame_home,0,3,self.obj.bt_cups_home)
                if self.var_game_home==7: 
                    self.createButtons(self.frame_cups_home,0,2,self.bt_cups_home)
                    self.obj.createButtons(self.obj.frame_home,0,2,self.obj.bt_cups_home)

                if self.var_game_home==9: 
                    self.createButtons(self.frame_cups_home,0,1,self.bt_cups_home)
                    self.obj.createButtons(self.obj.frame_home,0,1,self.obj.bt_cups_home)


            
            
        else: # away
            self.bt_cups_away[id].place_forget()
            #really change display
            self.obj.bt_cups_away[id].place_forget()

            self.away_cups_hit +=1
            self.var_game_away +=1
            if self.var_game_away==4 or self.var_game_away==7 or self.var_game_away==9:
                #do rerack
                for i in self.bt_cups_away:
                    i.place_forget()
                for i in self.obj.bt_cups_away:
                    i.place_forget()
                self.obj.bt_cups_away.clear()    
                self.bt_cups_away.clear()
                if self.var_game_away==4: 
                    self.createButtons(self.frame_cups_away,190,3,self.bt_cups_away)
                    self.obj.createButtons(self.obj.frame_away,190,3,self.obj.bt_cups_away)
                if self.var_game_away==7: 
                    self.createButtons(self.frame_cups_away,190,2,self.bt_cups_away)
                    self.obj.createButtons(self.obj.frame_away,190,2,self.obj.bt_cups_away)

                if self.var_game_away==9: 
                    self.createButtons(self.frame_cups_away,190,1,self.bt_cups_away)
                    self.obj.createButtons(self.obj.frame_away,190,1,self.obj.bt_cups_away)  
            #really change display

        if self.var_game_home >=10 and self.var_game_away>=10:
            self.bt_overtime.place(relx=0.5, rely = 0.7, anchor=CENTER)
            self.bt_newgame.place(relx=0.5, rely = 0.9, anchor=CENTER)
        #check overtime
        self.updateDisplay()

    def cuppressed_miss(self, idTeam):
        if idTeam==0:
            self.home_cups_miss +=1
        else:
            self.away_cups_miss +=1

        self.updateDisplay()

    def overtime(self):
        for i in self.bt_cups_home:
            i.place_forget()
        for i in self.obj.bt_cups_home:
            i.place_forget()
        self.obj.bt_cups_home.clear()    
        self.bt_cups_home.clear()
        for i in self.bt_cups_away:
            i.place_forget()
        for i in self.obj.bt_cups_away:
            i.place_forget()
        self.obj.bt_cups_away.clear()    
        self.bt_cups_away.clear()
        

        self.createButtons(self.frame_cups_home,0,2,self.bt_cups_home)
        self.obj.createButtons(self.obj.frame_home,0,2,self.obj.bt_cups_home)

        self.createButtons(self.frame_cups_away,190,2,self.bt_cups_away)
        self.obj.createButtons(self.obj.frame_away,190,2,self.obj.bt_cups_away)
        self.updateDisplay()   
    def newgame(self):
        pass

    def updateDisplay(self):
        

        #build to strings
        #home
        percent = ""
        if (self.home_cups_miss+self.home_cups_hit)==0:
            percent = "100%"
        else:
            percent = '{0:.0%}'.format((self.home_cups_hit/(self.home_cups_miss+self.home_cups_hit)))
    
        self.obj.var_stats_heim.set(str(self.home_cups_hit)+":"+str(self.home_cups_miss)+" " + percent  )
        
        #away
        if (self.away_cups_miss+self.away_cups_hit)==0:
            percent1 = "100%"
        else:
            percent1 = '{0:.0%}'.format((self.away_cups_hit/(self.away_cups_miss+self.away_cups_hit)))
        self.obj.var_stats_auswaerts.set(str(self.away_cups_hit)+":"+str(self.away_cups_miss)+" " + percent1  )
        self.master.update()
        self.obj.master.update()

        #self.var_stats_auswaerts.set("0% 0/0")
        #self.var_stats_heim.set("0/0 0%")

        
    


class Einstellungen:
    
    def __init__(self,screen_einstellungen):
        self.master = screen_einstellungen
        aufloesungen = ["1920x200",]
        data=[] #nichts drinnen
        self.teams = []
        self.teams_player = []

        self.master.geometry("670x330")
        self.master.title("Bierpong Scoreboard - Einstellungen")
        

        self.lb_resolution = Label(screen_einstellungen, text="Auflösung")
        self.lb_resolution.place(relx=0.015, rely=0.2)
        self.cb_resolution = ttk.Combobox(screen_einstellungen, value=aufloesungen, state='readonly')
        self.cb_resolution.place(relx=0.2, rely=0.2)
    

        self.lb_hometeam = Label(screen_einstellungen, text="Heimteam")
        self.lb_hometeam.place(relx=0.015, rely=0.3)
        self.cb_hometeam = ttk.Combobox(screen_einstellungen, value=self.teams, postcommand = self.updateCB)
        self.cb_hometeam.place(relx=0.2, rely=0.3)


        self.lb_awayteam = Label(screen_einstellungen, text="Auswärtsteam")
        self.lb_awayteam.place(relx=0.015, rely=0.4)
        self.cb_awayteam = ttk.Combobox(screen_einstellungen, value=self.teams, postcommand = self.updateCB)
        self.cb_awayteam.place(relx=0.2, rely=0.4)


        self.lb_playerhome = Label(screen_einstellungen, text="Spieler-Heim")
        self.lb_playerhome.place(relx=0.6, rely=0.3)
        self.cb_playerhome = ttk.Combobox(screen_einstellungen, postcommand= self.updateCB_Home)
        self.cb_playerhome.place(relx=0.75, rely=0.3)


        self.lb_playeraway = Label(screen_einstellungen, text="Spieler-Auswärts")
        self.lb_playeraway.place(relx=0.6, rely=0.4)
        self.cb_playeraway = ttk.Combobox(screen_einstellungen, postcommand = self.updateCB_Away)
        self.cb_playeraway.place(relx=0.75, rely=0.4)


        self.bt_getdata = ttk.Button(screen_einstellungen, text="Lade Daten", command=self.getdata)
        self.bt_getdata.place(relx=0.55, rely=0.15, height=35, width=290)
        
        self.bt_newgame = ttk.Button(screen_einstellungen, text="New Game", command=self.newGame )
        self.bt_newgame.place(relx=0.45, rely=0.75,relwidth=0.3)

        self.sep_setting = ttk.Separator(screen_einstellungen)
        self.sep_setting.place(relx=0.3, rely=0.625, relwidth=0.1)

    def getdata(self):
        self.teams.clear()
        response = requests.get("https://bpbl.de/tabelle/")
        soup = BeautifulSoup(response.text, 'lxml')
        table = soup.find('table',{'class':'sp-league-table'})

        for href in table.find_all('a'):
            players = []
            self.teams.append(href.getText())
            #players.append(href.getText()) #teamname
            #print (href.get('href'))
            tmpurl = href.get('href')
            
            tmp_response = requests.get(tmpurl)
            soup = BeautifulSoup(tmp_response.text, 'lxml')
            tmp_table =  soup.find('table',{'class':'sp-player-list'})
            for player in tmp_table.find_all('a'):
                #clean female players from ♀
                tmp_player = player.getText()
                new_player = tmp_player.replace('♀',"")        
                players.append(new_player)
            #print (players)
            self.teams_player.append(players.copy())

    def newGame(self):
        #TODO implementierung doubles
        self.win = Toplevel(self.master)
        dis = Display(self.win, self.cb_resolution.get(),self.cb_playerhome.get(), self.cb_playeraway.get())
        self.win2 = Toplevel(self.win)
        Controller(self.win2, dis)
    
    def updateCB(self):
        
        self.cb_hometeam['values'] = self.teams.copy()
        self.cb_awayteam['values'] = self.teams.copy()
        
    def updateCB_Home(self):
        
        if len(self.cb_hometeam.get())>0:
            #get index of team
            
            self.cb_playerhome['values'] = self.teams_player[self.teams.index(self.cb_hometeam.get())].copy()

    def updateCB_Away(self):
        if len(self.cb_awayteam.get())>0:
            #get index of team
            
            self.cb_playeraway['values'] = self.teams_player[self.teams.index(self.cb_awayteam.get())].copy()

    
def main():
    

    #read from file saved data
    #give data to function if size zero - disable selection
    root = Tk()
    app = Einstellungen(root)
    root.mainloop()







if  __name__ == "__main__":
    main()
