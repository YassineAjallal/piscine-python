import time
import datetime


seconds = time.time()
date = datetime.datetime.now()
date.strftime("%B")
print(f"Seconds since January 1, 1970: {'{:,}'.format(seconds)} or {'{:e}'.format(seconds)} in scientific notation")
print(f"{date.strftime('%b %d %Y')}")