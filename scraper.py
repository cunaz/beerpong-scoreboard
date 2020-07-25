import requests
from bs4 import BeautifulSoup

teams = []
response = requests.get("https://bpbl.de/tabelle/")
soup = BeautifulSoup(response.text, 'lxml')
table = soup.find('table',{'class':'sp-league-table'})
for row in table.find_all('a'):
    teams.append(row.getText())
#print(teams)
lTeams_url = []
for href in table.find_all('a'):
    print (href.get('href'))
    tmpurl = href.get('href')
    lTeams_url.append(href.get('href'))
    players = []
    tmp_response = requests.get(tmpurl)
    soup = BeautifulSoup(tmp_response.text, 'lxml')
    tmp_table =  soup.find('table',{'class':'sp-player-list'})
    for player in tmp_table.find_all('a'):
        #clean female players from ♀
        tmp_player = player.getText()
        new_player = tmp_player.replace('♀',"")        
        players.append(new_player)
    print (players)
    
    

