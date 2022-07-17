# from utils import now
# import asyncio
import datetime
import math
import time

# infinite loop for printing countdown
while True:
    for i in iter(int, 1):
        delta = datetime.datetime(2022, 7, 20) - datetime.datetime.now()
        if delta.days == 1:
            daystxt = " day, "
        else:
            daystxt = " days, "
        hours = delta.seconds / 3600
        if hours == 1:
            hourstxt = " hour, "
        else:
            hourstxt = " hours, "
        minutes = ((delta.seconds / 3600) % 1) * 60
        if minutes == 1:
            minutestxt = " minute, and "
        else:
            minutestxt = " minutes, and "
        seconds = (minutes % 1) * 60
        if round(seconds) == 1:
            secondstxt = " second."
        else:
            secondstxt = " seconds."
        x = str(delta.days) + daystxt + str(math.floor(hours)) + hourstxt + str(math.floor(minutes)) + minutestxt + str(round(seconds)) + secondstxt
        print(f"x = {x}")
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
