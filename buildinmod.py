import math
import random
import datetime
import os
import sys
import json
import time
print("Value of pi:", math.pi)
print("Random choice from list:", random.choice(['app', 'bat', 'cat']))
today = datetime.date.today()
print("Today's date:", today)
print("Current working directory:", os.getcwd())
print("Python version:", sys.version)
data = {"name": "Trisha", "age": 20}
json_str = json.dumps(data)
print("Python dict to json str:", json_str)
print("Current time in seconds ", time.time())
