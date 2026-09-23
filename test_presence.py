from pypresence import Presence
import time

CLIENT_ID = "1548258204952043520"

rpc = Presence(CLIENT_ID)
rpc.connect()

rpc.update(
    details="Uploading README.txt about user...",
    state="[#################--------] 67%",
    start=None,
    end=None,
)

print("Rich Presence active.")

while True:
    time.sleep(15)