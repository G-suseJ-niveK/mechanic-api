from datetime import time
from typing import Optional, List
from pydantic import BaseModel
from configs.environment import Config
import pytz

# env
tz = pytz.timezone(Config.TIME_ZONE)

class TemplateApiInsertSchema(BaseModel) :
  time : float
  count : int
  data : List[dict]
