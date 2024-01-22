import customtkinter
from PIL import Image
import psutil

# --> Setting gernal aspects of custom Tkinter:

#set Appearance Mode to the operating System default value
customtkinter.set_appearance_mode("dark")

#set default color theme
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"



# --> Initalizing methods:

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




# --> Initalizing the Main Elements

# Initalizing Window:
app = customtkinter.CTk()
app.geometry("600x600")
app.title("Adblocker")

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
progressbar = customtkinter.CTkProgressBar(master=app, width=440, height=30, orientation="horizontal", corner_radius=5, progress_color="green")
progressbar.place(x=155,y=565)





# --> initalizing Images:

# Menu-bar Image:
logo = customtkinter.CTkImage(light_image=Image.open("icons8-adblocking-96.png"), dark_image=Image.open("icons8-adblocking-96.png"),size=(128,128))
logo_label = customtkinter.CTkLabel(menu, image=logo, text="")
logo_label.place(x=11,y=10)

# "Change Theme" button Image:
theme_image = customtkinter.CTkImage(light_image=Image.open("icons8-night-mode-24.png"), dark_image=Image.open("icons8-night-mode-24.png"),size=(20,20))

# "Start" button Image:
start_image = customtkinter.CTkImage(light_image=Image.open("icons8-spielen-26.png"), dark_image=Image.open("icons8-spielen-26.png"),size=(20,20))

# "Stop" button Image:
stop_image = customtkinter.CTkImage(light_image=Image.open("icons8-stop-26.png"), dark_image=Image.open("icons8-stop-26.png"),size=(20,20))

# "Home" button Image:
home_image = customtkinter.CTkImage(light_image=Image.open("icons8-zuhause-26.png"), dark_image=Image.open("icons8-zuhause-26.png"),size=(20,20))

# "Settings" button Image:
settings_image = customtkinter.CTkImage(light_image=Image.open("icons8-einstellungen-50.png"), dark_image=Image.open("icons8-einstellungen-50.png"),size=(20,20))

# "About" button Image:
about_image = customtkinter.CTkImage(light_image=Image.open("icons8-info-50.png"), dark_image=Image.open("icons8-info-50.png"),size=(20,20))



# --> Initalizing Elements of the Menu-bar:

# "Menu" label:
label = customtkinter.CTkLabel(menu, width=140,text="AD Blocker - Menu",fg_color=("#3A7EBF", "#1F538D"),text_color="white", corner_radius= 5)
label.place(x=5,y=150)

# "Start" button:
button_start = customtkinter.CTkButton(menu, width=140, text="Start", command = home_button_action, image=start_image, fg_color="green")
button_start.place(x=5, y= 200)

# "Stop" button:
button_stop = customtkinter.CTkButton(menu, width=140, text="Stop", command = home_button_action, image=stop_image, fg_color="red")
button_stop.place(x=5, y= 235)

# "CPU" label:
cpu_label = customtkinter.CTkLabel(menu, width=140,fg_color=("#3A7EBF", "#1F538D"),text_color="white", corner_radius= 5)
cpu_label.place(x=5,y=285)

# "RAM" label:
ram_label = customtkinter.CTkLabel(menu, width=140,fg_color=("#3A7EBF", "#1F538D"),text_color="white", corner_radius= 5)
ram_label.place(x=5,y=320)

# Button "Light" Theme:
button_light_theme = customtkinter.CTkButton(menu, width=140, text="Switch Theme", command=theme_change_light, image=theme_image)
button_light_theme.place(x=5,y=450)

# Button "Dark" Theme:
button_dark_theme = customtkinter.CTkButton(menu,width=140, text="Switch Theme", command=theme_change_dark, image=theme_image)

# "Home" button:
button_home = customtkinter.CTkButton(menu, width=140, text="Home", command = home_button_action, image=home_image)
button_home.place(x=5, y= 495)

# "About" button:
button_about = customtkinter.CTkButton(menu, width=140, text="About", command = about_button_action, image=about_image)
button_about.place(x=5, y= 530)

# "Settings" button:
button_settings = customtkinter.CTkButton(menu, width=140, text="Settings", command = settings_button_action,  image=settings_image)
button_settings.place(x=5,y=565)



# --> Initalizing Elements of Main_frame:

# Initalizing Tabview Widget:
tabview = customtkinter.CTkTabview(main_frame,width=440, border_color=("#1F538D"), border_width=1, anchor="nw")
tabview.place(x=5,y=0)
tabview.add("Statistics")  # add tab at the end
tabview.add("Import/Export")  # add tab at the end
tabview.set("Statistics")  # set currently visible tab



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

update_resources()
app.mainloop()