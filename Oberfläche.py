import customtkinter
from PIL import Image
import psutil
import time

app = customtkinter.CTk()
app.geometry("600x600")
app.title("Adblocker")
app.grid_rowconfigure(0, weight=0)
app.grid_columnconfigure(0, weight=0)

#set Appearance Mode to the operating System default value
customtkinter.set_appearance_mode("dark")

#set default color theme
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
    
def theme_change_light():

    customtkinter.set_appearance_mode("light")
    button_light_theme.grid_remove()
    button_dark_theme.grid(row=2,column=0,padx=10,pady=(350,10),sticky="we")

def theme_change_dark():

    customtkinter.set_appearance_mode("dark")
    button_dark_theme.grid_remove()
    button_light_theme.grid(row=2,column=0,padx=10,pady=(350,10),sticky="we")

def update_resources():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    task_label.configure(text=f"CPU: {cpu_usage}%\nMemory: {memory_usage}%")
    app.after(1000, update_resources)  # Update every second    

frame = customtkinter.CTkFrame(app, border_color=("#1F538D"), border_width=1)
frame.grid(row=0,column=0,padx=0,pady=(0,0),sticky="nws")


label = customtkinter.CTkLabel(frame,text="AD Blocker - Menu",fg_color=("#3A7EBF", "#1F538D"),text_color="white", corner_radius= 5)
label.grid(row=1,column=0,padx=10,pady=(10,0),sticky="we")

tabview = customtkinter.CTkTabview(master=app, border_color=("#1F538D"), border_width=1)
tabview.grid(row=0,column=1,padx=5,pady=(0,0), sticky = "nw")

tabview.add("Statistics")  # add tab at the end
tabview.add("Import/Export")  # add tab at the end
tabview.set("Statistics")  # set currently visible tab

task_tabview = customtkinter.CTkTabview(app, border_color=("#1F538D"), border_width=1, anchor='nw')
task_tabview.grid(row=0,column=1,padx=5,pady=(255,0),sticky="nw")

task_tabview.add("System Resources",)  # add tab at the end

task_tabview.grid_rowconfigure(0, weight=0)
task_tabview.grid_columnconfigure(0, weight=0)

logo = customtkinter.CTkImage(light_image=Image.open("icons8-adblocking-96.png"), dark_image=Image.open("icons8-adblocking-96.png"),size=(128,128))
logo_label = customtkinter.CTkLabel(frame, image=logo, text="")  # display image with a CTkLabel
logo_label.grid(row=0,column=0,padx=25,pady=(10,0))

theme_image = customtkinter.CTkImage(light_image=Image.open("icons8-night-mode-24.png"), dark_image=Image.open("icons8-night-mode-24.png"),size=(20,20))
theme_image_label = customtkinter.CTkLabel(frame, image=theme_image, text="")  # display image with a CTkLabel
theme_image_label.grid(row=2,column=0,padx=10,pady=(10,0),sticky="w")

settings_image = customtkinter.CTkImage(light_image=Image.open("icons8-einstellungen-50.png"), dark_image=Image.open("icons8-einstellungen-50.png"),size=(20,20))
settings_image_label = customtkinter.CTkLabel(frame, image=settings_image, text="")  # display image with a CTkLabel
settings_image_label.grid(row=2,column=0,padx=10,pady=(10,0),sticky="w")

about_image = customtkinter.CTkImage(light_image=Image.open("icons8-info-50.png"), dark_image=Image.open("icons8-info-50.png"),size=(20,20))
about_image_label = customtkinter.CTkLabel(frame, image=about_image, text="")  # display image with a CTkLabel
about_image_label.grid(row=2,column=0,padx=10,pady=(10,0),sticky="w")


button_light_theme = customtkinter.CTkButton(frame, text="Switch Theme", command=theme_change_light, image=theme_image)
button_light_theme.grid(row=2,column=0,padx=10,pady=(350,10),sticky="we")

button_dark_theme = customtkinter.CTkButton(frame, text="Switch Theme", command=theme_change_dark, image=theme_image)

button_settings = customtkinter.CTkButton(frame, text="Settings", image=settings_image)
button_settings.grid(row=3,column=0,padx=10,pady=(30,10),sticky="we")

button_about = customtkinter.CTkButton(frame, text="About", command=theme_change_light, image=about_image)
button_about.grid(row=4,column=0,padx=10,pady=(0,10),sticky="we")

task_label = customtkinter.CTkLabel(master=task_tabview.tab("System Resources"),fg_color=("#3A7EBF", "#1F538D"), corner_radius= 5)
task_label.grid(row=4,column=0,padx=10,pady=(0,10),sticky="we")

update_resources()
app.mainloop()      