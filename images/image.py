# This module initalizes all images using the PILLOW librari and CTkImage from Customtkinter

from  __init__ import *

base_path = os.getcwd()


# Menu-bar Image:
logo = customtkinter.CTkImage(light_image=Image.open(f"{base_path}/images/icon-blocker.png"), dark_image=Image.open(f"{base_path}/images/icon-blocker.png"),size=(128,128))

# "Change Theme" button Image:
theme_image = customtkinter.CTkImage(light_image=Image.open(f"{base_path}/images/icon-theme.png"), dark_image=Image.open(f"{base_path}/images/icon-theme.png"),size=(20,20))

# "Start" button Image:
start_image = customtkinter.CTkImage(light_image=Image.open(f"{base_path}/images/icon-play.png"), dark_image=Image.open(f"{base_path}/images/icon-play.png"),size=(20,20))

# "Stop" button Image:
stop_image = customtkinter.CTkImage(light_image=Image.open(f"{base_path}/images/icon-stop.png"), dark_image=Image.open(f"{base_path}/images/icon-stop.png"),size=(20,20))

# "Home" button Image:
home_image = customtkinter.CTkImage(light_image=Image.open(f"{base_path}/images/icon-home.png"), dark_image=Image.open(f"{base_path}/images/icon-home.png"),size=(20,20))

# "Settings" button Image:
settings_image = customtkinter.CTkImage(light_image=Image.open(f"{base_path}/images/icon-settings.png"), dark_image=Image.open(f"{base_path}/images/icon-settings.png"),size=(20,20))

# "About" button Image:
about_image = customtkinter.CTkImage(light_image=Image.open(f"{base_path}/images/icon-info.png"), dark_image=Image.open(f"{base_path}/images/icon-info.png"),size=(20,20))

# "Sync" button Image:
sync_image = customtkinter.CTkImage(light_image=Image.open(f"{base_path}/images/icon-sync.png"), dark_image=Image.open(f"{base_path}/images/icon-sync.png"),size=(20,20))

# "Remove" button Image:
remove_image = customtkinter.CTkImage(light_image=Image.open(f"{base_path}/images/icon-delete.png"), dark_image=Image.open(f"{base_path}/images/icon-delete.png"),size=(20,20))

# "Remove" button Image:
search_image = customtkinter.CTkImage(light_image=Image.open(f"{base_path}/images/icon-search.png"), dark_image=Image.open(f"{base_path}/images/icon-search.png"),size=(20,20))