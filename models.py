from pydantic import BaseModel
from typing import List, Tuple

class Event(BaseModel):
  time: str
  team: str
  score: List[int]
  player: str

class Foul(Event):
  pass

class Offside(Event):
  pass

class Corner(Event):
  pass