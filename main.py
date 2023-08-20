from tkinter import *
from datetime import datetime
import pytz


def update_timer(tz, country, block_name):
    time_zone = datetime.now(pytz.timezone(tz))
    country.itemconfig(block_name, text=time_zone.strftime("%H:%M:%S"))
    window.after(1000, update_timer, tz, country, block_name)


window = Tk()
window.config(pady=100, padx=100)
window.title("Time Zones")

title_label = Label()
title_label.config(text="Different Time Zones", font=("Arial", 30, "normal"))
title_label.grid(row=0, column=0, columnspan=2)

poland = Canvas()
poland.create_rectangle(50, 25, 300, 200, fill="blue")
poland.create_text(175, 50, text="Poland, Warsaw", font=("Arial", 20, "normal"), fill="white")
block_poland = poland.create_text(175, 100, font=("Arial", 15, "normal"), fill="white")
update_timer(tz='Europe/Warsaw', country=poland, block_name=block_poland)
poland.grid(column=0, row=1)

russia_moscow = Canvas()
russia_moscow.create_rectangle(50, 25, 300, 200, fill="green")
russia_moscow.create_text(175, 50, text="Russia, Moscow", font=("Arial", 20, "normal"), fill="white")
block_russia_moscow = russia_moscow.create_text(175, 100, font=("Arial", 15, "normal"), fill="white")
update_timer(tz='Europe/Moscow', country=russia_moscow, block_name=block_russia_moscow)
russia_moscow.grid(column=1, row=1)

us_new_york = Canvas()
us_new_york.create_rectangle(50, 25, 300, 200, fill="purple")
us_new_york.create_text(175, 50, text="USA, New York", font=("Arial", 20, "normal"), fill="white")
block_us_new_york = us_new_york.create_text(175, 100, font=("Arial", 15, "normal"), fill="white")
update_timer(tz='US/Eastern', country=us_new_york, block_name=block_us_new_york)
us_new_york.grid(column=0, row=2)

japan_tokyo = Canvas()
japan_tokyo.create_rectangle(50, 25, 300, 200, fill="black")
japan_tokyo.create_text(175, 50, text="Japan, Tokyo", font=("Arial", 20, "normal"), fill="white")
block_japan_tokyo = japan_tokyo.create_text(175, 100, font=("Arial", 15, "normal"), fill="white")
update_timer(tz='Asia/Tokyo', country=japan_tokyo, block_name=block_japan_tokyo)
japan_tokyo.grid(column=1, row=2)

window.mainloop()
