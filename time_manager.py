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
if Path("last_update.txt").exists():
    print("VAN BAZDMEG")
    loaded_time = load_last_update()
    print(loaded_time)

else:
    save_last_update(current_time)