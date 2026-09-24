from datetime import datetime, timedelta
from pathlib import Path

def get_current_time():
    return datetime.now()

def load_last_update():
    with open("last_update.txt", "r") as file:
        last_update = file.read()

    last_update = datetime.fromisoformat(last_update)
    return last_update

def save_last_update(time_update):
    with open("last_update.txt", "w") as file:
        file.write(str(time_update))

current_time = get_current_time()
if Path("last_update.txt").exists() and Path("last_update.txt").stat().st_size > 0:
    loaded_time = load_last_update()

else:
    save_last_update(current_time)
    loaded_time = current_time

# At this point, the project was GitHubbed. Date: 2026.09.23

elapsed_time = current_time - loaded_time
def update_check(elapsed_time):
    if elapsed_time >= timedelta(hours=30):
        return "ERROR_EVENT"

    elif elapsed_time >= timedelta(hours=24):
        return "UPDATE"

    else:
        return "WAIT"

update_status = update_check(elapsed_time)