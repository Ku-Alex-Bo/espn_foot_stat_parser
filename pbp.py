from models import *
from typing import List
import re

#Класс PBP для получения play-by-play в виде массива объектов Event
class PBP:
  _event_list = None
  _team_1 = None
  _team_2 = None

  _corner_score = [0,0]
  _offside_score = [0,0]

  _res_list = []

  def __init__(self, event_list: List[tuple], team_1: str, team_2: str) -> None:
    self._event_list = event_list
    self._team_1 = team_1
    self._team_2 = team_2

  def __call__(self) -> List[Event]:
    for event in reversed(self._event_list):
      if "Offside" in event[1]:
        self.insert_offside(event)
        continue
    return self._res_list

  #Функции вставки event объектов
  #Добавляем оффсайд
  def insert_offside(self, event: tuple[str,str]) -> None:
    cur_team = self._team_1 if self._team_1 in event[1] else self._team_2

    #Прибавляем счет
    if cur_team == self._team_1:
      self._offside_score[0]+=1
    else:
      self._offside_score[1]+=1

    #Находим игрока
    player_pattern = fr"(?<={cur_team}\.).*(?=is caught offside)"
    player_match = re.search(string = event[1], pattern = player_pattern)

    offside = {
        "time": event[0],
        "team": cur_team,
        "score": self._offside_score,
        "player": player_match.group().strip()
    }

    self._res_list.append(
        Offside(**offside)
    )
