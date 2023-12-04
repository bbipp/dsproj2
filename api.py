import requests
import sqlite3
from datetime import datetime
import time


##manage tables
connection = sqlite3.connect("pi.sqlite")
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS pi")

table = """ Create TABLE pi (
            factor NUMERIC,
            pi INTEGER,
            time DATE
        ); """
cursor.execute(table)

##loops to add to db
i = 1
while i <= 60:
    if datetime.now().second == 0:
        response = requests.get("https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi")
        cursor.execute("insert into 'pi' (factor, pi, time) VALUES (? ,?, ?)", (int(response.json()["factor"]), (response.json()["pi"]), response.json()["time"]))
        connection.commit()
        i += 1
        time.sleep(5) ##loops so fast that the if statement is true mutliple times a minute
        
    
connection.close()
