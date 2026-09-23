import random, time
from time_manager import get_current_time

with open("progress.txt", "r") as file:
    percent_value = int(file.read())


# Idő managelés
while True:
     print("Uploading README.txt about user...\n")
# percent_value = 50 #temporary tesztelési érték

# A random +-x% ugrás
     upload_jump = random.randint(-5, 5)


     if upload_jump == 0:
      print("README.txt has been corrupted. Upload will automatically restart in 24 hours.")

    # A limitek és bounce-back
     else:
          checking_value = percent_value + upload_jump

          if checking_value >= 100:
            print("Overupload error (code 7_OUL). Recovering data from last checkpoint...")
            recovery_drop = random.randint(5, 7)
            percent_value = percent_value - recovery_drop

          elif checking_value <= 0:
            print("File disappeared error (code 7_FNF). Restartin upload from new directory...")
            recovery_boost = random.randint(2, 10)
            percent_value = percent_value + recovery_boost

          else:
               percent_value = checking_value


          with open("progress.txt", "w") as file:
            file.write(str(percent_value)) 

    #print(percent_value)

    # ASCII feltöltés bar
     bar_length = 25
     filled = round(bar_length * (percent_value / 100))
     empty = bar_length - filled

     print("[" + "#"*filled + "-"*empty +"]" + " " + str(percent_value) + "%")


   #else: 
       #print("NO UPDATE YET")
