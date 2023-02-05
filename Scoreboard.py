
from tkinter import *
import tkinter.ttk as ttk
from bs4 import BeautifulSoup
import functools
import grequests
#test
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
                tmp.place(x=  abs(190-(breite*45)-offset-side-(round(abs(rows-4)*(45/2)))), y=135-(hoehe*45) ,height='45', width='45')
                tmp.configure(image=self.img_cup_beer)
                tmp.configure(borderwidth="0")
                tmp.configure(background=self.background_color)
                arr.append(tmp)
            offset += int(45/2)

    
    def __init__(self, master, aufloesung, playerhome, playeraway, playerhome2, playeraway2):
        #self.master = Toplevel(master)
        self.fontcolor = "white"
        self.background_color = "black"
        self.font = "Bebas Kai"
        
        self.fontsize_stats = 30
        self.var_spieler_heim = StringVar()
        self.var_spieler_auswaerts = StringVar()
        
        if len(playerhome2)>0:
            tmp = ""
            tmp += playerhome + "/" + playerhome2
            self.var_spieler_heim.set(tmp)
            tmp= ""
            tmp += playeraway + "/" + playeraway2
            self.var_spieler_auswaerts.set(tmp)
            self.fontsize_playername = 22
        else:
            self.fontsize_playername = 40
            self.var_spieler_heim.set(playerhome)
            self.var_spieler_auswaerts.set(playeraway)
        
        
        
        self.var_stats_heim = StringVar()
        self.var_stats_auswaerts = StringVar()
        self.var_stats_auswaerts.set("0% 0/0")
        self.var_stats_heim.set("0/0 0%")
        self.var_stats_heim_set = StringVar()
        self.var_stats_auswaerts_set = StringVar()
        self.var_stats_heim_set.set("0/0 0%")
        self.var_stats_auswaerts_set.set("0/0 0%")


        self.img_cup_beer_base = """iVBORw0KGgoAAAANSUhEUgAAAC0AAAAtCAYAAAA6GuKaAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAFfSURBVGhD7ZjbEYMgEEXFCtJTKkllqSQ9pQMiI0wU3d278hLH8xO/2MP1qkOMtXbIgjHyQtYaf5VEmjQiSpGwAb10iiiFcgOj/8UoIexQroslXUp2DyB1Oemawg5gHp+0Uvj7fvqrLY/Xx1+BMInT0qAwJ0oBb4AQ35cGhI/IxkDyO+JbaUE4h2yMKB+Jq155JYQd2nXX0kzKpYQD7PqR11+6oXAAFdd9EU+CKF0r5QAyb5YW3hinwXuySddOOSDN7bTTvVQjMPmSSbeqRoCb32k9OuSWrsUtXQtSWn2myww3f0SO7Kdi8r1ep1tVRJo7S/dSEe8p1qN22si8zjvNVKRW2uychd866YbiqLBDVY9S4tp1L/JfXgA8hh2Rh5Ml6kpLO5TnR24D6moxzxcv7Whx8GWEHfKDKCyQHWCenPSSkqkrwtF9EUulrlxXl3RMSvIJAaRJL0E2kOVODcMPZGW3H7oNvYMAAAAASUVORK5CYII="""
        self.img_cup_beer = PhotoImage(data=self.img_cup_beer_base)
        self.img_cup_water_base = """iVBORw0KGgoAAAANSUhEUgAAAC0AAAAtCAYAAAA6GuKaAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAFeSURBVGhD7ZhLEoMgEETFG+R42eVo2eV4OQKREiqKzkyP/MTybeKKebStFjHW2iELxsgLWWv8VRJp0ogoRcIG9NIpohTKDYz+F6OEsEO5LpZ0Kdk9gNTlpGsKO4B5fNJK4dfn66+2vJ8PfwXCJE5Lg8KcKAW8AUJ8XxoQPiIbA8nviG+lBeEcsjGifCSueuWVEHZo111LMymXEg6w60def+mGwgFUXPdFPAmidK2UA8i8WVp4Y5wG78kmXTvlgDS30073Uo3A5Esm3aoaAW5+p/XokFu6Frd0LUhp9ZkuM9z8ETmyn4rJ93qdblURae4s3UtFvKdYj9ppI/M67zRTkVpps3MWfuukG4qjwg5VPUqJa9e9yH95AfAYdkQeTpaoKy3tUJ4fuQ2oq8U8X7y0o8XBlxF2yA+isEB2gHly0ktKpq4IR/dFLJW6cl1d0jEpyScEkCa9BNlAljs1DD+vILcf1CsOlgAAAABJRU5ErkJggg=="""
        self.img_cup_water = PhotoImage(data=self.img_cup_water_base)
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
        #percentage all games
        self.lb_stats_heim = Label(self.master, textvariable=self.var_stats_heim, fg=self.fontcolor, bg=self.background_color, font=(self.font, self.fontsize_stats) )
        self.lb_stats_heim.place(relx=0, rely=0.5, anchor=NW)
        self.lb_stats_auswaerts = Label(self.master, textvariable=self.var_stats_auswaerts, fg=self.fontcolor, bg=self.background_color, font=(self.font, self.fontsize_stats))
        self.lb_stats_auswaerts.place(relx=1, rely=0.5, anchor=NE)
        #percentage per game
        self.lb_stats_heim_set = Label(self.master, textvariable=self.var_stats_heim_set, fg=self.fontcolor, bg=self.background_color, font=(self.font, self.fontsize_stats-8))
        self.lb_stats_heim_set.place(relx=0, rely=0.75, anchor=NW)
        self.lb_stats_auswaerts_set = Label(self.master, textvariable=self.var_stats_auswaerts_set, fg=self.fontcolor, bg=self.background_color, font=(self.font, self.fontsize_stats-8))
        self.lb_stats_auswaerts_set.place(relx=1, rely=0.75, anchor=NE)


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
        self.lb_spielstand = Label(self.frame1, textvariable=self.var_spielstand, fg=self.fontcolor,bg=self.background_color, font=(self.font, self.fontsize_stats+10))
        self.lb_spielstand.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.var_satz = StringVar()
        self.var_satz.set("0:0")
        self.lb_satz = Label(self.frame1, textvariable=self.var_satz,fg=self.fontcolor,bg=self.background_color, font=(self.font, self.fontsize_stats) )
        self.lb_satz.place(relx=0.5, rely=0.2, anchor=CENTER)


        #TODO Skalierbarkeit der Breite
        
        self.var_wongames_home = StringVar()
        self.var_wongames_away = StringVar()

        self.la_games_home = Label(self.master, textvariable=self.var_wongames_home, fg=self.fontcolor, bg=self.background_color, font=(self.font, 18) )
        self.la_games_home.place(relx=0.32, rely=0.2, anchor=CENTER)
        self.la_games_away = Label(self.master, textvariable=self.var_wongames_away, fg= self.fontcolor, bg=self.background_color, font=(self.font, 18))
        self.la_games_away.place(relx=0.68, rely=0.2, anchor=CENTER)

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
        self.img_cup_beer = self.obj.img_cup_beer
        self.img_cup_water = self.obj.img_cup_water
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

        self.var_satz = StringVar()
        self.var_satz.set("0:0")
        self.lb_satz = Label(self.frame_cups, textvariable=self.var_satz,fg=self.fontcolor,bg=self.background_color, font=(self.font, self.fontsize_stats+10) )
        self.lb_satz.place(relx=0.5, rely=0.2, anchor=CENTER)


        self.bt_overtime = Button(self.frame_cups, text="OT", command=self.overtime)
        self.bt_newgame = Button(self.frame_cups, text="New Game", command=self.newgame)
        
        #TODO
        #self.bt_edit_score = Button(self.master, text="Satz manuell eingeben", command=self.editscore)
        #self.bt_edit_score.place(relx= 0.1, rely= 0.7)
        


        self.ergebnisse = []
        #aktuelle sätze
        self.var_satz_home = 0
        self.var_satz_away = 0
        #akuteller spielstand
        self.var_game_home = 0
        self.var_game_away = 0
        #ewiger hits
        self.home_cups_hit = 0
        self.home_cups_miss = 0
        self.away_cups_hit = 0
        self.away_cups_miss = 0
        #ewige hits pro satz
        self.home_cups_hit_set = 0
        self.home_cups_miss_set = 0
        self.away_cups_hit_set = 0
        self.away_cups_miss_set = 0
        
        self.master.mainloop()

    def editscore(self):
        pass

    def cuppressed_hit(self, id, idTeam):
        if idTeam==0: # home
            self.bt_cups_home[id].place_forget()
            #really change display
            self.obj.bt_cups_home[id].place_forget()
            
            self.home_cups_hit +=1
            self.var_game_home +=1
            self.home_cups_hit_set +=1

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

            #rerack in der overtime
            if self.var_game_home >10 and self.var_game_home%3==0: 
                for i in self.bt_cups_home:
                    i.place_forget()
                for i in self.obj.bt_cups_home:
                    i.place_forget()
                self.obj.bt_cups_home.clear()    
                self.bt_cups_home.clear()
                self.createButtons(self.frame_cups_home,0,1,self.bt_cups_home)
                self.obj.createButtons(self.obj.frame_home,0,1,self.obj.bt_cups_home)

  
        else: # away
            self.bt_cups_away[id].place_forget()
            #really change display
            self.obj.bt_cups_away[id].place_forget()

            self.away_cups_hit +=1
            self.var_game_away +=1
            self.away_cups_hit_set +=1

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
            
            #rerack in der overtime
            if self.var_game_away>10 and (self.var_game_away%3)==0: 
                for i in self.bt_cups_away:
                    i.place_forget()
                for i in self.obj.bt_cups_away:
                    i.place_forget()
                self.obj.bt_cups_away.clear()    
                self.bt_cups_away.clear()
                self.createButtons(self.frame_cups_away,190,1,self.bt_cups_away)
                self.obj.createButtons(self.obj.frame_away,190,1,self.obj.bt_cups_away)
            
            
            
            
            #really change display

         

        if self.var_game_home >=10 or self.var_game_away>=10:
            self.bt_overtime.place(relx=0.5, rely = 0.7, anchor=CENTER)
            self.bt_newgame.place(relx=0.5, rely = 0.9, anchor=CENTER)
        #check overtime
        self.updateDisplay()

    def cuppressed_miss(self, idTeam):
        if idTeam==0:
            self.home_cups_miss +=1
            self.home_cups_miss_set +=1
        else:
            self.away_cups_miss +=1
            self.away_cups_miss_set +=1

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

        tmp = ""
        self.ergebnisse.append(tmp)
        if self.var_game_home>self.var_game_away:
            tmp = self.obj.var_wongames_home.get()
            tmp += " " + str(self.var_game_home)+":"+str(self.var_game_away)
            self.obj.var_wongames_home.set(tmp)

            #satz wird geändert
            self.var_satz_home += 1
        else:
            tmp = self.obj.var_wongames_away.get()
            tmp += " " + str(self.var_game_home)+":"+str(self.var_game_away)
            self.obj.var_wongames_away.set(tmp)
            self.var_satz_away += 1

        tmp = ""
        tmp = str(self.var_satz_home)+ ":" + str(self.var_satz_away)
        self.var_satz.set(tmp)
        self.obj.var_satz.set(tmp)


        self.var_game_home = 0
        self.var_game_away = 0

        #percentage pro satz reset
        self.home_cups_hit_set = 0
        self.home_cups_miss_set = 0
        self.away_cups_hit_set = 0
        self.away_cups_miss_set = 0 
        
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

        self.createButtons(self.frame_cups_home,0,4,self.bt_cups_home)
        self.obj.createButtons(self.obj.frame_home,0,4,self.obj.bt_cups_home)

        self.createButtons(self.frame_cups_away,190,4,self.bt_cups_away)
        self.obj.createButtons(self.obj.frame_away,190,4,self.obj.bt_cups_away)
        
        self.bt_newgame.place_forget()
        self.bt_overtime.place_forget()

        self.updateDisplay()

    def updateDisplay(self):
        

        #build to strings
        #home
        percent = ""
        if (self.home_cups_miss+self.home_cups_hit)==0:
            percent = "100%"
        else:
            percent = '{0:.0%}'.format((self.home_cups_hit/(self.home_cups_miss+self.home_cups_hit)))
    
        self.obj.var_stats_heim.set(str(self.home_cups_hit)+":"+str(self.home_cups_miss)+" " + percent  )
        #stats pro satz
        if (self.home_cups_miss_set+self.home_cups_hit_set)==0:
            percent = "100%"
        else:
            percent = '{0:.0%}'.format((self.home_cups_hit_set/(self.home_cups_hit_set+self.home_cups_miss_set)))
        self.obj.var_stats_heim_set.set(str(self.home_cups_hit_set)+":"+str(self.home_cups_miss_set)+ " " + percent)

        #away
        if (self.away_cups_miss+self.away_cups_hit)==0:
            percent1 = "100%"
        else:
            percent1 = '{0:.0%}'.format((self.away_cups_hit/(self.away_cups_miss+self.away_cups_hit)))
        self.obj.var_stats_auswaerts.set(str(self.away_cups_hit)+":"+str(self.away_cups_miss)+" " + percent1  )
        #stats pro satz
        if (self.away_cups_miss_set+self.away_cups_hit_set)==0:
            percent = "100%"
        else:
            percent = '{0:.0%}'.format((self.away_cups_hit_set/(self.away_cups_hit_set+self.away_cups_miss_set)))
        self.obj.var_stats_auswaerts_set.set(str(self.away_cups_hit_set)+":"+str(self.away_cups_miss_set)+ " " + percent)




        stand = ""
        stand = str(self.var_game_home)+":"+str(self.var_game_away)
        self.var_spielstand.set(stand)
        self.obj.var_spielstand.set(stand)
        
        self.master.update()
        self.obj.master.update()

        #self.var_stats_auswaerts.set("0% 0/0")
        #self.var_stats_heim.set("0/0 0%")

        
    


class Einstellungen:
    
    def __init__(self,screen_einstellungen):
        self.master = screen_einstellungen
        aufloesungen = ["1920x200",]
        self.teams = []
        self.teams_player = []
        
        self.master.geometry("670x330")
        self.master.title("Bierpong Scoreboard - Einstellungen")        
        self.lb_resolution = Label(self.master, text="Auflösung")
        self.lb_resolution.place(relx=0.015, rely=0.2)
        self.cb_resolution = ttk.Combobox(self.master, value=aufloesungen, state='readonly')
        self.cb_resolution.place(relx=0.2, rely=0.2)
    

        self.lb_hometeam = Label(self.master, text="Heimteam")
        self.lb_hometeam.place(relx=0.015, rely=0.3)
        self.cb_hometeam = ttk.Combobox(self.master, value=self.teams, postcommand = self.updateCB)
        self.cb_hometeam.place(relx=0.2, rely=0.3)


        self.lb_awayteam = Label(self.master, text="Auswärtsteam")
        self.lb_awayteam.place(relx=0.015, rely=0.4)
        self.cb_awayteam = ttk.Combobox(self.master, value=self.teams, postcommand = self.updateCB)
        self.cb_awayteam.place(relx=0.2, rely=0.4)


        self.lb_playerhome = Label(self.master, text="Spieler-Heim")
        self.lb_playerhome.place(relx=0.54, rely=0.3)
        self.cb_playerhome = ttk.Combobox(self.master, postcommand= self.updateCB_Home)
        self.cb_playerhome.place(relx=0.75, rely=0.3)


        self.lb_playeraway = Label(self.master, text="Spieler-Auswärts")
        self.lb_playeraway.place(relx=0.54, rely=0.4)
        self.cb_playeraway = ttk.Combobox(self.master, postcommand = self.updateCB_Away)
        self.cb_playeraway.place(relx=0.75, rely=0.4)


        self.bt_getdata = ttk.Button(self.master, text="Lade Daten", command=self.getdata)
        self.bt_getdata.place(relx=0.55, rely=0.15, height=35, width=290)
        
        self.bt_newgame = ttk.Button(self.master, text="New Game", command=self.newGame )
        self.bt_newgame.place(relx=0.45, rely=0.75,relwidth=0.3)

        self.sep_setting = ttk.Separator(self.master)
        self.sep_setting.place(relx=0.333, rely=0.666, relwidth=0.333)

        self.var_double = IntVar()
        self.bt_doubles = Checkbutton(self.master, text="Doppel", variable = self.var_double, onvalue=1, offvalue=0 , command=self.checkDoubles)
        self.bt_doubles.place(relx=0.2, rely=0.5)

        self.lb_playerhome_2 = Label(self.master, text="Spieler-Heim-Doppel")
        self.lb_playerhome_2.place(relx=0.54, rely=0.5)
        self.cb_playerhome_2 = ttk.Combobox(self.master, postcommand= self.updateCB_Home, state=DISABLED)
        self.cb_playerhome_2.place(relx=0.75, rely=0.5)


        self.lb_playeraway_2 = Label(self.master, text="Spieler-Auswärts-Doppel")
        self.lb_playeraway_2.place(relx=0.54, rely=0.6)
        self.cb_playeraway_2 = ttk.Combobox(self.master, postcommand = self.updateCB_Away, state=DISABLED)
        self.cb_playeraway_2.place(relx=0.75, rely=0.6)


    def checkDoubles(self):
        if self.var_double.get() == 1:
            self.cb_playerhome_2.configure(state=NORMAL)
            self.cb_playeraway_2.configure(state=NORMAL)
        else:
            self.cb_playerhome_2.configure(state=DISABLED)
            self.cb_playeraway_2.configure(state=DISABLED)
            self.cb_playeraway_2.set("")
            self.cb_playerhome_2.set("")

    def getdata(self):
        self.teams.clear()

        listligen = [["https://bpbl.de/tabellen/bundesliga/"],["https://bpbl.de/tabellen/2-bundesliga/"], ["https://bpbl.de/tabellen/3-bundesliga-a/"],["https://bpbl.de/tabellen/3-bundesliga-b/"],["https://bpbl.de/tabellen/4-bundesliga-a/"],["https://bpbl.de/tabellen/4-bundesliga-b/"],["https://bpbl.de/tabellen/4-bundesliga-c/"], ["https://bpbl.de/tabellen/4-bundesliga-d/"]  ]
        liganamen = ["Liga 1", "Liga 2", "Liga 3A","Liga 3B", "Liga 4A", "Liga 4B", "Liga 4C", "Liga 4D"]
        for count,i in enumerate(listligen):
            platzhalter = "------- {0} ------".format(liganamen[count])
            self.teams.append(platzhalter)
            self.teams_player.append([])
            	
            #domains = ["https://bpbl.de/tabellen/bundesliga/"]
            req = (grequests.get(u) for u in i )
            response = grequests.map(req)
            soup = BeautifulSoup(response[0].text, 'lxml')
            table = soup.find('table',{'class':'sp-league-table'})
        

            l_teamurls = []
            l_requests = []
            for href in table.find_all('a'):
                #fill team list
                self.teams.append(href.getText())
                l_teamurls.append(href.get('href'))
            for i in l_teamurls:
                l_requests.append(grequests.get(i))
                
            responses = grequests.map(l_requests)
            for resp in responses:
                players = []
                soup = BeautifulSoup(resp.text, 'lxml')
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
        dis = Display(self.win, self.cb_resolution.get(),self.cb_playerhome.get(), self.cb_playeraway.get(), self.cb_playerhome_2.get(), self.cb_playeraway_2.get())
        self.win2 = Toplevel(self.win)
        Controller(self.win2, dis)
    
    def updateCB(self):
        
        self.cb_hometeam['values'] = self.teams.copy()
        self.cb_awayteam['values'] = self.teams.copy()
        
    def updateCB_Home(self):
        
        if len(self.cb_hometeam.get())>0:
            #get index of team
            
            self.cb_playerhome['values'] = self.teams_player[self.teams.index(self.cb_hometeam.get())].copy()
            self.cb_playerhome_2['values'] = self.teams_player[self.teams.index(self.cb_hometeam.get())].copy()


    def updateCB_Away(self):
        if len(self.cb_awayteam.get())>0:
            #get index of team
            
            self.cb_playeraway['values'] = self.teams_player[self.teams.index(self.cb_awayteam.get())].copy()
            self.cb_playeraway_2['values'] = self.teams_player[self.teams.index(self.cb_awayteam.get())].copy()

    
def main():
    

    #read from file saved data
    #give data to function if size zero - disable selection
    root = Tk()
    app = Einstellungen(root)
    root.mainloop()



if  __name__ == "__main__":
    main()
