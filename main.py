import requests
from bs4 import BeautifulSoup
from pbp import PBP

url = "https://www.espn.com/soccer/commentary/_/gameId/704826"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

###
events = []
###

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    comments = soup.find_all(class_='MatchCommentary__Comment')
    teams = soup.find_all(class_="ScoreCell__TeamName ScoreCell__TeamName--displayName db")
    team_1 = teams[0].text.strip()
    team_2 = teams[1].text.strip()

    for comment in comments:
        time = comment.find(class_='MatchCommentary__Comment__Timestamp').text.strip()
        event = comment.find(class_='MatchCommentary__Comment__GameDetails').text.strip()
        events.append((time, event))
else:
    print(f"Не удалось загрузить страницу. Статус: {response.status_code}")

pbp = PBP(events, team_1 = team_1, team_2=team_2)
res = pbp()

for elem in res:
    print(elem)