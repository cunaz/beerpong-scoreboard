
class becher:
    def __init__(self, identifier):
        self.identifier = identifier
        self.state = True
    def hit(self):
        self.state = False    
    def istHit(self):
        return self.state
    
class setting:
    def __init__(self):
        self.team = []
        self.teams_player=[]
        self.font = "Helvetica"


    def getdata(self):
        self.teams.clear()

        listligen = [["https://bpbl.de/tabellen/bundesliga/"],["https://bpbl.de/tabellen/2-bundesliga/"], ["https://bpbl.de/tabellen/3-bundesliga-a/"],["https://bpbl.de/tabellen/3-bundesliga-b/"],["https://bpbl.de/tabellen/4-bundesliga-a/"],["https://bpbl.de/tabellen/4-bundesliga-b/"],["https://bpbl.de/tabellen/4-bundesliga-c/"]  ]
        liganamen = ["Liga 1", "Liga 2", "Liga 3A","Liga 3B", "Liga 4A", "Liga 4B", "Liga 4C"]
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

    pass

class game:
    def __init__(self):
        self.playerH1



class Spieler:
    def __init__(self):
        self.Hit

