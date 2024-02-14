import customtkinter
import psutil
import requests
import json
from tkinter import ttk
import time
import threading
import os
import images.image as images
import sys

# --> Setting gernal aspects of custom Tkinter:

#set Appearance Mode to the operating System default value
customtkinter.set_appearance_mode("dark")

#set default color theme
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

# Deactivate automatic scaling
customtkinter.deactivate_automatic_dpi_awareness()

bild = images.start_image

# --> Initalizing methods:

#stop function called when closing window:
def exit():
    sys.exit()

# Function showing current System Resoruces:
def update_resources():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    cpu_label.configure(text=f"CPU: {cpu_usage}%")
    ram_label.configure(text=f"Memory: {memory_usage}%")
    app.after(1000, update_resources)  # Update every second    

# Setting "Light" Theme:
def theme_change_light():

    customtkinter.set_appearance_mode("light")
    button_light_theme.place_forget()
    button_dark_theme.place(x=5,y=450)

# Setting "Dark" Theme:
def theme_change_dark():

    customtkinter.set_appearance_mode("dark")
    button_dark_theme.place_forget()
    button_light_theme.place(x=5,y=450)

# Theme Change Function:
def theme_change(choice):

    print("optionmenu dropdown clicked:", choice)

    if choice == "Auto (System default)":
        customtkinter.set_appearance_mode("system")

    if choice == "Dark":
        customtkinter.set_appearance_mode("dark")

    if choice == "Light":
        customtkinter.set_appearance_mode("light")

# "Home" Button Action:
def home_button_action():
    about_frame.place_forget()
    settings_frame.place_forget()
    main_frame.place(x=150,y=0)

# "About" Button Action:
def about_button_action():
    main_frame.place_forget()
    settings_frame.place_forget()
    about_frame.place(x=150,y=0)

# "Settings" Button Action:
def settings_button_action():
    main_frame.place_forget()
    about_frame.place_forget()
    settings_frame.place(x=150,y=0)

# "Start" Button Action:
def start_button_action():
    url= "http://localhost/start"
    
    try:
        response = requests.post(url)
    
        if response.status_code == 200:
            buffer = json.loads(response.text)
            status_label.configure(text=f"Running: {buffer["running"]}", fg_color="green")
    except:
        status_label.configure(text=f"Unable to reach Server", fg_color="#990000")

def stop_button_action():
    url= "http://localhost/stop"
    
    try:
        response = requests.post(url)

        if response.status_code == 200:
            buffer = json.loads(response.text)
            status_label.configure(text=f"Running: {buffer["running"]}", fg_color="red")
    except:
        status_label.configure(text=f"Unable to reach Server", fg_color="#990000")

# Import Links to the Database:
def import_button_action():
    background_thread = threading.Thread(target=reset)
    link= link_entry.get()
    url= f"http://localhost/add?link={link}"
    
    try:
        response = requests.post(url)
        buffer = json.loads(response.text)
        print(buffer)
        
        if buffer['success'] == True:
            import_status_label.configure(text="Link imported successfully", fg_color="green")
        elif buffer["success"] == False:
            import_status_label.configure(text=f"Error during importing: {buffer["error"]}", fg_color="red")
        import_status_label.place(x=10, y=45)
        getlinks()
 
    except:
        import_status_label.configure(text="Error during importing", fg_color="red")
        import_status_label.place(x=10, y=45)
        getlinks()

    background_thread.start()
# Get all links from Database:
def getlinks():
    url = "http://localhost/blocked"

    response = requests.get(url)
    data = json.loads(response.text)
    id=1
    if table.get_children():
        table.delete(*table.get_children())
    for element in data:
        table.insert(parent='',index='end',text='', values=(id,element))
        id = id +1
    
def on_select(event):
    selected_item = table.selection()[0]
    values = table.item(selected_item, 'values')
    print(values)

def change_window_scaling(choice):
    scale = int(choice)
    scale = scale /100
    customtkinter.set_window_scaling(scale)
    customtkinter.set_widget_scaling(scale)
    table.column_stretch = 1.25
    table.row_stretch = 1.25

def remove_rows():
    background_thread = threading.Thread(target=reset)
    item_id = table.selection()[0]
    link = table.item(item_id)["values"][1]

    url= f"http://localhost/delete?link={link}"
    
    try:
        response = requests.delete(url)
        buffer = json.loads(response.text)
        
        if buffer['success'] == True:
            remove_button.configure(text="Deleted", fg_color="red")
        elif buffer["success"] == False:
            remove_button.configure(text=f"Error: {buffer["error"]}", fg_color="red")

        table.delete(item_id)
        getlinks()
       
 
    except:
        remove_button.configure(text="Error", fg_color="red")
        getlinks()

    background_thread.start()

def search(value_to_find):
    for i, row in enumerate(table.get_children()):
        row_value = table.item(row)["values"][1]  # Ändern Sie den Index basierend auf der Spalte, in der Sie suchen möchten
        if row_value == value_to_find:
            table.selection_set(row)
            table.yview(i)  # Scrollen Sie zur Zeile
            return

def search_button_action():
    value = search_entry.get()
    search(value)

def reset():
    import_button.configure(state="disabled")
    remove_button.configure(state="disabled")
    time.sleep(1)
    remove_button.configure(text="Remove selected Row")
    import_status_label.place_forget()
    import_button.configure(state="normal")
    remove_button.configure(state="normal")

def export_button_action():
    url = "http://localhost/blocked"

    response = requests.get(url)
    data = json.loads(response.text)
    with open('meine_datei.txt', 'w') as f:
        json.dump(data, f)

    os.system('meine_datei.txt')

def change_ip_button_action():
    dialog = customtkinter.CTkInputDialog(text="Type in your new Ip Adress:", title="IP change")

    newip = dialog.get_input()

    with open('ip.cfg', 'w') as config:
        json.dump(newip, config)
        

# --> Initalizing the Main Elements

# Initalizing Window:
app = customtkinter.CTk()
app.geometry("600x600")
app.title("Adblocker")
app.protocol("WM_DELETE_WINDOW", exit)



# Initalizing Menu-bar:
menu = customtkinter.CTkFrame(master=app, width=150, height=600, border_width=1, border_color="#1F538D")
menu.place(x=0,y=0)

# Initalizing Main-frame:
main_frame = customtkinter.CTkFrame(master=app, width=450, height=600, fg_color="transparent")
main_frame.place(x=150,y=0)

# Initalizing About-frame:
about_frame = customtkinter.CTkFrame(master=app, width=450, height=600, fg_color="transparent")

# Initalizing Settings-frame:
settings_frame = customtkinter.CTkFrame(master=app, width=450, height=600, fg_color="transparent")

# Initalizing Progressbar:
status_label = customtkinter.CTkLabel(master=app, width=440, height=30, text="", corner_radius=5, fg_color="blue")
status_label.place(x=155,y=565)


# --> Initalizing Elements of the Menu-bar:

# Image:
logo_label = customtkinter.CTkLabel(menu, image= images.logo, text="")
logo_label.place(x=11,y=10)

# "Menu" label:
label = customtkinter.CTkLabel(menu, width=140,text="AD Blocker - Menu",fg_color=("#3A7EBF", "#1F538D"),text_color="white", corner_radius= 5)
label.place(x=5,y=150)

# "Start" button:
button_start = customtkinter.CTkButton(menu, width=140, text="Start", command = start_button_action, image=images.start_image, fg_color="green")
button_start.place(x=5, y= 200)

# "Stop" button:
button_stop = customtkinter.CTkButton(menu, width=140, text="Stop", command = stop_button_action, image=images.stop_image, fg_color="red")
button_stop.place(x=5, y= 235)

# "CPU" label:
cpu_label = customtkinter.CTkLabel(menu, width=140,fg_color=("#3A7EBF", "#1F538D"),text_color="white", corner_radius= 5)
cpu_label.place(x=5,y=285)

# "RAM" label:
ram_label = customtkinter.CTkLabel(menu, width=140,fg_color=("#3A7EBF", "#1F538D"),text_color="white", corner_radius= 5)
ram_label.place(x=5,y=320)

# Button "Light" Theme:
button_light_theme = customtkinter.CTkButton(menu, width=140, text="Switch Theme", command=theme_change_light, image=images.theme_image)
button_light_theme.place(x=5,y=450)

# Button "Dark" Theme:
button_dark_theme = customtkinter.CTkButton(menu,width=140, text="Switch Theme", command=theme_change_dark, image=images.theme_image)

# "Home" button:
button_home = customtkinter.CTkButton(menu, width=140, text="Home", command = home_button_action, image=images.home_image)
button_home.place(x=5, y= 495)

# "About" button:
button_about = customtkinter.CTkButton(menu, width=140, text="About", command = about_button_action, image=images.about_image)
button_about.place(x=5, y= 530)

# "Settings" button:
button_settings = customtkinter.CTkButton(menu, width=140, text="Settings", command = settings_button_action,  image=images.settings_image)
button_settings.place(x=5,y=565)



# --> Initalizing Elements of Main_frame:

# Initalizing Tabview Widget:
tabview = customtkinter.CTkTabview(main_frame,width=440, border_color=("#1F538D"), border_width=1, anchor="nw")
tabview.place(x=5,y=0)
tabview.add("Statistics")  # add tab at the end
tabview.add("Import/Export")  # add tab at the end
tabview.set("Statistics")  # set currently visible tab

tabview1 = customtkinter.CTkTabview(main_frame,width=440, height = 300, border_color=("#1F538D"), border_width=1, anchor="nw")
tabview1.place(x=5,y=250)
tabview1.add("blocked Links")


# --> Initalizing Elements of Tabview

link_entry = customtkinter.CTkEntry(tabview.tab("Import/Export"), placeholder_text="Please enter a Link", width= 350)
link_entry.place(x=10,y=10)

import_button = customtkinter.CTkButton(tabview.tab("Import/Export"), width= 50, text="Add", command = import_button_action)
import_button.place(x=365,y=10)

import_status_label = customtkinter.CTkLabel(tabview.tab("Import/Export"), width = 405, fg_color="transparent", corner_radius=5, text = "")
import_status_label.place(x=10, y=45)

export_button = customtkinter.CTkButton(tabview.tab("Import/Export"), width= 450, text="Export Links", command = export_button_action)
export_button.place(x=10,y=80)

# --> Initalizing Elements of Tabview 1:
table = ttk.Treeview(tabview1.tab("blocked Links"), height = 9)
table['columns'] = ('link_id', 'link_name')

table.column("#0", width=0, stretch="no")
table.column("link_id",anchor="center", width=20)
table.column("link_name",anchor="center",width=395)

table.heading("#0",text="",anchor="center")
table.heading("link_id",text="Id",anchor="center")
table.heading("link_name",text="Link",anchor="center")

table.bind("<ButtonRelease-1>", on_select)

table.place(x=5,y=35)

# create scrollbar for Table
table_scrollbar = customtkinter.CTkScrollbar(tabview1.tab("blocked Links"), command=table.yview)
table_scrollbar.pack(side='right', fill='y')

table.configure(yscrollcommand= table_scrollbar.set)

sync_button = customtkinter.CTkButton(tabview1.tab("blocked Links"), width= 50, text="Sync", command = getlinks, image=images.sync_image)
sync_button.place(x=5,y=0)

remove_button = customtkinter.CTkButton(tabview1.tab("blocked Links"), width= 175, text="Remove selected Row", command = remove_rows, image = images.remove_image, fg_color="red")
remove_button.place(x=85,y=0)

search_entry = customtkinter.CTkEntry(tabview1.tab("blocked Links"), placeholder_text="Search", width= 100)
search_entry.place(x=268,y=0)

search_button = customtkinter.CTkButton(tabview1.tab("blocked Links"), width= 15, text="", command = search_button_action, image = images.search_image)
search_button.place(x=375,y=0)

# --> Initalizing Elements of About:

#h1
about_h1 = customtkinter.CTkLabel(about_frame, text="About", width=440, fg_color="transparent",font=("",40))
about_h1.place(x=5,y=10)



# --> Initalizing Elements of Settings:

#h1:
settings_h1 = customtkinter.CTkLabel(settings_frame, text="Settings", width=440, fg_color="transparent",font=("",40))
settings_h1.place(x=5,y=10)

#Theme text:
theme_text = customtkinter.CTkLabel(settings_frame, text="Theme:", width=140, fg_color="transparent",font=("",20))
theme_text.place(x=5,y=70)

#Theme Drop-Down:
theme_optionmenu = customtkinter.CTkOptionMenu(settings_frame, values=["Dark", "Light", "Auto (System default)"], command=theme_change)
theme_optionmenu.place(x=155,y=70)

#Window-sclaing text:
window_scaling_text = customtkinter.CTkLabel(settings_frame, text="Scaling:", width=140, fg_color="transparent",font=("",20))
window_scaling_text.place(x=5,y=105)

#Windwos-scaling Drop-Down:
window_scaling_optionmenu = customtkinter.CTkOptionMenu(settings_frame, values=["100","125","150","175","200","225","250"], command=change_window_scaling)
window_scaling_optionmenu.place(x=155,y=105)

#IP change text:
ip_change_text = customtkinter.CTkLabel(settings_frame, text="Change IP:", width=140, fg_color="transparent",font=("",20))
ip_change_text.place(x=5,y=140)

#Ip Change button
ip_change_button = customtkinter.CTkButton(settings_frame, text="change Ip Adress", width=140, command=change_ip_button_action)
ip_change_button.place(x=155,y=140)