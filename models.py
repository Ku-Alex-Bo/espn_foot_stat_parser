from pydantic import BaseModel
from typing import List, Tuple

class Event(BaseModel):
  time: str
  type: str
  team: str
  score: List[int]
  player: str

class Foul(Event):
  pass

class Offside(Event):
  pass

class Corner(Event):
  pass

class Medical(BaseModel):
  time: str
  type: str
  score: int