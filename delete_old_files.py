import os
import schedule
import time
from datetime import datetime, timedelta

def delete_old_files():
    print("Deleting old files...")
    directory = './images'
    cutoff = datetime.now() - timedelta(seconds=10)
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        modified_time = datetime.fromtimestamp(os.path.getmtime(filepath))
        if modified_time < cutoff:
            os.remove(filepath)

schedule.every().minutes.at(":10").do(delete_old_files)  # run at midnight every day

while True:
    schedule.run_pending()
    time.sleep(1)