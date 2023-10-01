import tkinter as tk
import customtkinter as ctk
import ttkbootstrap as ttk
import iso3166 as iso
import datetime
from script import *
prays = []
# prevent button spam
lastcall = datetime.datetime.now()
def check_time():
    global lastcall
    diff = datetime.datetime.now() - lastcall
    if diff.microseconds + diff.seconds*1000000 > 1000000:
        lastcall = datetime.datetime.now()
        return True
    return False
# create timetable
    # comands


def button_comand():
   if check_time():
    error_label.place_forget()
    if len(prays) > 0: delete()
    timetable_close()
    window.after(500, lambda : get_data())
    window.after(700, timetable_open)
def delete():
    global prays
    for i in prays: 
        i.clear()
def get_data():
    times = ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']
    try:
        table = get_times(country_search.get(), city_search.get())
    except:
        error_label.place(relx = 0.5, rely=0.5, anchor = 'center')
    else:
        for i, j in table.items():
            if i in times : prays.append(Time(timetable_frame, i, j))
      
    # animations
def animate_underline():
    global line_w
    if line_w < 0.5:
        line_w += 0.012
        line.place_configure(relwidth=line_w)
        window.after(10, animate_underline)
def timetable_close():
    global time_y, time_relheight
    if time_relheight > 0.01:
        time_y += 0.01
        time_relheight -= 0.02
        timetable_frame.place_configure(rely=time_y, relheight=time_relheight)
        window.after(10, timetable_close)
def timetable_open():
    global time_y, time_relheight
    if time_relheight < 0.6:
      time_y -= 0.01
      time_relheight += 0.02
      timetable_frame.place_configure(rely=time_y, relheight=time_relheight)
      window.after(10, timetable_open)
      
      
#window 
window = ttk.Window(themename='vapor')
window.title('مواقيت الصلاة')
window.geometry('900x700+500+200')
window.resizable(False, False)

# vars
city = ttk.StringVar(value=None)
line_w = -0.15
time_y = 0.35
time_relheight = 0.6
countries = [c.name for c in iso.countries]

#frames
timetable_frame = ttk.Frame(window, style='darkly')
top_frame = ttk.Frame(window)
line = ctk.CTkFrame(top_frame, height=5, fg_color= 'white')
search_frame = ttk.Frame(window)
class Time(ttk.Frame):
    def __init__(self, master, time, value):
        super().__init__(master, bootstyle = 'warning')
        self.configure(bootstyle = 'superhero')
        self.key = ttk.Label(self, text = time, bootstyle='vapor')
        self.value = ttk.Label(self, text= value)
        self.pack(expand= True, fill = 'both', pady= 10, padx = 5)
        self.key.pack(side = 'left', padx = 10)
        self.value.pack(side = 'right', padx=10)
    def clear(self):
        self.pack_forget()




# widgets
label = ctk.CTkLabel(top_frame, text = 'Pray Times', font=('calibry', 30))
country_search = ttk.Combobox(search_frame, values=countries)
city_search = ctk.CTkEntry(search_frame, placeholder_text='type city for search...')
button = ttk.Button(search_frame, text = 'search', command=button_comand)
country_search.set('Egypt')
error_label = ttk.Label(timetable_frame, bootstyle= 'danger', text= 'Input Error...', font = 'calibry 25 bold')
# combobox = ctk.CTkComboBox(window, values=["option 1", "option 2"])




# layout
top_frame.place(x=0, y=0, relwidth=1, relheight=0.15)
label.place(relx = 0.5, rely = 0.5, anchor = 'center')
line.place(relx = 0.5, rely = 0.9, relwidth = line_w, anchor = 'center')
animate_underline()
timetable_frame.place(relx=0.2, rely= time_y, relheight=time_relheight, relwidth=0.6)
search_frame.place(relx = 0.1, rely=0.25, relwidth=0.8, relheight=0.05)
search_frame.rowconfigure(0, weight=1, uniform='a')
search_frame.columnconfigure((0,1), weight=7, uniform='a')
search_frame.columnconfigure((2), weight=4, uniform='a')
country_search.grid(row = 0, column = 0, sticky = 'nsew')
city_search.grid(row = 0, column = 1, sticky = 'nsew', padx = 10)
button.grid(row = 0, column = 2, sticky = 'nsew')


# binding
window.bind('<KeyPress-Return>', lambda _ : button_comand())
window.mainloop()