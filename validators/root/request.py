from typing import Optional
from pydantic import BaseModel
from configs.environment import Config
import pytz

# env
tz = pytz.timezone(Config.TIME_ZONE)

class TemplateApiInsertSchema(BaseModel) :
  name1 : Optional[str]
  name2 : dict
  name3 : str
