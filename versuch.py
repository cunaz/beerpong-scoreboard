
from tkinter import *
import tkinter.ttk as ttk
import requests
from bs4 import BeautifulSoup




class Einstellungen:
    
    def __init__(self,screen_einstellungen):
        self.master = screen_einstellungen
        aufloesungen = ["1920x1080",]
        data=[] #nichts drinnen
        self.teams = []
        self.teams_player = []

        self.master.geometry("670x330")
        self.master.title("Bierpong Scoreboard - Einstellungen")
        

        self.lb_resolution = Label(screen_einstellungen, text="Auflösung")
        self.lb_resolution.place(relx=0.015, rely=0.2)
        self.cb_resolution = ttk.Combobox(screen_einstellungen, value=aufloesungen)
        self.cb_resolution.place(relx=0.2, rely=0.2)
    

        self.lb_hometeam = Label(screen_einstellungen, text="Heimteam")
        self.lb_hometeam.place(relx=0.015, rely=0.3)
        self.cb_hometeam = ttk.Combobox(screen_einstellungen, value=self.teams, postcommand = self.updateCB)
        self.cb_hometeam.place(relx=0.2, rely=0.3)


        self.lb_awayteam = Label(screen_einstellungen, text="Auswärtsteam")
        self.lb_awayteam.place(relx=0.015, rely=0.4)
        self.cb_awayteam = ttk.Combobox(screen_einstellungen, value=self.teams, postcommand = self.updateCB)
        self.cb_awayteam.place(relx=0.2, rely=0.4)

#####################################
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
        
        self.bt_newgame = ttk.Button(screen_einstellungen, text="New Game", )
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
