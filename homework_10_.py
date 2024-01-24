import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime

def get_weather():
    url = "https://ua.sinoptik.ua/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    temperature_element = soup.find("p", class_="today-temp")
    temperature = temperature_element.text.strip() if temperature_element else None

    return temperature

def save_to_database(date_time, temperature):
    connection = sqlite3.connect("weather_database.db")
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS weather_data 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                       date_time TEXT, 
                       temperature TEXT)''')

    cursor.execute("INSERT INTO weather_data (date_time, temperature) VALUES (?, ?)", (date_time, temperature))

    connection.commit()

    connection.close()

if __name__ == "__main__":
    current_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    current_temperature = get_weather()

    if current_temperature:
        save_to_database(current_date_time, current_temperature)
        print("Дані успішно збережено.")
    else:
        print("Не вдалося отримати дані про температуру.")


