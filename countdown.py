# from utils import now
# import asyncio
import datetime
import math
import time

# infinite loop for printing countdown
while True:
    for i in iter(int, 1):
        delta = datetime.datetime(2022, 7, 20) - datetime.datetime.now()
        hours = delta.seconds / 3600
        minutes = ((delta.seconds / 3600) % 1) * 60
        seconds = (minutes % 1) * 60
        y = "%s days, %s hours, %s minutes, and %s seconds."%(str(delta.days), str(math.floor(hours)), str(math.floor(minutes)), str(round(seconds)))
        print(f"y = {y}")
        time.sleep(1)

# debugging area
# for i in range(60):
#     delta = datetime.datetime(2022, 7, 20) - datetime.datetime.now()
#     hours = delta.seconds / 3600
#     minutes = ((delta.seconds / 3600) % 1) * 60
#     seconds = (minutes % 1) * 60
#     print("floor: ", round(seconds), "seconds | act: ", seconds)
#     time.sleep(1)
#     i+=1

      
      
# async def foo():
#  while True:
#    await asyncio.sleep(1)
#    output = x
#    Element("outputDiv2").write(output)
